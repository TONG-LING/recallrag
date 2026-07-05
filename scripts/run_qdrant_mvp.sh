#!/usr/bin/env bash
set -euo pipefail
python3 -m recallrag.cli qdrant-health --url http://localhost:6333
python3 -m recallrag.cli qdrant-build \
  --index runs/base \
  --patch-index runs/patches \
  --out runs/qdrant \
  --url http://localhost:6333 \
  --main-collection recallrag_main \
  --patch-collection recallrag_patch
python3 -m recallrag.cli qdrant-eval \
  --questions case/eval/questions.jsonl \
  --out runs/qdrant_main \
  --url http://localhost:6333 \
  --main-collection recallrag_main \
  --patch-collection recallrag_patch \
  --main-k 5 \
  --patch-k 0 \
  --final-k 5 \
  --coverage-threshold 0.65
python3 -m recallrag.cli qdrant-eval \
  --questions case/eval/questions.jsonl \
  --out runs/qdrant \
  --url http://localhost:6333 \
  --main-collection recallrag_main \
  --patch-collection recallrag_patch \
  --main-k 5 \
  --patch-k 3 \
  --final-k 5 \
  --coverage-threshold 0.65
python3 -m recallrag.cli qdrant-compare \
  --main-only-dir runs/qdrant_main \
  --main-patch-dir runs/qdrant \
  --out runs/qdrant/qdrant_comparison_report.md
python3 -m recallrag.cli eval-bm25-hybrid \
  --index runs/base \
  --questions case/eval/questions.jsonl \
  --out runs/hybrid_bm25 \
  --top-k 5 \
  --coverage-threshold 0.65 \
  --alpha-dense 0.65
python3 -m recallrag.cli final-triage \
  --base-dir runs/base \
  --patch-eval-dir runs/hybrid \
  --bm25-dir runs/hybrid_bm25 \
  --qdrant-dir runs/qdrant \
  --out runs/triage
