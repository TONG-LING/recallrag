#!/usr/bin/env bash
set -euo pipefail
# Requires LM Studio embedding endpoint at http://localhost:1234/v1/embeddings
# Requires Qdrant server for qdrant-build/eval steps.

python3 scripts/import_beir_scifact.py
python3 scripts/import_beir_dataset.py --src datasets/beir/nfcorpus/nfcorpus --name NFCorpus --out case_beir/nfcorpus --max-queries 80 --distractors 700

python3 -m recallrag.cli run-baseline --docs case_beir/scifact/docs --questions case_beir/scifact/eval/questions.jsonl --out runs/scifact_base --chunk-size 520 --overlap 80 --keep-heading --top-k 5 --coverage-threshold 0.65
python3 -m recallrag.cli diagnose --index runs/scifact_base --questions case_beir/scifact/eval/questions.jsonl --out runs/scifact_base --coverage-threshold 0.65
python3 -m recallrag.cli materialize-patches --index runs/scifact_base --out runs/scifact_patches
python3 -m recallrag.cli eval-hybrid --index runs/scifact_base --patch-index runs/scifact_patches --questions case_beir/scifact/eval/questions.jsonl --out runs/scifact_hybrid --top-k 5 --coverage-threshold 0.65
python3 -m recallrag.cli eval-bm25-hybrid --index runs/scifact_base --questions case_beir/scifact/eval/questions.jsonl --out runs/scifact_hybrid_bm25 --top-k 5 --coverage-threshold 0.65 --alpha-dense 0.65
python3 -m recallrag.cli qdrant-build --index runs/scifact_base --patch-index runs/scifact_patches --out runs/scifact_qdrant --url http://localhost:6333 --main-collection recallrag_scifact_main --patch-collection recallrag_scifact_patch
python3 -m recallrag.cli qdrant-eval --questions case_beir/scifact/eval/questions.jsonl --out runs/scifact_qdrant_main --url http://localhost:6333 --main-collection recallrag_scifact_main --patch-collection recallrag_scifact_patch --main-k 5 --patch-k 0 --final-k 5 --coverage-threshold 0.65
python3 -m recallrag.cli qdrant-eval --questions case_beir/scifact/eval/questions.jsonl --out runs/scifact_qdrant --url http://localhost:6333 --main-collection recallrag_scifact_main --patch-collection recallrag_scifact_patch --main-k 5 --patch-k 3 --final-k 5 --coverage-threshold 0.65
python3 -m recallrag.cli qdrant-compare --main-only-dir runs/scifact_qdrant_main --main-patch-dir runs/scifact_qdrant --out runs/scifact_qdrant/qdrant_comparison_report.md

python3 -m recallrag.cli run-baseline --docs case_beir/nfcorpus/docs --questions case_beir/nfcorpus/eval/questions.jsonl --out runs/nfcorpus_base --chunk-size 520 --overlap 80 --keep-heading --top-k 5 --coverage-threshold 0.65
python3 -m recallrag.cli diagnose --index runs/nfcorpus_base --questions case_beir/nfcorpus/eval/questions.jsonl --out runs/nfcorpus_base --coverage-threshold 0.65
python3 -m recallrag.cli materialize-patches --index runs/nfcorpus_base --out runs/nfcorpus_patches
python3 -m recallrag.cli eval-hybrid --index runs/nfcorpus_base --patch-index runs/nfcorpus_patches --questions case_beir/nfcorpus/eval/questions.jsonl --out runs/nfcorpus_hybrid --top-k 5 --coverage-threshold 0.65
python3 -m recallrag.cli eval-bm25-hybrid --index runs/nfcorpus_base --questions case_beir/nfcorpus/eval/questions.jsonl --out runs/nfcorpus_hybrid_bm25 --top-k 5 --coverage-threshold 0.65 --alpha-dense 0.65
python3 -m recallrag.cli qdrant-build --index runs/nfcorpus_base --patch-index runs/nfcorpus_patches --out runs/nfcorpus_qdrant --url http://localhost:6333 --main-collection recallrag_nfcorpus_main --patch-collection recallrag_nfcorpus_patch
python3 -m recallrag.cli qdrant-eval --questions case_beir/nfcorpus/eval/questions.jsonl --out runs/nfcorpus_qdrant_main --url http://localhost:6333 --main-collection recallrag_nfcorpus_main --patch-collection recallrag_nfcorpus_patch --main-k 5 --patch-k 0 --final-k 5 --coverage-threshold 0.65
python3 -m recallrag.cli qdrant-eval --questions case_beir/nfcorpus/eval/questions.jsonl --out runs/nfcorpus_qdrant --url http://localhost:6333 --main-collection recallrag_nfcorpus_main --patch-collection recallrag_nfcorpus_patch --main-k 5 --patch-k 3 --final-k 5 --coverage-threshold 0.65
python3 -m recallrag.cli qdrant-compare --main-only-dir runs/nfcorpus_qdrant_main --main-patch-dir runs/nfcorpus_qdrant --out runs/nfcorpus_qdrant/qdrant_comparison_report.md

python3 scripts/make_generalization_report.py
