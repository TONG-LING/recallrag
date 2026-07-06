# Baseline Retrieval Report

## Config

- **main_index**: `runs/zh120_c600_o0_base`
- **patch_index**: `runs/zh120_c600_o0_patches`
- **questions**: `case_zh_dureader_120/eval/questions_patch_source.jsonl`
- **top_k**: `5`
- **coverage_threshold**: `0.65`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`
- **main_chunks**: `634`
- **patch_chunks**: `6`
- **candidate_patch_chunks**: `56`

## Metrics

- **total**: 120
- **recall@5**: 0.9333
- **mrr**: 0.5715
- **hits**: 112
- **failed**: 8
- **coverage_threshold**: 0.6500

## Failed Queries

### zh003 — zh_long_span_boundary_candidate
- question: 黄山风景古诗赞
- gold: `zh_doc_003.md > 关键材料`
- best_topk_coverage: 0.511
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_003.md::c0003` score=0.654791 cov=0.174 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_003.md::c0001` score=0.622243 cov=0.429 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_003.md::c0002` score=0.597123 cov=0.511 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_039.md::c0001` score=0.553658 cov=0.0 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_003.md::c0000` score=0.547744 cov=0.052 section=

### zh006 — zh_long_span_boundary_candidate
- question: 春光成语
- gold: `zh_doc_006.md > 关键材料`
- best_topk_coverage: 0.605
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_006.md::c0001` score=0.7042 cov=0.605 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_006.md::c0003` score=0.694138 cov=0.254 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_006.md::c0000` score=0.6565 cov=0.178 section=
  - rank 4: `zh_doc_006.md::c0002` score=0.615207 cov=0.605 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_063.md::c0002` score=0.455123 cov=0.0 section=中文复杂检索文档 > 关键材料

### zh010 — zh_long_span_boundary_candidate
- question: 硫磺皂能长期用吗
- gold: `zh_doc_010.md > 关键材料`
- best_topk_coverage: 0.587
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_010.md::c0003` score=0.798557 cov=0.11 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_010.md::c0000` score=0.732089 cov=0.095 section=
  - rank 3: `zh_doc_010.md::c0001` score=0.717852 cov=0.587 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_007.md::c0001` score=0.624501 cov=0.0 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_007.md::c0003` score=0.613941 cov=0.0 section=中文复杂检索文档 > 关键材料

### zh011 — zh_long_span_boundary_candidate
- question: 比较好看的电视剧
- gold: `zh_doc_011.md > 关键材料`
- best_topk_coverage: 0.623
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_011.md::c0003` score=0.614397 cov=0.043 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_011.md::c0000` score=0.570812 cov=0.096 section=
  - rank 3: `zh_doc_011.md::c0001` score=0.536391 cov=0.623 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_011.md::c0002` score=0.490927 cov=0.546 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_071.md::c0004` score=0.456387 cov=0.0 section=中文复杂检索文档 > 背景材料2

### zh017 — zh_long_span_boundary_candidate
- question: 阴部变白
- gold: `zh_doc_017.md > 关键材料`
- best_topk_coverage: 0.629
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_017.md::c0001` score=0.723828 cov=0.546 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_017.md::c0000` score=0.707581 cov=0.092 section=
  - rank 3: `zh_doc_017.md::c0003` score=0.670737 cov=0.059 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_017.md::c0002` score=0.606127 cov=0.629 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_009.md::c0005` score=0.587302 cov=0.0 section=中文复杂检索文档 > 补充材料2

### zh027 — zh_long_span_boundary_candidate
- question: 小米平板钢化膜怎么贴
- gold: `zh_doc_027.md > 关键材料`
- best_topk_coverage: 0.305
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_027.md::c0003` score=0.751987 cov=0.305 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_027.md::c0004` score=0.703079 cov=0.01 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_027.md::c0000` score=0.669625 cov=0.139 section=
  - rank 4: `zh_doc_081.md::c0002` score=0.659272 cov=0.0 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_081.md::c0003` score=0.654886 cov=0.0 section=中文复杂检索文档 > 背景材料1

### zh033 — zh_long_span_boundary_candidate
- question: 电暖桌哪个牌子好
- gold: `zh_doc_033.md > 关键材料`
- best_topk_coverage: 0.574
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_033.md::c0001` score=0.782459 cov=0.558 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_033.md::c0004` score=0.75954 cov=0.147 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_033.md::c0003` score=0.752341 cov=0.125 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_033.md::c0000` score=0.750479 cov=0.166 section=
  - rank 5: `zh_doc_033.md::c0002` score=0.748154 cov=0.574 section=中文复杂检索文档 > 关键材料

