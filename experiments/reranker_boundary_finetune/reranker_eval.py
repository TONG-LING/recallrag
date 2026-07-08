#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from reranker_common import configure_hf_endpoint, load_jsonl, make_cross_encoder, resolve_device, write_json

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_MODEL = "BAAI/bge-reranker-base"
DEFAULT_EVAL_CANDIDATES = str(SCRIPT_DIR / "data" / "eval_candidates.jsonl")
CANDIDATE_K = 20
TOP_K = 5
BATCH_SIZE = 16


def first_true_rank(rows: list[dict], top_k: int | None = None) -> int | None:
    rows = rows if top_k is None else rows[:top_k]
    return next((i for i, row in enumerate(rows, 1) if row.get("label")), None)


def rerank_candidates(model, query: str, candidates: list[dict]) -> list[dict]:
    pairs = [(query, cand.get("text", "")) for cand in candidates]
    scores = model.predict(pairs, batch_size=BATCH_SIZE, show_progress_bar=False) if pairs else []
    reranked = []
    for cand, score in zip(candidates, scores):
        row = dict(cand)
        row["rerank_score"] = float(score)
        reranked.append(row)
    reranked.sort(
        key=lambda row: (row.get("rerank_score", float("-inf")), row.get("dense_score", float("-inf"))),
        reverse=True,
    )
    return reranked


def filter_rows(rows: list[dict], split_filter: str, subset_filter: str) -> list[dict]:
    if split_filter != "all":
        rows = [row for row in rows if row.get("split") == split_filter]
    if subset_filter == "boundary_sensitive":
        rows = [row for row in rows if row.get("boundary_sensitive")]
    elif subset_filter == "non_boundary_sensitive":
        rows = [row for row in rows if not row.get("boundary_sensitive")]
    return rows


def write_eval_report(path: str | Path, metrics: dict, results: list[dict]) -> None:
    fixed = [row["qid"] for row in results if (not row["success_before_rerank"]) and row["success"]]
    regressed = [row["qid"] for row in results if row["success_before_rerank"] and (not row["success"])]
    lines = ["# Cross-Encoder Reranker Evaluation", "", "## Metrics", ""]
    for key, value in metrics.items():
        lines.append(f"- **{key}**: `{value:.6f}`" if isinstance(value, float) else f"- **{key}**: `{value}`")
    lines += ["", "## Query Movement", "", f"- fixed: `{fixed}`", f"- regressed: `{regressed}`"]
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def cmd_eval(args: argparse.Namespace) -> None:
    source_rows = load_jsonl(DEFAULT_EVAL_CANDIDATES)
    rows = filter_rows(source_rows, args.split_filter, args.subset_filter)
    if not rows:
        raise RuntimeError("No eval rows left after applying split/subset filters.")

    model = make_cross_encoder(
        args.model_name_or_path,
        args.max_length,
        args.trust_remote_code,
        device=resolve_device(args.device),
    )

    results = []
    dense_hits = rerank_hits = fixed = regressed = improved = missing_positive = 0
    dense_rr = rerank_rr = 0.0

    for row in rows:
        candidates = row["candidates"][:CANDIDATE_K]
        dense_rank = first_true_rank(candidates, TOP_K)
        candidate_rank = first_true_rank(candidates, None)
        if candidate_rank is None:
            missing_positive += 1

        reranked = rerank_candidates(model, row["query"], candidates)
        rerank_rank = first_true_rank(reranked, TOP_K)

        dense_success = dense_rank is not None
        rerank_success = rerank_rank is not None
        dense_hits += int(dense_success)
        rerank_hits += int(rerank_success)
        dense_rr += 1.0 / dense_rank if dense_rank else 0.0
        rerank_rr += 1.0 / rerank_rank if rerank_rank else 0.0
        fixed += int((not dense_success) and rerank_success)
        regressed += int(dense_success and (not rerank_success))
        improved += int(candidate_rank is not None and rerank_rank is not None and rerank_rank < candidate_rank)

        results.append(
            {
                "qid": row["qid"],
                "split": row.get("split"),
                "boundary_sensitive": row.get("boundary_sensitive", False),
                "query": row["query"],
                "success_before_rerank": dense_success,
                "rank_before_rerank": dense_rank,
                "success": rerank_success,
                "rank": rerank_rank,
                "first_relevant_candidate_rank_before_rerank": candidate_rank,
                "candidate_k": len(candidates),
                "top_k": TOP_K,
                "top_k_after_rerank": [
                    {
                        "rank": i,
                        "chunk_id": cand.get("chunk_id"),
                        "doc_id": cand.get("doc_id"),
                        "coverage": cand.get("coverage"),
                        "label": cand.get("label"),
                        "dense_score": cand.get("dense_score"),
                        "rerank_score": cand.get("rerank_score"),
                    }
                    for i, cand in enumerate(reranked[:TOP_K], 1)
                ],
            }
        )

    n = len(rows)
    metrics = {
        "source_total": len(source_rows),
        "total": n,
        "split_filter": args.split_filter,
        "subset_filter": args.subset_filter,
        "dense_recall@5": dense_hits / n if n else 0.0,
        "recall@5": rerank_hits / n if n else 0.0,
        "dense_mrr": dense_rr / n if n else 0.0,
        "mrr": rerank_rr / n if n else 0.0,
        "mrr_delta": (rerank_rr - dense_rr) / n if n else 0.0,
        "dense_hits_before_rerank": dense_hits,
        "hits": rerank_hits,
        "rerank_fixed": fixed,
        "rerank_regressed": regressed,
        "rerank_improved": improved,
        "candidate_missing_positive": missing_positive,
        "candidate_k": CANDIDATE_K,
        "top_k": TOP_K,
        "model_name_or_path": args.model_name_or_path,
    }

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_json(out_dir / "retrieval_results.json", results)
    write_json(out_dir / "metrics.json", metrics)
    write_eval_report(out_dir / "eval_report.md", metrics, results)
    print(json.dumps(metrics, ensure_ascii=False, indent=2))
    print(f"wrote eval -> {out_dir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-name-or-path", default=DEFAULT_MODEL)
    parser.add_argument("--out", default=str(SCRIPT_DIR / "outputs" / "eval"))
    parser.add_argument("--device", default=None)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--trust-remote-code", action="store_true")
    parser.add_argument("--hf-endpoint", default=None)
    parser.add_argument("--no-hf-mirror", action="store_true")
    parser.add_argument("--split-filter", choices=["all", "train", "dev", "test"], default="test")
    parser.add_argument("--subset-filter", choices=["all", "boundary_sensitive", "non_boundary_sensitive"], default="all")
    parser.set_defaults(func=cmd_eval)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    endpoint = configure_hf_endpoint(
        getattr(args, "hf_endpoint", None),
        use_mirror=not getattr(args, "no_hf_mirror", False),
    )
    if getattr(args, "hf_endpoint", None) is not None or getattr(args, "no_hf_mirror", False):
        print(f"==> HF_ENDPOINT={endpoint}")
    args.func(args)


if __name__ == "__main__":
    main()
