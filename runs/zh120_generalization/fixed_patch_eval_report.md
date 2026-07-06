# Baseline Retrieval Report

## Config

- **mode**: `heldout_main_plus_fixed_patch`
- **index**: `runs/zh120_base`
- **patch_dir**: `runs/zh120_patches`
- **questions**: `case_zh_dureader_120/eval/questions_heldout.jsonl`
- **top_k**: `5`
- **coverage_threshold**: `0.65`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`
- **selected_patch_chunks**: `24`

## Metrics

- **total**: 120
- **recall@5**: 0.3250
- **mrr**: 0.1374
- **hits**: 39
- **failed**: 81
- **coverage_threshold**: 0.6500

## Failed Queries

### zh001_holdout — zh_long_span_boundary_candidate
- question: 在高速公路上超速20%以上但不到50%会被扣多少分？
- gold: `zh_doc_001.md > 关键材料`
- best_topk_coverage: 0.646
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_001.md::c0012` score=0.760203 cov=0.646 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_001.md::c0011` score=0.731466 cov=0.454 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_001.md::c0015` score=0.717755 cov=0.565 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_001.md::c0027` score=0.714801 cov=0.366 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_001.md::c0016` score=0.711604 cov=0.513 section=中文复杂检索文档 > 关键材料

### zh002_holdout — zh_long_span_boundary_candidate
- question: 空气净化器采用哪种净化方式效果更佳
- gold: `zh_doc_002.md > 关键材料`
- best_topk_coverage: 0.163
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_002.md::c0001` score=0.757725 cov=0.13 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_002.md::c0003` score=0.752255 cov=0.163 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_002.md::c0012` score=0.725282 cov=0.111 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_002.md::c0000` score=0.724837 cov=0.139 section=
  - rank 5: `zh_doc_002.md::c0002` score=0.721232 cov=0.129 section=中文复杂检索文档 > 背景材料2

### zh003_holdout — zh_long_span_boundary_candidate
- question: 有哪些古诗赞美了黄山的风景？
- gold: `zh_doc_003.md > 关键材料`
- best_topk_coverage: 0.206
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_003.md::c0009` score=0.677149 cov=0.035 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_003.md::c0003` score=0.661641 cov=0.184 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_003.md::c0004` score=0.650391 cov=0.206 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_003.md::c0006` score=0.644333 cov=0.203 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_003.md::c0005` score=0.638897 cov=0.203 section=中文复杂检索文档 > 关键材料

### zh004_holdout — zh_long_span_boundary_candidate
- question: 一天内频繁放屁是什么原因？
- gold: `zh_doc_004.md > 关键材料`
- best_topk_coverage: 0.276
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_004.md::c0022` score=0.663908 cov=0.274 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_004.md::c0021` score=0.654881 cov=0.273 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_004.md::c0019` score=0.647976 cov=0.198 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_004.md::c0024` score=0.645613 cov=0.276 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_004.md::c0002` score=0.640017 cov=0.06 section=中文复杂检索文档 > 背景材料1

### zh005_holdout — zh_long_span_boundary_candidate
- question: 叉车有多少种类型
- gold: `zh_doc_005.md > 关键材料`
- best_topk_coverage: 0.38
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_005.md::c0015` score=0.735002 cov=0.361 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_005.md::c0019` score=0.700537 cov=0.341 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_005.md::c0017` score=0.684514 cov=0.318 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_005.md::c0018` score=0.682781 cov=0.342 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_005.md::c0016` score=0.670491 cov=0.38 section=中文复杂检索文档 > 关键材料

### zh006_holdout — zh_long_span_boundary_candidate
- question: 有哪些关于春光的成语？
- gold: `zh_doc_006.md > 关键材料`
- best_topk_coverage: 0.337
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_006.md::c0008` score=0.622801 cov=0.176 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_006.md::c0003` score=0.617665 cov=0.31 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_006.md::c0002` score=0.613236 cov=0.13 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_006.md::c0005` score=0.603189 cov=0.337 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_006.md::c0004` score=0.595267 cov=0.298 section=中文复杂检索文档 > 关键材料

### zh007_holdout — zh_long_span_boundary_candidate
- question: 频繁使用肥皂来清洁面部是否合适
- gold: `zh_doc_007.md > 关键材料`
- best_topk_coverage: 0.346
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_007.md::c0007` score=0.740783 cov=0.346 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_007.md::c0006` score=0.74059 cov=0.33 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_007.md::c0004` score=0.72748 cov=0.295 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_007.md::c0011` score=0.717233 cov=0.133 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_007.md::c0009` score=0.717034 cov=0.117 section=中文复杂检索文档 > 关键材料

### zh008_holdout — zh_long_span_boundary_candidate
- question: 冬天如何饲养鹦鹉
- gold: `zh_doc_008.md > 关键材料`
- best_topk_coverage: 0.276
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_008.md::c0003` score=0.728248 cov=0.064 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_008.md::c0004` score=0.702451 cov=0.183 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_008.md::c0011` score=0.699367 cov=0.095 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_008.md::c0010` score=0.671529 cov=0.07 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_008.md::c0006` score=0.634814 cov=0.276 section=中文复杂检索文档 > 关键材料

### zh009_holdout — zh_long_span_boundary_candidate
- question: 附睾部位出现肿胀是怎么回事？
- gold: `zh_doc_009.md > 关键材料`
- best_topk_coverage: 0.446
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_009.md::c0006` score=0.776014 cov=0.42 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_009.md::c0007` score=0.763399 cov=0.446 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_009.md::c0013` score=0.730463 cov=0.098 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_009.md::c0010` score=0.723639 cov=0.396 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_009.md::c0009` score=0.710827 cov=0.348 section=中文复杂检索文档 > 关键材料

### zh010_holdout — zh_long_span_boundary_candidate
- question: 硫磺皂可以一直使用吗
- gold: `zh_doc_010.md > 关键材料`
- best_topk_coverage: 0.277
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_010.md::c0008` score=0.750881 cov=0.053 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_010.md::c0009` score=0.722115 cov=0.042 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_010.md::c0000` score=0.71787 cov=0.054 section=
  - rank 4: `zh_doc_010.md::c0010` score=0.714376 cov=0.057 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_010.md::c0004` score=0.685195 cov=0.277 section=中文复杂检索文档 > 关键材料

### zh011_holdout — zh_long_span_boundary_candidate
- question: 有哪些比较好看的电视剧？
- gold: `zh_doc_011.md > 关键材料`
- best_topk_coverage: 0.19
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_011.md::c0009` score=0.597942 cov=0.038 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_011.md::c0000` score=0.596106 cov=0.078 section=
  - rank 3: `zh_doc_011.md::c0007` score=0.560225 cov=0.19 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_011.md::c0008` score=0.530713 cov=0.037 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_011.md::c0001` score=0.509269 cov=0.042 section=中文复杂检索文档 > 背景材料1

### zh012_holdout — zh_long_span_boundary_candidate
- question: 夏天适合喝哪些饮料
- gold: `zh_doc_012.md > 关键材料`
- best_topk_coverage: 0.365
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_012.md::c0001` score=0.69333 cov=0.116 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_012.md::c0000` score=0.666458 cov=0.112 section=
  - rank 3: `zh_doc_012.md::c0002` score=0.647251 cov=0.307 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_012.md::c0003` score=0.627677 cov=0.365 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_012.md::c0008` score=0.610999 cov=0.057 section=中文复杂检索文档 > 补充材料1

### zh013_holdout — zh_long_span_boundary_candidate
- question: workgroup是什么意思
- gold: `zh_doc_013.md > 关键材料`
- best_topk_coverage: 0.395
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_013.md::c0000` score=0.731449 cov=0.093 section=
  - rank 2: `zh_doc_013.md::c0001` score=0.584905 cov=0.189 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_013.md::c0006` score=0.51446 cov=0.351 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_013.md::c0003` score=0.507619 cov=0.395 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_013.md::c0010` score=0.483167 cov=0.09 section=中文复杂检索文档 > 补充材料1

### zh014_holdout — zh_long_span_boundary_candidate
- question: 如何提升肺活量
- gold: `zh_doc_014.md > 关键材料`
- best_topk_coverage: 0.38
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_014.md::c0006` score=0.728034 cov=0.336 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_014.md::c0000` score=0.726767 cov=0.128 section=
  - rank 3: `zh_doc_014.md::c0007` score=0.724011 cov=0.38 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_014.md::c0011` score=0.717151 cov=0.09 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_014.md::c0005` score=0.715769 cov=0.227 section=中文复杂检索文档 > 背景材料2

### zh016_holdout — zh_long_span_boundary_candidate
- question: 油电混合动力汽车能不能享受购置税减免政策
- gold: `zh_doc_016.md > 关键材料`
- best_topk_coverage: 0.405
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_016.md::c0006` score=0.804967 cov=0.387 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_016.md::c0004` score=0.744228 cov=0.281 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_016.md::c0011` score=0.738684 cov=0.313 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_016.md::c0010` score=0.726794 cov=0.405 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_016.md::c0012` score=0.72593 cov=0.158 section=中文复杂检索文档 > 补充材料2

