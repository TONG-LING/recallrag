# RecallRAG

RecallRAG is a retrieval debugging and patch-index benchmark for long-document RAG.

This project is not a generic chatbot demo. It is built for a narrower and more practical question:

> The answer is in the document, so why does top-k still fail to return a complete evidence chunk?

The core claim is also narrow on purpose:

- It does not claim that a patch layer beats every production retrieval stack.
- It does claim that some retrieval failures are really local evidence-boundary failures.
- For that failure type, a small side patch index can recover missing evidence without rewriting the main index.

## What Problem This Project Targets

Many retrieval failures are not true document-level misses.

In this project, the gold document is often already near the top, but the returned chunk is incomplete:

- the chunk starts too early or too late
- the answer span is split across adjacent chunks
- the returned chunk contains the right document but not enough local evidence

RecallRAG treats this as a local repair problem.

Instead of rebuilding the whole corpus or claiming a brand new chunking method, it does the following:

1. Run baseline dense retrieval.
2. Diagnose failed queries.
3. Localize suspicious near-miss windows inside the gold document.
4. Materialize candidate patch chunks around those windows.
5. Validate patches in a separate side index.
6. Keep only patches that actually fix retrieval.

The main index is kept unchanged. The patch index is a small shadow layer.

## Core Idea

```text
baseline retrieval
-> failure diagnosis
-> local patch candidate generation
-> patch validation
-> keep only successful patches
-> evaluate main + patch
-> optionally serve main and patch as two Qdrant collections
```

The current implementation supports both:

- offline experiments with JSON chunk/vector files
- online shadow-index experiments with Qdrant

## How Success Is Measured

This project does not use a weak success definition such as:

- "the correct document appeared somewhere in the result list"

Instead, success means:

- within top-k, there is a chunk from the gold document
- and that chunk covers enough of the gold evidence span

Current formal setting:

- `top_k = 5`
- `coverage_threshold = 0.65`

In code, relevance is span-coverage based for span-style questions. That means this benchmark is specifically aimed at evidence completeness, not only document recall.

## Main Result Snapshot

Current primary benchmark:

- dataset: `case_zh_dureader_120/`
- main result directories: `runs/zh120_*`
- patch-source queries: `case_zh_dureader_120/eval/questions_patch_source.jsonl`
- held-out queries: `case_zh_dureader_120/eval/questions_heldout.jsonl`

### Main 120-query benchmark

| Route | Recall@5 | MRR | Hits |
|---|---:|---:|---:|
| `main` | 0.1417 | 0.0651 | 17 / 120 |
| `main + rerank` | 0.1333 | 0.0822 | 16 / 120 |
| `BM25` | 0.0667 | 0.0244 | 8 / 120 |
| `Dense + BM25` | 0.0917 | 0.0318 | 11 / 120 |
| `Dense + BM25 + RRF + rerank` | 0.1333 | 0.0822 | 16 / 120 |
| `HyDE + Dense + BM25 + RRF + rerank` | 0.1250 | 0.0739 | 15 / 120 |
| `main + patch` | 0.3417 | 0.1501 | 41 / 120 |
| `main + patch + rerank` | 0.3250 | 0.2001 | 39 / 120 |

Key reading:

- Patch is the strongest recall-improving route in this benchmark.
- Reranking helps ordering quality, but not recall.
- Stronger retrieval combinations such as BM25 hybrid, RRF, and HyDE do not remove the need for local evidence repair on this dataset.

### Held-out query generalization

This is the most important validity check in the repo.

- Patch selection is done on `questions_patch_source.jsonl`.
- The selected patch set is then frozen.
- That frozen patch set is evaluated on rewritten held-out queries in `questions_heldout.jsonl`.

| Route | Recall@5 | MRR | Hits |
|---|---:|---:|---:|
| `main` | 0.1417 | 0.0608 | 17 / 120 |
| `main + fixed patch` | 0.3250 | 0.1374 | 39 / 120 |

### Paired significance

Patch-source benchmark:

- `17 / 120 -> 41 / 120`
- wins: `24`
- losses: `0`
- exact McNemar p-value: `1.1920928955078125e-07`

Held-out benchmark:

- `17 / 120 -> 39 / 120`
- wins: `22`
- losses: `0`
- exact McNemar p-value: `4.76837158203125e-07`

