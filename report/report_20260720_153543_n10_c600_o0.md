# RecallRAG 本地工程化评估报告

- **生成时间**：`2026-07-20 15:36:14`
- **运行编号**：`20260720_153543`
- **报告目录**：`/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0`
- **评估题目数**：`10` / `120`

## 1. 结论摘要

本次评估围绕 RAG 检索中的证据召回完整性问题展开：主索引保持不变，仅在失败样例触发后生成旁路 Patch Index，并通过验证门决定是否启用 patch。

| 项目 | 结果 |
|---|---:|
| 指标来源 | Qdrant 双集合检索 |
| Main-only Hits | 3 / 10 |
| Main+Patch Hits | 7 / 10 |
| Hit 增量 | +4 |
| Recall@5 增量 | 0.4000 |
| MRR 增量 | 0.1950 |
| 已接受 Patch 数 | 4 |
| 修复 query 数 | 4 |
| 回归 query 数 | 0 |

> 安全性结论：本次评估未观察到 main+patch 相比 main-only 的成功样例回归。

## 2. 环境与依赖检查

| 检查项 | 状态 | 关键信息 |
|---|---|---|
| Embedding 服务 | `ok` | endpoint=`http://localhost:1234/v1/embeddings`, model=`text-embedding-bge-large-zh-v1.5`, dim=`1024`, latency=`0.082s` |
| Qdrant 服务 | `ok` | url=`http://localhost:6333`, collections=`6`, latency=`0.001s` |

本次运行使用临时 Qdrant collection：

- main collection：`recallrag_tmp_20260720_153543_main`
- patch collection：`recallrag_tmp_20260720_153543_patch`

## 3. 评估配置

| 配置项 | 值 |
|---|---|
| 文档目录 | `/mnt/d/projects/RecallRAG/case_zh_dureader_120/docs` |
| 原始问题集 | `/mnt/d/projects/RecallRAG/case_zh_dureader_120/eval/questions_patch_source.jsonl` |
| 临时问题集 | `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/questions.jsonl` |
| 题目选择方式 | `first_n` |
| chunk_size / overlap | `600` / `0` |
| keep_heading | `True` |
| top_k | `5` |
| patch_k | `3` |
| coverage_threshold | `0.65` |
| batch_size | `4` |

## 4. 评估口径

本报告不使用普通文档级命中作为唯一标准，而采用证据级命中：Top-K 结果必须来自正确文档，并且 chunk 对 gold evidence span 的覆盖率达到阈值。

- **成功标准**：`doc_id` 匹配且 evidence coverage ≥ `0.65`。
- **Patch 触发条件**：仅对 main-only 失败且诊断为 near-miss / 局部上下文不足的样例生成 candidate。
- **Patch 接受条件**：candidate 单独 probe 能修复源 query，合并后全量评估不引入 regression。
- **BM25 countercheck**：如果 BM25 或 Dense+BM25 能修复该失败，说明失败可能是检索策略敏感，不应直接归因于 chunking。
- **Qdrant 验证**：Main Index 与 Patch Index 使用独立 collection，验证旁路 patch 在向量库形态下的检索效果。

## 5. Qdrant 主检索指标

本脚本默认要求 Qdrant 已启动，最终检索效果以 Qdrant 双集合验证为准。离线向量产物评估只用于诊断、patch candidate 筛选和一致性对照。

| Route | Recall@5 | MRR | Hits | Failed |
|---|---:|---:|---:|---:|
| main collection | 0.3000 | 0.1333 | 3 / 10 | 7 |
| main + patch collections | 0.7000 | 0.3283 | 7 / 10 | 3 |
| delta | 0.4000 | 0.1950 | 4 | - |

### 5.1 离线候选筛选指标

以下指标来自本地 `chunks.json` / `vectors.json` 产物，用于 patch 生成、probe、回归检查和 Qdrant 写入前的候选筛选。该表不是第二套线上路由。

| Route | Recall@5 | MRR | Hits | Failed |
|---|---:|---:|---:|---:|
| offline main-only | 0.3000 | 0.1333 | 3 / 10 | 7 |
| offline main + patch | 0.7000 | 0.3283 | 7 / 10 | 3 |
| offline delta | 0.4000 | 0.1950 | 4 | - |

## 6. 配对检验

| 指标 | 值 |
|---|---:|
| before_hits | 3 |
| after_hits | 7 |
| wins | 4 |
| losses | 0 |
| ties | 6 |
| recall_delta | 0.4000 |
| recall_delta_bootstrap_ci95 | `[0.1, 0.7]` |
| mrr_delta | 0.1950 |
| mrr_delta_bootstrap_ci95 | `[0.025, 0.41]` |
| exact_mcnemar_pvalue | 0.125 |