### zh017_holdout — zh_long_span_boundary_candidate
- question: 阴部颜色变白是怎么回事？
- gold: `zh_doc_017.md > 关键材料`
- best_topk_coverage: 0.321
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_017.md::c0003` score=0.629924 cov=0.139 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_017.md::c0004` score=0.606869 cov=0.321 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_017.md::c0001` score=0.594921 cov=0.055 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_017.md::c0000` score=0.592021 cov=0.036 section=
  - rank 5: `zh_doc_017.md::c0010` score=0.591876 cov=0.025 section=中文复杂检索文档 > 补充材料2

### zh018_holdout — zh_long_span_boundary_candidate
- question: 怎么进行ETF基金的买入和卖出操作
- gold: `zh_doc_018.md > 关键材料`
- best_topk_coverage: 0.429
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_018.md::c0003` score=0.765366 cov=0.289 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_018.md::c0004` score=0.756831 cov=0.429 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_018.md::c0008` score=0.736933 cov=0.168 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_018.md::c0000` score=0.731527 cov=0.176 section=
  - rank 5: `zh_doc_018.md::c0009` score=0.71812 cov=0.194 section=中文复杂检索文档 > 补充材料2

### zh019_holdout — zh_long_span_boundary_candidate
- question: 实习期间的驾照扣分有什么后果？
- gold: `zh_doc_019.md > 关键材料`
- best_topk_coverage: 0.553
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_019.md::c0008` score=0.710719 cov=0.432 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_019.md::c0010` score=0.705359 cov=0.269 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_019.md::c0009` score=0.69691 cov=0.437 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_019.md::c0006` score=0.678269 cov=0.553 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_019.md::c0007` score=0.661679 cov=0.503 section=中文复杂检索文档 > 关键材料

### zh020_holdout — zh_long_span_boundary_candidate
- question: 私立大学与公立大学有什么不同
- gold: `zh_doc_020.md > 关键材料`
- best_topk_coverage: 0.409
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_020.md::c0012` score=0.72693 cov=0.084 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_020.md::c0013` score=0.700886 cov=0.09 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_020.md::c0006` score=0.692811 cov=0.124 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_020.md::c0003` score=0.681837 cov=0.097 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_020.md::c0011` score=0.669605 cov=0.409 section=中文复杂检索文档 > 关键材料

### zh022_holdout — zh_long_span_boundary_candidate
- question: 如何种植香菜
- gold: `zh_doc_022.md > 关键材料`
- best_topk_coverage: 0.386
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_022.md::c0018` score=0.700172 cov=0.083 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_022.md::c0016` score=0.695891 cov=0.104 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_022.md::c0001` score=0.695294 cov=0.104 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_022.md::c0012` score=0.693843 cov=0.386 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_022.md::c0002` score=0.680289 cov=0.189 section=中文复杂检索文档 > 背景材料1

### zh023_holdout — zh_long_span_boundary_candidate
- question: 怎样将电脑中的文件传输到iPad上？
- gold: `zh_doc_023.md > 关键材料`
- best_topk_coverage: 0.472
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_023.md::c0004` score=0.718117 cov=0.417 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_023.md::c0001` score=0.701652 cov=0.094 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_023.md::c0009` score=0.674122 cov=0.174 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_023.md::c0003` score=0.665554 cov=0.123 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_023.md::c0005` score=0.659876 cov=0.472 section=中文复杂检索文档 > 关键材料

### zh024_holdout — zh_long_span_boundary_candidate
- question: c1驾驶证被扣满12分该如何处理
- gold: `zh_doc_024.md > 关键材料`
- best_topk_coverage: 0.575
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_024.md::c0012` score=0.803631 cov=0.2 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_024.md::c0005` score=0.800927 cov=0.375 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_024.md::c0006` score=0.772408 cov=0.575 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_024.md::c0010` score=0.764697 cov=0.41 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_024.md::c0011` score=0.757677 cov=0.182 section=中文复杂检索文档 > 补充材料1

### zh025_holdout — zh_long_span_boundary_candidate
- question: tf卡和sd卡有什么不同
- gold: `zh_doc_025.md > 关键材料`
- best_topk_coverage: 0.448
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_025.md::c0010` score=0.791845 cov=0.328 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_025.md::c0011` score=0.781212 cov=0.345 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_025.md::c0019` score=0.778068 cov=0.145 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_025.md::c0003` score=0.777314 cov=0.448 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_025.md::c0002` score=0.776557 cov=0.299 section=中文复杂检索文档 > 背景材料1

### zh027_holdout — zh_long_span_boundary_candidate
- question: 小米平板的钢化膜该如何粘贴
- gold: `zh_doc_027.md > 关键材料`
- best_topk_coverage: 0.041
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_027.md::c0010` score=0.710518 cov=0.037 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_027.md::c0011` score=0.678523 cov=0.01 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_081.md::c0005` score=0.66888 cov=0.0 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_027.md::c0000` score=0.662547 cov=0.041 section=
  - rank 5: `zh_doc_081.md::c0014` score=0.658076 cov=0.0 section=中文复杂检索文档 > 关键材料

