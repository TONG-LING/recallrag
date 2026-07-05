#!/usr/bin/env bash
set -euo pipefail
python3 -m recallrag.cli run-baseline \
  --docs case/docs \
  --questions case/eval/questions.jsonl \
  --out runs/base \
  --chunk-size 260 \
  --overlap 0 \
  --top-k 5 \
  --coverage-threshold 0.65
python3 -m recallrag.cli diagnose \
  --index runs/base \
  --questions case/eval/questions.jsonl \
  --coverage-threshold 0.65
python3 -m recallrag.cli materialize-patches \
  --index runs/base \
  --out runs/patches
python3 -m recallrag.cli eval-hybrid \
  --index runs/base \
  --patch-index runs/patches \
  --questions case/eval/questions.jsonl \
  --out runs/hybrid \
  --top-k 5 \
  --coverage-threshold 0.65
