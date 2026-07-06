# Baseline Retrieval Report

## Config

- **main_index**: `runs/zh120_base`
- **patch_index**: `runs/zh120_patches`
- **questions**: `case_zh_dureader_120/eval/questions.jsonl`
- **top_k**: `5`
- **coverage_threshold**: `0.65`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`
- **main_chunks**: `1634`
- **patch_chunks**: `24`
- **candidate_patch_chunks**: `412`

## Metrics

- **total**: 120
- **recall@5**: 0.3417
- **mrr**: 0.1501
- **hits**: 41
- **failed**: 79
- **coverage_threshold**: 0.6500

## Failed Queries

### zh001 — zh_long_span_boundary_candidate
- question: 高速公路超速20以上不足50扣几分
- gold: `zh_doc_001.md > 关键材料`
- best_topk_coverage: 0.646
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_001.md::c0038` score=0.803289 cov=0.425 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_001.md::c0012` score=0.800873 cov=0.646 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_001.md::c0011` score=0.793865 cov=0.454 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_001.md::c0021` score=0.793326 cov=0.348 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_001.md::c0027` score=0.78027 cov=0.366 section=中文复杂检索文档 > 补充材料1

### zh002 — zh_long_span_boundary_candidate
- question: 空气净化器哪种净化方式好
- gold: `zh_doc_002.md > 关键材料`
- best_topk_coverage: 0.163
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_002.md::c0001` score=0.731342 cov=0.13 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_002.md::c0003` score=0.721687 cov=0.163 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_002.md::c0002` score=0.700999 cov=0.129 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_002.md::c0012` score=0.692261 cov=0.111 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_002.md::c0000` score=0.688329 cov=0.139 section=

### zh003 — zh_long_span_boundary_candidate
- question: 黄山风景古诗赞
- gold: `zh_doc_003.md > 关键材料`
- best_topk_coverage: 0.206
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_003.md::c0009` score=0.669186 cov=0.035 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_003.md::c0004` score=0.641883 cov=0.206 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_003.md::c0006` score=0.640429 cov=0.203 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_003.md::c0005` score=0.637525 cov=0.203 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_003.md::c0003` score=0.624273 cov=0.184 section=中文复杂检索文档 > 背景材料2

### zh004 — zh_long_span_boundary_candidate
- question: 一天放很多屁
- gold: `zh_doc_004.md > 关键材料`
- best_topk_coverage: 0.276
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_004.md::c0021` score=0.721794 cov=0.273 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_004.md::c0002` score=0.716717 cov=0.06 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_004.md::c0024` score=0.71572 cov=0.276 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_004.md::c0000` score=0.711929 cov=0.084 section=
  - rank 5: `zh_doc_004.md::c0022` score=0.703598 cov=0.274 section=中文复杂检索文档 > 关键材料

### zh005 — zh_long_span_boundary_candidate
- question: 叉车有几种
- gold: `zh_doc_005.md > 关键材料`
- best_topk_coverage: 0.361
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_005.md::c0015` score=0.757383 cov=0.361 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_005.md::c0018` score=0.731891 cov=0.342 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_005.md::c0019` score=0.729321 cov=0.341 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_005.md::c0017` score=0.726236 cov=0.318 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_005.md::c0023` score=0.712021 cov=0.118 section=中文复杂检索文档 > 补充材料2

### zh006 — zh_long_span_boundary_candidate
- question: 春光成语
- gold: `zh_doc_006.md > 关键材料`
- best_topk_coverage: 0.31
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_006.md::c0003` score=0.72807 cov=0.31 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_006.md::c0008` score=0.716385 cov=0.176 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_006.md::c0002` score=0.708238 cov=0.13 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_006.md::c0004` score=0.705245 cov=0.298 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_006.md::c0001` score=0.69651 cov=0.123 section=中文复杂检索文档 > 背景材料1

### zh007 — zh_long_span_boundary_candidate
- question: 经常用肥皂洗脸好吗
- gold: `zh_doc_007.md > 关键材料`
- best_topk_coverage: 0.33
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_007.md::c0011` score=0.791461 cov=0.133 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_007.md::c0009` score=0.78962 cov=0.117 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_007.md::c0010` score=0.761643 cov=0.105 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_007.md::c0004` score=0.755951 cov=0.295 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_007.md::c0006` score=0.755655 cov=0.33 section=中文复杂检索文档 > 关键材料

### zh008 — zh_long_span_boundary_candidate
- question: 冬天怎样养鹦鹉
- gold: `zh_doc_008.md > 关键材料`
- best_topk_coverage: 0.276
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_008.md::c0003` score=0.725259 cov=0.064 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_008.md::c0004` score=0.698984 cov=0.183 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_008.md::c0011` score=0.694763 cov=0.095 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_008.md::c0010` score=0.666714 cov=0.07 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_008.md::c0006` score=0.628609 cov=0.276 section=中文复杂检索文档 > 关键材料

### zh009 — zh_long_span_boundary_candidate
- question: 附睾肿胀
- gold: `zh_doc_009.md > 关键材料`
- best_topk_coverage: 0.42
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_009.md::c0006` score=0.762107 cov=0.42 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_009.md::c0013` score=0.745968 cov=0.098 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_009.md::c0005` score=0.725792 cov=0.229 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_009.md::c0012` score=0.71285 cov=0.126 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_009.md::c0010` score=0.71118 cov=0.396 section=中文复杂检索文档 > 关键材料

### zh010 — zh_long_span_boundary_candidate
- question: 硫磺皂能长期用吗
- gold: `zh_doc_010.md > 关键材料`
- best_topk_coverage: 0.277
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_010.md::c0008` score=0.793187 cov=0.053 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_010.md::c0009` score=0.765948 cov=0.042 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_010.md::c0000` score=0.764083 cov=0.054 section=
  - rank 4: `zh_doc_010.md::c0010` score=0.74988 cov=0.057 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_010.md::c0004` score=0.724318 cov=0.277 section=中文复杂检索文档 > 关键材料

### zh011 — zh_long_span_boundary_candidate
- question: 比较好看的电视剧
- gold: `zh_doc_011.md > 关键材料`
- best_topk_coverage: 0.19
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_011.md::c0000` score=0.618039 cov=0.078 section=
  - rank 2: `zh_doc_011.md::c0009` score=0.6152 cov=0.038 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_011.md::c0007` score=0.585963 cov=0.19 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_011.md::c0008` score=0.570159 cov=0.037 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_011.md::c0001` score=0.550349 cov=0.042 section=中文复杂检索文档 > 背景材料1

### zh012 — zh_long_span_boundary_candidate
- question: 夏天喝什么饮品好
- gold: `zh_doc_012.md > 关键材料`
- best_topk_coverage: 0.365
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_012.md::c0001` score=0.659401 cov=0.116 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_012.md::c0000` score=0.653822 cov=0.112 section=
  - rank 3: `zh_doc_012.md::c0002` score=0.615091 cov=0.307 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_012.md::c0008` score=0.587689 cov=0.057 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_012.md::c0003` score=0.58283 cov=0.365 section=中文复杂检索文档 > 关键材料

### zh013 — zh_long_span_boundary_candidate
- question: workgroup是什么
- gold: `zh_doc_013.md > 关键材料`
- best_topk_coverage: 0.395
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_013.md::c0000` score=0.707351 cov=0.093 section=
  - rank 2: `zh_doc_013.md::c0001` score=0.564231 cov=0.189 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_013.md::c0006` score=0.493052 cov=0.351 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_013.md::c0003` score=0.48635 cov=0.395 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_013.md::c0010` score=0.485068 cov=0.09 section=中文复杂检索文档 > 补充材料1

### zh014 — zh_long_span_boundary_candidate
- question: 怎样锻炼肺活量
- gold: `zh_doc_014.md > 关键材料`
- best_topk_coverage: 0.336
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_014.md::c0000` score=0.703814 cov=0.128 section=
  - rank 2: `zh_doc_014.md::c0005` score=0.701206 cov=0.227 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_014.md::c0011` score=0.699531 cov=0.09 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_014.md::c0006` score=0.697848 cov=0.336 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_014.md::c0003` score=0.6853 cov=0.077 section=中文复杂检索文档 > 背景材料1

### zh016 — zh_long_span_boundary_candidate
- question: 油电混合动力汽车购置税优惠吗
- gold: `zh_doc_016.md > 关键材料`
- best_topk_coverage: 0.405
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_016.md::c0006` score=0.806264 cov=0.387 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_016.md::c0004` score=0.758899 cov=0.281 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_016.md::c0011` score=0.742778 cov=0.313 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_016.md::c0012` score=0.736712 cov=0.158 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_016.md::c0010` score=0.732338 cov=0.405 section=中文复杂检索文档 > 关键材料