逐 query 明细见：`/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/hybrid/paired_significance.json`

## 7. 失败诊断统计

main-only 失败 query 数：`7`。诊断阶段只基于 retrieval trace 定位 near-miss 窗口，不使用 gold span 来生成 patch。

### 7.1 按 failure family 统计

| failure_family | count |
|---|---:|
| `chunking_failure_candidate` | 7 |

### 7.2 按 diagnosed_failure_type 统计

| diagnosed_failure_type | count |
|---|---:|
| `missing_local_context_candidate` | 7 |

## 8. Patch 生成与筛选

Patch 采用旁路索引策略：主索引不被改写；candidate 先进入临时 patch 集，经过 probe 和全量回归检查后，才允许进入 selected patch 集。

| 项目 | 数量 / 分布 |
|---|---|
| materialized patch candidates | `28` |
| candidate probe results | `28` |
| probe candidate type counts | `{'adjacent_merge': 7, 'contextual': 7, 'local_proposition': 7, 'local_summary': 7}` |
| selected patch candidates | `4` |
| selected patch type counts | `{'adjacent_merge': 3, 'contextual': 1}` |
| patch decision counts | `{'accepted': 4, 'candidate_not_selected': 24}` |

| movement | qids |
|---|---|
| fixed | `zh002, zh004, zh007, zh008` |
| regressed | `-` |
| unchanged_failure | `zh003, zh006, zh010` |

## 9. BM25 / Dense+BM25 反证检查

该部分用于判断失败是否只是 dense retrieval 策略问题。如果 BM25 或 Dense+BM25 能修复，则该样例不应简单归因于 chunk 边界问题。

| Route | Recall@5 | MRR | Hits | Failed |
|---|---:|---:|---:|---:|
| dense | 0.3000 | 0.1333 | 3 / 10 | 7 |
| bm25 | 0.2000 | 0.0450 | 2 / 10 | 8 |
| dense_bm25 | 0.3000 | 0.0650 | 3 / 10 | 7 |

## 10. Final Triage 汇总

Final triage 综合 dense 失败、patch 修复、BM25 countercheck 和 Qdrant 验证信号，输出最终工程动作。

| 项目 | 数量 |
|---|---:|
| total_dense_failures | 7 |
| accepted_patch_candidates | 4 |
| retrieval_strategy_sensitive | 0 |
| manual_review | 3 |

## 11. 逐失败样例工程决策表

| qid | question | raw diagnosis | patch_allowed | final_decision | accepted_patch_type | base_cov | patch_cov | bm25_fixed | qdrant_patch_fixed | action |
|---|---|---|---:|---|---|---:|---:|---:|---:|---|
| zh002 | 空气净化器哪种净化方式好 | `missing_local_context_candidate` | True | `接受 Patch` | `adjacent_merge` | 0.578 | 0.952 | False | True | `accept_patch_for_shadow_index; optional later merge` |
| zh003 | 黄山风景古诗赞 | `missing_local_context_candidate` | True | `人工复核` | `-` | 0.511 | 0.511 | False | False | `manual_review_or_new_strategy` |
| zh004 | 一天放很多屁 | `missing_local_context_candidate` | True | `接受 Patch` | `contextual` | 0.576 | 0.786 | False | True | `accept_patch_for_shadow_index; optional later merge` |
| zh006 | 春光成语 | `missing_local_context_candidate` | True | `人工复核` | `-` | 0.605 | 0.605 | False | False | `manual_review_or_new_strategy` |
| zh007 | 经常用肥皂洗脸好吗 | `missing_local_context_candidate` | True | `接受 Patch` | `adjacent_merge` | 0.648 | 0.886 | False | True | `accept_patch_for_shadow_index; optional later merge` |
| zh008 | 冬天怎样养鹦鹉 | `missing_local_context_candidate` | True | `接受 Patch` | `adjacent_merge` | 0.623 | 0.834 | False | True | `accept_patch_for_shadow_index; optional later merge` |
| zh010 | 硫磺皂能长期用吗 | `missing_local_context_candidate` | True | `人工复核` | `-` | 0.587 | 0.587 | False | False | `manual_review_or_new_strategy` |

## 12. 逐失败样例详细说明

### zh002 — 空气净化器哪种净化方式好