### zh101 — zh_long_span_boundary_candidate
- question: 小米的平板好用吗
- gold: `zh_doc_101.md > 关键材料`
- best_topk_coverage: 0.592
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_101.md::c0003` score=0.734905 cov=0.526 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_101.md::c0004` score=0.721231 cov=0.592 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_101.md::c0000` score=0.705761 cov=0.132 section=
  - rank 4: `zh_doc_101.md::c0005` score=0.699823 cov=0.14 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_101.md::c0001` score=0.687347 cov=0.114 section=中文复杂检索文档 > 背景材料1

## All Query Summary

| qid | expected type | success | rank | best cov | gold rank hint |
|---|---|---:|---:|---:|---:|
| zh001 | zh_long_span_boundary_candidate | True | 2 | 0.778 | 1 |
| zh002 | zh_long_span_boundary_candidate | True | 1 | 0.952 | 1 |
| zh003 | zh_long_span_boundary_candidate | False | None | 0.511 | 1 |
| zh004 | zh_long_span_boundary_candidate | True | 2 | 0.786 | 1 |
| zh005 | zh_long_span_boundary_candidate | True | 2 | 0.661 | 1 |
| zh006 | zh_long_span_boundary_candidate | False | None | 0.605 | 1 |
| zh007 | zh_long_span_boundary_candidate | True | 4 | 0.886 | 1 |
| zh008 | zh_long_span_boundary_candidate | True | 5 | 0.834 | 1 |
| zh009 | zh_long_span_boundary_candidate | True | 3 | 0.732 | 1 |
| zh010 | zh_long_span_boundary_candidate | False | None | 0.587 | 1 |
| zh011 | zh_long_span_boundary_candidate | False | None | 0.623 | 1 |
| zh012 | zh_long_span_boundary_candidate | True | 3 | 0.708 | 1 |
| zh013 | zh_long_span_boundary_candidate | True | 2 | 0.786 | 1 |
| zh014 | zh_long_span_boundary_candidate | True | 4 | 0.755 | 1 |
| zh015 | zh_long_span_boundary_candidate | True | 1 | 0.777 | 1 |
| zh016 | zh_long_span_boundary_candidate | True | 5 | 0.797 | 1 |
| zh017 | zh_long_span_boundary_candidate | False | None | 0.629 | 1 |
| zh018 | zh_long_span_boundary_candidate | True | 2 | 0.736 | 1 |
| zh019 | zh_long_span_boundary_candidate | True | 2 | 0.885 | 1 |
| zh020 | zh_long_span_boundary_candidate | True | 5 | 0.824 | 1 |
| zh021 | zh_long_span_boundary_candidate | True | 1 | 0.73 | 1 |
| zh022 | zh_long_span_boundary_candidate | True | 1 | 0.653 | 1 |
| zh023 | zh_long_span_boundary_candidate | True | 4 | 0.765 | 1 |
| zh024 | zh_long_span_boundary_candidate | True | 5 | 0.879 | 1 |
| zh025 | zh_long_span_boundary_candidate | True | 2 | 0.841 | 1 |
| zh026 | zh_long_span_boundary_candidate | True | 1 | 0.705 | 1 |
| zh027 | zh_long_span_boundary_candidate | False | None | 0.305 | 1 |
| zh028 | zh_long_span_boundary_candidate | True | 3 | 0.947 | 1 |
| zh029 | zh_long_span_boundary_candidate | True | 2 | 0.712 | 1 |
| zh030 | zh_long_span_boundary_candidate | True | 5 | 0.833 | 1 |
| zh031 | zh_long_span_boundary_candidate | True | 1 | 0.94 | 1 |
| zh032 | zh_long_span_boundary_candidate | True | 5 | 0.914 | 1 |
| zh033 | zh_long_span_boundary_candidate | False | None | 0.574 | 1 |
| zh034 | zh_long_span_boundary_candidate | True | 4 | 0.856 | 1 |
| zh035 | zh_long_span_boundary_candidate | True | 3 | 0.897 | 1 |
| zh036 | zh_long_span_boundary_candidate | True | 1 | 0.946 | 1 |
| zh037 | zh_long_span_boundary_candidate | True | 2 | 0.711 | 1 |
| zh038 | zh_long_span_boundary_candidate | True | 3 | 0.7 | 1 |
| zh039 | zh_long_span_boundary_candidate | True | 1 | 0.945 | 1 |
| zh040 | zh_long_span_boundary_candidate | True | 2 | 0.998 | 1 |
| zh041 | zh_long_span_boundary_candidate | True | 3 | 0.733 | 1 |
| zh042 | zh_long_span_boundary_candidate | True | 1 | 0.98 | 1 |
| zh043 | zh_long_span_boundary_candidate | True | 3 | 0.833 | 1 |
| zh044 | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh045 | zh_long_span_boundary_candidate | True | 2 | 0.869 | 1 |
| zh046 | zh_long_span_boundary_candidate | True | 3 | 0.657 | 1 |
| zh047 | zh_long_span_boundary_candidate | True | 5 | 0.792 | 1 |
| zh048 | zh_long_span_boundary_candidate | True | 2 | 0.744 | 1 |
| zh049 | zh_long_span_boundary_candidate | True | 3 | 0.982 | 1 |
| zh050 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh051 | zh_long_span_boundary_candidate | True | 1 | 0.896 | 1 |
| zh052 | zh_long_span_boundary_candidate | True | 1 | 0.928 | 1 |
| zh053 | zh_long_span_boundary_candidate | True | 1 | 0.914 | 1 |
| zh054 | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh055 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh056 | zh_long_span_boundary_candidate | True | 4 | 0.833 | 1 |
| zh057 | zh_long_span_boundary_candidate | True | 5 | 0.854 | 1 |
| zh058 | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh059 | zh_long_span_boundary_candidate | True | 1 | 0.871 | 1 |
| zh060 | zh_long_span_boundary_candidate | True | 1 | 0.678 | 1 |
| zh061 | zh_long_span_boundary_candidate | True | 2 | 0.782 | 1 |
| zh062 | zh_long_span_boundary_candidate | True | 1 | 0.8 | 1 |
| zh063 | zh_long_span_boundary_candidate | True | 4 | 1.0 | 1 |
| zh064 | zh_long_span_boundary_candidate | True | 1 | 0.995 | 1 |
| zh065 | zh_long_span_boundary_candidate | True | 2 | 0.683 | 1 |
| zh066 | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh067 | zh_long_span_boundary_candidate | True | 3 | 0.997 | 1 |
| zh068 | zh_long_span_boundary_candidate | True | 2 | 0.7 | 1 |
| zh069 | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh070 | zh_long_span_boundary_candidate | True | 4 | 0.878 | 1 |
| zh071 | zh_long_span_boundary_candidate | True | 1 | 0.948 | 1 |
| zh072 | zh_long_span_boundary_candidate | True | 1 | 0.984 | 1 |
| zh073 | zh_long_span_boundary_candidate | True | 1 | 0.942 | 1 |
| zh074 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh075 | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh076 | zh_long_span_boundary_candidate | True | 1 | 0.781 | 1 |
| zh077 | zh_long_span_boundary_candidate | True | 1 | 0.852 | 1 |
| zh078 | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh079 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh080 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh081 | zh_long_span_boundary_candidate | True | 3 | 0.726 | 2 |
| zh082 | zh_long_span_boundary_candidate | True | 4 | 1.0 | 1 |
| zh083 | zh_long_span_boundary_candidate | True | 1 | 0.776 | 1 |
| zh084 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh085 | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh086 | zh_long_span_boundary_candidate | True | 3 | 0.79 | 1 |
| zh087 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh088 | zh_long_span_boundary_candidate | True | 2 | 0.79 | 1 |
| zh089 | zh_long_span_boundary_candidate | True | 2 | 0.791 | 1 |
| zh090 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh091 | zh_long_span_boundary_candidate | True | 1 | 0.808 | 1 |
| zh092 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh093 | zh_long_span_boundary_candidate | True | 1 | 0.846 | 1 |
| zh094 | zh_long_span_boundary_candidate | True | 3 | 0.886 | 1 |
| zh095 | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh096 | zh_long_span_boundary_candidate | True | 2 | 0.72 | 1 |
| zh097 | zh_long_span_boundary_candidate | True | 1 | 0.89 | 1 |
| zh098 | zh_long_span_boundary_candidate | True | 2 | 0.873 | 1 |
| zh099 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh100 | zh_long_span_boundary_candidate | True | 1 | 0.913 | 1 |
| zh101 | zh_long_span_boundary_candidate | False | None | 0.592 | 1 |
| zh102 | zh_long_span_boundary_candidate | True | 5 | 0.807 | 1 |
| zh103 | zh_long_span_boundary_candidate | True | 1 | 0.874 | 1 |
| zh104 | zh_long_span_boundary_candidate | True | 4 | 0.859 | 1 |
| zh105 | zh_long_span_boundary_candidate | True | 1 | 0.789 | 1 |
| zh106 | zh_long_span_boundary_candidate | True | 5 | 0.653 | 1 |
| zh107 | zh_long_span_boundary_candidate | True | 1 | 0.982 | 1 |
| zh108 | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh109 | zh_long_span_boundary_candidate | True | 1 | 0.94 | 1 |
| zh110 | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh111 | zh_long_span_boundary_candidate | True | 1 | 0.986 | 1 |
| zh112 | zh_long_span_boundary_candidate | True | 1 | 0.982 | 1 |
| zh113 | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh114 | zh_long_span_boundary_candidate | True | 1 | 0.867 | 1 |
| zh115 | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh116 | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh117 | zh_long_span_boundary_candidate | True | 3 | 1.0 | 1 |
| zh118 | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh119 | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh120 | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