### zh028_holdout — zh_long_span_boundary_candidate
- question: 如何阻止陌生人连接我的路由器并强制他们断开WiFi？
- gold: `zh_doc_028.md > 关键材料`
- best_topk_coverage: 0.606
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_028.md::c0002` score=0.587689 cov=0.264 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_028.md::c0003` score=0.584467 cov=0.606 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_028.md::c0001` score=0.580502 cov=0.185 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_028.md::c0006` score=0.566602 cov=0.206 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_028.md::c0000` score=0.552765 cov=0.155 section=

### zh029_holdout — zh_long_span_boundary_candidate
- question: 如何从事卫浴产品的销售工作？
- gold: `zh_doc_029.md > 关键材料`
- best_topk_coverage: 0.524
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_029.md::c0002` score=0.718062 cov=0.058 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_029.md::c0001` score=0.693467 cov=0.082 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_029.md::c0004` score=0.643196 cov=0.524 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_029.md::c0006` score=0.629869 cov=0.445 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_029.md::c0003` score=0.618196 cov=0.193 section=中文复杂检索文档 > 背景材料2

### zh030_holdout — zh_long_span_boundary_candidate
- question: 外伤缝针后有哪些食物需要避免
- gold: `zh_doc_030.md > 关键材料`
- best_topk_coverage: 0.289
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_030.md::c0003` score=0.740938 cov=0.122 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_030.md::c0002` score=0.739648 cov=0.189 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_030.md::c0005` score=0.728392 cov=0.187 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_030.md::c0004` score=0.719353 cov=0.228 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_030.md::c0010` score=0.719051 cov=0.289 section=中文复杂检索文档 > 关键材料

### zh031_holdout — zh_long_span_boundary_candidate
- question: 超级会员指的是什么
- gold: `zh_doc_031.md > 关键材料`
- best_topk_coverage: 0.517
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_031.md::c0007` score=0.671294 cov=0.244 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_031.md::c0006` score=0.651189 cov=0.244 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_031.md::c0003` score=0.640571 cov=0.517 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_031.md::c0002` score=0.621524 cov=0.254 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_031.md::c0008` score=0.621217 cov=0.192 section=中文复杂检索文档 > 补充材料2

### zh032_holdout — zh_long_span_boundary_candidate
- question: 杭州劳动仲裁的咨询电话是多少？
- gold: `zh_doc_032.md > 关键材料`
- best_topk_coverage: 0.396
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_032.md::c0002` score=0.727329 cov=0.236 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_032.md::c0005` score=0.652414 cov=0.396 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_032.md::c0017` score=0.636188 cov=0.192 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_032.md::c0016` score=0.635231 cov=0.124 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_032.md::c0007` score=0.622875 cov=0.192 section=中文复杂检索文档 > 补充材料1

### zh033_holdout — zh_long_span_boundary_candidate
- question: 电暖桌什么品牌值得推荐
- gold: `zh_doc_033.md > 关键材料`
- best_topk_coverage: 0.349
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_033.md::c0004` score=0.808403 cov=0.349 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_033.md::c0001` score=0.792388 cov=0.103 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_033.md::c0010` score=0.780213 cov=0.065 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_033.md::c0007` score=0.777469 cov=0.091 section=中文复杂检索文档 > 补充
  - rank 5: `zh_doc_033.md::c0011` score=0.777449 cov=0.077 section=中文复杂检索文档 > 补充材料2

### zh034_holdout — zh_long_span_boundary_candidate
- question: 板栗能不能用蒸的方式食用？
- gold: `zh_doc_034.md > 关键材料`
- best_topk_coverage: 0.49
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_034.md::c0004` score=0.719049 cov=0.14 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_034.md::c0005` score=0.686871 cov=0.49 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_034.md::c0011` score=0.634595 cov=0.106 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_034.md::c0010` score=0.633482 cov=0.097 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_034.md::c0009` score=0.631804 cov=0.106 section=中文复杂检索文档 > 补充材料1

### zh036_holdout — zh_long_span_boundary_candidate
- question: 如何在苹果系统里显示隐藏文件
- gold: `zh_doc_036.md > 关键材料`
- best_topk_coverage: 0.525
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_036.md::c0004` score=0.766781 cov=0.478 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_036.md::c0003` score=0.743326 cov=0.525 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_036.md::c0005` score=0.730206 cov=0.442 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_036.md::c0000` score=0.682885 cov=0.221 section=
  - rank 5: `zh_doc_036.md::c0006` score=0.66732 cov=0.269 section=中文复杂检索文档 > 补充材料1

### zh037_holdout — zh_long_span_boundary_candidate
- question: 海淀医院做孕前检查怎么预约
- gold: `zh_doc_037.md > 关键材料`
- best_topk_coverage: 0.44
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_037.md::c0004` score=0.769442 cov=0.44 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_037.md::c0003` score=0.728431 cov=0.212 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_037.md::c0006` score=0.717087 cov=0.271 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_037.md::c0000` score=0.709768 cov=0.071 section=
  - rank 5: `zh_doc_037.md::c0009` score=0.635866 cov=0.085 section=中文复杂检索文档 > 补充材料2

### zh038_holdout — zh_long_span_boundary_candidate
- question: 梦幻西游里有哪些赚钱的方法
- gold: `zh_doc_038.md > 关键材料`
- best_topk_coverage: 0.494
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_038.md::c0003` score=0.716008 cov=0.081 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_038.md::c0000` score=0.71382 cov=0.074 section=
  - rank 3: `zh_doc_038.md::c0007` score=0.669059 cov=0.168 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_038.md::c0005` score=0.669046 cov=0.494 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_038.md::c0009` score=0.637141 cov=0.038 section=中文复杂检索文档 > 补充材料2

### zh039_holdout — zh_long_span_boundary_candidate
- question: 有哪些诗句是与庐山相关的？
- gold: `zh_doc_039.md > 关键材料`
- best_topk_coverage: 0.486
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_039.md::c0002` score=0.652324 cov=0.244 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_039.md::c0005` score=0.651849 cov=0.267 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_039.md::c0003` score=0.63742 cov=0.486 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_039.md::c0006` score=0.602166 cov=0.053 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_039.md::c0004` score=0.592391 cov=0.388 section=中文复杂检索文档 > 关键材料

### zh040_holdout — zh_long_span_boundary_candidate
- question: 现在在哪儿能下载到音乐
- gold: `zh_doc_040.md > 关键材料`
- best_topk_coverage: 0.493
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_040.md::c0000` score=0.621134 cov=0.137 section=
  - rank 2: `zh_doc_040.md::c0001` score=0.605671 cov=0.096 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_040.md::c0003` score=0.589252 cov=0.493 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_040.md::c0006` score=0.577623 cov=0.103 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_040.md::c0007` score=0.571041 cov=0.066 section=中文复杂检索文档 > 补充材料1

### zh041_holdout — zh_long_span_boundary_candidate
- question: 治疗颈椎病用什么药
- gold: `zh_doc_041.md > 关键材料`
- best_topk_coverage: 0.419
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_041.md::c0012` score=0.687851 cov=0.107 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_041.md::c0011` score=0.686108 cov=0.109 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_041.md::c0004` score=0.626184 cov=0.103 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_041.md::c0007` score=0.615187 cov=0.419 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_041.md::c0005` score=0.596134 cov=0.137 section=中文复杂检索文档 > 背景材料2

