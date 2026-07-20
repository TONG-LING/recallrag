# RecallRAG 实验运行手册

这份文档只放复现实验用的命令。项目思路和主要结果看 [README.md](README.md)。

## 0. 准备环境

```bash
cd /mnt/d/projects/recallrag
source .venv/bin/activate
```

确认 embedding 服务可用：

```text
http://localhost:1234/v1/embeddings
```

当前主实验 embedding 模型：

```text
text-embedding-bge-large-zh-v1.5
```

## 一键本地工程评估

该脚本会检查 embedding endpoint 和本地 Qdrant，按指定题目数量运行 baseline、diagnosis、patch、hybrid eval、BM25 countercheck、Qdrant 双集合验证和 final triage，并在项目内的 `temp/` 下生成完整临时产物和中文评估报告，`temp/` 已加入 `.gitignore`。运行前需要确保 Qdrant 已启动。

运行 120 题：

```bash
./scripts/run_local_engineering_eval.sh --limit 120
```

运行小样本调试：

```bash
./scripts/run_local_engineering_eval.sh --limit 10
```


常用参数：

```bash
./scripts/run_local_engineering_eval.sh \
  --limit 120 \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --qdrant-url http://localhost:6333 \
  --chunk-size 600 \
  --overlap 0 \
  --out temp/engineering_eval_120
```

输出入口：

```text
report/latest_report.md
report/report_<run_id>_n<limit>_c<chunk_size>_o<overlap>.md
temp/<run>/report.md
temp/<run>/runs/base/failure_diagnosis.md
temp/<run>/runs/hybrid/comparison_report.md
temp/<run>/runs/triage/final_triage_report.md
temp/<run>/logs/
```

`report.md` 和 `report/latest_report.md` 包含结论摘要、运行环境、评估设置、向量库检索结果、修复稳定性、失败问题和补丁决策、已接受补丁明细、检索策略对照、结论边界和文件位置。

## 1. 诊断版 `220/0`

这个设置主要用来暴露 chunk 边界问题。

### 1.1 Baseline

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

### 1.2 诊断失败 query

```bash
python3 -m recallrag.cli diagnose \
  --index runs/zh120_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_base \
  --coverage-threshold 0.65
```

### 1.3 生成 patch candidates

```bash
python3 -m recallrag.cli materialize-patches \
  --index runs/zh120_base \
  --out runs/zh120_patches \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5
```

### 1.4 评估 `main + patch`

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

### 1.5 配对检验

```bash
python3 scripts/paired_significance.py \
  --before runs/zh120_base/retrieval_results.json \
  --after runs/zh120_hybrid/retrieval_results.json \
  --out-json runs/zh120_hybrid/paired_significance.json \
  --out-md runs/zh120_hybrid/paired_significance.md
```

## 2. Reranker 和主流检索对照

### 2.1 Dense + rerank

```bash
python3 -m recallrag.cli eval-rerank \
  --index runs/zh120_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_rerank_main \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --candidate-k 20 \
  --coverage-threshold 0.65 \
  --reranker-model-path /mnt/d/projects/hf_models/BAAI__bge-reranker-v2-m3 \
  --reranker-device cuda:0
```

### 2.2 `main + patch + rerank`

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
  --reranker-model-path /mnt/d/projects/hf_models/BAAI__bge-reranker-v2-m3 \
  --reranker-device cuda:0
```

### 2.3 BM25 / Dense + BM25

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

### 2.4 Dense + BM25 + RRF + rerank

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
  --coverage-threshold 0.65 \
  --reranker-model-path /mnt/d/projects/hf_models/BAAI__bge-reranker-v2-m3 \
  --reranker-device cuda:0
```

### 2.5 HyDE + Dense + BM25 + RRF + rerank

HyDE 需要设置 API key：

```bash
export RECALLRAG_HYDE_API_KEY=<your_key>
```

```bash
python3 -m recallrag.cli eval-rrf-rerank \
  --index runs/zh120_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_hyde_rrf_rerank \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --dense-k 20 \
  --bm25-k 20 \
  --candidate-k 20 \
  --rrf-k 60 \
  --coverage-threshold 0.65 \
  --reranker-model-path /mnt/d/projects/hf_models/BAAI__bge-reranker-v2-m3 \
  --reranker-device cuda:0 \
  --hyde-model deepseek-v4-flash \
  --hyde-endpoint <your_hyde_endpoint> \
  --hyde-protocol messages \
  --hyde-auth-mode x-api-key \
  --hyde-disable-thinking
```

## 3. Held-out query 检查

### 3.1 生成 held-out 改写 query

```bash
export RECALLRAG_QUERY_REWRITE_API_KEY=<your_key>
```

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

### 3.2 用冻结 patch 评估 held-out query

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

## 4. 更强切分和相邻块扩展

### 4.1 overlap 和大 chunk 对照