### zh017 — zh_long_span_boundary_candidate
- question: 阴部变白
- gold: `zh_doc_017.md > 关键材料`
- best_topk_coverage: 0.321
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_017.md::c0003` score=0.704028 cov=0.139 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_017.md::c0010` score=0.695302 cov=0.025 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_017.md::c0000` score=0.680065 cov=0.036 section=
  - rank 4: `zh_doc_017.md::c0001` score=0.677015 cov=0.055 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_017.md::c0004` score=0.6637 cov=0.321 section=中文复杂检索文档 > 关键材料

### zh018 — zh_long_span_boundary_candidate
- question: 如何买卖etf基金
- gold: `zh_doc_018.md > 关键材料`
- best_topk_coverage: 0.429
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_018.md::c0003` score=0.779355 cov=0.289 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_018.md::c0008` score=0.752162 cov=0.168 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_018.md::c0004` score=0.739006 cov=0.429 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_018.md::c0000` score=0.730025 cov=0.176 section=
  - rank 5: `zh_doc_018.md::c0009` score=0.715477 cov=0.194 section=中文复杂检索文档 > 补充材料2

### zh019 — zh_long_span_boundary_candidate
- question: 在实习期内的驾驶证扣分会怎样
- gold: `zh_doc_019.md > 关键材料`
- best_topk_coverage: 0.553
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_019.md::c0008` score=0.78234 cov=0.432 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_019.md::c0010` score=0.778796 cov=0.269 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_019.md::c0009` score=0.768031 cov=0.437 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_019.md::c0000` score=0.759158 cov=0.362 section=
  - rank 5: `zh_doc_019.md::c0006` score=0.75374 cov=0.553 section=中文复杂检索文档 > 关键材料

### zh020 — zh_long_span_boundary_candidate
- question: 私立大学和公立大学的区别
- gold: `zh_doc_020.md > 关键材料`
- best_topk_coverage: 0.124
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_020.md::c0012` score=0.798635 cov=0.084 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_020.md::c0013` score=0.771631 cov=0.09 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_020.md::c0006` score=0.767051 cov=0.124 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_020.md::c0003` score=0.758501 cov=0.097 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_020.md::c0001` score=0.747361 cov=0.091 section=中文复杂检索文档 > 背景材料1

### zh022 — zh_long_span_boundary_candidate
- question: 怎样种香菜
- gold: `zh_doc_022.md > 关键材料`
- best_topk_coverage: 0.386
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_022.md::c0018` score=0.727831 cov=0.083 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_022.md::c0016` score=0.713854 cov=0.104 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_022.md::c0012` score=0.697449 cov=0.386 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_022.md::c0001` score=0.693759 cov=0.104 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_022.md::c0002` score=0.692033 cov=0.189 section=中文复杂检索文档 > 背景材料1

### zh023 — zh_long_span_boundary_candidate
- question: 如何把电脑上的东西传到ipad上
- gold: `zh_doc_023.md > 关键材料`
- best_topk_coverage: 0.472
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_023.md::c0004` score=0.774824 cov=0.417 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_023.md::c0001` score=0.765848 cov=0.094 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_023.md::c0005` score=0.74954 cov=0.472 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_023.md::c0009` score=0.749145 cov=0.174 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_023.md::c0003` score=0.737408 cov=0.123 section=中文复杂检索文档 > 背景材料2

### zh024 — zh_long_span_boundary_candidate
- question: c1扣12分怎么办
- gold: `zh_doc_024.md > 关键材料`
- best_topk_coverage: 0.41
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_024.md::c0005` score=0.774622 cov=0.375 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_024.md::c0012` score=0.77032 cov=0.2 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_024.md::c0002` score=0.768508 cov=0.174 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_024.md::c0010` score=0.765909 cov=0.41 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_024.md::c0001` score=0.765593 cov=0.336 section=中文复杂检索文档 > 背景材料1

### zh025 — zh_long_span_boundary_candidate
- question: tf与sd卡的区别
- gold: `zh_doc_025.md > 关键材料`
- best_topk_coverage: 0.448
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_025.md::c0010` score=0.82889 cov=0.328 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_025.md::c0011` score=0.815012 cov=0.345 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_025.md::c0002` score=0.811458 cov=0.299 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_025.md::c0014` score=0.811217 cov=0.328 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_025.md::c0003` score=0.809384 cov=0.448 section=中文复杂检索文档 > 背景材料1

### zh027 — zh_long_span_boundary_candidate
- question: 小米平板钢化膜怎么贴
- gold: `zh_doc_027.md > 关键材料`
- best_topk_coverage: 0.041
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_027.md::c0010` score=0.715024 cov=0.037 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_081.md::c0005` score=0.688865 cov=0.0 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_027.md::c0011` score=0.680883 cov=0.01 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_081.md::c0014` score=0.680777 cov=0.0 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_027.md::c0000` score=0.666384 cov=0.041 section=

