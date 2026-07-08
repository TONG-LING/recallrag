#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import random
import re
from collections import Counter
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]

CHUNKS_PATH = REPO_ROOT / "runs" / "zh120_c600_o0_base" / "chunks.json"
RESULTS_PATH = REPO_ROOT / "runs" / "zh120_c600_o0_base" / "retrieval_results.json"
QUESTIONS_PATH = REPO_ROOT / "case_zh_dureader_120" / "eval" / "questions_patch_source.jsonl"
TRAIN_CANDIDATE_LIMIT = 30
EVAL_CANDIDATE_LIMIT = 20
POS_PER_QUERY = 1
PARTIAL_PER_QUERY = 3
WRONG_PER_QUERY = 1

LATIN_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")
CJK_SPAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]+")
EN_STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "being", "been", "to", "of",
    "in", "on", "for", "and", "or", "but", "why", "how", "what", "when", "where",
    "can", "could", "should", "would", "does", "do", "did", "it", "this", "that",
    "with", "without", "into", "from", "by", "as", "at", "if", "then", "than",
}


def read_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_questions(path: str | Path) -> list[dict]:
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def normalize_text(text: str) -> str:
    return " ".join((text or "").replace("\u3000", " ").replace("\xa0", " ").split())


def mixed_tokens(text: str, *, drop_stopwords: bool = False, min_ascii_len: int = 1, cjk_ngram: int = 2) -> list[str]:
    norm = normalize_text(text).lower()
    tokens: list[str] = []
    for token in LATIN_TOKEN_RE.findall(norm):
        if len(token) < min_ascii_len:
            continue
        if drop_stopwords and token in EN_STOPWORDS:
            continue
        tokens.append(token)
    for span in CJK_SPAN_RE.findall(norm):
        chars = [ch for ch in span if ch.strip()]
        if not chars:
            continue
        if len(chars) < cjk_ngram:
            tokens.extend(chars)
            continue
        tokens.extend("".join(chars[i : i + cjk_ngram]) for i in range(len(chars) - cjk_ngram + 1))
    return tokens


def coverage(gold_span: str, chunk_text: str) -> float:
    gold_tokens = mixed_tokens(gold_span)
    if not gold_tokens:
        return 0.0
    chunk_tokens = set(mixed_tokens(chunk_text))
    hit = sum(1 for token in gold_tokens if token in chunk_tokens)
    return hit / len(gold_tokens)


def relevance_score(question: dict, chunk: dict) -> float:
    if chunk.get("doc_id") != question.get("gold_doc"):
        return 0.0
    if question.get("eval_mode") == "doc" or (not question.get("gold_span")):
        return 1.0
    return coverage(question.get("gold_span", ""), chunk.get("text", ""))


def write_json(path: str | Path, obj, *, indent: int | None = None) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(obj, ensure_ascii=False, indent=indent)
    path.write_text(text + ("" if text.endswith("\n") else "\n"), encoding="utf-8")


def write_jsonl(path: str | Path, rows: list[dict]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=str(SCRIPT_DIR / "data"))
    parser.add_argument("--coverage-threshold", type=float, default=0.65)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def build_split_map(qids: list[str], out_dir: Path, seed: int) -> dict[str, str]:
    source_path = out_dir / "splits.json"
    if source_path.exists():
        qid_split = read_json(source_path)["qid_split"]
        missing = [qid for qid in qids if qid not in qid_split]
        if missing:
            raise RuntimeError(f"split source `{source_path}` is missing qids: {missing[:5]}")
        return {qid: qid_split[qid] for qid in qids}

    shuffled = list(qids)
    random.Random(seed).shuffle(shuffled)
    train_n = round(len(shuffled) * 0.70)
    dev_n = round(len(shuffled) * 0.15)
    qid_split: dict[str, str] = {}
    for idx, qid in enumerate(shuffled):
        qid_split[qid] = "train" if idx < train_n else "dev" if idx < train_n + dev_n else "test"
    return qid_split


def first_positive_rank(rows: list[dict]) -> int | None:
    return next((idx for idx, row in enumerate(rows, 1) if row["label"]), None)


def row_sort_key(row: dict, *, wrong: bool = False) -> tuple[float, int, int]:
    if wrong:
        return (row["dense_rank"], -row["dense_score"], len(row["text"]))
    return (-row["coverage"], row["dense_rank"], len(row["text"]))


def make_dense_rows(question: dict, result: dict, chunks: dict[str, dict], threshold: float) -> list[dict]:
    rows = []
    for trace in result.get("top_n_trace", [])[:TRAIN_CANDIDATE_LIMIT]:
        chunk = chunks.get(trace["chunk_id"])
        if not chunk:
            continue
        coverage = round(float(relevance_score(question, chunk)), 6)
        rows.append(
            {
                "chunk_id": chunk["chunk_id"],
                "doc_id": chunk["doc_id"],
                "text": chunk["text"],
                "dense_rank": int(trace["rank"]),
                "dense_score": float(trace["score"]),
                "coverage": coverage,
                "label": bool(chunk["doc_id"] == question["gold_doc"] and coverage >= threshold),
            }
        )
    return rows


