#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from recallrag.embeddings import require_equal_length
from recallrag.eval import evaluate_with_reranker, load_questions, write_rerank_report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Evaluate main + fixed selected patch with local reranker."
    )
    parser.add_argument("--index", default="runs/zh_base", help="Main index directory")
    parser.add_argument("--patch-dir", default="runs/zh_patches", help="Patch dir with selected patch artifacts")
    parser.add_argument("--questions", default="case_zh_dureader/eval/questions.jsonl", help="Questions jsonl")
    parser.add_argument("--out", default="runs/zh_patch_rerank", help="Output directory")
    parser.add_argument("--endpoint", default="http://localhost:1234/v1/embeddings", help="Embedding endpoint")
    parser.add_argument("--model", default="text-embedding-bge-large-zh-v1.5", help="Embedding model")
    parser.add_argument("--top-k", type=int, default=5, help="Top-k")
    parser.add_argument("--candidate-k", type=int, default=20, help="Rerank candidate_k")
    parser.add_argument("--coverage-threshold", type=float, default=0.65, help="Coverage threshold")
    parser.add_argument("--reranker-model-path", required=True, help="Local reranker model path")
    parser.add_argument("--reranker-device", default=None, help="Reranker device")
    parser.add_argument("--reranker-batch-size", type=int, default=8, help="Reranker batch size")
    parser.add_argument("--reranker-max-length", type=int, default=512, help="Reranker max length")
    parser.add_argument("--reranker-no-fp16", action="store_true", help="Disable fp16")
    return parser.parse_args()


def _load_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _write_json(path: str | Path, obj) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    args = parse_args()
    main_chunks = _load_json(Path(args.index) / "chunks.json")
    main_vectors = _load_json(Path(args.index) / "vectors.json")
    patch_chunks = _load_json(Path(args.patch_dir) / "selected_patch_chunks.json")
    patch_vectors = _load_json(Path(args.patch_dir) / "selected_patch_vectors.json")
    require_equal_length("main_chunks", main_chunks, "main_vectors", main_vectors, "eval_fixed_patch_rerank.main")
    require_equal_length("patch_chunks", patch_chunks, "patch_vectors", patch_vectors, "eval_fixed_patch_rerank.patch")
    questions = load_questions(args.questions)

    chunks = main_chunks + patch_chunks
    vectors = main_vectors + patch_vectors
    results, metrics = evaluate_with_reranker(
        chunks,
        vectors,
        questions,
        endpoint=args.endpoint,
        model=args.model,
        top_k=args.top_k,
        candidate_k=args.candidate_k,
        coverage_threshold=args.coverage_threshold,
        reranker_model_path=args.reranker_model_path,
        reranker_device=args.reranker_device,
        reranker_batch_size=args.reranker_batch_size,
        reranker_max_length=args.reranker_max_length,
        reranker_use_fp16=not args.reranker_no_fp16,
    )

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / "retrieval_results.json", results)
    _write_json(out_dir / "metrics.json", metrics)
    write_rerank_report(
        out_dir / "eval_report.md",
        metrics,
        results,
        {
            "mode": "main_plus_fixed_patch_rerank",
            "index": args.index,
            "patch_dir": args.patch_dir,
            "questions": args.questions,
            "top_k": args.top_k,
            "candidate_k": args.candidate_k,
            "coverage_threshold": args.coverage_threshold,
            "endpoint": args.endpoint,
            "model": args.model,
            "reranker_model_path": args.reranker_model_path,
            "reranker_device": args.reranker_device,
            "reranker_batch_size": args.reranker_batch_size,
            "reranker_max_length": args.reranker_max_length,
            "reranker_use_fp16": not args.reranker_no_fp16,
            "selected_patch_chunks": len(patch_chunks),
        },
    )
    print(json.dumps(metrics, ensure_ascii=False, indent=2))
    print(f"wrote fixed patch rerank report -> {out_dir / 'eval_report.md'}")


if __name__ == "__main__":
    main()