### zh044_holdout — zh_long_span_boundary_candidate
- question: 哪个银行换外汇比较划算
- gold: `zh_doc_044.md > 关键材料`
- best_topk_coverage: 0.296
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_044.md::c0000` score=0.837078 cov=0.079 section=
  - rank 2: `zh_doc_044.md::c0006` score=0.793027 cov=0.229 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_044.md::c0002` score=0.78104 cov=0.174 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_044.md::c0005` score=0.75847 cov=0.296 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_044.md::c0001` score=0.74562 cov=0.095 section=中文复杂检索文档 > 背景材料1

### zh046_holdout — zh_long_span_boundary_candidate
- question: 手机的外放喇叭进水了怎么办
- gold: `zh_doc_046.md > 关键材料`
- best_topk_coverage: 0.491
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_046.md::c0008` score=0.696545 cov=0.072 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_046.md::c0007` score=0.676428 cov=0.109 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_046.md::c0005` score=0.664652 cov=0.491 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_046.md::c0002` score=0.643837 cov=0.084 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_046.md::c0000` score=0.637236 cov=0.114 section=

### zh047_holdout — zh_long_span_boundary_candidate
- question: 哪些借条在法律上是无效的
- gold: `zh_doc_047.md > 关键材料`
- best_topk_coverage: 0.422
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_047.md::c0001` score=0.741739 cov=0.154 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_047.md::c0013` score=0.73445 cov=0.167 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_047.md::c0000` score=0.723938 cov=0.184 section=
  - rank 4: `zh_doc_047.md::c0002` score=0.720976 cov=0.159 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_047.md::c0011` score=0.712119 cov=0.422 section=中文复杂检索文档 > 关键材料

### zh048_holdout — zh_long_span_boundary_candidate
- question: M8A1装备的是哪种火炮？
- gold: `zh_doc_048.md > 关键材料`
- best_topk_coverage: 0.477
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_048.md::c0008` score=0.706489 cov=0.102 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_048.md::c0007` score=0.667052 cov=0.102 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_048.md::c0003` score=0.658033 cov=0.177 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_048.md::c0004` score=0.655823 cov=0.472 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_048.md::c0005` score=0.633667 cov=0.477 section=中文复杂检索文档 > 关键材料

### zh050_holdout — zh_long_span_boundary_candidate
- question: xm外汇平台口碑如何
- gold: `zh_doc_050.md > 关键材料`
- best_topk_coverage: 0.265
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_050.md::c0006` score=0.812131 cov=0.232 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_050.md::c0002` score=0.803868 cov=0.21 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_050.md::c0000` score=0.775092 cov=0.084 section=
  - rank 4: `zh_doc_050.md::c0005` score=0.754963 cov=0.265 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_050.md::c0001` score=0.698795 cov=0.084 section=中文复杂检索文档 > 背景材料1

### zh051_holdout — zh_long_span_boundary_candidate
- question: 双人床的最小宽度是多少
- gold: `zh_doc_051.md > 关键材料`
- best_topk_coverage: 0.533
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_051.md::c0008` score=0.741128 cov=0.533 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_051.md::c0014` score=0.730487 cov=0.119 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_051.md::c0000` score=0.725263 cov=0.078 section=
  - rank 4: `zh_doc_051.md::c0001` score=0.715183 cov=0.072 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_051.md::c0002` score=0.712327 cov=0.078 section=中文复杂检索文档 > 背景材料1

### zh053_holdout — zh_long_span_boundary_candidate
- question: 龟头敏感度偏低该如何处理
- gold: `zh_doc_053.md > 关键材料`
- best_topk_coverage: 0.481
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_053.md::c0000` score=0.745622 cov=0.051 section=
  - rank 2: `zh_doc_053.md::c0017` score=0.730058 cov=0.117 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_053.md::c0004` score=0.72608 cov=0.133 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_053.md::c0012` score=0.720118 cov=0.481 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_053.md::c0014` score=0.71969 cov=0.241 section=中文复杂检索文档 > 补充材料1

### zh054_holdout — zh_long_span_boundary_candidate
- question: 沪陕高速的最高时速限制是多少
- gold: `zh_doc_054.md > 关键材料`
- best_topk_coverage: 0.552
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_054.md::c0003` score=0.732824 cov=0.552 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_054.md::c0004` score=0.710115 cov=0.542 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_054.md::c0002` score=0.696204 cov=0.265 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_054.md::c0005` score=0.636443 cov=0.286 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_054.md::c0006` score=0.626635 cov=0.094 section=中文复杂检索文档 > 补充材料1

### zh055_holdout — zh_long_span_boundary_candidate
- question: ios9 怎样关闭搜索最近联系人的功能
- gold: `zh_doc_055.md > 关键材料`
- best_topk_coverage: 0.611
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_055.md::c0000` score=0.806104 cov=0.459 section=
  - rank 2: `zh_doc_055.md::c0006` score=0.803598 cov=0.301 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_055.md::c0002` score=0.79172 cov=0.601 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_055.md::c0003` score=0.790894 cov=0.611 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_055.md::c0005` score=0.780475 cov=0.462 section=中文复杂检索文档 > 关键材料

### zh056_holdout — zh_long_span_boundary_candidate
- question: 尸兄这部作品里主角拥有什么能力
- gold: `zh_doc_056.md > 关键材料`
- best_topk_coverage: 0.51
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_056.md::c0005` score=0.638826 cov=0.51 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_056.md::c0002` score=0.627709 cov=0.072 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_056.md::c0008` score=0.608882 cov=0.067 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_056.md::c0003` score=0.60737 cov=0.045 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_056.md::c0007` score=0.601117 cov=0.281 section=中文复杂检索文档 > 关键材料

### zh057_holdout — zh_long_span_boundary_candidate
- question: Word为什么无法编辑
- gold: `zh_doc_057.md > 关键材料`
- best_topk_coverage: 0.546
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_057.md::c0001` score=0.732444 cov=0.166 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_057.md::c0000` score=0.678005 cov=0.101 section=
  - rank 3: `zh_doc_057.md::c0014` score=0.673849 cov=0.141 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_057.md::c0002` score=0.638525 cov=0.146 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_057.md::c0016` score=0.637572 cov=0.546 section=中文复杂检索文档 > 关键材料

### zh058_holdout — zh_long_span_boundary_candidate
- question: 我国历史上第一位取得辉煌成就的爱国诗人是谁
- gold: `zh_doc_058.md > 关键材料`
- best_topk_coverage: 0.25
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_058.md::c0009` score=0.657736 cov=0.115 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_058.md::c0006` score=0.656446 cov=0.25 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_058.md::c0007` score=0.631431 cov=0.149 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_058.md::c0008` score=0.60688 cov=0.091 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_058.md::c0003` score=0.590235 cov=0.173 section=中文复杂检索文档 > 背景材料2

### zh062_holdout — zh_long_span_boundary_candidate
- question: 电脑的自动休眠功能要怎么关闭
- gold: `zh_doc_062.md > 关键材料`
- best_topk_coverage: 0.506
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_062.md::c0005` score=0.789118 cov=0.103 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_062.md::c0006` score=0.781576 cov=0.253 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_062.md::c0000` score=0.766098 cov=0.203 section=
  - rank 4: `zh_doc_062.md::c0008` score=0.74053 cov=0.506 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_062.md::c0011` score=0.731916 cov=0.171 section=中文复杂检索文档 > 补充材料1

### zh064_holdout — zh_long_span_boundary_candidate
- question: 血清中的甘油三酯水平较低
- gold: `zh_doc_064.md > 关键材料`
- best_topk_coverage: 0.639
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_064.md::c0003` score=0.741319 cov=0.511 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_064.md::c0002` score=0.740751 cov=0.584 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_064.md::c0004` score=0.738232 cov=0.639 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_064.md::c0010` score=0.70847 cov=0.203 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_064.md::c0012` score=0.698882 cov=0.361 section=中文复杂检索文档 > 补充材料2

