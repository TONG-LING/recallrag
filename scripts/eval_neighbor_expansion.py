#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from recallrag.embeddings import embed_lmstudio, require_equal_length, require_vector_dimensions
from recallrag.eval import (
    _top_row,
    build_ranked_result,
    first_relevant_rank,
    load_questions,
    retrieve,
)


def _load_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _write_json(path: str | Path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def _build_doc_positions(chunks: list[dict]) -> tuple[dict[str, list[dict]], dict[str, int]]:
    by_doc: dict[str, list[dict]] = {}
    for chunk in chunks:
        by_doc.setdefault(chunk["doc_id"], []).append(chunk)
    position_by_chunk_id: dict[str, int] = {}
    for doc_id, doc_chunks in by_doc.items():
        doc_chunks.sort(key=lambda row: (row.get("start_offset", 0), row.get("chunk_id", "")))
        for pos, chunk in enumerate(doc_chunks):
            position_by_chunk_id[chunk["chunk_id"]] = pos
    return by_doc, position_by_chunk_id


def _expand_row(
    row: dict,
    doc_chunks: list[dict],
    anchor_pos: int,
    radius: int,
) -> dict:
    left = max(0, anchor_pos - radius)
    right = min(len(doc_chunks), anchor_pos + radius + 1)
    window = doc_chunks[left:right]
    merged_text = "\n".join(chunk.get("text", "") for chunk in window)
    expanded = dict(row)
    expanded["text"] = merged_text
    expanded["start_offset"] = min(chunk.get("start_offset", 0) for chunk in window)
    expanded["end_offset"] = max(chunk.get("end_offset", 0) for chunk in window)
    expanded["merged_chunk_ids"] = [chunk["chunk_id"] for chunk in window]
    expanded["merged_chunk_count"] = len(window)
    expanded["source_index"] = row.get("source_index", "main")
    return expanded


def _expand_ranked_rows(
    ranked_rows: list[dict],
    by_doc: dict[str, list[dict]],
    position_by_chunk_id: dict[str, int],
    radius: int,
) -> list[dict]:
    expanded_rows: list[dict] = []
    seen_windows: set[tuple[str, int, int]] = set()
    for row in ranked_rows:
        doc_id = row.get("doc_id")
        chunk_id = row.get("chunk_id")
        if doc_id not in by_doc or chunk_id not in position_by_chunk_id:
            expanded_rows.append(dict(row))
            continue
        doc_chunks = by_doc[doc_id]
        pos = position_by_chunk_id[chunk_id]
        expanded = _expand_row(row, doc_chunks, pos, radius)
        window_key = (
            doc_id,
            expanded.get("start_offset", 0),
            expanded.get("end_offset", 0),
        )
        if window_key in seen_windows:
            continue
        seen_windows.add(window_key)
        expanded_rows.append(expanded)
    return expanded_rows


def _write_report(path: str | Path, metrics: dict, results: list[dict], config: dict):
    improved = [row for row in results if (not row.get("success_before_expansion")) and row.get("success")]
    failed = [row for row in results if not row.get("success")]
    lines: list[str] = []
    lines.append("# Neighbor Expansion Report")
    lines.append("")
    lines.append("## Config")
    lines.append("")
    for key, value in config.items():
        lines.append(f"- **{key}**: `{value}`")
    lines.append("")
    lines.append("## Metrics")
    lines.append("")
    for key, value in metrics.items():
        if isinstance(value, float):
            lines.append(f"- **{key}**: {value:.4f}")
        else:
            lines.append(f"- **{key}**: {value}")
    lines.append("")
    lines.append("## Fixed By Neighbor Expansion")
    lines.append("")
    if not improved:
        lines.append("No query was fixed by neighbor expansion under the current setup.")
    for row in improved:
        lines.append(f"### {row['qid']}")
        lines.append(f"- question: {row['question']}")
        lines.append(f"- rank before expansion: {row.get('rank_before_expansion')}")
        lines.append(f"- rank after expansion: {row.get('rank')}")
        lines.append(f"- best_topk_coverage before: {row.get('best_topk_coverage_before_expansion')}")
        lines.append(f"- best_topk_coverage after: {row.get('best_topk_coverage')}")
        lines.append("")
    lines.append("## Still Failed")
    lines.append("")
    if not failed:
        lines.append("No failed queries after neighbor expansion.")
    for row in failed:
        lines.append(f"### {row['qid']}")
        lines.append(f"- question: {row['question']}")
        lines.append(f"- rank before expansion: {row.get('rank_before_expansion')}")
        lines.append(f"- rank after expansion: {row.get('rank')}")
        lines.append(f"- best_topk_coverage before: {row.get('best_topk_coverage_before_expansion')}")
        lines.append(f"- best_topk_coverage after: {row.get('best_topk_coverage')}")
        lines.append("")
    lines.append("## All Query Summary")
    lines.append("")
    lines.append("| qid | success before | success after | rank before | rank after | total chars top-5 |")
    lines.append("|---|---:|---:|---:|---:|---:|")
    for row in results:
        lines.append(
            f"| {row['qid']} | {row.get('success_before_expansion')} | {row.get('success')} | "
            f"{row.get('rank_before_expansion')} | {row.get('rank')} | {row.get('total_chars_top5_after_expansion')} |"
        )
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")


def evaluate_neighbor_expansion(
    index_dir: str | Path,
    questions_path: str | Path,
    out_dir: str | Path,
    endpoint: str,
    model: str,
    top_k: int = 5,
    coverage_threshold: float = 0.65,
    radius: int = 1,
):
    index_dir = Path(index_dir)
    out_dir = Path(out_dir)
    chunks = _load_json(index_dir / "chunks.json")
    vectors = _load_json(index_dir / "vectors.json")
    questions = load_questions(questions_path)
    require_equal_length("chunks", chunks, "vectors", vectors, "evaluate_neighbor_expansion")
    vector_dim = require_vector_dimensions(vectors, "evaluate_neighbor_expansion.candidate_vectors") if vectors else None
    qvecs = embed_lmstudio([question["question"] for question in questions], endpoint=endpoint, model=model)
    require_equal_length("questions", questions, "query_vectors", qvecs, "evaluate_neighbor_expansion")
    if qvecs:
        require_vector_dimensions(qvecs, "evaluate_neighbor_expansion.query_vectors", expected_dim=vector_dim)

    by_doc, position_by_chunk_id = _build_doc_positions(chunks)

    results: list[dict] = []
    dense_rr = 0.0
    expanded_rr = 0.0
    dense_hits = 0
    expanded_hits = 0
    fixed = 0
    avg_chars_total = 0.0
    avg_merged_chunks_total = 0.0

    for question, qvec in zip(questions, qvecs):
        dense_all = retrieve(qvec, chunks, vectors, top_k=len(chunks))
        dense_success_rank = first_relevant_rank(question, dense_all[:top_k], coverage_threshold)
        expanded_all = _expand_ranked_rows(dense_all, by_doc, position_by_chunk_id, radius)
        result = build_ranked_result(question, expanded_all, top_k=top_k, coverage_threshold=coverage_threshold)
        total_chars_top5 = sum(len(row.get("text", "")) for row in expanded_all[:top_k])
        avg_chars_per_item_top5 = total_chars_top5 / top_k if top_k else 0.0
        total_merged_chunks_top5 = sum(row.get("merged_chunk_count", 1) for row in expanded_all[:top_k])
        avg_merged_chunks_top5 = total_merged_chunks_top5 / top_k if top_k else 0.0
        result.update(
            {
                "success_before_expansion": dense_success_rank is not None,
                "rank_before_expansion": dense_success_rank,
                "best_topk_coverage_before_expansion": max(
                    (row.get("coverage", 0.0) for row in [_top_row(question, dense_row, i) for i, dense_row in enumerate(dense_all[:top_k], 1)]),
                    default=0.0,
                ),
                "top_k_before_expansion": [_top_row(question, row, i) for i, row in enumerate(dense_all[:top_k], 1)],
                "total_chars_top5_after_expansion": total_chars_top5,
                "avg_chars_per_item_top5_after_expansion": round(avg_chars_per_item_top5, 2),
                "avg_merged_chunks_top5": round(avg_merged_chunks_top5, 3),
            }
        )
        dense_hits += int(dense_success_rank is not None)
        expanded_hits += int(result["success"])
        dense_rr += 1.0 / dense_success_rank if dense_success_rank else 0.0
        expanded_rr += 1.0 / result["rank"] if result["rank"] else 0.0
        fixed += int((dense_success_rank is None) and result["success"])
        avg_chars_total += total_chars_top5
        avg_merged_chunks_total += avg_merged_chunks_top5
        results.append(result)

    metrics = {
        "total": len(questions),
        f"dense_recall@{top_k}": dense_hits / len(questions) if questions else 0.0,
        f"recall@{top_k}": expanded_hits / len(questions) if questions else 0.0,
        "dense_mrr": dense_rr / len(questions) if questions else 0.0,
        "mrr": expanded_rr / len(questions) if questions else 0.0,
        "dense_hits_before_expansion": dense_hits,
        "hits": expanded_hits,
        "failed": len(questions) - expanded_hits,
        "fixed_by_expansion": fixed,
        "coverage_threshold": coverage_threshold,
        "neighbor_radius": radius,
        "avg_top5_total_chars": avg_chars_total / len(questions) if questions else 0.0,
        "avg_top5_chars_per_item": (avg_chars_total / len(questions) / top_k) if questions and top_k else 0.0,
        "avg_top5_merged_chunks": avg_merged_chunks_total / len(questions) if questions else 0.0,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / "retrieval_results.json", results)
    _write_json(out_dir / "metrics.json", metrics)
    _write_report(
        out_dir / "eval_report.md",
        metrics,
        results,
        {
            "index": str(index_dir),
            "questions": str(questions_path),
            "top_k": top_k,
            "coverage_threshold": coverage_threshold,
            "neighbor_radius": radius,
            "endpoint": endpoint,
            "model": model,
        },
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", required=True)
    parser.add_argument("--questions", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--endpoint", default="http://localhost:1234/v1/embeddings")
    parser.add_argument("--model", default="bge-small-en-v1.5")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--coverage-threshold", type=float, default=0.65)
    parser.add_argument("--radius", type=int, default=1)
    args = parser.parse_args()
    evaluate_neighbor_expansion(
        index_dir=args.index,
        questions_path=args.questions,
        out_dir=args.out,
        endpoint=args.endpoint,
        model=args.model,
        top_k=args.top_k,
        coverage_threshold=args.coverage_threshold,
        radius=args.radius,
    )


if __name__ == "__main__":
    main()
