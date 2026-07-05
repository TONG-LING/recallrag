# RecallRAG

RecallRAG 不是普通的 RAG 应用演示。

它是一个用于排查检索失败的实验系统，要解决的问题是：

> 文档里明明有答案，为什么 topK 里还是没有完整的证据块？

现在重点不是“给 RAG 多加一个 patch 层就一定更强”，而是：

```text
baseline 检索失败
-> 判断是不是 chunk / local context 问题
-> 只对可疑局部窗口生成备选 patch
-> 用独立 patch index 单独验证
-> 只保留验证有效的局部修补
```

## 当前主要结论

当前正式讲的版本是：

- 中文复杂文档扩样实验：`case_zh_dureader_120/`
- 主结果目录：`runs/zh120_*`
- 新问法验证：`case_zh_dureader_120/eval/questions_heldout.jsonl`
- 小样本机制验证：`case_zh_dureader/` + `runs/zh_*`
- Qdrant 双集合：`recallrag_zh_main` + `recallrag_zh_patch`
- 本地 reranker：`BAAI/bge-reranker-v2-m3`
- 主流对照：BM25、Dense+BM25、RRF、HyDE

旧英文 controlled case 还保留着，但现在只算历史记录，不再作为主结果。

## 当前主要结果

### 扩样主对照（120 条）

| 路线 | Recall@5 | MRR | 说明 |
|---|---:|---:|---|
| `main` | 0.1417 | 0.0651 | `17 / 120`，能检索到相关文档，但完整的证据块不够 |
| `main + rerank` | 0.1333 | 0.0822 | MRR 提升，但召回降到 `16 / 120` |
| `BM25` | 0.0667 | 0.0244 | 纯词法召回更弱 |
| `Dense + BM25` | 0.0917 | 0.0318 | 在这批问题上没有超过 dense |
| `Dense + BM25 + RRF + rerank` | 0.1333 | 0.0822 | 没有超过 dense baseline |
| `HyDE + Dense + BM25 + RRF + rerank` | 0.1250 | 0.0739 | HyDE 在这批问题上也没有提高召回 |
| `main + patch` | 0.3417 | 0.1501 | `41 / 120`，新增了一批命中 |
| `main + patch + rerank` | 0.3250 | 0.2001 | 排序更好，但召回掉到 `39 / 120` |

### 新问法验证（固定 patch，不重选）

| 路线 | Recall@5 | MRR | 说明 |
|---|---:|---:|
| `main` | 0.1417 | 0.0608 | 改写 query 后 baseline 基本不变 |
| `main + fixed patch` | 0.3250 | 0.1374 | `39 / 120`，固定 patch 对新问法仍然有效 |

这里需要特别说明：

> 这里的 Recall@5，不是“有没有检索到正确文档”，  
> 而是“前 5 个结果里有没有足够完整的证据块”。

### paired 统计

120 条扩样主实验里：

- `17 / 120 -> 41 / 120`
- wins：`24`
- losses：`0`
- exact McNemar p-value：`1.19e-7`

120 条新问法验证里：

- `17 / 120 -> 39 / 120`
- wins：`22`
- losses：`0`
- exact McNemar p-value：`4.77e-7`

这两个结果合起来说明：

> patch 的效果不只是“只对原始问题有效”，  
> 换一种问法后，固定 patch 仍然保留了大部分效果。

还需要补充一点：

> 120 条版本补充常见检索路线以后，  
> 结论反而更清楚了：  
> patch 负责补齐证据，rerank 负责调整排序。  
> 这批数据上，rerank / RRF / HyDE 都没有提高召回。

### 小样本机制验证和更完整的对照实验

早期 18 条小样本现在还保留着，主要用于：

- 更快演示 patch 机制
- 运行 reranker / RRF / HyDE 这些补充对照

对应结果：

| 路线 | Recall@5 | MRR |
|---|---:|---:|
| `main` | 0.1111 | 0.0556 |
| `main + rerank` | 0.1111 | 0.0741 |
| `main + patch` | 0.4444 | 0.1796 |
| `main + patch + rerank` | 0.4444 | 0.2796 |
| `Dense + BM25 + RRF + rerank` | 0.1111 | 0.0741 |
| `HyDE + Dense + BM25 + RRF + rerank` | 0.1111 | 0.0741 |

因此更准确的说法是：

> 18 条版本负责证明“patch 和 rerank 不是一回事”。  
> 120 条版本负责补样本量、补全对照路线、再补一份新问法验证。

### 当前比较准确的结论

更准确的说法是：

> 相关文档往往已经能进前几条检索结果，  
> 主要问题是 chunk 不够完整。  
> patch 对这类局部证据缺口有效，但不是适用于所有问题的通用方法。

## 推荐先看哪里

如果需要快速看懂项目，可以先看这几份：

- 文档总入口：`project_docs/00_docs_start_here.md`
- 面试入口：`project_docs/02_interview_materials/00_interview_start_here.md`
- 主实验总结：`project_docs/03_experiment_reports/production_patch_report.md`
- 运行入口：`project_docs/05_run_guides_and_setup/RUN_BASELINE.md`
- 现场演示：`project_docs/05_run_guides_and_setup/INTERVIEW_DEMO_RUNBOOK.md`

现在仓库里主要用来阅读和面试讲解的文档，已经统一收在 `project_docs/` 下面。

## 仓库结构

```text
recallrag/      主要实现
project_docs/   当前主要文档
case_zh_dureader/ 中文主实验数据
case/           旧英文 controlled case
case_beir/      BEIR 补充数据
runs/           实验结果
scripts/        构建数据和旧脚本
tests/          单元测试
tools/qdrant/   本地 Qdrant binary
```

主要模块：

```text
eval.py              baseline retrieval 评估
diagnose.py          failure diagnosis
patch_index.py       patch 备选内容生成与验证
bm25.py              BM25 / dense+BM25 对照
strong_baselines.py  RRF / rerank / HyDE 对照
qdrant_backend.py    Qdrant 双集合与在线合并
triage.py            最终归因和边界判断
```

## 当前最常用的命令

安装：

```bash
pip install -e .
```

测试：

```bash
python3 -m unittest discover -s tests -v
```

当前中文主实验入口：

```bash
cd /mnt/d/projects/RecallRAG
source /mnt/d/projects/.venvs/recallrag-reranker/bin/activate
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

更完整的运行说明见：

- `project_docs/05_run_guides_and_setup/RUN_BASELINE.md`
- `project_docs/05_run_guides_and_setup/QDRANT_BACKEND.md`

## 这两个脚本不要当主入口

仓库里这两个脚本还在：

- `scripts/run_mvp.sh`
- `scripts/run_qdrant_mvp.sh`

但它们运行的还是早期英文小样本：

- `case/`
- `runs/base`
- `runs/qdrant`
- `recallrag_main`
- `recallrag_patch`

所以它们现在更适合作为：

- 历史机制验证脚本
- 旧英文快速演示脚本

不要把这些脚本得到的结果当成当前主实验结论。

## 当前环境说明

Embedding endpoint：

```text
http://localhost:1234/v1/embeddings
```

当前主实验 embedding 模型：

```text
text-embedding-bge-large-zh-v1.5
```

Qdrant binary：

```text
tools/qdrant/qdrant
```