### zh028 — zh_long_span_boundary_candidate
- question: 怎么控制路由器把蹭wifi的人给踢了
- gold: `zh_doc_028.md > 关键材料`
- best_topk_coverage: 0.606
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_028.md::c0001` score=0.767757 cov=0.185 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_028.md::c0002` score=0.752065 cov=0.264 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_028.md::c0006` score=0.746267 cov=0.206 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_028.md::c0003` score=0.737798 cov=0.606 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_028.md::c0000` score=0.727815 cov=0.155 section=

### zh029 — zh_long_span_boundary_candidate
- question: 怎么做卫浴销售
- gold: `zh_doc_029.md > 关键材料`
- best_topk_coverage: 0.524
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_029.md::c0002` score=0.765427 cov=0.058 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_029.md::c0001` score=0.758003 cov=0.082 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_029.md::c0000` score=0.700068 cov=0.065 section=
  - rank 4: `zh_doc_029.md::c0004` score=0.697954 cov=0.524 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_029.md::c0006` score=0.678474 cov=0.445 section=中文复杂检索文档 > 关键材料

### zh030 — zh_long_span_boundary_candidate
- question: 外伤缝针不能吃什么
- gold: `zh_doc_030.md > 关键材料`
- best_topk_coverage: 0.289
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_030.md::c0002` score=0.731877 cov=0.189 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_030.md::c0012` score=0.72219 cov=0.11 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_030.md::c0003` score=0.715443 cov=0.122 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_030.md::c0010` score=0.705943 cov=0.289 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_030.md::c0000` score=0.702306 cov=0.136 section=

### zh031 — zh_long_span_boundary_candidate
- question: 超级会员是什么
- gold: `zh_doc_031.md > 关键材料`
- best_topk_coverage: 0.517
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_031.md::c0007` score=0.685755 cov=0.244 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_031.md::c0006` score=0.675546 cov=0.244 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_031.md::c0003` score=0.664838 cov=0.517 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_031.md::c0008` score=0.64287 cov=0.192 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_031.md::c0001` score=0.639057 cov=0.198 section=中文复杂检索文档 > 背景材料1

### zh032 — zh_long_span_boundary_candidate
- question: 杭州劳动仲裁电话
- gold: `zh_doc_032.md > 关键材料`
- best_topk_coverage: 0.396
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_032.md::c0002` score=0.772656 cov=0.236 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_032.md::c0016` score=0.747523 cov=0.124 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_032.md::c0017` score=0.736539 cov=0.192 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_032.md::c0007` score=0.729514 cov=0.192 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_032.md::c0005` score=0.725384 cov=0.396 section=中文复杂检索文档 > 关键材料

### zh033 — zh_long_span_boundary_candidate
- question: 电暖桌哪个牌子好
- gold: `zh_doc_033.md > 关键材料`
- best_topk_coverage: 0.349
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_033.md::c0004` score=0.795673 cov=0.349 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_033.md::c0001` score=0.78351 cov=0.103 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_033.md::c0007` score=0.770173 cov=0.091 section=中文复杂检索文档 > 补充
  - rank 4: `zh_doc_033.md::c0008` score=0.76646 cov=0.089 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_033.md::c0011` score=0.763818 cov=0.077 section=中文复杂检索文档 > 补充材料2

### zh034 — zh_long_span_boundary_candidate
- question: 板栗可以蒸着吃吗
- gold: `zh_doc_034.md > 关键材料`
- best_topk_coverage: 0.49
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_034.md::c0004` score=0.728715 cov=0.14 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_034.md::c0005` score=0.710006 cov=0.49 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_034.md::c0010` score=0.634665 cov=0.097 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_034.md::c0001` score=0.633847 cov=0.118 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_034.md::c0007` score=0.626063 cov=0.471 section=中文复杂检索文档 > 关键材料

### zh036 — zh_long_span_boundary_candidate
- question: 苹果系统怎么查看隐藏文件
- gold: `zh_doc_036.md > 关键材料`
- best_topk_coverage: 0.525
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_036.md::c0004` score=0.760116 cov=0.478 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_036.md::c0003` score=0.756305 cov=0.525 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_036.md::c0005` score=0.743847 cov=0.442 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_036.md::c0000` score=0.704396 cov=0.221 section=
  - rank 5: `zh_doc_036.md::c0006` score=0.665136 cov=0.269 section=中文复杂检索文档 > 补充材料1

### zh037 — zh_long_span_boundary_candidate
- question: 海淀医院孕前检查
- gold: `zh_doc_037.md > 关键材料`
- best_topk_coverage: 0.44
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_037.md::c0000` score=0.733445 cov=0.071 section=
  - rank 2: `zh_doc_037.md::c0006` score=0.726264 cov=0.271 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_037.md::c0004` score=0.719806 cov=0.44 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_037.md::c0003` score=0.70958 cov=0.212 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_037.md::c0002` score=0.617172 cov=0.079 section=中文复杂检索文档 > 背景材料2

### zh038 — zh_long_span_boundary_candidate
- question: 玩梦幻西游怎么赚钱
- gold: `zh_doc_038.md > 关键材料`
- best_topk_coverage: 0.494
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_038.md::c0003` score=0.725846 cov=0.081 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_038.md::c0000` score=0.720347 cov=0.074 section=
  - rank 3: `zh_doc_038.md::c0005` score=0.644158 cov=0.494 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_038.md::c0007` score=0.639311 cov=0.168 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_038.md::c0009` score=0.620881 cov=0.038 section=中文复杂检索文档 > 补充材料2

### zh039 — zh_long_span_boundary_candidate
- question: 跟庐山有关的诗句
- gold: `zh_doc_039.md > 关键材料`
- best_topk_coverage: 0.486
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_039.md::c0005` score=0.716488 cov=0.267 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_039.md::c0002` score=0.706315 cov=0.244 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_039.md::c0006` score=0.688108 cov=0.053 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_039.md::c0003` score=0.677811 cov=0.486 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_039.md::c0001` score=0.675124 cov=0.065 section=中文复杂检索文档 > 背景材料1

### zh040 — zh_long_span_boundary_candidate
- question: 现在去哪里下载音乐
- gold: `zh_doc_040.md > 关键材料`
- best_topk_coverage: 0.493
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_040.md::c0000` score=0.631478 cov=0.137 section=
  - rank 2: `zh_doc_040.md::c0001` score=0.618767 cov=0.096 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_040.md::c0003` score=0.61806 cov=0.493 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_040.md::c0006` score=0.610036 cov=0.103 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_040.md::c0007` score=0.609738 cov=0.066 section=中文复杂检索文档 > 补充材料1