```bash
python3 -m recallrag.cli run-baseline \
  --docs case_zh_dureader_120/docs \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_c220_o50_base \
  --chunk-size 220 \
  --overlap 50 \
  --keep-heading \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --batch-size 4 \
  --top-k 5 \
  --coverage-threshold 0.65

python3 -m recallrag.cli run-baseline \
  --docs case_zh_dureader_120/docs \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_c220_o100_base \
  --chunk-size 220 \
  --overlap 100 \
  --keep-heading \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --batch-size 4 \
  --top-k 5 \
  --coverage-threshold 0.65

python3 -m recallrag.cli run-baseline \
  --docs case_zh_dureader_120/docs \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_c400_o0_base \
  --chunk-size 400 \
  --overlap 0 \
  --keep-heading \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --batch-size 4 \
  --top-k 5 \
  --coverage-threshold 0.65

python3 -m recallrag.cli run-baseline \
  --docs case_zh_dureader_120/docs \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_c600_o0_base \
  --chunk-size 600 \
  --overlap 0 \
  --keep-heading \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --batch-size 4 \
  --top-k 5 \
  --coverage-threshold 0.65
```

### 4.2 相邻块扩展 baseline

```bash
PYTHONPATH=. python3 scripts/eval_neighbor_expansion.py \
  --index runs/zh120_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_neighbor_r1 \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --coverage-threshold 0.65 \
  --radius 1
```

```bash
PYTHONPATH=. python3 scripts/eval_neighbor_expansion.py \
  --index runs/zh120_c600_o0_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_c600_o0_neighbor_r1 \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --coverage-threshold 0.65 \
  --radius 1
```

## 5. 较强固定切分 `600/0 + patch`

```bash
python3 -m recallrag.cli diagnose \
  --index runs/zh120_c600_o0_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --coverage-threshold 0.65

python3 -m recallrag.cli materialize-patches \
  --index runs/zh120_c600_o0_base \
  --out runs/zh120_c600_o0_patches \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --batch-size 4

python3 -m recallrag.cli eval-hybrid \
  --index runs/zh120_c600_o0_base \
  --patch-index runs/zh120_c600_o0_patches \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_c600_o0_hybrid \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --coverage-threshold 0.65
```

配对检验：

```bash
python3 scripts/paired_significance.py \
  --before runs/zh120_c600_o0_base/retrieval_results.json \
  --after runs/zh120_c600_o0_hybrid/retrieval_results.json \
  --out-json runs/zh120_c600_o0_hybrid/paired_significance.json \
  --out-md runs/zh120_c600_o0_hybrid/paired_significance.md
```

单独评估 `600/0 + rerank`：

```bash
python3 -m recallrag.cli eval-rerank \
  --index runs/zh120_c600_o0_base \
  --questions case_zh_dureader_120/eval/questions_patch_source.jsonl \
  --out runs/zh120_c600_o0_rerank \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --candidate-k 20 \
  --coverage-threshold 0.65 \
  --reranker-model-path /mnt/d/projects/hf_models/BAAI__bge-reranker-v2-m3 \
  --reranker-device cuda:0
```

held-out：

```bash
PYTHONPATH=. python3 scripts/eval_fixed_patch_generalization.py \
  --index runs/zh120_c600_o0_base \
  --patch-dir runs/zh120_c600_o0_patches \
  --questions case_zh_dureader_120/eval/questions_heldout.jsonl \
  --out runs/zh120_c600_o0_generalization \
  --endpoint http://localhost:1234/v1/embeddings \
  --model text-embedding-bge-large-zh-v1.5 \
  --top-k 5 \
  --coverage-threshold 0.65
```

## 6. Qdrant 双集合

先启动 Qdrant。可以用自己的 Qdrant，也可以在 `tools/qdrant/qdrant` 存在时运行：

```bash
bash scripts/start_qdrant.sh
```

构建 main collection 和 patch collection：

```bash
python3 -m recallrag.cli qdrant-build \
  --index runs/zh120_base \
  --patch-index runs/zh120_patches \
  --out runs/zh120_qdrant \
  --url http://localhost:6333 \
  --main-collection recallrag_main \
  --patch-collection recallrag_patch
```

评估 main + patch：

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

评估 main + patch + rerank：

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
  --coverage-threshold 0.65 \
  --reranker-model-path /mnt/d/projects/hf_models/BAAI__bge-reranker-v2-m3 \
  --reranker-device cuda:0
```

## 7. 测试

```bash
python3 -m unittest discover -s tests -v
```

## 8. 附属实验：reranker 微调

这个实验位于：

```text
experiments/reranker_boundary_finetune/
```

它依赖 `600/0` 检索结果：

```text
runs/zh120_c600_o0_base/chunks.json
runs/zh120_c600_o0_base/retrieval_results.json
```

运行：

```bash
cd experiments/reranker_boundary_finetune
python3 -m pip install -r requirements.txt
bash run_example.sh
```

核心结果：

```text
Recall@5: 0.944444 -> 0.944444
MRR:      0.668519 -> 0.824074
hits:     17 / 18  -> 17 / 18
```

这个结果说明它主要改善排序质量，不负责扩大候选召回。
运行产生的训练样本、模型和详细输出默认写入 `data/`、`outputs/`，这些目录不会提交到仓库。
