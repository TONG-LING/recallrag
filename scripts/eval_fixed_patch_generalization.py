#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from recallrag.eval import evaluate, load_questions, write_report
from recallrag.embeddings import require_equal_length


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate a fixed selected patch set on held-out queries."
    )
    parser.add_argument(
        "--index",
        default="runs/zh_base",
        help="Main index directory with chunks.json and vectors.json",
    )
    parser.add_argument(
        "--patch-dir",
        default="runs/zh_patches",
        help="Patch directory with selected_patch_chunks.json and selected_patch_vectors.json",
    )
    parser.add_argument(
        "--questions",
        default="case_zh_dureader/eval/questions_heldout.jsonl",
        help="Held-out questions.jsonl",
    )
    parser.add_argument(
        "--out",
        default="runs/zh_generalization",
        help="Output directory",
    )
    parser.add_argument(
        "--endpoint",
        default="http://localhost:1234/v1/embeddings",
        help="Embedding endpoint",
    )
    parser.add_argument(
        "--model",
        default="text-embedding-bge-large-zh-v1.5",
        help="Embedding model",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Top-k",
    )
    parser.add_argument(
        "--coverage-threshold",
        type=float,
        default=0.65,
        help="Coverage threshold",
    )
    return parser.parse_args()


def _load_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _write_json(path: str | Path, obj) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def _comparison(before: dict[str, dict], after: dict[str, dict]) -> dict:
    fixed = []
    regressed = []
    unchanged_failure = []
    unchanged_success = []
    movements = []
    for qid, base_row in before.items():
        patch_row = after[qid]
        if (not base_row["success"]) and patch_row["success"]:
            movement = "fixed"
            fixed.append(qid)
        elif base_row["success"] and (not patch_row["success"]):
            movement = "regressed"
            regressed.append(qid)
        elif (not base_row["success"]) and (not patch_row["success"]):
            movement = "unchanged_failure"
            unchanged_failure.append(qid)
        else:
            movement = "unchanged_success"
            unchanged_success.append(qid)
        movements.append(
            {
                "qid": qid,
                "movement": movement,
                "before_rank": base_row["rank"],
                "after_rank": patch_row["rank"],
                "before_best_coverage": base_row["best_topk_coverage"],
                "after_best_coverage": patch_row["best_topk_coverage"],
            }
        )
    return {
        "fixed": fixed,
        "regressed": regressed,
        "unchanged_failure": unchanged_failure,
        "unchanged_success_count": len(unchanged_success),
        "movements": movements,
    }