Interpretation:

- The improvement is not just a reranking artifact.
- The improvement is not only visible on the same queries used to source the repairs.
- The fixed patch set still helps on new phrasings of the same evidence need.

## Why The Patch Result Matters

The main benchmark improvement comes from a very small repair footprint:

- main chunks: `1634`
- selected patch chunks: `24`
- patch/main ratio: `0.0147`

So the project is not "make everything bigger and hope recall increases".
It is "repair a narrow failure type with a small, validated side index".

## Repository Layout

```text
recallrag/                Core implementation
scripts/                  Dataset, held-out, and evaluation utilities
tests/                    Unit tests
case/                     Legacy English controlled case
case_beir/                Additional historical benchmark material
case_zh_dureader/         Earlier Chinese small benchmark
case_zh_dureader_120/     Current primary Chinese long-document benchmark
tools/qdrant/             Local Qdrant area for binary/server storage
```

Important modules:

```text
recallrag/eval.py              Dense retrieval evaluation and coverage-based scoring
recallrag/diagnose.py          Failure diagnosis
recallrag/patch_index.py       Patch materialization and offline validation
recallrag/bm25.py              BM25 and dense+BM25 baselines
recallrag/strong_baselines.py  RRF, reranking, and HyDE baselines
recallrag/qdrant_backend.py    Online main/patch collections with Qdrant
recallrag/reranker.py          Local cross-encoder reranker wrapper
recallrag/cli.py               CLI entrypoint
```

## Environment Requirements

Minimum:

- Python `3.10+`
- a shell environment that can run local Python scripts
- an OpenAI-compatible embedding endpoint exposing `/v1/embeddings`

Optional but recommended:

- a CUDA-capable GPU for reranker experiments
- PyTorch + Transformers for the local reranker
- a local Qdrant server for online shadow-index experiments

## Installation

### 1. Create a Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
pip install -e .
```

Optional API dependencies:

```bash
pip install "fastapi>=0.115,<1.0" "uvicorn>=0.30,<1.0"
```

### 2. Install reranker dependencies

The reranker is not part of the base runtime dependencies in `pyproject.toml`.
Install it manually when you need reranking:

```bash
pip install torch transformers
```

If you want a dedicated reranker environment, that is also fine.

### 3. Keep API keys out of commands

This repo now supports environment-variable based API keys for the two places that may call an external generation model:

```bash
cp .env.example .env
```

Then set:

- `RECALLRAG_HYDE_API_KEY` for HyDE generation in `eval-rrf-rerank`
- `RECALLRAG_QUERY_REWRITE_API_KEY` for `scripts/build_query_heldout.py`

This is safer than putting keys directly on the command line.

## Models And Services Used In The Current Main Experiment

### Embedding model

Current main Chinese benchmark:

- endpoint: `http://localhost:1234/v1/embeddings`
- model: `text-embedding-bge-large-zh-v1.5`
- vector dimension: `1024`

The embedding client expects an OpenAI-style response with:

- `data`
- one embedding per input row
- correct `index` ordering

### Reranker model

Current local cross-encoder reranker:

- model: `BAAI/bge-reranker-v2-m3`

Implementation details:

- code path: `recallrag/reranker.py`
- default Hugging Face model id: `BAAI/bge-reranker-v2-m3`
- if local path `/mnt/d/projects/hf_models/BAAI__bge-reranker-v2-m3` exists, the code prefers that path
- you can override with `RECALLRAG_RERANKER_MODEL`

### HyDE model

Current published `zh120` HyDE ablation recorded:

- HyDE enabled: `true`
- HyDE generation model: `deepseek-v4-flash`

Important detail:

- the generic code default in `recallrag/strong_baselines.py` is still `hy-mt2-1.8b`
- the current formal `zh120` result was not produced with that default
- the current held-out query rewrite file also records `deepseek-v4-flash`

### Database

For online shadow-index evaluation, this project uses Qdrant:

- default URL: `http://localhost:6333`
- default main collection: `recallrag_main`
- default patch collection: `recallrag_patch`

The Qdrant binary is not guaranteed to be bundled for future public use.
If `tools/qdrant/qdrant` is not present on your machine, provide your own local Qdrant server.

## Qdrant Setup