- gold：`zh_doc_002.md > 关键材料`
- 原始诊断：`chunking_failure_candidate / missing_local_context_candidate`
- 诊断置信度：`0.82`
- 诊断原因：failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_002.md::c0002` without using gold labels
- 是否允许生成 patch：`True`
- final_decision：`接受 Patch`
- recommended_action：`accept_patch_for_shadow_index; optional later merge`

检索信号：

- dense_failed：`True`
- json_patch_fixed：`True`
- qdrant_patch_fixed：`True`
- bm25_fixed：`False`
- dense_bm25_fixed：`False`
- coverage：`0.578` -> `0.952`

Patch 决策：

- accepted：`['patch_zh002_001_adjacent_merge']`
- needs_review：`[]`
- rejected：`[]`
- candidate_not_selected：`['patch_zh002_001_contextual', 'patch_zh002_001_local_proposition', 'patch_zh002_001_local_summary']`

决策依据：

- Patch retrieval fixes the source query and BM25/hybrid does not explain it away.
- JSON patch decisions: 4 candidates; accepted patch ids=['patch_zh002_001_adjacent_merge']; accepted candidate types=['adjacent_merge'].
- Qdrant main+patch retrieval fixes the query.

### zh003 — 黄山风景古诗赞

- gold：`zh_doc_003.md > 关键材料`
- 原始诊断：`chunking_failure_candidate / missing_local_context_candidate`
- 诊断置信度：`0.82`
- 诊断原因：failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_003.md::c0003` without using gold labels
- 是否允许生成 patch：`True`
- final_decision：`人工复核`
- recommended_action：`manual_review_or_new_strategy`

检索信号：

- dense_failed：`True`
- json_patch_fixed：`False`
- qdrant_patch_fixed：`False`
- bm25_fixed：`False`
- dense_bm25_fixed：`False`
- coverage：`0.511` -> `0.511`

Patch 决策：

- accepted：`[]`
- needs_review：`[]`
- rejected：`[]`
- candidate_not_selected：`['patch_zh003_002_adjacent_merge', 'patch_zh003_002_contextual', 'patch_zh003_002_local_proposition', 'patch_zh003_002_local_summary']`

决策依据：

- Neither patch nor BM25/hybrid fixed the failure.
- JSON patch decisions: 4 candidates; accepted patch ids=[]; accepted candidate types=[].

### zh004 — 一天放很多屁

- gold：`zh_doc_004.md > 关键材料`
- 原始诊断：`chunking_failure_candidate / missing_local_context_candidate`
- 诊断置信度：`0.82`
- 诊断原因：failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_004.md::c0007` without using gold labels
- 是否允许生成 patch：`True`
- final_decision：`接受 Patch`
- recommended_action：`accept_patch_for_shadow_index; optional later merge`

检索信号：

- dense_failed：`True`
- json_patch_fixed：`True`
- qdrant_patch_fixed：`True`
- bm25_fixed：`False`
- dense_bm25_fixed：`False`
- coverage：`0.576` -> `0.786`

Patch 决策：

- accepted：`['patch_zh004_003_contextual']`
- needs_review：`[]`
- rejected：`[]`
- candidate_not_selected：`['patch_zh004_003_adjacent_merge', 'patch_zh004_003_local_proposition', 'patch_zh004_003_local_summary']`

决策依据：

- Patch retrieval fixes the source query and BM25/hybrid does not explain it away.
- JSON patch decisions: 4 candidates; accepted patch ids=['patch_zh004_003_contextual']; accepted candidate types=['contextual'].
- Qdrant main+patch retrieval fixes the query.

### zh006 — 春光成语

- gold：`zh_doc_006.md > 关键材料`
- 原始诊断：`chunking_failure_candidate / missing_local_context_candidate`
- 诊断置信度：`0.82`
- 诊断原因：failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_006.md::c0000` without using gold labels
- 是否允许生成 patch：`True`
- final_decision：`人工复核`
- recommended_action：`manual_review_or_new_strategy`

检索信号：

- dense_failed：`True`
- json_patch_fixed：`False`
- qdrant_patch_fixed：`False`
- bm25_fixed：`False`
- dense_bm25_fixed：`False`
- coverage：`0.605` -> `0.605`

Patch 决策：

- accepted：`[]`
- needs_review：`[]`
- rejected：`[]`
- candidate_not_selected：`['patch_zh006_004_adjacent_merge', 'patch_zh006_004_contextual', 'patch_zh006_004_local_proposition', 'patch_zh006_004_local_summary']`

决策依据：

- Neither patch nor BM25/hybrid fixed the failure.
- JSON patch decisions: 4 candidates; accepted patch ids=[]; accepted candidate types=[].

### zh007 — 经常用肥皂洗脸好吗