### zh041 — zh_long_span_boundary_candidate
- question: 治疗颈椎病药物
- gold: `zh_doc_041.md > 关键材料`
- best_topk_coverage: 0.419
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_041.md::c0011` score=0.718112 cov=0.109 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_041.md::c0012` score=0.659429 cov=0.107 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_041.md::c0007` score=0.64828 cov=0.419 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_041.md::c0004` score=0.633362 cov=0.103 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_041.md::c0005` score=0.612472 cov=0.137 section=中文复杂检索文档 > 背景材料2

### zh044 — zh_long_span_boundary_candidate
- question: 换外汇哪个银行好
- gold: `zh_doc_044.md > 关键材料`
- best_topk_coverage: 0.296
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_044.md::c0000` score=0.838119 cov=0.079 section=
  - rank 2: `zh_doc_044.md::c0002` score=0.79677 cov=0.174 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_044.md::c0006` score=0.777312 cov=0.229 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_044.md::c0001` score=0.777075 cov=0.095 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_044.md::c0005` score=0.737872 cov=0.296 section=中文复杂检索文档 > 关键材料

### zh046 — zh_long_span_boundary_candidate
- question: 手机外放进水
- gold: `zh_doc_046.md > 关键材料`
- best_topk_coverage: 0.491
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_046.md::c0000` score=0.735881 cov=0.114 section=
  - rank 2: `zh_doc_046.md::c0007` score=0.731744 cov=0.109 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_046.md::c0002` score=0.719792 cov=0.084 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_046.md::c0006` score=0.708113 cov=0.316 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_046.md::c0005` score=0.705311 cov=0.491 section=中文复杂检索文档 > 关键材料

### zh047 — zh_long_span_boundary_candidate
- question: 什么样的借条不具法律效力
- gold: `zh_doc_047.md > 关键材料`
- best_topk_coverage: 0.6
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_047.md::c0012` score=0.789541 cov=0.147 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_047.md::c0013` score=0.787995 cov=0.167 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_047.md::c0011` score=0.771312 cov=0.422 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_047.md::c0009` score=0.765161 cov=0.6 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_047.md::c0000` score=0.757008 cov=0.184 section=

### zh048 — zh_long_span_boundary_candidate
- question: m8a1用什么炮
- gold: `zh_doc_048.md > 关键材料`
- best_topk_coverage: 0.472
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_048.md::c0008` score=0.710665 cov=0.102 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_048.md::c0003` score=0.678927 cov=0.177 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_048.md::c0006` score=0.656858 cov=0.267 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_048.md::c0007` score=0.653699 cov=0.102 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_048.md::c0004` score=0.643155 cov=0.472 section=中文复杂检索文档 > 关键材料

### zh050 — zh_long_span_boundary_candidate
- question: xm外汇平台怎么样
- gold: `zh_doc_050.md > 关键材料`
- best_topk_coverage: 0.265
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_050.md::c0002` score=0.829139 cov=0.21 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_050.md::c0006` score=0.828971 cov=0.232 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_050.md::c0000` score=0.785202 cov=0.084 section=
  - rank 4: `zh_doc_050.md::c0005` score=0.761813 cov=0.265 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_050.md::c0001` score=0.69274 cov=0.084 section=中文复杂检索文档 > 背景材料1

### zh051 — zh_long_span_boundary_candidate
- question: 双人床最小宽度
- gold: `zh_doc_051.md > 关键材料`
- best_topk_coverage: 0.533
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_051.md::c0014` score=0.760512 cov=0.119 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_051.md::c0008` score=0.755889 cov=0.533 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_051.md::c0000` score=0.748644 cov=0.078 section=
  - rank 4: `zh_doc_051.md::c0001` score=0.74724 cov=0.072 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_051.md::c0010` score=0.737072 cov=0.316 section=中文复杂检索文档 > 关键材料

### zh053 — zh_long_span_boundary_candidate
- question: 龟头敏感度低怎么办
- gold: `zh_doc_053.md > 关键材料`
- best_topk_coverage: 0.481
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_053.md::c0000` score=0.767137 cov=0.051 section=
  - rank 2: `zh_doc_053.md::c0017` score=0.748517 cov=0.117 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_053.md::c0004` score=0.741236 cov=0.133 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_053.md::c0014` score=0.738331 cov=0.241 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_053.md::c0012` score=0.735203 cov=0.481 section=中文复杂检索文档 > 关键材料

### zh054 — zh_long_span_boundary_candidate
- question: 沪陕高速限速多少
- gold: `zh_doc_054.md > 关键材料`
- best_topk_coverage: 0.552
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_054.md::c0003` score=0.723663 cov=0.552 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_054.md::c0004` score=0.707036 cov=0.542 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_054.md::c0002` score=0.686627 cov=0.265 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_054.md::c0006` score=0.649845 cov=0.094 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_054.md::c0000` score=0.637797 cov=0.096 section=

### zh055 — zh_long_span_boundary_candidate
- question: ios9 如何关闭搜索最近联系人
- gold: `zh_doc_055.md > 关键材料`
- best_topk_coverage: 0.611
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_055.md::c0000` score=0.806686 cov=0.459 section=
  - rank 2: `zh_doc_055.md::c0006` score=0.790157 cov=0.301 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_055.md::c0002` score=0.787668 cov=0.601 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_055.md::c0003` score=0.780202 cov=0.611 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_055.md::c0005` score=0.765803 cov=0.462 section=中文复杂检索文档 > 关键材料

### zh057 — zh_long_span_boundary_candidate
- question: word怎么不能修改
- gold: `zh_doc_057.md > 关键材料`
- best_topk_coverage: 0.166
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_057.md::c0012` score=0.73894 cov=0.121 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_057.md::c0001` score=0.728443 cov=0.166 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_057.md::c0000` score=0.720023 cov=0.101 section=
  - rank 4: `zh_doc_057.md::c0020` score=0.710982 cov=0.155 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_057.md::c0014` score=0.709205 cov=0.141 section=中文复杂检索文档 > 背景材料2

### zh058 — zh_long_span_boundary_candidate
- question: 我国古代第一个有伟大成就的爱国诗人是( )
- gold: `zh_doc_058.md > 关键材料`
- best_topk_coverage: 0.25
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_058.md::c0006` score=0.698524 cov=0.25 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_058.md::c0009` score=0.696693 cov=0.115 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_058.md::c0007` score=0.667553 cov=0.149 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_058.md::c0008` score=0.642596 cov=0.091 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_058.md::c0010` score=0.634981 cov=0.077 section=中文复杂检索文档 > 补充材料1

### zh062 — zh_long_span_boundary_candidate
- question: 如何取消电脑的自动休眠
- gold: `zh_doc_062.md > 关键材料`
- best_topk_coverage: 0.253
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_062.md::c0005` score=0.827728 cov=0.103 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_062.md::c0006` score=0.806609 cov=0.253 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_062.md::c0000` score=0.782576 cov=0.203 section=
  - rank 4: `zh_doc_062.md::c0004` score=0.735234 cov=0.226 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_062.md::c0011` score=0.732563 cov=0.171 section=中文复杂检索文档 > 补充材料1

### zh064 — zh_long_span_boundary_candidate
- question: 血清甘油三脂偏低
- gold: `zh_doc_064.md > 关键材料`
- best_topk_coverage: 0.639
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_064.md::c0004` score=0.792332 cov=0.639 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_064.md::c0002` score=0.78608 cov=0.584 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_064.md::c0003` score=0.784021 cov=0.511 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_064.md::c0012` score=0.762149 cov=0.361 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_064.md::c0001` score=0.75843 cov=0.491 section=中文复杂检索文档 > 背景材料1