### zh066_holdout — zh_long_span_boundary_candidate
- question: 电动牙刷的清洁效果好吗
- gold: `zh_doc_066.md > 关键材料`
- best_topk_coverage: 0.567
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_066.md::c0007` score=0.696507 cov=0.173 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_066.md::c0012` score=0.685143 cov=0.136 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_066.md::c0003` score=0.679891 cov=0.567 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_066.md::c0005` score=0.674555 cov=0.141 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_066.md::c0000` score=0.674064 cov=0.204 section=

### zh067_holdout — zh_long_span_boundary_candidate
- question: 武松的生肖是什么
- gold: `zh_doc_067.md > 关键材料`
- best_topk_coverage: 0.432
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_067.md::c0004` score=0.679776 cov=0.432 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_067.md::c0000` score=0.590713 cov=0.009 section=
  - rank 3: `zh_doc_067.md::c0001` score=0.561164 cov=0.015 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_067.md::c0008` score=0.557361 cov=0.009 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_067.md::c0002` score=0.537705 cov=0.006 section=中文复杂检索文档 > 背景材料1

### zh070_holdout — zh_long_span_boundary_candidate
- question: QQ频繁断线是什么原因
- gold: `zh_doc_070.md > 关键材料`
- best_topk_coverage: 0.375
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_070.md::c0002` score=0.774846 cov=0.375 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_070.md::c0004` score=0.761866 cov=0.308 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_070.md::c0010` score=0.743203 cov=0.091 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_070.md::c0005` score=0.741163 cov=0.061 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_070.md::c0007` score=0.739629 cov=0.07 section=中文复杂检索文档 > 补充材料1

### zh071_holdout — zh_long_span_boundary_candidate
- question: 还珠格格第一部的配乐有哪些
- gold: `zh_doc_071.md > 关键材料`
- best_topk_coverage: 0.617
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_071.md::c0014` score=0.680351 cov=0.617 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_071.md::c0003` score=0.676982 cov=0.16 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_071.md::c0016` score=0.648576 cov=0.436 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_071.md::c0002` score=0.643614 cov=0.157 section=中文复杂检索文档 > 背景
  - rank 5: `zh_doc_071.md::c0004` score=0.598674 cov=0.233 section=中文复杂检索文档 > 背景材料2

### zh072_holdout — zh_long_span_boundary_candidate
- question: 我的世界手机版0.12.1如何制作末地传送门
- gold: `zh_doc_072.md > 关键材料`
- best_topk_coverage: 0.42
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_072.md::c0007` score=0.783344 cov=0.179 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_072.md::c0002` score=0.776444 cov=0.153 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_072.md::c0006` score=0.761387 cov=0.199 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_072.md::c0003` score=0.752297 cov=0.42 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_072.md::c0000` score=0.74366 cov=0.169 section=

### zh074_holdout — zh_long_span_boundary_candidate
- question: 胃部功能
- gold: `zh_doc_074.md > 关键材料`
- best_topk_coverage: 0.595
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_074.md::c0003` score=0.75728 cov=0.588 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_074.md::c0005` score=0.703502 cov=0.17 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_074.md::c0002` score=0.677977 cov=0.088 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_074.md::c0004` score=0.677683 cov=0.595 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_074.md::c0000` score=0.669471 cov=0.124 section=

### zh075_holdout — zh_long_span_boundary_candidate
- question: 艾俐缇陶瓷的质量如何？
- gold: `zh_doc_075.md > 关键材料`
- best_topk_coverage: 0.137
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_075.md::c0006` score=0.68664 cov=0.02 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_075.md::c0002` score=0.648661 cov=0.137 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_075.md::c0005` score=0.585361 cov=0.067 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_075.md::c0007` score=0.551989 cov=0.032 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_075.md::c0001` score=0.532862 cov=0.032 section=中文复杂检索文档 > 背景材料1

### zh076_holdout — zh_long_span_boundary_candidate
- question: 公共事业管理归属于哪个专业门类
- gold: `zh_doc_076.md > 关键材料`
- best_topk_coverage: 0.567
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_076.md::c0002` score=0.803449 cov=0.567 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_076.md::c0008` score=0.733973 cov=0.201 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_076.md::c0006` score=0.733685 cov=0.201 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_076.md::c0010` score=0.725223 cov=0.201 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_076.md::c0001` score=0.719534 cov=0.443 section=中文复杂检索文档 > 背景材料1

### zh077_holdout — zh_long_span_boundary_candidate
- question: 市面上有没有真正不含人工添加成分的护肤品？
- gold: `zh_doc_077.md > 关键材料`
- best_topk_coverage: 0.584
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_077.md::c0018` score=0.693796 cov=0.584 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_077.md::c0019` score=0.689213 cov=0.379 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_077.md::c0021` score=0.650753 cov=0.162 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_077.md::c0020` score=0.590668 cov=0.157 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_077.md::c0017` score=0.588826 cov=0.422 section=中文复杂检索文档 > 背景材料2

### zh078_holdout — zh_long_span_boundary_candidate
- question: 旅行发票能报销吗
- gold: `zh_doc_078.md > 关键材料`
- best_topk_coverage: 0.578
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_078.md::c0000` score=0.788672 cov=0.067 section=
  - rank 2: `zh_doc_078.md::c0004` score=0.781161 cov=0.578 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_078.md::c0005` score=0.758968 cov=0.11 section=中文复杂检索文档 > 补充材料
  - rank 4: `zh_doc_078.md::c0006` score=0.738513 cov=0.126 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_078.md::c0002` score=0.736203 cov=0.253 section=中文复杂检索文档 > 背景材料2

### zh079_holdout — zh_long_span_boundary_candidate
- question: 百度云能用来下载种子吗
- gold: `zh_doc_079.md > 关键材料`
- best_topk_coverage: 0.527
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_079.md::c0003` score=0.744918 cov=0.527 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_079.md::c0002` score=0.719486 cov=0.197 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_079.md::c0005` score=0.71211 cov=0.191 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_079.md::c0006` score=0.705853 cov=0.182 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_079.md::c0000` score=0.705197 cov=0.167 section=

### zh081_holdout — zh_long_span_boundary_candidate
- question: 如何正确粘贴手机钢化保护膜
- gold: `zh_doc_081.md > 关键材料`
- best_topk_coverage: 0.588
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_081.md::c0013` score=0.721484 cov=0.588 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_081.md::c0006` score=0.7122 cov=0.155 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_081.md::c0005` score=0.709763 cov=0.161 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_081.md::c0008` score=0.705323 cov=0.164 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_081.md::c0003` score=0.698637 cov=0.215 section=中文复杂检索文档 > 背景材料1