- gold：`zh_doc_007.md > 关键材料`
- 原始诊断：`chunking_failure_candidate / missing_local_context_candidate`
- 诊断置信度：`0.82`
- 诊断原因：failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_007.md::c0001` without using gold labels
- 是否允许生成 patch：`True`
- final_decision：`接受 Patch`
- recommended_action：`accept_patch_for_shadow_index; optional later merge`

检索信号：

- dense_failed：`True`
- json_patch_fixed：`True`
- qdrant_patch_fixed：`True`
- bm25_fixed：`False`
- dense_bm25_fixed：`False`
- coverage：`0.648` -> `0.886`

Patch 决策：

- accepted：`['patch_zh007_005_adjacent_merge']`
- needs_review：`[]`
- rejected：`[]`
- candidate_not_selected：`['patch_zh007_005_contextual', 'patch_zh007_005_local_proposition', 'patch_zh007_005_local_summary']`

决策依据：

- Patch retrieval fixes the source query and BM25/hybrid does not explain it away.
- JSON patch decisions: 4 candidates; accepted patch ids=['patch_zh007_005_adjacent_merge']; accepted candidate types=['adjacent_merge'].
- Qdrant main+patch retrieval fixes the query.

### zh008 — 冬天怎样养鹦鹉

- gold：`zh_doc_008.md > 关键材料`
- 原始诊断：`chunking_failure_candidate / missing_local_context_candidate`
- 诊断置信度：`0.82`
- 诊断原因：failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_008.md::c0001` without using gold labels
- 是否允许生成 patch：`True`
- final_decision：`接受 Patch`
- recommended_action：`accept_patch_for_shadow_index; optional later merge`

检索信号：

- dense_failed：`True`
- json_patch_fixed：`True`
- qdrant_patch_fixed：`True`
- bm25_fixed：`False`
- dense_bm25_fixed：`False`
- coverage：`0.623` -> `0.834`

Patch 决策：

- accepted：`['patch_zh008_006_adjacent_merge']`
- needs_review：`[]`
- rejected：`[]`
- candidate_not_selected：`['patch_zh008_006_contextual', 'patch_zh008_006_local_proposition', 'patch_zh008_006_local_summary']`

决策依据：

- Patch retrieval fixes the source query and BM25/hybrid does not explain it away.
- JSON patch decisions: 4 candidates; accepted patch ids=['patch_zh008_006_adjacent_merge']; accepted candidate types=['adjacent_merge'].
- Qdrant main+patch retrieval fixes the query.

### zh010 — 硫磺皂能长期用吗