### zh066 — zh_long_span_boundary_candidate
- question: 电动牙刷刷的干净吗
- gold: `zh_doc_066.md > 关键材料`
- best_topk_coverage: 0.567
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_066.md::c0000` score=0.707145 cov=0.204 section=
  - rank 2: `zh_doc_066.md::c0002` score=0.679272 cov=0.226 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_066.md::c0001` score=0.657612 cov=0.192 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_066.md::c0003` score=0.654244 cov=0.567 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_066.md::c0012` score=0.653712 cov=0.136 section=中文复杂检索文档 > 补充材料2

### zh067 — zh_long_span_boundary_candidate
- question: 武松属什么
- gold: `zh_doc_067.md > 关键材料`
- best_topk_coverage: 0.432
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_067.md::c0004` score=0.738443 cov=0.432 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_067.md::c0000` score=0.619936 cov=0.009 section=
  - rank 3: `zh_doc_067.md::c0001` score=0.606905 cov=0.015 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_067.md::c0002` score=0.595267 cov=0.006 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_067.md::c0008` score=0.589824 cov=0.009 section=中文复杂检索文档 > 补充材料2

### zh070 — zh_long_span_boundary_candidate
- question: qq经常掉线怎么回事
- gold: `zh_doc_070.md > 关键材料`
- best_topk_coverage: 0.375
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_070.md::c0010` score=0.77694 cov=0.091 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_070.md::c0007` score=0.773237 cov=0.07 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_070.md::c0005` score=0.766215 cov=0.061 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_070.md::c0002` score=0.763796 cov=0.375 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_070.md::c0000` score=0.756283 cov=0.091 section=

### zh071 — zh_long_span_boundary_candidate
- question: 还珠格格第一部背景音乐
- gold: `zh_doc_071.md > 关键材料`
- best_topk_coverage: 0.617
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_071.md::c0014` score=0.674057 cov=0.617 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_071.md::c0003` score=0.668164 cov=0.16 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_071.md::c0002` score=0.645427 cov=0.157 section=中文复杂检索文档 > 背景
  - rank 4: `zh_doc_071.md::c0001` score=0.600619 cov=0.24 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_071.md::c0016` score=0.590631 cov=0.436 section=中文复杂检索文档 > 关键材料

### zh072 — zh_long_span_boundary_candidate
- question: 我的世界手机版0.12.1末地传送门怎么做
- gold: `zh_doc_072.md > 关键材料`
- best_topk_coverage: 0.42
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_072.md::c0007` score=0.793499 cov=0.179 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_072.md::c0002` score=0.788137 cov=0.153 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_072.md::c0006` score=0.776798 cov=0.199 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_072.md::c0003` score=0.768848 cov=0.42 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_072.md::c0000` score=0.748886 cov=0.169 section=

### zh074 — zh_long_span_boundary_candidate
- question: 胃功能
- gold: `zh_doc_074.md > 关键材料`
- best_topk_coverage: 0.595
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_074.md::c0003` score=0.726428 cov=0.588 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_074.md::c0002` score=0.692637 cov=0.088 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_074.md::c0005` score=0.675135 cov=0.17 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_074.md::c0000` score=0.666446 cov=0.124 section=
  - rank 5: `zh_doc_074.md::c0004` score=0.639707 cov=0.595 section=中文复杂检索文档 > 关键材料

### zh075 — zh_long_span_boundary_candidate
- question: 艾俐缇陶瓷怎么样
- gold: `zh_doc_075.md > 关键材料`
- best_topk_coverage: 0.137
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_075.md::c0006` score=0.740568 cov=0.02 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_075.md::c0002` score=0.704304 cov=0.137 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_075.md::c0005` score=0.668771 cov=0.067 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_075.md::c0000` score=0.616834 cov=0.017 section=
  - rank 5: `zh_doc_075.md::c0001` score=0.61612 cov=0.032 section=中文复杂检索文档 > 背景材料1

### zh076 — zh_long_span_boundary_candidate
- question: 公共事业管理属于什么专业类别
- gold: `zh_doc_076.md > 关键材料`
- best_topk_coverage: 0.567
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_076.md::c0002` score=0.817078 cov=0.567 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_076.md::c0006` score=0.745191 cov=0.201 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_076.md::c0008` score=0.744038 cov=0.201 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_076.md::c0010` score=0.736766 cov=0.201 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_076.md::c0009` score=0.72771 cov=0.179 section=中文复杂检索文档 > 补充材料1

### zh077 — zh_long_span_boundary_candidate
- question: 天然无添加的护肤品存在吗
- gold: `zh_doc_077.md > 关键材料`
- best_topk_coverage: 0.584
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_077.md::c0018` score=0.762698 cov=0.584 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_077.md::c0019` score=0.735145 cov=0.379 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_077.md::c0020` score=0.694087 cov=0.157 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_077.md::c0021` score=0.688663 cov=0.162 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_077.md::c0017` score=0.669468 cov=0.422 section=中文复杂检索文档 > 背景材料2

### zh078 — zh_long_span_boundary_candidate
- question: 旅行发票 可以报吗
- gold: `zh_doc_078.md > 关键材料`
- best_topk_coverage: 0.578
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_078.md::c0000` score=0.764365 cov=0.067 section=
  - rank 2: `zh_doc_078.md::c0002` score=0.73661 cov=0.253 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_078.md::c0005` score=0.729432 cov=0.11 section=中文复杂检索文档 > 补充材料
  - rank 4: `zh_doc_078.md::c0006` score=0.720072 cov=0.126 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_078.md::c0004` score=0.715157 cov=0.578 section=中文复杂检索文档 > 关键材料

### zh079 — zh_long_span_boundary_candidate
- question: 种子可以用百度云下载吗
- gold: `zh_doc_079.md > 关键材料`
- best_topk_coverage: 0.527
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_079.md::c0003` score=0.708657 cov=0.527 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_079.md::c0006` score=0.683756 cov=0.182 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_079.md::c0002` score=0.679092 cov=0.197 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_079.md::c0000` score=0.674459 cov=0.167 section=
  - rank 5: `zh_doc_079.md::c0005` score=0.667999 cov=0.191 section=中文复杂检索文档 > 关键材料

### zh081 — zh_long_span_boundary_candidate
- question: 手机钢化保护膜怎么贴
- gold: `zh_doc_081.md > 关键材料`
- best_topk_coverage: 0.588
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_081.md::c0005` score=0.765848 cov=0.161 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_081.md::c0013` score=0.759441 cov=0.588 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_027.md::c0004` score=0.753285 cov=0.0 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_081.md::c0006` score=0.753031 cov=0.155 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_081.md::c0014` score=0.752088 cov=0.579 section=中文复杂检索文档 > 关键材料