### zh082_holdout — zh_long_span_boundary_candidate
- question: 中国历史上哪个朝代最为兴盛
- gold: `zh_doc_082.md > 关键材料`
- best_topk_coverage: 0.09
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_082.md::c0005` score=0.576056 cov=0.053 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_082.md::c0010` score=0.573998 cov=0.025 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_082.md::c0000` score=0.564025 cov=0.053 section=
  - rank 4: `zh_doc_082.md::c0001` score=0.562578 cov=0.09 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_082.md::c0007` score=0.550745 cov=0.072 section=中文复杂检索文档 > 补充材料1

### zh083_holdout — zh_long_span_boundary_candidate
- question: 如何更改民族信息？
- gold: `zh_doc_083.md > 关键材料`
- best_topk_coverage: 0.637
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_083.md::c0024` score=0.729384 cov=0.637 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_083.md::c0032` score=0.727289 cov=0.18 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_083.md::c0001` score=0.715356 cov=0.236 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_083.md::c0000` score=0.687346 cov=0.159 section=
  - rank 5: `zh_doc_083.md::c0031` score=0.666244 cov=0.242 section=中文复杂检索文档 > 补充材料1

### zh085_holdout — zh_long_span_boundary_candidate
- question: 白带闻起来像酸奶一样的气味正常吗？
- gold: `zh_doc_085.md > 关键材料`
- best_topk_coverage: 0.371
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_085.md::c0013` score=0.6681 cov=0.18 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_085.md::c0015` score=0.667184 cov=0.371 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_085.md::c0002` score=0.666211 cov=0.096 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_085.md::c0018` score=0.661752 cov=0.114 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_085.md::c0001` score=0.65378 cov=0.084 section=中文复杂检索文档 > 背景材料1

### zh089_holdout — zh_long_span_boundary_candidate
- question: 部落冲突如何搜索死鱼
- gold: `zh_doc_089.md > 关键材料`
- best_topk_coverage: 0.456
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_089.md::c0000` score=0.794343 cov=0.092 section=
  - rank 2: `zh_doc_089.md::c0002` score=0.767173 cov=0.456 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_089.md::c0001` score=0.748279 cov=0.092 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_089.md::c0006` score=0.724386 cov=0.092 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_089.md::c0004` score=0.71547 cov=0.189 section=中文复杂检索文档 > 关键材料

### zh090_holdout — zh_long_span_boundary_candidate
- question: 牛剖层移膜皮革指的是什么
- gold: `zh_doc_090.md > 关键材料`
- best_topk_coverage: 0.404
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_090.md::c0016` score=0.777128 cov=0.404 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_090.md::c0001` score=0.76202 cov=0.129 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_090.md::c0000` score=0.755913 cov=0.138 section=
  - rank 4: `zh_doc_090.md::c0018` score=0.754907 cov=0.285 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_090.md::c0005` score=0.742647 cov=0.169 section=中文复杂检索文档 > 背景材料1

### zh093_holdout — zh_long_span_boundary_candidate
- question: 在成都审验驾驶证需要哪些材料？
- gold: `zh_doc_093.md > 关键材料`
- best_topk_coverage: 0.256
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_093.md::c0016` score=0.685552 cov=0.128 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_093.md::c0000` score=0.678031 cov=0.132 section=
  - rank 3: `zh_doc_093.md::c0009` score=0.674488 cov=0.256 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_093.md::c0005` score=0.671268 cov=0.15 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_093.md::c0012` score=0.649623 cov=0.161 section=中文复杂检索文档 > 补充材料1

### zh094_holdout — zh_long_span_boundary_candidate
- question: 霜是如何形成的
- gold: `zh_doc_094.md > 关键材料`
- best_topk_coverage: 0.077
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_094.md::c0011` score=0.687779 cov=0.028 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_094.md::c0000` score=0.677318 cov=0.043 section=
  - rank 3: `zh_doc_094.md::c0001` score=0.614185 cov=0.062 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_094.md::c0006` score=0.604701 cov=0.077 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_094.md::c0012` score=0.587471 cov=0.02 section=中文复杂检索文档 > 补充材料2

### zh095_holdout — zh_long_span_boundary_candidate
- question: 卫生间适合用哪种地砖
- gold: `zh_doc_095.md > 关键材料`
- best_topk_coverage: 0.576
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_095.md::c0001` score=0.672397 cov=0.154 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_095.md::c0002` score=0.656619 cov=0.142 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_095.md::c0007` score=0.651769 cov=0.576 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_095.md::c0006` score=0.650532 cov=0.576 section=中文复杂检索文档 > 关
  - rank 5: `zh_doc_095.md::c0000` score=0.616831 cov=0.142 section=

### zh096_holdout — zh_long_span_boundary_candidate
- question: 肠结核有哪些临床表现
- gold: `zh_doc_096.md > 关键材料`
- best_topk_coverage: 0.557
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_096.md::c0005` score=0.7436 cov=0.557 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_096.md::c0001` score=0.729507 cov=0.126 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_096.md::c0007` score=0.70421 cov=0.12 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_096.md::c0006` score=0.678819 cov=0.191 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_096.md::c0002` score=0.67819 cov=0.117 section=中文复杂检索文档 > 背景材料1

### zh097_holdout — zh_long_span_boundary_candidate
- question: 如何给表带钻孔
- gold: `zh_doc_097.md > 关键材料`
- best_topk_coverage: 0.526
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_097.md::c0008` score=0.727829 cov=0.081 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_097.md::c0003` score=0.719908 cov=0.25 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_097.md::c0005` score=0.692814 cov=0.407 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_097.md::c0004` score=0.676368 cov=0.526 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_097.md::c0006` score=0.673219 cov=0.09 section=中文复杂检索文档 > 补充材料1

### zh100_holdout — zh_long_span_boundary_candidate
- question: 红枣表面出现了一层白色粉末
- gold: `zh_doc_100.md > 关键材料`
- best_topk_coverage: 0.58
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_100.md::c0004` score=0.806733 cov=0.309 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_100.md::c0006` score=0.790904 cov=0.066 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_100.md::c0005` score=0.7828 cov=0.057 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_100.md::c0003` score=0.767798 cov=0.58 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_100.md::c0000` score=0.729262 cov=0.093 section=

### zh101_holdout — zh_long_span_boundary_candidate
- question: 小米的平板电脑使用体验怎么样
- gold: `zh_doc_101.md > 关键材料`
- best_topk_coverage: 0.577
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_101.md::c0010` score=0.711219 cov=0.577 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_101.md::c0016` score=0.707443 cov=0.044 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_101.md::c0013` score=0.672655 cov=0.081 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_101.md::c0001` score=0.664476 cov=0.066 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_101.md::c0000` score=0.660689 cov=0.096 section=

### zh102_holdout — zh_long_span_boundary_candidate
- question: 尺神经麻痹的治疗方法是什么
- gold: `zh_doc_102.md > 关键材料`
- best_topk_coverage: 0.164
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_102.md::c0005` score=0.738727 cov=0.164 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_102.md::c0011` score=0.735389 cov=0.072 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_102.md::c0009` score=0.720307 cov=0.098 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_102.md::c0004` score=0.712152 cov=0.078 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_102.md::c0002` score=0.707177 cov=0.11 section=中文复杂检索文档 > 背景材料1