def main() -> None:
    args = parse_args()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    main_chunks = _load_json(Path(args.index) / "chunks.json")
    main_vectors = _load_json(Path(args.index) / "vectors.json")
    patch_chunks = _load_json(Path(args.patch_dir) / "selected_patch_chunks.json")
    patch_vectors = _load_json(Path(args.patch_dir) / "selected_patch_vectors.json")
    require_equal_length("main_chunks", main_chunks, "main_vectors", main_vectors, "eval_fixed_patch_generalization.main")
    require_equal_length("patch_chunks", patch_chunks, "patch_vectors", patch_vectors, "eval_fixed_patch_generalization.patch")
    questions = load_questions(args.questions)

    main_results, main_metrics = evaluate(
        main_chunks,
        main_vectors,
        questions,
        endpoint=args.endpoint,
        model=args.model,
        top_k=args.top_k,
        coverage_threshold=args.coverage_threshold,
    )
    combined_chunks = main_chunks + patch_chunks
    combined_vectors = main_vectors + patch_vectors
    patch_results, patch_metrics = evaluate(
        combined_chunks,
        combined_vectors,
        questions,
        endpoint=args.endpoint,
        model=args.model,
        top_k=args.top_k,
        coverage_threshold=args.coverage_threshold,
    )

    main_by_qid = {row["qid"]: row for row in main_results}
    patch_by_qid = {row["qid"]: row for row in patch_results}
    movement = _comparison(main_by_qid, patch_by_qid)
    comparison = {
        "mode": "fixed_selected_patch_generalization",
        "questions": str(Path(args.questions).resolve()),
        "main_index": str(Path(args.index).resolve()),
        "patch_dir": str(Path(args.patch_dir).resolve()),
        "selected_patch_chunks": len(patch_chunks),
        "main_only": main_metrics,
        "main_plus_fixed_patch": patch_metrics,
        "delta": {
            "recall": patch_metrics.get(f"recall@{args.top_k}", 0.0) - main_metrics.get(f"recall@{args.top_k}", 0.0),
            "mrr": patch_metrics.get("mrr", 0.0) - main_metrics.get("mrr", 0.0),
            "hits": patch_metrics.get("hits", 0) - main_metrics.get("hits", 0),
        },
        **movement,
    }

    _write_json(out_dir / "main_retrieval_results.json", main_results)
    _write_json(out_dir / "main_metrics.json", main_metrics)
    _write_json(out_dir / "fixed_patch_retrieval_results.json", patch_results)
    _write_json(out_dir / "fixed_patch_metrics.json", patch_metrics)
    _write_json(out_dir / "comparison.json", comparison)

    write_report(
        out_dir / "main_eval_report.md",
        main_metrics,
        main_results,
        {
            "mode": "heldout_main_only",
            "index": args.index,
            "questions": args.questions,
            "top_k": args.top_k,
            "coverage_threshold": args.coverage_threshold,
            "endpoint": args.endpoint,
            "model": args.model,
        },
    )
    write_report(
        out_dir / "fixed_patch_eval_report.md",
        patch_metrics,
        patch_results,
        {
            "mode": "heldout_main_plus_fixed_patch",
            "index": args.index,
            "patch_dir": args.patch_dir,
            "questions": args.questions,
            "top_k": args.top_k,
            "coverage_threshold": args.coverage_threshold,
            "endpoint": args.endpoint,
            "model": args.model,
            "selected_patch_chunks": len(patch_chunks),
        },
    )

    lines = [
        "# Fixed Patch Held-out Generalization Report",
        "",
        "## Setup",
        "",
        f"- questions: `{args.questions}`",
        f"- main index: `{args.index}`",
        f"- fixed patch source: `{args.patch_dir}`",
        f"- selected patch chunks: `{len(patch_chunks)}`",
        f"- top_k: `{args.top_k}`",
        f"- coverage_threshold: `{args.coverage_threshold}`",
        "",
        "## Metrics",
        "",
        "| Route | Recall@5 | MRR | Hits |",
        "|---|---:|---:|---:|",
        f"| main | {main_metrics.get('recall@5', 0.0):.4f} | {main_metrics.get('mrr', 0.0):.4f} | {main_metrics.get('hits', 0)} / {main_metrics.get('total', 0)} |",
        f"| main + fixed patch | {patch_metrics.get('recall@5', 0.0):.4f} | {patch_metrics.get('mrr', 0.0):.4f} | {patch_metrics.get('hits', 0)} / {patch_metrics.get('total', 0)} |",
        "",
        f"- fixed: {movement['fixed']}",
        f"- regressed: {movement['regressed']}",
        f"- unchanged_failure: {movement['unchanged_failure']}",
        f"- unchanged_success_count: {movement['unchanged_success_count']}",
        "",
        "## Why This Report Matters",
        "",
        "- Patch selection is frozen before this evaluation.",
        "- This report tests whether the already selected patch set still helps on unseen query wording.",
        "- It is not a claim of document-level universal generalization. It is a query-held-out check for the same repaired evidence windows.",
        "",
        "## Query Movement",
        "",
        "| qid | movement | before rank | after rank | before coverage | after coverage |",
        "|---|---|---:|---:|---:|---:|",
    ]
    for row in movement["movements"]:
        lines.append(
            f"| {row['qid']} | {row['movement']} | {row['before_rank']} | {row['after_rank']} | {row['before_best_coverage']} | {row['after_best_coverage']} |"
        )
    Path(out_dir / "comparison_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(comparison, ensure_ascii=False, indent=2))
    print(f"wrote held-out comparison -> {out_dir / 'comparison_report.md'}")


if __name__ == "__main__":
    main()
