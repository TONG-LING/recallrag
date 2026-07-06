# Baseline Retrieval Report

## Config

- **mode**: `heldout_main_only`
- **index**: `runs/zh120_c600_o0_base`
- **questions**: `case_zh_dureader_120/eval/questions_heldout.jsonl`
- **top_k**: `5`
- **coverage_threshold**: `0.65`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`

## Metrics

- **total**: 120
- **recall@5**: 0.8917
- **mrr**: 0.5696
- **hits**: 107
- **failed**: 13
- **coverage_threshold**: 0.6500

## Failed Queries

### zh002_holdout — zh_long_span_boundary_candidate
- question: 空气净化器采用哪种净化方式效果更佳
- gold: `zh_doc_002.md > 关键材料`
- best_topk_coverage: 0.566
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_002.md::c0002` score=0.729815 cov=0.566 section=中文复杂检索文档 > 关
  - rank 2: `zh_doc_002.md::c0001` score=0.720197 cov=0.222 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_002.md::c0000` score=0.715468 cov=0.207 section=
  - rank 4: `zh_doc_002.md::c0004` score=0.689452 cov=0.242 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_002.md::c0005` score=0.666238 cov=0.085 section=中文复杂检索文档 > 补充材料2

### zh003_holdout — zh_long_span_boundary_candidate
- question: 有哪些古诗赞美了黄山的风景？
- gold: `zh_doc_003.md > 关键材料`
- best_topk_coverage: 0.511
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_003.md::c0003` score=0.674743 cov=0.174 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_003.md::c0001` score=0.629486 cov=0.429 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_003.md::c0002` score=0.596836 cov=0.511 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_039.md::c0001` score=0.561894 cov=0.0 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_003.md::c0000` score=0.545228 cov=0.052 section=

### zh004_holdout — zh_long_span_boundary_candidate
- question: 一天内频繁放屁是什么原因？
- gold: `zh_doc_004.md > 关键材料`
- best_topk_coverage: 0.576
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_004.md::c0008` score=0.641248 cov=0.576 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_004.md::c0007` score=0.6152 cov=0.463 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_004.md::c0006` score=0.612865 cov=0.292 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_004.md::c0009` score=0.610046 cov=0.407 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_004.md::c0010` score=0.606559 cov=0.22 section=中文复杂检索文档 > 补充材料1

### zh006_holdout — zh_long_span_boundary_candidate
- question: 有哪些关于春光的成语？
- gold: `zh_doc_006.md > 关键材料`
- best_topk_coverage: 0.605
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_006.md::c0001` score=0.604574 cov=0.605 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_006.md::c0003` score=0.580445 cov=0.254 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_006.md::c0000` score=0.544669 cov=0.178 section=
  - rank 4: `zh_doc_006.md::c0002` score=0.535157 cov=0.605 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_003.md::c0003` score=0.375508 cov=0.0 section=中文复杂检索文档 > 关键材料

### zh007_holdout — zh_long_span_boundary_candidate
- question: 频繁使用肥皂来清洁面部是否合适
- gold: `zh_doc_007.md > 关键材料`
- best_topk_coverage: 0.648
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_007.md::c0001` score=0.716603 cov=0.45 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_007.md::c0002` score=0.70289 cov=0.648 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_007.md::c0004` score=0.701275 cov=0.137 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_007.md::c0003` score=0.699613 cov=0.339 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_007.md::c0000` score=0.668272 cov=0.203 section=

### zh008_holdout — zh_long_span_boundary_candidate
- question: 冬天如何饲养鹦鹉
- gold: `zh_doc_008.md > 关键材料`
- best_topk_coverage: 0.623
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_008.md::c0001` score=0.748831 cov=0.33 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_008.md::c0004` score=0.675337 cov=0.097 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_008.md::c0002` score=0.613851 cov=0.623 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_008.md::c0003` score=0.607338 cov=0.421 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_008.md::c0000` score=0.563427 cov=0.068 section=

### zh010_holdout — zh_long_span_boundary_candidate
- question: 硫磺皂可以一直使用吗
- gold: `zh_doc_010.md > 关键材料`
- best_topk_coverage: 0.587
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_010.md::c0003` score=0.747173 cov=0.11 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_010.md::c0000` score=0.68366 cov=0.095 section=
  - rank 3: `zh_doc_010.md::c0001` score=0.680134 cov=0.587 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_007.md::c0001` score=0.58401 cov=0.0 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_007.md::c0003` score=0.578324 cov=0.0 section=中文复杂检索文档 > 关键材料

