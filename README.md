# RecallRAG

RecallRAG is a retrieval debugging benchmark for long-document RAG. It comes from one practical question:

> The answer is in the document, so why does top-k still fail to return a complete evidence chunk?

This repo focuses on a specific failure mode:

- the right document is already being retrieved
- but the retrieved chunk is incomplete
- the answer span is split across local chunk boundaries

In this repo, I treat that as a local repair problem. Instead of rebuilding the full corpus, RecallRAG adds a small validated side index of local repair chunks, referred to here as the patch index.

## Core Idea

```text
baseline dense retrieval
-> diagnose failed queries
-> localize suspicious near-miss windows
-> materialize patch candidates
-> validate patches in a side index
-> keep only successful patches
-> evaluate main + patch
```

The main index stays unchanged. The patch index acts as a small shadow layer.

## What Counts As Success

This benchmark uses a stricter criterion than "the gold document appeared somewhere in the results."

A query is counted as successful only when:

- a top-k result comes from the gold document
- and that chunk covers enough of the gold evidence span

Main setup:

| Item | Value |
|---|---|
| top-k | `5` |
| coverage threshold | `0.65` |
| dataset | `case_zh_dureader_120/` |
| chunk size | `220` |
| overlap | `0` |
| keep heading | `true` |
| main chunks | `1634` |
| selected patch chunks | `24` |

So Recall@5 here means:

- top-5 contains a sufficiently complete evidence chunk
- not just "top-5 contains the right document"

## Main Results

Primary benchmark:

- patch-source queries: `case_zh_dureader_120/eval/questions_patch_source.jsonl`
- held-out queries: `case_zh_dureader_120/eval/questions_heldout.jsonl`
- main result directories: `runs/zh120_*`

### 120-query main benchmark

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

On this benchmark:

- patch is the strongest recall-improving route in this benchmark
- reranking improves ordering, but not recall
- stronger retrieval combinations still do not remove the local evidence-boundary problem here

### Held-out query generalization

The selected patch set is frozen first, then evaluated on rewritten held-out queries.

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

The main takeaway is simple:

- many failures are local evidence-boundary failures
- a tiny validated patch layer can fix them
- the effect is still visible on held-out query rewrites

## Repository Layout

```text
recallrag/                Core implementation
scripts/                  Dataset and evaluation utilities
tests/                    Unit tests
case/                     Legacy English controlled case
case_beir/                Historical benchmark material
case_zh_dureader/         Earlier Chinese benchmark
case_zh_dureader_120/     Current main Chinese benchmark
tools/qdrant/             Local Qdrant area
```

Important modules:

```text
recallrag/eval.py              Dense retrieval and coverage scoring
recallrag/diagnose.py          Failure diagnosis
recallrag/patch_index.py       Patch generation and offline validation
recallrag/bm25.py              BM25 and dense+BM25 baselines
recallrag/strong_baselines.py  RRF, rerank, and HyDE baselines
recallrag/qdrant_backend.py    Qdrant main/patch serving
recallrag/reranker.py          Local cross-encoder reranker
recallrag/cli.py               CLI entrypoint
```

## Environment

Minimum:

- Python `3.10+`
- an OpenAI-compatible embedding endpoint at `/v1/embeddings`

Recommended:

- GPU for reranker experiments
- `torch` and `transformers`
- local Qdrant for online shadow-index evaluation

Install:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
pip install -e .
pip install torch transformers
```

Optional API serving extras:

```bash
pip install "fastapi>=0.115,<1.0" "uvicorn>=0.30,<1.0"
```

## Main Experiment Setup

| Component | Current main setting |
|---|---|
| embedding endpoint | `http://localhost:1234/v1/embeddings` |
| embedding model | `text-embedding-bge-large-zh-v1.5` |
| embedding dimension | `1024` |
| reranker model | `BAAI/bge-reranker-v2-m3` |
| HyDE model in the current `zh120` run | `deepseek-v4-flash` |
| Qdrant URL | `http://localhost:6333` |
| main collection | `recallrag_main` |
| patch collection | `recallrag_patch` |

Practical notes:

- `recallrag/reranker.py` prefers local path `/mnt/d/projects/hf_models/BAAI__bge-reranker-v2-m3` if it exists.
- `recallrag/strong_baselines.py` still has a generic HyDE default of `hy-mt2-1.8b`, but the current formal `zh120` HyDE result was produced with `deepseek-v4-flash`.
- If `tools/qdrant/qdrant` is not present, use your own local Qdrant server.

## API Keys

Use environment variables instead of putting keys directly on the command line.

`.env.example` includes:

```bash
RECALLRAG_HYDE_API_KEY=
RECALLRAG_QUERY_REWRITE_API_KEY=
```

These are used by:

- `RECALLRAG_HYDE_API_KEY`: HyDE generation in `eval-rrf-rerank`
- `RECALLRAG_QUERY_REWRITE_API_KEY`: `scripts/build_query_heldout.py`

## Dataset

Current main dataset: `case_zh_dureader_120/`

Source metadata is recorded in `case_zh_dureader_120/source_metadata.json`.

| Field | Value |
|---|---|
| source | `zyznull/dureader-retrieval-ranking` dev subset |
| source URL | `https://huggingface.co/datasets/zyznull/dureader-retrieval-ranking/resolve/main/dev.jsonl.gz` |
| sample size | `120` |
| negatives per document | `4` |
| positive length range | `380` to `1400` |
| seed | `42` |

Split files:

- `eval/questions.jsonl`: original questions
- `eval/questions_patch_source.jsonl`: patch-source split
- `eval/questions_heldout.jsonl`: held-out rewritten split

## Reproducing The Main Benchmark

### 1. Baseline

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

### 2. Diagnose and build patch candidates

```bash
python3 -m recallrag.cli diagnose \
  --index runs/zh120_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --coverage-threshold 0.65

python3 -m recallrag.cli materialize-patches \
  --index runs/zh120_base \
  --out runs/zh120_patches \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5
```

### 3. Evaluate baseline + patch

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

This step writes the selected patch set used in later runs:

- `selected_patch_chunks.json`
- `selected_patch_vectors.json`

### 4. Main comparison baselines

Main rerank:

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

BM25 / dense+BM25:

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

RRF + rerank, optionally with HyDE:

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

Fixed patch + rerank:

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

## Held-out Evaluation

Build the held-out rewrites:

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

Evaluate the frozen patch set on held-out queries:

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

## Qdrant Workflow

Start your own Qdrant server, or use `bash scripts/start_qdrant.sh` if `tools/qdrant/qdrant` is available.

Build collections:

```bash
python3 -m recallrag.cli qdrant-build \
  --index runs/zh120_base \
  --patch-index runs/zh120_patches \
  --out runs/zh120_qdrant \
  --url http://localhost:6333 \
  --main-collection recallrag_main \
  --patch-collection recallrag_patch
```

Evaluate online main + patch:

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

Evaluate online main + patch + rerank:

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

## Limitations

- This project targets evidence-boundary failures, not every retrieval problem.
- Patch helps only when there is a recoverable local evidence gap.
- The held-out check is query-held-out, not document-held-out.
- Online Qdrant serving is supported, but patch selection is still an offline validation step.
- The primary conclusion should come from `case_zh_dureader_120/` and `runs/zh120_*`.

## Testing

```bash
python3 -m unittest discover -s tests -v
```
