# Boundary-aware Reranker Fine-tuning

这个目录是 RecallRAG 的附属实验。

主项目主要处理一种情况：

```text
候选池里没有完整证据 -> 用 Patch Index 补证据
```

这个实验处理另一种情况：

```text
候选池里已经有完整证据 -> 用 reranker 把完整证据排到半截证据前面
```

它不是通用 reranker 微调，也不负责扩大召回候选池。它只验证一个更具体的问题：

> 当 dense retrieval 的 Top-k 里同时存在完整答案块和半截答案块时，能不能让 cross-encoder reranker 更偏向完整答案块？

## 数据构造

数据来自主项目的 `600/0` 检索结果：

```text
runs/zh120_c600_o0_base/chunks.json
runs/zh120_c600_o0_base/retrieval_results.json
case_zh_dureader_120/eval/questions_patch_source.jsonl
```

每道题只看 dense retrieval 的 Top-30 候选，然后按 `gold_doc + gold_span` 计算 coverage。

样本分三类：

| kind | label | meaning |
|---|---:|---|
| `positive_complete_evidence` | `1` | 正确文档，且 coverage >= 0.65 |
| `same_doc_incomplete` | `0` | 正确文档，但只覆盖半截答案 |
| `high_rank_wrong_doc` | `0` | 排名靠前，但文档不对 |

采样策略：

```text
每题最多 1 个完整答案块
每题最多 3 个半截答案块
每题最多 1 个高排错文档块
```

这样做的目的不是重新训练一个通用 reranker，而是让模型重点学会区分：

```text
同一篇正确文档里的完整证据块 和 半截证据块
```

## 当前结果

120 道题按固定 seed 划分成 train / dev / test，当前 test split 是 `18` 题。

| metric | base reranker | fine-tuned reranker |
|---|---:|---:|
| Recall@5 | 0.944444 | 0.944444 |
| MRR | 0.668519 | 0.824074 |
| hits | 17 / 18 | 17 / 18 |
| rerank_improved | 6 | 10 |
| rerank_regressed | 0 | 0 |

解释：

- Recall@5 没有变，因为这个实验不扩大候选池。
- MRR 上升，说明完整答案块被排得更靠前。
- `candidate_missing_positive = 1`，说明有 1 道题的 Top-20 里本来就没有完整答案块，reranker 无法修复。

默认训练配置：

| setting | value |
|---|---:|
| base model | `BAAI/bge-reranker-base` |
| epochs | `2` |
| batch size | `8` |
| learning rate | `2e-5` |
| max length | `512` |
| warmup steps | `8` |
| train pairs | `346` |
| dev pairs | `81` |

轻量结果保存在：

```text
results/compare_report.md
results/eval_base_test/metrics.json
results/eval_finetuned_test/metrics.json
results/train/train_config.json
```

训练后的模型、候选数据和大 JSON 不提交到仓库。
本地重跑后，训练目录额外生成：

```text
outputs/.../loss_history.jsonl
outputs/.../loss_curve.png
```

## 运行方式

先确保主项目已经生成了 `600/0` 检索结果，尤其是：

```text
runs/zh120_c600_o0_base/chunks.json
runs/zh120_c600_o0_base/retrieval_results.json
```

安装依赖：

```bash
cd experiments/reranker_boundary_finetune
python3 -m pip install -r requirements.txt
```

一键运行：

```bash
bash run_example.sh
```

默认流程：

```text
1. 从主项目 Top-30 检索结果构造训练样本
2. 评估 base reranker
3. 微调 BAAI/bge-reranker-base
4. 保存 step-level loss_history.jsonl 和 loss_curve.png
5. 评估 fine-tuned reranker
6. 输出 before/after 对比
```

默认模型是：

```text
BAAI/bge-reranker-base
```

如果本地已有模型，可以这样指定：

```bash
MODEL_NAME_OR_PATH=/path/to/bge-reranker-base bash run_example.sh
```

## 和主项目的关系

这个实验的定位是排序侧补充：

- RecallRAG 主线：解决“完整证据不在候选池里”的问题。
- Reranker 微调：解决“完整证据在候选池里，但排序不够靠前”的问题。

因此它适合作为主项目的附属实验，而不是单独开一个项目。