### zh011_holdout — zh_long_span_boundary_candidate
- question: 有哪些比较好看的电视剧？
- gold: `zh_doc_011.md > 关键材料`
- best_topk_coverage: 0.623
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_011.md::c0003` score=0.596844 cov=0.043 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_011.md::c0000` score=0.527878 cov=0.096 section=
  - rank 3: `zh_doc_011.md::c0001` score=0.516093 cov=0.623 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_011.md::c0002` score=0.452031 cov=0.546 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_071.md::c0004` score=0.408613 cov=0.0 section=中文复杂检索文档 > 背景材料2

### zh017_holdout — zh_long_span_boundary_candidate
- question: 阴部颜色变白是怎么回事？
- gold: `zh_doc_017.md > 关键材料`
- best_topk_coverage: 0.629
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_017.md::c0001` score=0.64429 cov=0.546 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_017.md::c0000` score=0.599606 cov=0.092 section=
  - rank 3: `zh_doc_017.md::c0003` score=0.548584 cov=0.059 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_017.md::c0002` score=0.523492 cov=0.629 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_009.md::c0005` score=0.491121 cov=0.0 section=中文复杂检索文档 > 补充材料2

### zh027_holdout — zh_long_span_boundary_candidate
- question: 小米平板的钢化膜该如何粘贴
- gold: `zh_doc_027.md > 关键材料`
- best_topk_coverage: 0.305
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_027.md::c0003` score=0.748183 cov=0.305 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_027.md::c0004` score=0.699798 cov=0.01 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_027.md::c0000` score=0.673562 cov=0.139 section=
  - rank 4: `zh_doc_081.md::c0003` score=0.655423 cov=0.0 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_081.md::c0002` score=0.648098 cov=0.0 section=中文复杂检索文档 > 背景材料1

### zh033_holdout — zh_long_span_boundary_candidate
- question: 电暖桌什么品牌值得推荐
- gold: `zh_doc_033.md > 关键材料`
- best_topk_coverage: 0.574
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_033.md::c0001` score=0.797964 cov=0.558 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_033.md::c0004` score=0.777173 cov=0.147 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_033.md::c0003` score=0.771366 cov=0.125 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_033.md::c0000` score=0.765308 cov=0.166 section=
  - rank 5: `zh_doc_033.md::c0002` score=0.765242 cov=0.574 section=中文复杂检索文档 > 关键材料

### zh067_holdout — zh_long_span_boundary_candidate
- question: 武松的生肖是什么
- gold: `zh_doc_067.md > 关键材料`
- best_topk_coverage: 0.646
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_067.md::c0001` score=0.59923 cov=0.646 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_067.md::c0000` score=0.583993 cov=0.018 section=
  - rank 3: `zh_doc_067.md::c0003` score=0.555832 cov=0.009 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_067.md::c0002` score=0.465914 cov=0.39 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_011.md::c0002` score=0.335008 cov=0.0 section=中文复杂检索文档 > 关键材料

### zh101_holdout — zh_long_span_boundary_candidate
- question: 小米的平板电脑使用体验怎么样
- gold: `zh_doc_101.md > 关键材料`
- best_topk_coverage: 0.592
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_101.md::c0003` score=0.693485 cov=0.526 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_101.md::c0004` score=0.69255 cov=0.592 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_101.md::c0005` score=0.680938 cov=0.14 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_101.md::c0000` score=0.665286 cov=0.132 section=
  - rank 5: `zh_doc_101.md::c0001` score=0.656352 cov=0.114 section=中文复杂检索文档 > 背景材料1

## All Query Summary