### zh082 — zh_long_span_boundary_candidate
- question: 中国古代最繁荣的朝代
- gold: `zh_doc_082.md > 关键材料`
- best_topk_coverage: 0.09
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_082.md::c0000` score=0.714721 cov=0.053 section=
  - rank 2: `zh_doc_082.md::c0007` score=0.666743 cov=0.072 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_082.md::c0006` score=0.662502 cov=0.05 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_082.md::c0005` score=0.658606 cov=0.053 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_082.md::c0001` score=0.655165 cov=0.09 section=中文复杂检索文档 > 背景材料1

### zh083 — zh_long_span_boundary_candidate
- question: 怎么改民族
- gold: `zh_doc_083.md > 关键材料`
- best_topk_coverage: 0.637
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_083.md::c0024` score=0.701472 cov=0.637 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_083.md::c0032` score=0.694781 cov=0.18 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_083.md::c0001` score=0.689997 cov=0.236 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_083.md::c0000` score=0.689758 cov=0.159 section=
  - rank 5: `zh_doc_083.md::c0031` score=0.66117 cov=0.242 section=中文复杂检索文档 > 补充材料1

### zh085 — zh_long_span_boundary_candidate
- question: 白带有酸奶味
- gold: `zh_doc_085.md > 关键材料`
- best_topk_coverage: 0.371
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_085.md::c0022` score=0.739082 cov=0.099 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_085.md::c0000` score=0.733913 cov=0.111 section=
  - rank 3: `zh_doc_085.md::c0015` score=0.716563 cov=0.371 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_085.md::c0002` score=0.715085 cov=0.096 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_085.md::c0020` score=0.71487 cov=0.066 section=中文复杂检索文档 > 补充材料1

### zh089 — zh_long_span_boundary_candidate
- question: 部落冲突怎么搜死鱼
- gold: `zh_doc_089.md > 关键材料`
- best_topk_coverage: 0.456
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_089.md::c0000` score=0.799365 cov=0.092 section=
  - rank 2: `zh_doc_089.md::c0002` score=0.768671 cov=0.456 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_089.md::c0001` score=0.75385 cov=0.092 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_089.md::c0004` score=0.716928 cov=0.189 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_089.md::c0006` score=0.706617 cov=0.092 section=中文复杂检索文档 > 补充材料2

### zh090 — zh_long_span_boundary_candidate
- question: 牛剖层移膜皮是什么
- gold: `zh_doc_090.md > 关键材料`
- best_topk_coverage: 0.545
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_090.md::c0016` score=0.716423 cov=0.404 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_090.md::c0001` score=0.697076 cov=0.129 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_090.md::c0017` score=0.688208 cov=0.545 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_090.md::c0018` score=0.684439 cov=0.285 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_090.md::c0010` score=0.680742 cov=0.103 section=中文复杂检索文档 > 背景材料2

### zh093 — zh_long_span_boundary_candidate
- question: 成都审驾照需要什么
- gold: `zh_doc_093.md > 关键材料`
- best_topk_coverage: 0.179
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_093.md::c0016` score=0.728736 cov=0.128 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_093.md::c0000` score=0.718554 cov=0.132 section=
  - rank 3: `zh_doc_093.md::c0008` score=0.717447 cov=0.179 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_093.md::c0015` score=0.716465 cov=0.11 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_093.md::c0003` score=0.715875 cov=0.172 section=中文复杂检索文档 > 背景材料1

### zh094 — zh_long_span_boundary_candidate
- question: 霜是怎么形成的
- gold: `zh_doc_094.md > 关键材料`
- best_topk_coverage: 0.077
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_094.md::c0011` score=0.699358 cov=0.028 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_094.md::c0000` score=0.696477 cov=0.043 section=
  - rank 3: `zh_doc_094.md::c0001` score=0.631211 cov=0.062 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_094.md::c0006` score=0.603478 cov=0.077 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_094.md::c0012` score=0.588446 cov=0.02 section=中文复杂检索文档 > 补充材料2

### zh095 — zh_long_span_boundary_candidate
- question: 卫生间铺什么地砖好
- gold: `zh_doc_095.md > 关键材料`
- best_topk_coverage: 0.576
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_095.md::c0001` score=0.646309 cov=0.154 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_095.md::c0002` score=0.640473 cov=0.142 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_095.md::c0007` score=0.629031 cov=0.576 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_095.md::c0006` score=0.625607 cov=0.576 section=中文复杂检索文档 > 关
  - rank 5: `zh_doc_095.md::c0000` score=0.600526 cov=0.142 section=

### zh096 — zh_long_span_boundary_candidate
- question: 肠结核的症状
- gold: `zh_doc_096.md > 关键材料`
- best_topk_coverage: 0.557
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_096.md::c0005` score=0.757349 cov=0.557 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_096.md::c0001` score=0.756082 cov=0.126 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_096.md::c0007` score=0.698159 cov=0.12 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_096.md::c0006` score=0.688033 cov=0.191 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_096.md::c0000` score=0.681931 cov=0.123 section=

### zh097 — zh_long_span_boundary_candidate
- question: 表带怎么打孔
- gold: `zh_doc_097.md > 关键材料`
- best_topk_coverage: 0.407
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_097.md::c0003` score=0.764732 cov=0.25 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_097.md::c0005` score=0.736675 cov=0.407 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_097.md::c0008` score=0.736257 cov=0.081 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_097.md::c0006` score=0.730123 cov=0.09 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_097.md::c0000` score=0.719884 cov=0.09 section=

### zh100 — zh_long_span_boundary_candidate
- question: 红枣表面有层白色粉末
- gold: `zh_doc_100.md > 关键材料`
- best_topk_coverage: 0.58
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_100.md::c0004` score=0.802301 cov=0.309 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_100.md::c0006` score=0.782271 cov=0.066 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_100.md::c0005` score=0.772031 cov=0.057 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_100.md::c0003` score=0.767725 cov=0.58 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_100.md::c0000` score=0.726394 cov=0.093 section=