### zh103_holdout — zh_long_span_boundary_candidate
- question: 北京办理出国体检的地点在哪里？
- gold: `zh_doc_103.md > 关键材料`
- best_topk_coverage: 0.623
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_103.md::c0004` score=0.778798 cov=0.623 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_103.md::c0006` score=0.737361 cov=0.242 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_103.md::c0007` score=0.715919 cov=0.361 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_103.md::c0001` score=0.709583 cov=0.242 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_103.md::c0005` score=0.674603 cov=0.576 section=中文复杂检索文档 > 关键材料

### zh110_holdout — zh_long_span_boundary_candidate
- question: 完美世界公司开发了哪些游戏
- gold: `zh_doc_110.md > 关键材料`
- best_topk_coverage: 0.607
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_110.md::c0000` score=0.691882 cov=0.061 section=
  - rank 2: `zh_doc_110.md::c0001` score=0.604878 cov=0.088 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_110.md::c0002` score=0.601517 cov=0.098 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_110.md::c0003` score=0.589344 cov=0.607 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_110.md::c0006` score=0.584048 cov=0.067 section=中文复杂检索文档 > 补充材料1

### zh113_holdout — zh_long_span_boundary_candidate
- question: 如何正确服用辅酶q10
- gold: `zh_doc_113.md > 关键材料`
- best_topk_coverage: 0.625
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_113.md::c0008` score=0.736305 cov=0.124 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_113.md::c0003` score=0.723775 cov=0.138 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_113.md::c0007` score=0.690586 cov=0.52 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_113.md::c0006` score=0.676752 cov=0.625 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_113.md::c0004` score=0.66553 cov=0.116 section=中文复杂检索文档 > 背景材料2