### Option A: use your own local Qdrant server

Run any local Qdrant instance that exposes:

```text
http://localhost:6333
```

### Option B: use the helper script

This repo includes:

- `scripts/start_qdrant.sh`

That script expects a local binary at:

- `tools/qdrant/qdrant`

If your binary is available there, start it with:

```bash
bash scripts/start_qdrant.sh
```

Health check:

```bash
python3 -m recallrag.cli qdrant-health --url http://localhost:6333
```

## Current Primary Dataset

Primary dataset directory:

- `case_zh_dureader_120/`

Source metadata is recorded in:

- `case_zh_dureader_120/source_metadata.json`

Current configuration:

| Field | Value |
|---|---|
| source | `zyznull/dureader-retrieval-ranking` dev subset |
| source URL | `https://huggingface.co/datasets/zyznull/dureader-retrieval-ranking/resolve/main/dev.jsonl.gz` |
| sample size | `120` |
| negatives per document | `4` |
| positive length range | `380` to `1400` |
| seed | `42` |
| documents | `120` |
| patch-source queries | `120` |
| held-out rewritten queries | `120` |

Data split files:

- `eval/questions.jsonl`: original evaluation questions
- `eval/questions_patch_source.jsonl`: explicit patch-source split used for patch generation
- `eval/questions_heldout.jsonl`: held-out rewritten queries for generalization check

## Current Main Experiment Configuration

From `runs/zh120_base/index_meta.json`:

| Field | Value |
|---|---|
| chunk size | `220` |
| overlap | `0` |
| keep heading | `true` |
| chunk count | `1634` |
| embedding model | `text-embedding-bge-large-zh-v1.5` |
| embedding dimension | `1024` |
| coverage threshold | `0.65` |

## Reproduce The Current Chinese Benchmark

### 1. Build the baseline index and run dense retrieval

```bash
python3 -m recallrag.cli run-baseline \
  --docs case_zh_dureader_120/docs \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_base \
  --chunk-size 220 \
  --overlap 0 \
  --keep-heading \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --coverage-threshold 0.65
```

### 2. Diagnose failed queries

```bash
python3 -m recallrag.cli diagnose \
  --index runs/zh120_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --coverage-threshold 0.65
```

### 3. Materialize patch candidates

```bash
python3 -m recallrag.cli materialize-patches \
  --index runs/zh120_base \
  --out runs/zh120_patches \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5
```

### 4. Evaluate baseline + selected patch index

```bash
python3 -m recallrag.cli eval-hybrid \
  --index runs/zh120_base \
  --patch-index runs/zh120_patches \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_hybrid \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --coverage-threshold 0.65
```

This step writes:

- `selected_patch_chunks.json`
- `selected_patch_vectors.json`

Those files are the frozen selected patch set used for later online or held-out evaluation.

## Reproduce Comparison Baselines

### Main + local reranker

```bash
python3 -m recallrag.cli eval-rerank \
  --index runs/zh120_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_rerank_main \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --candidate-k 20 \
  --coverage-threshold 0.65
```

### Main + fixed patch + rerank

This is the route behind the `39 / 120` result in `runs/zh120_patch_rerank`.

```bash
python3 scripts/eval_fixed_patch_rerank.py \
  --index runs/zh120_base \
  --patch-dir runs/zh120_patches \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_patch_rerank \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --candidate-k 20 \
  --coverage-threshold 0.65 \
  --reranker-model-path <local_or_hf_reranker_path>
```

### BM25 and dense+BM25

```bash
python3 -m recallrag.cli eval-bm25-hybrid \
  --index runs/zh120_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_hybrid_bm25 \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --coverage-threshold 0.65 \
  --alpha-dense 0.65
```

### Dense + BM25 + RRF + rerank

```bash
python3 -m recallrag.cli eval-rrf-rerank \
  --index runs/zh120_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_rrf_rerank \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --dense-k 20 \
  --bm25-k 20 \
  --candidate-k 20 \
  --rrf-k 60 \
  --coverage-threshold 0.65
```

### HyDE + Dense + BM25 + RRF + rerank

Example command shape:

```bash
python3 -m recallrag.cli eval-rrf-rerank \
  --index runs/zh120_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_rrf_rerank_hyde \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --dense-k 20 \
  --bm25-k 20 \
  --candidate-k 20 \
  --rrf-k 60 \
  --coverage-threshold 0.65 \
  --hyde-model deepseek-v4-flash \
  --hyde-endpoint <your_messages_endpoint> \
  --hyde-protocol messages \
  --hyde-auth-mode x-api-key \
  --hyde-disable-thinking
```

If `--hyde-api-key` is omitted, the code uses `RECALLRAG_HYDE_API_KEY`.

## Build And Evaluate Held-out Queries

### 1. Build the held-out rewritten queries

The repo includes a dedicated builder:

```bash
python3 scripts/build_query_heldout.py \
  --questions case_zh_dureader_120/eval/questions.jsonl \
  --out case_zh_dureader_120/eval/questions_heldout.jsonl \
  --patch-source-out case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --endpoint <your_messages_endpoint> \
  --model deepseek-v4-flash \
  --protocol messages \
  --auth-mode x-api-key \
  --disable-thinking
```

If `--api-key` is omitted, the script uses `RECALLRAG_QUERY_REWRITE_API_KEY`.

Current checked-in held-out file records:

- rewrite model: `deepseek-v4-flash`
- rewrite endpoint: `https://api.openmodel.ai/v1/messages`

### 2. Evaluate the frozen patch set on held-out queries

```bash
python3 scripts/eval_fixed_patch_generalization.py \
  --index runs/zh120_base \
  --patch-dir runs/zh120_patches \
  --questions case_zh_dureader_120/eval/questions_heldout.jsonl \
  --out runs/zh120_generalization \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --coverage-threshold 0.65
```

This is the correct generalization protocol for this project:

- patch selection happens first
- selected patch chunks are frozen
- held-out queries do not participate in patch generation or patch selection

## Online Shadow-Index Workflow With Qdrant

After `runs/zh120_base` and `runs/zh120_patches` are ready:

### 1. Build Qdrant collections

```bash
python3 -m recallrag.cli qdrant-build \
  --index runs/zh120_base \
  --patch-index runs/zh120_patches \
  --out runs/zh120_qdrant \
  --url http://localhost:6333 \
  --main-collection recallrag_main \
  --patch-collection recallrag_patch
```

### 2. Evaluate online main + patch retrieval

```bash
python3 -m recallrag.cli qdrant-eval \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_qdrant \
  --url http://localhost:6333 \
  --main-collection recallrag_main \
  --patch-collection recallrag_patch \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --main-k 5 \
  --patch-k 3 \
  --final-k 5 \
  --coverage-threshold 0.65
```

### 3. Evaluate online main + patch + rerank

```bash
python3 -m recallrag.cli qdrant-eval-rerank \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_qdrant_rerank \
  --url http://localhost:6333 \
  --main-collection recallrag_main \
  --patch-collection recallrag_patch \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --main-k 10 \
  --patch-k 5 \
  --final-k 5 \
  --coverage-threshold 0.65
```

## What The Current Results Say

The current evidence supports a specific conclusion:

- Many failed queries already retrieve the right document neighborhood.
- The missing part is often complete local evidence, not document identity.
- A small validated patch index can recover that evidence more effectively than the current rerank-only or hybrid-only baselines in this benchmark.

The current evidence does not support an over-broad conclusion such as:

- "patch index is always better than strong hybrid retrieval"
- "patch index replaces BM25, reranking, or HyDE in production"
- "every retrieval failure is a chunking failure"

This repo is intentionally narrower and more defensible than that.

## Limitations

- The benchmark is designed for long-document evidence-boundary failures, not for every retrieval regime.
- Patch helps only when there is a recoverable local evidence gap.
- Held-out validation here is query-held-out, not document-held-out.
- Qdrant online serving is supported, but the patch selection workflow is still an offline validation step.
- The repo keeps legacy English and earlier Chinese cases for historical comparison, but the current primary conclusion should come from `case_zh_dureader_120/` and `runs/zh120_*`.

## Testing

Run unit tests with:

```bash
python3 -m unittest discover -s tests -v
```

## Notes For Future Public Packaging

- Heavy run artifacts under `runs/` are local experiment outputs.
- Personal study material under `project_docs/` is intentionally not the source of truth for this README.
- The formal README above is aligned to the actual code paths and raw experiment outputs in this repository.