### zh101 — zh_long_span_boundary_candidate
- question: 小米的平板好用吗
- gold: `zh_doc_101.md > 关键材料`
- best_topk_coverage: 0.577
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_101.md::c0010` score=0.767351 cov=0.577 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_101.md::c0016` score=0.747528 cov=0.044 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_101.md::c0013` score=0.712854 cov=0.081 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_101.md::c0001` score=0.699335 cov=0.066 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_101.md::c0000` score=0.696379 cov=0.096 section=

### zh102 — zh_long_span_boundary_candidate
- question: 尺神经麻痹治疗
- gold: `zh_doc_102.md > 关键材料`
- best_topk_coverage: 0.164
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_102.md::c0004` score=0.741975 cov=0.078 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_102.md::c0005` score=0.739667 cov=0.164 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_102.md::c0011` score=0.728995 cov=0.072 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_102.md::c0002` score=0.725525 cov=0.11 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_102.md::c0009` score=0.716223 cov=0.098 section=中文复杂检索文档 > 补充材料1

### zh103 — zh_long_span_boundary_candidate
- question: 北京出国体检在哪里
- gold: `zh_doc_103.md > 关键材料`
- best_topk_coverage: 0.623
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_103.md::c0004` score=0.790148 cov=0.623 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_103.md::c0006` score=0.769273 cov=0.242 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_103.md::c0001` score=0.768895 cov=0.242 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_103.md::c0007` score=0.763532 cov=0.361 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_103.md::c0000` score=0.727456 cov=0.222 section=

### zh110 — zh_long_span_boundary_candidate
- question: 完美世界出过什么游戏
- gold: `zh_doc_110.md > 关键材料`
- best_topk_coverage: 0.607
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_110.md::c0000` score=0.627388 cov=0.061 section=
  - rank 2: `zh_doc_110.md::c0001` score=0.565055 cov=0.088 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_110.md::c0006` score=0.560045 cov=0.067 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_110.md::c0003` score=0.55796 cov=0.607 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_110.md::c0004` score=0.525067 cov=0.473 section=中文复杂检索文档 > 关键材料

### zh113 — zh_long_span_boundary_candidate
- question: 辅酶q10的服用方法
- gold: `zh_doc_113.md > 关键材料`
- best_topk_coverage: 0.52
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_113.md::c0008` score=0.784521 cov=0.124 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_113.md::c0003` score=0.759457 cov=0.138 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_113.md::c0007` score=0.730721 cov=0.52 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_113.md::c0001` score=0.724021 cov=0.127 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_113.md::c0004` score=0.718931 cov=0.116 section=中文复杂检索文档 > 背景材料2