### zh117_holdout — zh_long_span_boundary_candidate
- question: 德国红铁元和绿铁元有哪些不同之处？
- gold: `zh_doc_117.md > 关键材料`
- best_topk_coverage: 0.227
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_117.md::c0002` score=0.733493 cov=0.227 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_117.md::c0001` score=0.696901 cov=0.199 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_117.md::c0006` score=0.662134 cov=0.224 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_117.md::c0005` score=0.655819 cov=0.217 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_117.md::c0000` score=0.627475 cov=0.189 section=

### zh118_holdout — zh_long_span_boundary_candidate
- question: 诛仙法宝的技能要如何重置
- gold: `zh_doc_118.md > 关键材料`
- best_topk_coverage: 0.354
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_118.md::c0004` score=0.679467 cov=0.354 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_118.md::c0005` score=0.657792 cov=0.08 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_118.md::c0001` score=0.655226 cov=0.038 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_118.md::c0000` score=0.649673 cov=0.046 section=
  - rank 5: `zh_doc_118.md::c0002` score=0.617937 cov=0.274 section=中文复杂检索文档 > 背景材料2

## All Query Summary

| qid | expected type | success | rank | best cov | gold rank hint |
|---|---|---:|---:|---:|---:|
| zh001_holdout | zh_long_span_boundary_candidate | False | None | 0.646 | 1 |
| zh002_holdout | zh_long_span_boundary_candidate | False | None | 0.163 | 1 |
| zh003_holdout | zh_long_span_boundary_candidate | False | None | 0.206 | 1 |
| zh004_holdout | zh_long_span_boundary_candidate | False | None | 0.276 | 1 |
| zh005_holdout | zh_long_span_boundary_candidate | False | None | 0.38 | 1 |
| zh006_holdout | zh_long_span_boundary_candidate | False | None | 0.337 | 1 |
| zh007_holdout | zh_long_span_boundary_candidate | False | None | 0.346 | 1 |
| zh008_holdout | zh_long_span_boundary_candidate | False | None | 0.276 | 1 |
| zh009_holdout | zh_long_span_boundary_candidate | False | None | 0.446 | 1 |
| zh010_holdout | zh_long_span_boundary_candidate | False | None | 0.277 | 1 |
| zh011_holdout | zh_long_span_boundary_candidate | False | None | 0.19 | 1 |
| zh012_holdout | zh_long_span_boundary_candidate | False | None | 0.365 | 1 |
| zh013_holdout | zh_long_span_boundary_candidate | False | None | 0.395 | 1 |
| zh014_holdout | zh_long_span_boundary_candidate | False | None | 0.38 | 1 |
| zh015_holdout | zh_long_span_boundary_candidate | True | 5 | 0.775 | 1 |
| zh016_holdout | zh_long_span_boundary_candidate | False | None | 0.405 | 1 |
| zh017_holdout | zh_long_span_boundary_candidate | False | None | 0.321 | 1 |
| zh018_holdout | zh_long_span_boundary_candidate | False | None | 0.429 | 1 |
| zh019_holdout | zh_long_span_boundary_candidate | False | None | 0.553 | 1 |
| zh020_holdout | zh_long_span_boundary_candidate | False | None | 0.409 | 1 |
| zh021_holdout | zh_long_span_boundary_candidate | True | 3 | 0.692 | 1 |
| zh022_holdout | zh_long_span_boundary_candidate | False | None | 0.386 | 1 |
| zh023_holdout | zh_long_span_boundary_candidate | False | None | 0.472 | 1 |
| zh024_holdout | zh_long_span_boundary_candidate | False | None | 0.575 | 1 |
| zh025_holdout | zh_long_span_boundary_candidate | False | None | 0.448 | 1 |
| zh026_holdout | zh_long_span_boundary_candidate | True | 2 | 0.921 | 1 |
| zh027_holdout | zh_long_span_boundary_candidate | False | None | 0.041 | 1 |
| zh028_holdout | zh_long_span_boundary_candidate | False | None | 0.606 | 1 |
| zh029_holdout | zh_long_span_boundary_candidate | False | None | 0.524 | 1 |
| zh030_holdout | zh_long_span_boundary_candidate | False | None | 0.289 | 1 |
| zh031_holdout | zh_long_span_boundary_candidate | False | None | 0.517 | 1 |
| zh032_holdout | zh_long_span_boundary_candidate | False | None | 0.396 | 1 |
| zh033_holdout | zh_long_span_boundary_candidate | False | None | 0.349 | 1 |
| zh034_holdout | zh_long_span_boundary_candidate | False | None | 0.49 | 1 |
| zh035_holdout | zh_long_span_boundary_candidate | True | 2 | 0.772 | 1 |
| zh036_holdout | zh_long_span_boundary_candidate | False | None | 0.525 | 1 |
| zh037_holdout | zh_long_span_boundary_candidate | False | None | 0.44 | 1 |
| zh038_holdout | zh_long_span_boundary_candidate | False | None | 0.494 | 1 |
| zh039_holdout | zh_long_span_boundary_candidate | False | None | 0.486 | 1 |
| zh040_holdout | zh_long_span_boundary_candidate | False | None | 0.493 | 1 |
| zh041_holdout | zh_long_span_boundary_candidate | False | None | 0.419 | 1 |
| zh042_holdout | zh_long_span_boundary_candidate | True | 2 | 0.842 | 1 |
| zh043_holdout | zh_long_span_boundary_candidate | True | 3 | 0.702 | 1 |
| zh044_holdout | zh_long_span_boundary_candidate | False | None | 0.296 | 1 |
| zh045_holdout | zh_long_span_boundary_candidate | True | 4 | 0.835 | 1 |
| zh046_holdout | zh_long_span_boundary_candidate | False | None | 0.491 | 1 |
| zh047_holdout | zh_long_span_boundary_candidate | False | None | 0.422 | 1 |
| zh048_holdout | zh_long_span_boundary_candidate | False | None | 0.477 | 1 |
| zh049_holdout | zh_long_span_boundary_candidate | True | 4 | 0.753 | 1 |
| zh050_holdout | zh_long_span_boundary_candidate | False | None | 0.265 | 1 |
| zh051_holdout | zh_long_span_boundary_candidate | False | None | 0.533 | 1 |
| zh052_holdout | zh_long_span_boundary_candidate | True | 5 | 0.733 | 1 |
| zh053_holdout | zh_long_span_boundary_candidate | False | None | 0.481 | 1 |
| zh054_holdout | zh_long_span_boundary_candidate | False | None | 0.552 | 1 |
| zh055_holdout | zh_long_span_boundary_candidate | False | None | 0.611 | 1 |
| zh056_holdout | zh_long_span_boundary_candidate | False | None | 0.51 | 1 |
| zh057_holdout | zh_long_span_boundary_candidate | False | None | 0.546 | 1 |
| zh058_holdout | zh_long_span_boundary_candidate | False | None | 0.25 | 1 |
| zh059_holdout | zh_long_span_boundary_candidate | True | 2 | 0.656 | 1 |
| zh060_holdout | zh_long_span_boundary_candidate | True | 2 | 0.717 | 1 |
| zh061_holdout | zh_long_span_boundary_candidate | True | 1 | 0.723 | 1 |
| zh062_holdout | zh_long_span_boundary_candidate | False | None | 0.506 | 1 |
| zh063_holdout | zh_long_span_boundary_candidate | True | 5 | 0.66 | 1 |
| zh064_holdout | zh_long_span_boundary_candidate | False | None | 0.639 | 1 |
| zh065_holdout | zh_long_span_boundary_candidate | True | 3 | 0.825 | 1 |
| zh066_holdout | zh_long_span_boundary_candidate | False | None | 0.567 | 1 |
| zh067_holdout | zh_long_span_boundary_candidate | False | None | 0.432 | 1 |
| zh068_holdout | zh_long_span_boundary_candidate | True | 3 | 0.67 | 1 |
| zh069_holdout | zh_long_span_boundary_candidate | True | 2 | 1.0 | 1 |
| zh070_holdout | zh_long_span_boundary_candidate | False | None | 0.375 | 1 |
| zh071_holdout | zh_long_span_boundary_candidate | False | None | 0.617 | 1 |
| zh072_holdout | zh_long_span_boundary_candidate | False | None | 0.42 | 1 |
| zh073_holdout | zh_long_span_boundary_candidate | True | 2 | 0.854 | 1 |
| zh074_holdout | zh_long_span_boundary_candidate | False | None | 0.595 | 1 |
| zh075_holdout | zh_long_span_boundary_candidate | False | None | 0.137 | 1 |
| zh076_holdout | zh_long_span_boundary_candidate | False | None | 0.567 | 1 |
| zh077_holdout | zh_long_span_boundary_candidate | False | None | 0.584 | 1 |
| zh078_holdout | zh_long_span_boundary_candidate | False | None | 0.578 | 1 |
| zh079_holdout | zh_long_span_boundary_candidate | False | None | 0.527 | 1 |
| zh080_holdout | zh_long_span_boundary_candidate | True | 1 | 0.848 | 1 |
| zh081_holdout | zh_long_span_boundary_candidate | False | None | 0.588 | 1 |
| zh082_holdout | zh_long_span_boundary_candidate | False | None | 0.09 | 1 |
| zh083_holdout | zh_long_span_boundary_candidate | False | None | 0.637 | 1 |
| zh084_holdout | zh_long_span_boundary_candidate | True | 2 | 0.71 | 1 |
| zh085_holdout | zh_long_span_boundary_candidate | False | None | 0.371 | 1 |
| zh086_holdout | zh_long_span_boundary_candidate | True | 5 | 0.656 | 1 |
| zh087_holdout | zh_long_span_boundary_candidate | True | 3 | 0.676 | 1 |
| zh088_holdout | zh_long_span_boundary_candidate | True | 3 | 0.949 | 1 |
| zh089_holdout | zh_long_span_boundary_candidate | False | None | 0.456 | 1 |
| zh090_holdout | zh_long_span_boundary_candidate | False | None | 0.404 | 1 |
| zh091_holdout | zh_long_span_boundary_candidate | True | 1 | 0.668 | 1 |
| zh092_holdout | zh_long_span_boundary_candidate | True | 4 | 0.662 | 1 |
| zh093_holdout | zh_long_span_boundary_candidate | False | None | 0.256 | 1 |
| zh094_holdout | zh_long_span_boundary_candidate | False | None | 0.077 | 1 |
| zh095_holdout | zh_long_span_boundary_candidate | False | None | 0.576 | 1 |
| zh096_holdout | zh_long_span_boundary_candidate | False | None | 0.557 | 1 |
| zh097_holdout | zh_long_span_boundary_candidate | False | None | 0.526 | 1 |
| zh098_holdout | zh_long_span_boundary_candidate | True | 1 | 0.682 | 1 |
| zh099_holdout | zh_long_span_boundary_candidate | True | 2 | 0.906 | 1 |
| zh100_holdout | zh_long_span_boundary_candidate | False | None | 0.58 | 1 |
| zh101_holdout | zh_long_span_boundary_candidate | False | None | 0.577 | 1 |
| zh102_holdout | zh_long_span_boundary_candidate | False | None | 0.164 | 1 |
| zh103_holdout | zh_long_span_boundary_candidate | False | None | 0.623 | 1 |
| zh104_holdout | zh_long_span_boundary_candidate | True | 5 | 0.722 | 1 |
| zh105_holdout | zh_long_span_boundary_candidate | True | 3 | 0.669 | 1 |
| zh106_holdout | zh_long_span_boundary_candidate | True | 4 | 0.773 | 1 |
| zh107_holdout | zh_long_span_boundary_candidate | True | 5 | 0.665 | 1 |
| zh108_holdout | zh_long_span_boundary_candidate | True | 3 | 0.674 | 1 |
| zh109_holdout | zh_long_span_boundary_candidate | True | 2 | 0.656 | 1 |
| zh110_holdout | zh_long_span_boundary_candidate | False | None | 0.607 | 1 |
| zh111_holdout | zh_long_span_boundary_candidate | True | 5 | 0.689 | 1 |
| zh112_holdout | zh_long_span_boundary_candidate | True | 3 | 0.849 | 1 |
| zh113_holdout | zh_long_span_boundary_candidate | False | None | 0.625 | 1 |
| zh114_holdout | zh_long_span_boundary_candidate | True | 2 | 0.656 | 1 |
| zh115_holdout | zh_long_span_boundary_candidate | True | 2 | 0.711 | 1 |
| zh116_holdout | zh_long_span_boundary_candidate | True | 2 | 0.671 | 1 |
| zh117_holdout | zh_long_span_boundary_candidate | False | None | 0.227 | 1 |
| zh118_holdout | zh_long_span_boundary_candidate | False | None | 0.354 | 1 |
| zh119_holdout | zh_long_span_boundary_candidate | True | 3 | 0.959 | 1 |
| zh120_holdout | zh_long_span_boundary_candidate | True | 4 | 0.67 | 1 |