def make_pair(split: str, qid: str, query: str, row: dict, kind: str, boundary_sensitive: bool) -> dict:
    return {
        "split": split,
        "qid": qid,
        "query": query,
        "text": row["text"],
        "label": 1.0 if kind == "positive_complete_evidence" else 0.0,
        "kind": kind,
        "coverage": row["coverage"],
        "chunk_id": row["chunk_id"],
        "doc_id": row["doc_id"],
        "dense_rank": row["dense_rank"],
        "boundary_sensitive": boundary_sensitive,
    }


def main() -> None:
    args = parse_args()
    out_dir = Path(args.out_dir)

    chunks = {row["chunk_id"]: row for row in read_json(CHUNKS_PATH)}
    results = read_json(RESULTS_PATH)
    questions = {row["qid"]: row for row in load_questions(QUESTIONS_PATH)}
    qid_split = build_split_map([row["qid"] for row in results], out_dir, args.seed)

    pairs: list[dict] = []
    eval_candidates: list[dict] = []
    boundary_sensitive_qids: list[str] = []
    skipped_no_positive_topn: list[str] = []
    questions_with_positive_topn = 0

    for result in results:
        qid = result["qid"]
        question = questions[qid]
        split = qid_split[qid]
        dense_rows = make_dense_rows(question, result, chunks, args.coverage_threshold)

        positives = [row for row in dense_rows if row["doc_id"] == question["gold_doc"] and row["coverage"] >= args.coverage_threshold]
        partials = [row for row in dense_rows if row["doc_id"] == question["gold_doc"] and 0.0 < row["coverage"] < args.coverage_threshold]
        wrongs = [row for row in dense_rows if row["doc_id"] != question["gold_doc"]]

        has_positive = bool(positives)
        boundary_sensitive = has_positive and bool(partials)
        if has_positive:
            questions_with_positive_topn += 1
        else:
            skipped_no_positive_topn.append(qid)
        if boundary_sensitive:
            boundary_sensitive_qids.append(qid)

        eval_rows = dense_rows[:EVAL_CANDIDATE_LIMIT]
        eval_candidates.append(
            {
                "qid": qid,
                "split": split,
                "query": question["question"],
                "gold_doc": question["gold_doc"],
                "candidate_k": len(eval_rows),
                "dense_success_at5": first_positive_rank(eval_rows[:5]) is not None,
                "dense_rank_at5": first_positive_rank(eval_rows[:5]),
                "first_relevant_candidate_rank": first_positive_rank(eval_rows),
                "boundary_sensitive": boundary_sensitive,
                "candidates": eval_rows,
            }
        )

        if not has_positive:
            continue

        for row in sorted(positives, key=row_sort_key)[:POS_PER_QUERY]:
            pairs.append(make_pair(split, qid, question["question"], row, "positive_complete_evidence", boundary_sensitive))
        for row in sorted(partials, key=row_sort_key)[:PARTIAL_PER_QUERY]:
            pairs.append(make_pair(split, qid, question["question"], row, "same_doc_incomplete", boundary_sensitive))
        for row in sorted(wrongs, key=lambda row: row_sort_key(row, wrong=True))[:WRONG_PER_QUERY]:
            pairs.append(make_pair(split, qid, question["question"], row, "high_rank_wrong_doc", boundary_sensitive))

    write_jsonl(out_dir / "pairs.jsonl", pairs)
    write_jsonl(out_dir / "eval_candidates.jsonl", eval_candidates)

    kind_counts = Counter(row["kind"] for row in pairs)
    split_counts = Counter(row["split"] for row in pairs)
    split_kind_counts = {
        split: {kind: sum(1 for row in pairs if row["split"] == split and row["kind"] == kind) for kind in sorted(kind_counts)}
        for split in sorted(split_counts)
    }
    summary = {
        "questions": len(results),
        "questions_with_positive_topn": questions_with_positive_topn,
        "boundary_sensitive_queries": len(boundary_sensitive_qids),
        "skipped_no_positive_topn": skipped_no_positive_topn,
        "coverage_threshold": args.coverage_threshold,
        "train_candidate_limit": TRAIN_CANDIDATE_LIMIT,
        "eval_candidate_limit": EVAL_CANDIDATE_LIMIT,
        "sampling_policy": {
            "positive_complete_evidence": POS_PER_QUERY,
            "same_doc_incomplete": PARTIAL_PER_QUERY,
            "high_rank_wrong_doc": WRONG_PER_QUERY,
            "random_wrong_doc": 0,
        },
        "total_pairs": len(pairs),
        "kind_counts": dict(kind_counts),
        "split_counts": dict(split_counts),
        "split_kind_counts": split_kind_counts,
    }
    write_json(
        out_dir / "splits.json",
        {"qid_split": qid_split, "boundary_sensitive_qids": boundary_sensitive_qids, "summary": summary},
        indent=2,
    )

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"wrote data -> {out_dir}")


if __name__ == "__main__":
    main()