### zh117 — zh_long_span_boundary_candidate
- question: 德国红铁元和绿铁元有什么区别
- gold: `zh_doc_117.md > 关键材料`
- best_topk_coverage: 0.227
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_117.md::c0002` score=0.767059 cov=0.227 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_117.md::c0001` score=0.756203 cov=0.199 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_117.md::c0006` score=0.736702 cov=0.224 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_117.md::c0005` score=0.703515 cov=0.217 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_117.md::c0000` score=0.694493 cov=0.189 section=

## All Query Summary

| qid | expected type | success | rank | best cov | gold rank hint |
|---|---|---:|---:|---:|---:|
| zh001 | zh_long_span_boundary_candidate | False | None | 0.646 | 1 |
| zh002 | zh_long_span_boundary_candidate | False | None | 0.163 | 1 |
| zh003 | zh_long_span_boundary_candidate | False | None | 0.206 | 1 |
| zh004 | zh_long_span_boundary_candidate | False | None | 0.276 | 1 |
| zh005 | zh_long_span_boundary_candidate | False | None | 0.361 | 1 |
| zh006 | zh_long_span_boundary_candidate | False | None | 0.31 | 1 |
| zh007 | zh_long_span_boundary_candidate | False | None | 0.33 | 1 |
| zh008 | zh_long_span_boundary_candidate | False | None | 0.276 | 1 |
| zh009 | zh_long_span_boundary_candidate | False | None | 0.42 | 1 |
| zh010 | zh_long_span_boundary_candidate | False | None | 0.277 | 1 |
| zh011 | zh_long_span_boundary_candidate | False | None | 0.19 | 1 |
| zh012 | zh_long_span_boundary_candidate | False | None | 0.365 | 1 |
| zh013 | zh_long_span_boundary_candidate | False | None | 0.395 | 1 |
| zh014 | zh_long_span_boundary_candidate | False | None | 0.336 | 1 |
| zh015 | zh_long_span_boundary_candidate | True | 5 | 0.775 | 1 |
| zh016 | zh_long_span_boundary_candidate | False | None | 0.405 | 1 |
| zh017 | zh_long_span_boundary_candidate | False | None | 0.321 | 1 |
| zh018 | zh_long_span_boundary_candidate | False | None | 0.429 | 1 |
| zh019 | zh_long_span_boundary_candidate | False | None | 0.553 | 1 |
| zh020 | zh_long_span_boundary_candidate | False | None | 0.124 | 1 |
| zh021 | zh_long_span_boundary_candidate | True | 3 | 0.692 | 1 |
| zh022 | zh_long_span_boundary_candidate | False | None | 0.386 | 1 |
| zh023 | zh_long_span_boundary_candidate | False | None | 0.472 | 1 |
| zh024 | zh_long_span_boundary_candidate | False | None | 0.41 | 1 |
| zh025 | zh_long_span_boundary_candidate | False | None | 0.448 | 1 |
| zh026 | zh_long_span_boundary_candidate | True | 4 | 0.921 | 1 |
| zh027 | zh_long_span_boundary_candidate | False | None | 0.041 | 1 |
| zh028 | zh_long_span_boundary_candidate | False | None | 0.606 | 1 |
| zh029 | zh_long_span_boundary_candidate | False | None | 0.524 | 1 |
| zh030 | zh_long_span_boundary_candidate | False | None | 0.289 | 1 |
| zh031 | zh_long_span_boundary_candidate | False | None | 0.517 | 1 |
| zh032 | zh_long_span_boundary_candidate | False | None | 0.396 | 1 |
| zh033 | zh_long_span_boundary_candidate | False | None | 0.349 | 1 |
| zh034 | zh_long_span_boundary_candidate | False | None | 0.49 | 1 |
| zh035 | zh_long_span_boundary_candidate | True | 3 | 0.772 | 1 |
| zh036 | zh_long_span_boundary_candidate | False | None | 0.525 | 1 |
| zh037 | zh_long_span_boundary_candidate | False | None | 0.44 | 1 |
| zh038 | zh_long_span_boundary_candidate | False | None | 0.494 | 1 |
| zh039 | zh_long_span_boundary_candidate | False | None | 0.486 | 1 |
| zh040 | zh_long_span_boundary_candidate | False | None | 0.493 | 1 |
| zh041 | zh_long_span_boundary_candidate | False | None | 0.419 | 1 |
| zh042 | zh_long_span_boundary_candidate | True | 2 | 0.842 | 1 |
| zh043 | zh_long_span_boundary_candidate | True | 3 | 0.702 | 1 |
| zh044 | zh_long_span_boundary_candidate | False | None | 0.296 | 1 |
| zh045 | zh_long_span_boundary_candidate | True | 3 | 0.835 | 1 |
| zh046 | zh_long_span_boundary_candidate | False | None | 0.491 | 1 |
| zh047 | zh_long_span_boundary_candidate | False | None | 0.6 | 1 |
| zh048 | zh_long_span_boundary_candidate | False | None | 0.472 | 1 |
| zh049 | zh_long_span_boundary_candidate | True | 4 | 0.753 | 1 |
| zh050 | zh_long_span_boundary_candidate | False | None | 0.265 | 1 |
| zh051 | zh_long_span_boundary_candidate | False | None | 0.533 | 1 |
| zh052 | zh_long_span_boundary_candidate | True | 5 | 0.733 | 1 |
| zh053 | zh_long_span_boundary_candidate | False | None | 0.481 | 1 |
| zh054 | zh_long_span_boundary_candidate | False | None | 0.552 | 1 |
| zh055 | zh_long_span_boundary_candidate | False | None | 0.611 | 1 |
| zh056 | zh_long_span_boundary_candidate | True | 4 | 0.908 | 1 |
| zh057 | zh_long_span_boundary_candidate | False | None | 0.166 | 1 |
| zh058 | zh_long_span_boundary_candidate | False | None | 0.25 | 1 |
| zh059 | zh_long_span_boundary_candidate | True | 2 | 0.656 | 1 |
| zh060 | zh_long_span_boundary_candidate | True | 1 | 0.717 | 1 |
| zh061 | zh_long_span_boundary_candidate | True | 1 | 0.723 | 1 |
| zh062 | zh_long_span_boundary_candidate | False | None | 0.253 | 1 |
| zh063 | zh_long_span_boundary_candidate | True | 5 | 0.66 | 1 |
| zh064 | zh_long_span_boundary_candidate | False | None | 0.639 | 1 |
| zh065 | zh_long_span_boundary_candidate | True | 5 | 0.825 | 1 |
| zh066 | zh_long_span_boundary_candidate | False | None | 0.567 | 1 |
| zh067 | zh_long_span_boundary_candidate | False | None | 0.432 | 1 |
| zh068 | zh_long_span_boundary_candidate | True | 2 | 0.67 | 1 |
| zh069 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh070 | zh_long_span_boundary_candidate | False | None | 0.375 | 1 |
| zh071 | zh_long_span_boundary_candidate | False | None | 0.617 | 1 |
| zh072 | zh_long_span_boundary_candidate | False | None | 0.42 | 1 |
| zh073 | zh_long_span_boundary_candidate | True | 3 | 0.854 | 1 |
| zh074 | zh_long_span_boundary_candidate | False | None | 0.595 | 1 |
| zh075 | zh_long_span_boundary_candidate | False | None | 0.137 | 1 |
| zh076 | zh_long_span_boundary_candidate | False | None | 0.567 | 1 |
| zh077 | zh_long_span_boundary_candidate | False | None | 0.584 | 1 |
| zh078 | zh_long_span_boundary_candidate | False | None | 0.578 | 1 |
| zh079 | zh_long_span_boundary_candidate | False | None | 0.527 | 1 |
| zh080 | zh_long_span_boundary_candidate | True | 1 | 0.848 | 1 |
| zh081 | zh_long_span_boundary_candidate | False | None | 0.588 | 1 |
| zh082 | zh_long_span_boundary_candidate | False | None | 0.09 | 1 |
| zh083 | zh_long_span_boundary_candidate | False | None | 0.637 | 1 |
| zh084 | zh_long_span_boundary_candidate | True | 1 | 0.71 | 1 |
| zh085 | zh_long_span_boundary_candidate | False | None | 0.371 | 1 |
| zh086 | zh_long_span_boundary_candidate | True | 5 | 0.656 | 1 |
| zh087 | zh_long_span_boundary_candidate | True | 5 | 0.676 | 1 |
| zh088 | zh_long_span_boundary_candidate | True | 3 | 0.949 | 1 |
| zh089 | zh_long_span_boundary_candidate | False | None | 0.456 | 1 |
| zh090 | zh_long_span_boundary_candidate | False | None | 0.545 | 1 |
| zh091 | zh_long_span_boundary_candidate | True | 1 | 0.668 | 1 |
| zh092 | zh_long_span_boundary_candidate | True | 5 | 0.662 | 1 |
| zh093 | zh_long_span_boundary_candidate | False | None | 0.179 | 1 |
| zh094 | zh_long_span_boundary_candidate | False | None | 0.077 | 1 |
| zh095 | zh_long_span_boundary_candidate | False | None | 0.576 | 1 |
| zh096 | zh_long_span_boundary_candidate | False | None | 0.557 | 1 |
| zh097 | zh_long_span_boundary_candidate | False | None | 0.407 | 1 |
| zh098 | zh_long_span_boundary_candidate | True | 1 | 0.682 | 1 |
| zh099 | zh_long_span_boundary_candidate | True | 2 | 0.906 | 1 |
| zh100 | zh_long_span_boundary_candidate | False | None | 0.58 | 1 |
| zh101 | zh_long_span_boundary_candidate | False | None | 0.577 | 1 |
| zh102 | zh_long_span_boundary_candidate | False | None | 0.164 | 1 |
| zh103 | zh_long_span_boundary_candidate | False | None | 0.623 | 1 |
| zh104 | zh_long_span_boundary_candidate | True | 5 | 0.722 | 1 |
| zh105 | zh_long_span_boundary_candidate | True | 3 | 0.669 | 1 |
| zh106 | zh_long_span_boundary_candidate | True | 3 | 0.773 | 1 |
| zh107 | zh_long_span_boundary_candidate | True | 5 | 0.665 | 1 |
| zh108 | zh_long_span_boundary_candidate | True | 5 | 0.674 | 1 |
| zh109 | zh_long_span_boundary_candidate | True | 2 | 0.656 | 1 |
| zh110 | zh_long_span_boundary_candidate | False | None | 0.607 | 1 |
| zh111 | zh_long_span_boundary_candidate | True | 5 | 0.689 | 1 |
| zh112 | zh_long_span_boundary_candidate | True | 2 | 0.849 | 1 |
| zh113 | zh_long_span_boundary_candidate | False | None | 0.52 | 1 |
| zh114 | zh_long_span_boundary_candidate | True | 1 | 0.656 | 1 |
| zh115 | zh_long_span_boundary_candidate | True | 2 | 0.711 | 1 |
| zh116 | zh_long_span_boundary_candidate | True | 4 | 0.671 | 1 |
| zh117 | zh_long_span_boundary_candidate | False | None | 0.227 | 1 |
| zh118 | zh_long_span_boundary_candidate | True | 5 | 0.897 | 1 |
| zh119 | zh_long_span_boundary_candidate | True | 4 | 0.959 | 1 |
| zh120 | zh_long_span_boundary_candidate | True | 5 | 0.67 | 1 |