- gold：`zh_doc_010.md > 关键材料`
- 原始诊断：`chunking_failure_candidate / missing_local_context_candidate`
- 诊断置信度：`0.82`
- 诊断原因：failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_010.md::c0000` without using gold labels
- 是否允许生成 patch：`True`
- final_decision：`人工复核`
- recommended_action：`manual_review_or_new_strategy`

检索信号：

- dense_failed：`True`
- json_patch_fixed：`False`
- qdrant_patch_fixed：`False`
- bm25_fixed：`False`
- dense_bm25_fixed：`False`
- coverage：`0.587` -> `0.587`

Patch 决策：

- accepted：`[]`
- needs_review：`[]`
- rejected：`[]`
- candidate_not_selected：`['patch_zh010_007_adjacent_merge', 'patch_zh010_007_contextual', 'patch_zh010_007_local_proposition', 'patch_zh010_007_local_summary']`

决策依据：

- Neither patch nor BM25/hybrid fixed the failure.
- JSON patch decisions: 4 candidates; accepted patch ids=[]; accepted candidate types=[].

## 13. 已接受 Patch 详情

### patch_zh002_001_adjacent_merge

| 字段 | 值 |
|---|---|
| qid | `zh002` |
| candidate_type | `adjacent_merge` |
| failure_type | `missing_local_context_candidate` |
| anchor_chunk_id | `zh_doc_002.md::c0002` |
| affected_main_chunks | `['zh_doc_002.md::c0001', 'zh_doc_002.md::c0002', 'zh_doc_002.md::c0003']` |
| before_rank / after_rank | `None` -> `1` |
| before_coverage / after_coverage | `0.578` -> `0.952` |
| individual_probe_rank | `1` |
| individual_probe_coverage | `0.952` |
| decision_reason | source query fixed and no regression detected |

### patch_zh004_003_contextual

| 字段 | 值 |
|---|---|
| qid | `zh004` |
| candidate_type | `contextual` |
| failure_type | `missing_local_context_candidate` |
| anchor_chunk_id | `zh_doc_004.md::c0007` |
| affected_main_chunks | `['zh_doc_004.md::c0006', 'zh_doc_004.md::c0007', 'zh_doc_004.md::c0008']` |
| before_rank / after_rank | `None` -> `2` |
| before_coverage / after_coverage | `0.576` -> `0.786` |
| individual_probe_rank | `2` |
| individual_probe_coverage | `0.786` |
| decision_reason | source query fixed and no regression detected |

### patch_zh007_005_adjacent_merge

| 字段 | 值 |
|---|---|
| qid | `zh007` |
| candidate_type | `adjacent_merge` |
| failure_type | `missing_local_context_candidate` |
| anchor_chunk_id | `zh_doc_007.md::c0001` |
| affected_main_chunks | `['zh_doc_007.md::c0000', 'zh_doc_007.md::c0001', 'zh_doc_007.md::c0002']` |
| before_rank / after_rank | `None` -> `4` |
| before_coverage / after_coverage | `0.648` -> `0.886` |
| individual_probe_rank | `4` |
| individual_probe_coverage | `0.886` |
| decision_reason | source query fixed and no regression detected |

### patch_zh008_006_adjacent_merge

| 字段 | 值 |
|---|---|
| qid | `zh008` |
| candidate_type | `adjacent_merge` |
| failure_type | `missing_local_context_candidate` |
| anchor_chunk_id | `zh_doc_008.md::c0001` |
| affected_main_chunks | `['zh_doc_008.md::c0000', 'zh_doc_008.md::c0001', 'zh_doc_008.md::c0002']` |
| before_rank / after_rank | `None` -> `5` |
| before_coverage / after_coverage | `0.623` -> `0.834` |
| individual_probe_rank | `5` |
| individual_probe_coverage | `0.834` |
| decision_reason | source query fixed and no regression detected |

## 14. 未接受 Patch 统计

| 状态 | 数量 | 说明 |
|---|---:|---|
| needs_review | 0 | 可能存在回归或证据不足，需要人工复核 |
| rejected | 0 | 源 query 未被修复 |
| candidate_not_selected | 24 | 同一 query 下存在更优候选，当前候选未被选中 |

## 15. Qdrant 双集合验证

Qdrant 验证用于确认 Main Index 和 Patch Index 分离后的检索行为。Patch collection 仅加载通过验证的 selected patch。

- qdrant fixed qids：`zh002, zh004, zh007, zh008`
- qdrant regressed qids：`-`
- qdrant unchanged_failure：`zh003, zh006, zh010`
- qdrant comparison report：`/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/qdrant_patch/qdrant_comparison_report.md`

## 16. 工程化解释与上线边界

- 主索引在整个流程中不被直接改写，patch 作为旁路增量层存在。
- patch 必须经过 source query probe 和全量 regression check，不能因为生成成功就直接进入检索系统。
- BM25 / Dense+BM25 反证检查用于避免把检索策略问题误判为 chunking 问题。
- Qdrant 侧采用 main collection 与 patch collection 分离，便于回滚、停用和重新验证。
- 如果源文档或来源窗口发生变化，应重新计算来源窗口 hash，并将旧 patch 标记为 stale 后重新验证。
- 本报告只评估检索证据召回，不评估最终 LLM 答案生成质量。

## 17. 风险与局限

1. 本次评估依赖当前 embedding 模型和本地服务状态，替换 embedding 后指标可能变化。
2. 评估集规模由 `--limit` 控制，小样本运行只适合作为流程检查，不应作为最终效果结论。
3. Patch 主要修复局部上下文不足或 chunk 边界断裂，不覆盖文档缺失、语义表达差异过大或 embedding 模型能力不足等失败。
4. Qdrant collection 为本次运行创建的临时集合；若需要长期保留，应另行制定 collection 命名、版本和清理策略。
5. accepted patch 仍应结合人工 case review，尤其是业务知识库场景中的事实一致性和时效性。

## 18. 输出产物索引

- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/run_config.json`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/base/eval_report.md`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/base/failure_diagnosis.md`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/base/failure_diagnosis.json`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/patches/patch_log.json`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/patches/patch_log_evaluated.json`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/hybrid/comparison_report.md`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/hybrid/comparison.json`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/hybrid/patch_decisions.json`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/hybrid/paired_significance.md`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/bm25/hybrid_bm25_report.md`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/triage/final_triage_report.md`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/triage/final_triage.json`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/qdrant_patch/qdrant_comparison_report.md`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/runs/qdrant_patch/qdrant_comparison_report.json`
- `/mnt/d/projects/RecallRAG/temp/engineering_eval_20260720_153543_n10_c600_o0/logs`