| qid | expected type | success | rank | best cov | gold rank hint |
|---|---|---:|---:|---:|---:|
| zh001_holdout | zh_long_span_boundary_candidate | True | 1 | 0.778 | 1 |
| zh002_holdout | zh_long_span_boundary_candidate | False | None | 0.566 | 1 |
| zh003_holdout | zh_long_span_boundary_candidate | False | None | 0.511 | 1 |
| zh004_holdout | zh_long_span_boundary_candidate | False | None | 0.576 | 1 |
| zh005_holdout | zh_long_span_boundary_candidate | True | 2 | 0.661 | 1 |
| zh006_holdout | zh_long_span_boundary_candidate | False | None | 0.605 | 1 |
| zh007_holdout | zh_long_span_boundary_candidate | False | None | 0.648 | 1 |
| zh008_holdout | zh_long_span_boundary_candidate | False | None | 0.623 | 1 |
| zh009_holdout | zh_long_span_boundary_candidate | True | 2 | 0.732 | 1 |
| zh010_holdout | zh_long_span_boundary_candidate | False | None | 0.587 | 1 |
| zh011_holdout | zh_long_span_boundary_candidate | False | None | 0.623 | 1 |
| zh012_holdout | zh_long_span_boundary_candidate | True | 3 | 0.708 | 1 |
| zh013_holdout | zh_long_span_boundary_candidate | True | 2 | 0.786 | 1 |
| zh014_holdout | zh_long_span_boundary_candidate | True | 2 | 0.755 | 1 |
| zh015_holdout | zh_long_span_boundary_candidate | True | 1 | 0.777 | 1 |
| zh016_holdout | zh_long_span_boundary_candidate | True | 5 | 0.797 | 1 |
| zh017_holdout | zh_long_span_boundary_candidate | False | None | 0.629 | 1 |
| zh018_holdout | zh_long_span_boundary_candidate | True | 1 | 0.736 | 1 |
| zh019_holdout | zh_long_span_boundary_candidate | True | 2 | 0.885 | 1 |
| zh020_holdout | zh_long_span_boundary_candidate | True | 5 | 0.824 | 1 |
| zh021_holdout | zh_long_span_boundary_candidate | True | 1 | 0.73 | 1 |
| zh022_holdout | zh_long_span_boundary_candidate | True | 1 | 0.653 | 1 |
| zh023_holdout | zh_long_span_boundary_candidate | True | 4 | 0.765 | 1 |
| zh024_holdout | zh_long_span_boundary_candidate | True | 5 | 0.879 | 1 |
| zh025_holdout | zh_long_span_boundary_candidate | True | 2 | 0.841 | 1 |
| zh026_holdout | zh_long_span_boundary_candidate | True | 2 | 0.705 | 1 |
| zh027_holdout | zh_long_span_boundary_candidate | False | None | 0.305 | 1 |
| zh028_holdout | zh_long_span_boundary_candidate | True | 3 | 0.947 | 1 |
| zh029_holdout | zh_long_span_boundary_candidate | True | 1 | 0.712 | 1 |
| zh030_holdout | zh_long_span_boundary_candidate | True | 5 | 0.833 | 1 |
| zh031_holdout | zh_long_span_boundary_candidate | True | 1 | 0.94 | 1 |
| zh032_holdout | zh_long_span_boundary_candidate | True | 4 | 0.914 | 1 |
| zh033_holdout | zh_long_span_boundary_candidate | False | None | 0.574 | 1 |
| zh034_holdout | zh_long_span_boundary_candidate | True | 4 | 0.856 | 1 |
| zh035_holdout | zh_long_span_boundary_candidate | True | 3 | 0.897 | 1 |
| zh036_holdout | zh_long_span_boundary_candidate | True | 1 | 0.946 | 1 |
| zh037_holdout | zh_long_span_boundary_candidate | True | 1 | 0.711 | 1 |
| zh038_holdout | zh_long_span_boundary_candidate | True | 1 | 0.7 | 1 |
| zh039_holdout | zh_long_span_boundary_candidate | True | 1 | 0.945 | 1 |
| zh040_holdout | zh_long_span_boundary_candidate | True | 2 | 0.998 | 1 |
| zh041_holdout | zh_long_span_boundary_candidate | True | 3 | 0.733 | 1 |
| zh042_holdout | zh_long_span_boundary_candidate | True | 1 | 0.98 | 1 |
| zh043_holdout | zh_long_span_boundary_candidate | True | 3 | 0.833 | 1 |
| zh044_holdout | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh045_holdout | zh_long_span_boundary_candidate | True | 2 | 0.869 | 1 |
| zh046_holdout | zh_long_span_boundary_candidate | True | 4 | 0.657 | 1 |
| zh047_holdout | zh_long_span_boundary_candidate | True | 5 | 0.792 | 1 |
| zh048_holdout | zh_long_span_boundary_candidate | True | 3 | 0.744 | 1 |
| zh049_holdout | zh_long_span_boundary_candidate | True | 3 | 0.982 | 1 |
| zh050_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh051_holdout | zh_long_span_boundary_candidate | True | 1 | 0.896 | 1 |
| zh052_holdout | zh_long_span_boundary_candidate | True | 1 | 0.928 | 1 |
| zh053_holdout | zh_long_span_boundary_candidate | True | 1 | 0.914 | 1 |
| zh054_holdout | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh055_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh056_holdout | zh_long_span_boundary_candidate | True | 3 | 0.833 | 1 |
| zh057_holdout | zh_long_span_boundary_candidate | True | 3 | 0.851 | 1 |
| zh058_holdout | zh_long_span_boundary_candidate | True | 4 | 1.0 | 1 |
| zh059_holdout | zh_long_span_boundary_candidate | True | 1 | 0.871 | 1 |
| zh060_holdout | zh_long_span_boundary_candidate | True | 1 | 0.678 | 1 |
| zh061_holdout | zh_long_span_boundary_candidate | True | 2 | 0.782 | 1 |
| zh062_holdout | zh_long_span_boundary_candidate | True | 1 | 0.8 | 1 |
| zh063_holdout | zh_long_span_boundary_candidate | True | 4 | 1.0 | 1 |
| zh064_holdout | zh_long_span_boundary_candidate | True | 1 | 0.995 | 1 |
| zh065_holdout | zh_long_span_boundary_candidate | True | 2 | 0.683 | 1 |
| zh066_holdout | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh067_holdout | zh_long_span_boundary_candidate | False | None | 0.646 | 1 |
| zh068_holdout | zh_long_span_boundary_candidate | True | 2 | 0.7 | 1 |
| zh069_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh070_holdout | zh_long_span_boundary_candidate | True | 4 | 0.878 | 1 |
| zh071_holdout | zh_long_span_boundary_candidate | True | 1 | 0.948 | 1 |
| zh072_holdout | zh_long_span_boundary_candidate | True | 1 | 0.984 | 1 |
| zh073_holdout | zh_long_span_boundary_candidate | True | 1 | 0.942 | 1 |
| zh074_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh075_holdout | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh076_holdout | zh_long_span_boundary_candidate | True | 1 | 0.781 | 1 |
| zh077_holdout | zh_long_span_boundary_candidate | True | 1 | 0.852 | 1 |
| zh078_holdout | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh079_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh080_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh081_holdout | zh_long_span_boundary_candidate | True | 3 | 0.726 | 2 |
| zh082_holdout | zh_long_span_boundary_candidate | True | 5 | 1.0 | 1 |
| zh083_holdout | zh_long_span_boundary_candidate | True | 1 | 0.776 | 1 |
| zh084_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh085_holdout | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh086_holdout | zh_long_span_boundary_candidate | True | 3 | 0.79 | 1 |
| zh087_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh088_holdout | zh_long_span_boundary_candidate | True | 2 | 0.79 | 1 |
| zh089_holdout | zh_long_span_boundary_candidate | True | 3 | 0.791 | 1 |
| zh090_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh091_holdout | zh_long_span_boundary_candidate | True | 1 | 0.808 | 1 |
| zh092_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh093_holdout | zh_long_span_boundary_candidate | True | 1 | 0.846 | 1 |
| zh094_holdout | zh_long_span_boundary_candidate | True | 4 | 0.886 | 1 |
| zh095_holdout | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh096_holdout | zh_long_span_boundary_candidate | True | 2 | 0.72 | 1 |
| zh097_holdout | zh_long_span_boundary_candidate | True | 2 | 0.89 | 1 |
| zh098_holdout | zh_long_span_boundary_candidate | True | 2 | 0.873 | 1 |
| zh099_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh100_holdout | zh_long_span_boundary_candidate | True | 1 | 0.913 | 1 |
| zh101_holdout | zh_long_span_boundary_candidate | False | None | 0.592 | 1 |
| zh102_holdout | zh_long_span_boundary_candidate | True | 5 | 0.807 | 1 |
| zh103_holdout | zh_long_span_boundary_candidate | True | 1 | 0.874 | 1 |
| zh104_holdout | zh_long_span_boundary_candidate | True | 4 | 0.859 | 1 |
| zh105_holdout | zh_long_span_boundary_candidate | True | 1 | 0.789 | 1 |
| zh106_holdout | zh_long_span_boundary_candidate | True | 5 | 0.653 | 1 |
| zh107_holdout | zh_long_span_boundary_candidate | True | 1 | 0.982 | 1 |
| zh108_holdout | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh109_holdout | zh_long_span_boundary_candidate | True | 1 | 0.94 | 1 |
| zh110_holdout | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh111_holdout | zh_long_span_boundary_candidate | True | 2 | 0.986 | 1 |
| zh112_holdout | zh_long_span_boundary_candidate | True | 1 | 0.982 | 1 |
| zh113_holdout | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh114_holdout | zh_long_span_boundary_candidate | True | 2 | 0.867 | 1 |
| zh115_holdout | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh116_holdout | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh117_holdout | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh118_holdout | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh119_holdout | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh120_holdout | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
