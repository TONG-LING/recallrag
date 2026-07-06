# Baseline Retrieval Report

## Config

- **docs**: `case_zh_dureader_120/docs`
- **questions**: `case_zh_dureader_120/eval/questions_patch_source.jsonl`
- **chunk_size**: `220`
- **overlap**: `100`
- **keep_heading**: `True`
- **top_k**: `5`
- **coverage_threshold**: `0.65`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`

## Metrics

- **total**: 120
- **recall@5**: 0.1000
- **mrr**: 0.0753
- **hits**: 12
- **failed**: 108
- **coverage_threshold**: 0.6500

## Failed Queries

### zh001 — zh_long_span_boundary_candidate
- question: 高速公路超速20以上不足50扣几分
- gold: `zh_doc_001.md > 关键材料`
- best_topk_coverage: 0.646
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_001.md::c0070` score=0.806165 cov=0.419 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_001.md::c0069` score=0.803453 cov=0.39 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_001.md::c0022` score=0.800873 cov=0.646 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_001.md::c0021` score=0.792428 cov=0.534 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_001.md::c0020` score=0.788961 cov=0.391 section=中文复杂检索文档 > 背景材料2

### zh002 — zh_long_span_boundary_candidate
- question: 空气净化器哪种净化方式好
- gold: `zh_doc_002.md > 关键材料`
- best_topk_coverage: 0.267
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_002.md::c0005` score=0.734196 cov=0.175 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_002.md::c0010` score=0.724986 cov=0.267 section=中文复杂检索文档 > 关
  - rank 3: `zh_doc_002.md::c0003` score=0.708202 cov=0.115 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_002.md::c0006` score=0.707527 cov=0.101 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_002.md::c0001` score=0.706358 cov=0.154 section=中文复杂检索文档 > 背景材料1

### zh003 — zh_long_span_boundary_candidate
- question: 黄山风景古诗赞
- gold: `zh_doc_003.md > 关键材料`
- best_topk_coverage: 0.222
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_003.md::c0017` score=0.66983 cov=0.033 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_003.md::c0009` score=0.646298 cov=0.194 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_003.md::c0016` score=0.644564 cov=0.057 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_003.md::c0011` score=0.640429 cov=0.203 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_003.md::c0013` score=0.637578 cov=0.222 section=中文复杂检索文档 > 关键材料

### zh004 — zh_long_span_boundary_candidate
- question: 一天放很多屁
- gold: `zh_doc_004.md > 关键材料`
- best_topk_coverage: 0.277
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_004.md::c0027` score=0.727765 cov=0.239 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_004.md::c0044` score=0.71572 cov=0.276 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_004.md::c0004` score=0.714307 cov=0.061 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_004.md::c0000` score=0.711929 cov=0.084 section=
  - rank 5: `zh_doc_004.md::c0038` score=0.711638 cov=0.277 section=中文复杂检索文档 > 关键材料

### zh005 — zh_long_span_boundary_candidate
- question: 叉车有几种
- gold: `zh_doc_005.md > 关键材料`
- best_topk_coverage: 0.371
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_005.md::c0028` score=0.771945 cov=0.371 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_005.md::c0027` score=0.761885 cov=0.254 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_005.md::c0035` score=0.733273 cov=0.326 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_005.md::c0033` score=0.731891 cov=0.342 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_005.md::c0032` score=0.726091 cov=0.349 section=中文复杂检索文档 > 关键材料

### zh006 — zh_long_span_boundary_candidate
- question: 春光成语
- gold: `zh_doc_006.md > 关键材料`
- best_topk_coverage: 0.357
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_006.md::c0014` score=0.769941 cov=0.339 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_006.md::c0005` score=0.742111 cov=0.307 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_006.md::c0007` score=0.741178 cov=0.326 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_006.md::c0008` score=0.731392 cov=0.357 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_006.md::c0001` score=0.715913 cov=0.1 section=中文复杂检索文档 > 背景材料1

### zh007 — zh_long_span_boundary_candidate
- question: 经常用肥皂洗脸好吗
- gold: `zh_doc_007.md > 关键材料`
- best_topk_coverage: 0.335
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_007.md::c0020` score=0.797595 cov=0.137 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_007.md::c0019` score=0.793768 cov=0.114 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_007.md::c0018` score=0.769789 cov=0.093 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_007.md::c0012` score=0.76856 cov=0.335 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_007.md::c0006` score=0.762692 cov=0.166 section=中文复杂检索文档 > 背景材料2

### zh008 — zh_long_span_boundary_candidate
- question: 冬天怎样养鹦鹉
- gold: `zh_doc_008.md > 关键材料`
- best_topk_coverage: 0.275
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_008.md::c0004` score=0.724676 cov=0.06 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_008.md::c0005` score=0.72399 cov=0.055 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_008.md::c0019` score=0.723605 cov=0.084 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_008.md::c0008` score=0.696016 cov=0.275 section=中文复杂检索文档 > 关键
  - rank 5: `zh_doc_008.md::c0007` score=0.693924 cov=0.143 section=中文复杂检索文档 > 背景材料2

### zh009 — zh_long_span_boundary_candidate
- question: 附睾肿胀
- gold: `zh_doc_009.md > 关键材料`
- best_topk_coverage: 0.42
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_009.md::c0012` score=0.762951 cov=0.418 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_009.md::c0011` score=0.762107 cov=0.42 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_009.md::c0010` score=0.756821 cov=0.315 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_009.md::c0023` score=0.753357 cov=0.093 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_009.md::c0024` score=0.740864 cov=0.093 section=中文复杂检索文档 > 补充材料2

### zh010 — zh_long_span_boundary_candidate
- question: 硫磺皂能长期用吗
- gold: `zh_doc_010.md > 关键材料`
- best_topk_coverage: 0.065
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_010.md::c0015` score=0.809773 cov=0.061 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_010.md::c0016` score=0.79905 cov=0.049 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_010.md::c0014` score=0.78941 cov=0.065 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_010.md::c0017` score=0.77396 cov=0.057 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_010.md::c0000` score=0.764083 cov=0.054 section=

### zh011 — zh_long_span_boundary_candidate
- question: 比较好看的电视剧
- gold: `zh_doc_011.md > 关键材料`
- best_topk_coverage: 0.173
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_011.md::c0000` score=0.618039 cov=0.078 section=
  - rank 2: `zh_doc_011.md::c0016` score=0.617086 cov=0.031 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_011.md::c0017` score=0.615748 cov=0.026 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_011.md::c0013` score=0.577456 cov=0.173 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_011.md::c0014` score=0.571671 cov=0.034 section=中文复杂检索文档 > 补充材料1

### zh012 — zh_long_span_boundary_candidate
- question: 夏天喝什么饮品好
- gold: `zh_doc_012.md > 关键材料`
- best_topk_coverage: 0.112
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_012.md::c0002` score=0.654497 cov=0.101 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_012.md::c0000` score=0.653822 cov=0.112 section=
  - rank 3: `zh_doc_012.md::c0001` score=0.632533 cov=0.109 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_012.md::c0015` score=0.621212 cov=0.08 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_012.md::c0014` score=0.615834 cov=0.078 section=中文复杂检索文档 > 补充材料1

### zh013 — zh_long_span_boundary_candidate
- question: workgroup是什么
- gold: `zh_doc_013.md > 关键材料`
- best_topk_coverage: 0.373
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_013.md::c0000` score=0.707351 cov=0.093 section=
  - rank 2: `zh_doc_013.md::c0005` score=0.580631 cov=0.373 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_013.md::c0002` score=0.575356 cov=0.189 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_013.md::c0001` score=0.574474 cov=0.093 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_013.md::c0011` score=0.493052 cov=0.351 section=中文复杂检索文档 > 关键材料

### zh014 — zh_long_span_boundary_candidate
- question: 怎样锻炼肺活量
- gold: `zh_doc_014.md > 关键材料`
- best_topk_coverage: 0.38
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_014.md::c0017` score=0.723591 cov=0.253 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_014.md::c0020` score=0.709046 cov=0.114 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_014.md::c0012` score=0.70829 cov=0.38 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_014.md::c0009` score=0.705976 cov=0.211 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_014.md::c0000` score=0.703814 cov=0.128 section=

### zh015 — zh_long_span_boundary_candidate
- question: 做胃镜注意
- gold: `zh_doc_015.md > 关键材料`
- best_topk_coverage: 0.433
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_015.md::c0014` score=0.721211 cov=0.343 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_015.md::c0011` score=0.720802 cov=0.433 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_015.md::c0010` score=0.716532 cov=0.428 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_015.md::c0015` score=0.693442 cov=0.287 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_015.md::c0012` score=0.691858 cov=0.376 section=中文复杂检索文档 > 关键材料

### zh016 — zh_long_span_boundary_candidate
- question: 油电混合动力汽车购置税优惠吗
- gold: `zh_doc_016.md > 关键材料`
- best_topk_coverage: 0.391
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_016.md::c0011` score=0.806264 cov=0.387 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_016.md::c0008` score=0.774423 cov=0.362 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_016.md::c0014` score=0.769314 cov=0.391 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_016.md::c0010` score=0.754076 cov=0.381 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_016.md::c0021` score=0.749349 cov=0.24 section=中文复杂检索文档 > 补充材料1

### zh017 — zh_long_span_boundary_candidate
- question: 阴部变白
- gold: `zh_doc_017.md > 关键材料`
- best_topk_coverage: 0.234
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_017.md::c0006` score=0.708334 cov=0.234 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_017.md::c0005` score=0.705511 cov=0.057 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_017.md::c0018` score=0.687928 cov=0.028 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_017.md::c0000` score=0.680065 cov=0.036 section=
  - rank 5: `zh_doc_017.md::c0002` score=0.679316 cov=0.055 section=中文复杂检索文档 > 背景材料1

### zh018 — zh_long_span_boundary_candidate
- question: 如何买卖etf基金
- gold: `zh_doc_018.md > 关键材料`
- best_topk_coverage: 0.375
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_018.md::c0006` score=0.790412 cov=0.333 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_018.md::c0005` score=0.766788 cov=0.223 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_018.md::c0015` score=0.764782 cov=0.165 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_018.md::c0007` score=0.763634 cov=0.375 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_018.md::c0016` score=0.74292 cov=0.134 section=中文复杂检索文档 > 补充材料2

### zh019 — zh_long_span_boundary_candidate
- question: 在实习期内的驾驶证扣分会怎样
- gold: `zh_doc_019.md > 关键材料`
- best_topk_coverage: 0.481
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_019.md::c0016` score=0.795916 cov=0.481 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_019.md::c0018` score=0.784818 cov=0.24 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_019.md::c0015` score=0.78334 cov=0.379 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_019.md::c0019` score=0.779941 cov=0.324 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_019.md::c0017` score=0.777944 cov=0.416 section=中文复杂检索文档 > 补充材料1

### zh020 — zh_long_span_boundary_candidate
- question: 私立大学和公立大学的区别
- gold: `zh_doc_020.md > 关键材料`
- best_topk_coverage: 0.3
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_020.md::c0021` score=0.810362 cov=0.3 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_020.md::c0005` score=0.799246 cov=0.106 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_020.md::c0022` score=0.798635 cov=0.084 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_020.md::c0004` score=0.789478 cov=0.097 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_020.md::c0023` score=0.775351 cov=0.089 section=中文复杂检索文档 > 补充材料1

### zh021 — zh_long_span_boundary_candidate
- question: 如何调水表数字
- gold: `zh_doc_021.md > 关键材料`
- best_topk_coverage: 0.335
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_021.md::c0010` score=0.823938 cov=0.222 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_021.md::c0011` score=0.822056 cov=0.325 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_021.md::c0009` score=0.781346 cov=0.06 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_021.md::c0012` score=0.736163 cov=0.335 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_021.md::c0021` score=0.685499 cov=0.055 section=中文复杂检索文档 > 补充材料1

### zh022 — zh_long_span_boundary_candidate
- question: 怎样种香菜
- gold: `zh_doc_022.md > 关键材料`
- best_topk_coverage: 0.391
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_022.md::c0033` score=0.727831 cov=0.083 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_022.md::c0032` score=0.707677 cov=0.093 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_022.md::c0030` score=0.706732 cov=0.072 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_022.md::c0023` score=0.703859 cov=0.391 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_022.md::c0028` score=0.702416 cov=0.154 section=中文复杂检索文档 > 关键材料

### zh023 — zh_long_span_boundary_candidate
- question: 如何把电脑上的东西传到ipad上
- gold: `zh_doc_023.md > 关键材料`
- best_topk_coverage: 0.503
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_023.md::c0007` score=0.791905 cov=0.362 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_023.md::c0009` score=0.768633 cov=0.503 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_023.md::c0002` score=0.762032 cov=0.094 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_023.md::c0006` score=0.761846 cov=0.125 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_023.md::c0001` score=0.755287 cov=0.164 section=中文复杂检索文档 > 背景材料1

### zh024 — zh_long_span_boundary_candidate
- question: c1扣12分怎么办
- gold: `zh_doc_024.md > 关键材料`
- best_topk_coverage: 0.382
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_024.md::c0021` score=0.800524 cov=0.129 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_024.md::c0009` score=0.792681 cov=0.367 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_024.md::c0008` score=0.7845 cov=0.155 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_024.md::c0005` score=0.777689 cov=0.382 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_024.md::c0020` score=0.771396 cov=0.279 section=中文复杂检索文档 > 补充材料1

### zh025 — zh_long_span_boundary_candidate
- question: tf与sd卡的区别
- gold: `zh_doc_025.md > 关键材料`
- best_topk_coverage: 0.347
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_025.md::c0019` score=0.827206 cov=0.347 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_025.md::c0025` score=0.814969 cov=0.308 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_025.md::c0001` score=0.812256 cov=0.145 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_025.md::c0018` score=0.80887 cov=0.287 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_025.md::c0011` score=0.808335 cov=0.207 section=中文复杂检索文档 > 背

### zh026 — zh_long_span_boundary_candidate
- question: 左肾部位疼痛
- gold: `zh_doc_026.md > 关键材料`
- best_topk_coverage: 0.56
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_026.md::c0005` score=0.810973 cov=0.22 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_026.md::c0006` score=0.801116 cov=0.56 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_026.md::c0009` score=0.799603 cov=0.469 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_026.md::c0007` score=0.794299 cov=0.482 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_026.md::c0008` score=0.79248 cov=0.551 section=中文复杂检索文档 > 关键材料

### zh027 — zh_long_span_boundary_candidate
- question: 小米平板钢化膜怎么贴
- gold: `zh_doc_027.md > 关键材料`
- best_topk_coverage: 0.078
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_027.md::c0017` score=0.779979 cov=0.078 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_027.md::c0018` score=0.7541 cov=0.059 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_027.md::c0019` score=0.73957 cov=0.023 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_081.md::c0024` score=0.68882 cov=0.0 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_027.md::c0016` score=0.680962 cov=0.043 section=中文复杂检索文档 > 补充材料1

### zh028 — zh_long_span_boundary_candidate
- question: 怎么控制路由器把蹭wifi的人给踢了
- gold: `zh_doc_028.md > 关键材料`
- best_topk_coverage: 0.403
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_028.md::c0004` score=0.779366 cov=0.352 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_028.md::c0002` score=0.761064 cov=0.185 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_028.md::c0010` score=0.746692 cov=0.403 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_028.md::c0011` score=0.746267 cov=0.206 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_028.md::c0001` score=0.745594 cov=0.185 section=中文复杂检索文档 > 背景材料1

### zh029 — zh_long_span_boundary_candidate
- question: 怎么做卫浴销售
- gold: `zh_doc_029.md > 关键材料`
- best_topk_coverage: 0.342
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_029.md::c0004` score=0.762925 cov=0.051 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_029.md::c0003` score=0.72762 cov=0.063 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_029.md::c0002` score=0.71714 cov=0.075 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_029.md::c0001` score=0.708463 cov=0.075 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_029.md::c0006` score=0.706226 cov=0.342 section=中文复杂检索文档 > 背景材料2

### zh030 — zh_long_span_boundary_candidate
- question: 外伤缝针不能吃什么
- gold: `zh_doc_030.md > 关键材料`
- best_topk_coverage: 0.262
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_030.md::c0005` score=0.724702 cov=0.132 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_030.md::c0004` score=0.723378 cov=0.171 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_030.md::c0022` score=0.72219 cov=0.11 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_030.md::c0003` score=0.713319 cov=0.262 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_030.md::c0021` score=0.708383 cov=0.179 section=中文复杂检索文档 > 补充材料1

### zh031 — zh_long_span_boundary_candidate
- question: 超级会员是什么
- gold: `zh_doc_031.md > 关键材料`
- best_topk_coverage: 0.483
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_031.md::c0004` score=0.689479 cov=0.323 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_031.md::c0006` score=0.685294 cov=0.483 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_031.md::c0011` score=0.675546 cov=0.244 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_031.md::c0014` score=0.668109 cov=0.226 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_031.md::c0005` score=0.667708 cov=0.453 section=中文复杂检索文档 > 背景材料2

### zh032 — zh_long_span_boundary_candidate
- question: 杭州劳动仲裁电话
- gold: `zh_doc_032.md > 关键材料`
- best_topk_coverage: 0.324
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_032.md::c0004` score=0.769716 cov=0.324 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_032.md::c0012` score=0.751862 cov=0.126 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_032.md::c0030` score=0.750811 cov=0.141 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_032.md::c0003` score=0.742295 cov=0.05 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_032.md::c0031` score=0.732036 cov=0.19 section=中文复杂检索文档 > 补充材料2

### zh033 — zh_long_span_boundary_candidate
- question: 电暖桌哪个牌子好
- gold: `zh_doc_033.md > 关键材料`
- best_topk_coverage: 0.325
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_033.md::c0007` score=0.80554 cov=0.325 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_033.md::c0006` score=0.786282 cov=0.172 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_033.md::c0001` score=0.781597 cov=0.093 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_033.md::c0023` score=0.781483 cov=0.067 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_033.md::c0002` score=0.78125 cov=0.111 section=中文复杂检索文档 > 背景材料1

### zh034 — zh_long_span_boundary_candidate
- question: 板栗可以蒸着吃吗
- gold: `zh_doc_034.md > 关键材料`
- best_topk_coverage: 0.433
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_034.md::c0008` score=0.720458 cov=0.277 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_034.md::c0009` score=0.70468 cov=0.433 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_034.md::c0002` score=0.639031 cov=0.104 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_034.md::c0017` score=0.63818 cov=0.108 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_034.md::c0018` score=0.635583 cov=0.112 section=中文复杂检索文档 > 补充材料2

### zh035 — zh_long_span_boundary_candidate
- question: 没越狱的iphone怎么清理垃圾
- gold: `zh_doc_035.md > 关键材料`
- best_topk_coverage: 0.432
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_035.md::c0015` score=0.796876 cov=0.125 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_035.md::c0013` score=0.787697 cov=0.125 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_035.md::c0003` score=0.783061 cov=0.39 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_035.md::c0004` score=0.777213 cov=0.432 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_035.md::c0016` score=0.774622 cov=0.143 section=中文复杂检索文档 > 补充材料2

### zh036 — zh_long_span_boundary_candidate
- question: 苹果系统怎么查看隐藏文件
- gold: `zh_doc_036.md > 关键材料`
- best_topk_coverage: 0.591
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_036.md::c0008` score=0.77137 cov=0.475 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_036.md::c0009` score=0.771011 cov=0.475 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_036.md::c0005` score=0.75834 cov=0.591 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_036.md::c0007` score=0.741491 cov=0.418 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_036.md::c0006` score=0.737442 cov=0.496 section=中文复杂检索文档 > 关键材料

### zh037 — zh_long_span_boundary_candidate
- question: 海淀医院孕前检查
- gold: `zh_doc_037.md > 关键材料`
- best_topk_coverage: 0.438
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_037.md::c0001` score=0.737219 cov=0.079 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_037.md::c0000` score=0.733445 cov=0.071 section=
  - rank 3: `zh_doc_037.md::c0007` score=0.730104 cov=0.438 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_037.md::c0005` score=0.729531 cov=0.119 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_037.md::c0006` score=0.728245 cov=0.315 section=中文复杂检索文档 > 背景材料2

### zh038 — zh_long_span_boundary_candidate
- question: 玩梦幻西游怎么赚钱
- gold: `zh_doc_038.md > 关键材料`
- best_topk_coverage: 0.315
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_038.md::c0000` score=0.720347 cov=0.074 section=
  - rank 2: `zh_doc_038.md::c0005` score=0.705161 cov=0.083 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_038.md::c0012` score=0.689638 cov=0.315 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_038.md::c0016` score=0.687371 cov=0.047 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_038.md::c0004` score=0.680521 cov=0.057 section=中文复杂检索文档 > 背景材料1

### zh039 — zh_long_span_boundary_candidate
- question: 跟庐山有关的诗句
- gold: `zh_doc_039.md > 关键材料`
- best_topk_coverage: 0.302
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_039.md::c0009` score=0.721372 cov=0.295 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_039.md::c0010` score=0.712314 cov=0.103 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_039.md::c0004` score=0.693433 cov=0.302 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_039.md::c0001` score=0.690287 cov=0.068 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_039.md::c0012` score=0.689795 cov=0.06 section=中文复杂检索文档 > 补充材料1

### zh040 — zh_long_span_boundary_candidate
- question: 现在去哪里下载音乐
- gold: `zh_doc_040.md > 关键材料`
- best_topk_coverage: 0.137
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_040.md::c0000` score=0.631478 cov=0.137 section=
  - rank 2: `zh_doc_040.md::c0001` score=0.616623 cov=0.115 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_040.md::c0014` score=0.611626 cov=0.051 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_040.md::c0002` score=0.611026 cov=0.093 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_040.md::c0011` score=0.610036 cov=0.103 section=中文复杂检索文档 > 补充材料1

### zh041 — zh_long_span_boundary_candidate
- question: 治疗颈椎病药物
- gold: `zh_doc_041.md > 关键材料`
- best_topk_coverage: 0.44
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_041.md::c0021` score=0.712307 cov=0.105 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_041.md::c0020` score=0.676401 cov=0.114 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_041.md::c0022` score=0.659429 cov=0.107 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_041.md::c0013` score=0.643275 cov=0.44 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_041.md::c0017` score=0.642157 cov=0.323 section=中文复杂检索文档 > 关键材料

### zh042 — zh_long_span_boundary_candidate
- question: 户外手电筒什么牌子好
- gold: `zh_doc_042.md > 关键材料`
- best_topk_coverage: 0.408
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_042.md::c0005` score=0.73549 cov=0.408 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_042.md::c0004` score=0.729215 cov=0.268 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_042.md::c0009` score=0.697348 cov=0.317 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_042.md::c0010` score=0.694663 cov=0.114 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_042.md::c0001` score=0.683455 cov=0.087 section=中文复杂检索文档 > 背景材料1

### zh043 — zh_long_span_boundary_candidate
- question: cfs和cy有什么不同
- gold: `zh_doc_043.md > 关键材料`
- best_topk_coverage: 0.47
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_043.md::c0003` score=0.603975 cov=0.47 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_043.md::c0002` score=0.603287 cov=0.186 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_043.md::c0020` score=0.51464 cov=0.012 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_043.md::c0021` score=0.491812 cov=0.01 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_043.md::c0018` score=0.477852 cov=0.012 section=中文复杂检索文档 > 补充材料1

### zh044 — zh_long_span_boundary_candidate
- question: 换外汇哪个银行好
- gold: `zh_doc_044.md > 关键材料`
- best_topk_coverage: 0.276
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_044.md::c0000` score=0.838119 cov=0.079 section=
  - rank 2: `zh_doc_044.md::c0002` score=0.787575 cov=0.095 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_044.md::c0004` score=0.778637 cov=0.276 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_044.md::c0011` score=0.777312 cov=0.229 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_044.md::c0001` score=0.774884 cov=0.075 section=中文复杂检索文档 > 背景材料1

### zh045 — zh_long_span_boundary_candidate
- question: 轻型羽绒服什么牌子好
- gold: `zh_doc_045.md > 关键材料`
- best_topk_coverage: 0.581
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_045.md::c0004` score=0.653962 cov=0.581 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_045.md::c0023` score=0.648316 cov=0.128 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_045.md::c0014` score=0.634516 cov=0.114 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_045.md::c0020` score=0.63437 cov=0.125 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_045.md::c0000` score=0.630254 cov=0.1 section=

### zh046 — zh_long_span_boundary_candidate
- question: 手机外放进水
- gold: `zh_doc_046.md > 关键材料`
- best_topk_coverage: 0.121
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_046.md::c0013` score=0.736211 cov=0.106 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_046.md::c0000` score=0.735881 cov=0.114 section=
  - rank 3: `zh_doc_046.md::c0014` score=0.732137 cov=0.069 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_046.md::c0003` score=0.729471 cov=0.111 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_046.md::c0001` score=0.728661 cov=0.121 section=中文复杂检索文档 > 背景材料1

### zh047 — zh_long_span_boundary_candidate
- question: 什么样的借条不具法律效力
- gold: `zh_doc_047.md > 关键材料`
- best_topk_coverage: 0.576
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_047.md::c0025` score=0.803932 cov=0.11 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_047.md::c0023` score=0.789936 cov=0.167 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_047.md::c0022` score=0.789541 cov=0.147 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_047.md::c0024` score=0.789147 cov=0.167 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_047.md::c0017` score=0.77774 cov=0.576 section=中文复杂检索文档 > 关键材料

### zh048 — zh_long_span_boundary_candidate
- question: m8a1用什么炮
- gold: `zh_doc_048.md > 关键材料`
- best_topk_coverage: 0.405
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_048.md::c0014` score=0.703011 cov=0.123 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_048.md::c0015` score=0.695703 cov=0.091 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_048.md::c0010` score=0.688617 cov=0.405 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_048.md::c0012` score=0.686008 cov=0.114 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_048.md::c0006` score=0.685585 cov=0.295 section=中文复杂检索文档 > 背景材料2

### zh049 — zh_long_span_boundary_candidate
- question: 西安人流手术费用要多少
- gold: `zh_doc_049.md > 关键材料`
- best_topk_coverage: 0.548
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_049.md::c0000` score=0.783485 cov=0.161 section=
  - rank 2: `zh_doc_049.md::c0010` score=0.775274 cov=0.267 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_049.md::c0009` score=0.770531 cov=0.484 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_049.md::c0011` score=0.767907 cov=0.217 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_049.md::c0008` score=0.752888 cov=0.548 section=中文复杂检索文档 > 关键材料

### zh050 — zh_long_span_boundary_candidate
- question: xm外汇平台怎么样
- gold: `zh_doc_050.md > 关键材料`
- best_topk_coverage: 0.462
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_050.md::c0005` score=0.857863 cov=0.462 section=中文复杂检索文档 > 关键材
  - rank 2: `zh_doc_050.md::c0010` score=0.831437 cov=0.122 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_050.md::c0004` score=0.830331 cov=0.261 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_050.md::c0011` score=0.828971 cov=0.232 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_050.md::c0012` score=0.826371 cov=0.33 section=中文复杂检索文档 > 补充材料1

### zh051 — zh_long_span_boundary_candidate
- question: 双人床最小宽度
- gold: `zh_doc_051.md > 关键材料`
- best_topk_coverage: 0.551
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_051.md::c0015` score=0.764575 cov=0.551 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_051.md::c0025` score=0.763691 cov=0.122 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_051.md::c0019` score=0.758952 cov=0.128 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_051.md::c0001` score=0.756731 cov=0.078 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_051.md::c0002` score=0.756432 cov=0.07 section=中文复杂检索文档 > 背景材料1

### zh052 — zh_long_span_boundary_candidate
- question: 生气时喂奶
- gold: `zh_doc_052.md > 关键材料`
- best_topk_coverage: 0.525
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_052.md::c0007` score=0.777736 cov=0.525 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_052.md::c0008` score=0.761106 cov=0.339 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_052.md::c0004` score=0.756922 cov=0.415 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_052.md::c0013` score=0.756064 cov=0.112 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_052.md::c0005` score=0.753494 cov=0.507 section=中文复杂检索文档 > 关键材料

### zh053 — zh_long_span_boundary_candidate
- question: 龟头敏感度低怎么办
- gold: `zh_doc_053.md > 关键材料`
- best_topk_coverage: 0.164
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_053.md::c0000` score=0.767137 cov=0.051 section=
  - rank 2: `zh_doc_053.md::c0031` score=0.750036 cov=0.124 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_053.md::c0008` score=0.74825 cov=0.119 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_053.md::c0030` score=0.743684 cov=0.164 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_053.md::c0007` score=0.741664 cov=0.117 section=中文复杂检索文档 > 背景材料2

### zh054 — zh_long_span_boundary_candidate
- question: 沪陕高速限速多少
- gold: `zh_doc_054.md > 关键材料`
- best_topk_coverage: 0.599
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_054.md::c0003` score=0.782317 cov=0.256 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_054.md::c0006` score=0.753651 cov=0.599 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_054.md::c0007` score=0.712444 cov=0.535 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_054.md::c0005` score=0.697798 cov=0.491 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_054.md::c0004` score=0.678945 cov=0.31 section=中文复杂检索文档 > 背景材料2

### zh055 — zh_long_span_boundary_candidate
- question: ios9 如何关闭搜索最近联系人
- gold: `zh_doc_055.md > 关键材料`
- best_topk_coverage: 0.535
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_055.md::c0000` score=0.806686 cov=0.459 section=
  - rank 2: `zh_doc_055.md::c0003` score=0.805276 cov=0.535 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_055.md::c0001` score=0.803622 cov=0.513 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_055.md::c0010` score=0.798832 cov=0.377 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_055.md::c0011` score=0.790157 cov=0.301 section=中文复杂检索文档 > 补充材料1

### zh056 — zh_long_span_boundary_candidate
- question: 尸兄主角能力
- gold: `zh_doc_056.md > 关键材料`
- best_topk_coverage: 0.53
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_056.md::c0008` score=0.709761 cov=0.294 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_056.md::c0003` score=0.684829 cov=0.072 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_056.md::c0009` score=0.682961 cov=0.53 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_056.md::c0013` score=0.681651 cov=0.226 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_056.md::c0004` score=0.679408 cov=0.07 section=中文复杂检索文档 > 背景材料1

### zh057 — zh_long_span_boundary_candidate
- question: word怎么不能修改
- gold: `zh_doc_057.md > 关键材料`
- best_topk_coverage: 0.166
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_057.md::c0002` score=0.769633 cov=0.166 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_057.md::c0022` score=0.73894 cov=0.121 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_057.md::c0001` score=0.732224 cov=0.11 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_057.md::c0021` score=0.73021 cov=0.101 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_057.md::c0026` score=0.726547 cov=0.146 section=中文复杂检索文档 > 背景材料2

### zh059 — zh_long_span_boundary_candidate
- question: 电热毯能烘干被子吗
- gold: `zh_doc_059.md > 关键材料`
- best_topk_coverage: 0.637
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_059.md::c0007` score=0.761955 cov=0.588 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_059.md::c0005` score=0.742513 cov=0.346 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_059.md::c0000` score=0.735688 cov=0.134 section=
  - rank 4: `zh_doc_059.md::c0008` score=0.732041 cov=0.637 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_059.md::c0006` score=0.719272 cov=0.595 section=中文复杂检索文档 > 背景材料2

### zh060 — zh_long_span_boundary_candidate
- question: 氨端聚二甲基硅氧烷是硅油吗
- gold: `zh_doc_060.md > 关键材料`
- best_topk_coverage: 0.327
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_060.md::c0017` score=0.690918 cov=0.327 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_060.md::c0023` score=0.672709 cov=0.123 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_060.md::c0026` score=0.656263 cov=0.103 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_060.md::c0008` score=0.645305 cov=0.13 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_060.md::c0029` score=0.627632 cov=0.128 section=中文复杂检索文档 > 补充材料1

### zh061 — zh_long_span_boundary_candidate
- question: 为什么中国必须守住18亿亩耕地红线
- gold: `zh_doc_061.md > 关键材料`
- best_topk_coverage: 0.342
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_061.md::c0001` score=0.778392 cov=0.109 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_061.md::c0011` score=0.776843 cov=0.342 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_061.md::c0010` score=0.77656 cov=0.113 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_061.md::c0016` score=0.771983 cov=0.261 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_061.md::c0017` score=0.768683 cov=0.161 section=中文复杂检索文档 > 补充材料1

### zh062 — zh_long_span_boundary_candidate
- question: 如何取消电脑的自动休眠
- gold: `zh_doc_062.md > 关键材料`
- best_topk_coverage: 0.253
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_062.md::c0010` score=0.847857 cov=0.129 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_062.md::c0009` score=0.820155 cov=0.1 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_062.md::c0011` score=0.806609 cov=0.253 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_062.md::c0000` score=0.782576 cov=0.203 section=
  - rank 5: `zh_doc_062.md::c0001` score=0.776435 cov=0.103 section=中文复杂检索文档 > 背景材料1

### zh063 — zh_long_span_boundary_candidate
- question: 象征孩子纯洁的花
- gold: `zh_doc_063.md > 关键材料`
- best_topk_coverage: 0.49
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_063.md::c0005` score=0.674741 cov=0.087 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_063.md::c0000` score=0.674036 cov=0.107 section=
  - rank 3: `zh_doc_063.md::c0015` score=0.666213 cov=0.213 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_063.md::c0008` score=0.664907 cov=0.447 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_063.md::c0014` score=0.651947 cov=0.49 section=中文复杂检索文档 > 补充材料1

### zh064 — zh_long_span_boundary_candidate
- question: 血清甘油三脂偏低
- gold: `zh_doc_064.md > 关键材料`
- best_topk_coverage: 0.639
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_064.md::c0007` score=0.79995 cov=0.639 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_064.md::c0005` score=0.789394 cov=0.539 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_064.md::c0004` score=0.787105 cov=0.556 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_064.md::c0006` score=0.78655 cov=0.526 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_064.md::c0008` score=0.773117 cov=0.524 section=中文复杂检索文档 > 关键材料

### zh065 — zh_long_span_boundary_candidate
- question: 哪种制氧机好
- gold: `zh_doc_065.md > 关键材料`
- best_topk_coverage: 0.571
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_065.md::c0012` score=0.701716 cov=0.191 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_065.md::c0008` score=0.692923 cov=0.558 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_065.md::c0007` score=0.691282 cov=0.356 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_065.md::c0009` score=0.688354 cov=0.571 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_065.md::c0016` score=0.682109 cov=0.196 section=中文复杂检索文档 > 补充材料1

### zh066 — zh_long_span_boundary_candidate
- question: 电动牙刷刷的干净吗
- gold: `zh_doc_066.md > 关键材料`
- best_topk_coverage: 0.582
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_066.md::c0000` score=0.707145 cov=0.204 section=
  - rank 2: `zh_doc_066.md::c0006` score=0.684864 cov=0.582 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_066.md::c0001` score=0.684189 cov=0.192 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_066.md::c0004` score=0.675635 cov=0.299 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_066.md::c0002` score=0.668933 cov=0.187 section=中文复杂检索文档 > 背景材料1

### zh067 — zh_long_span_boundary_candidate
- question: 武松属什么
- gold: `zh_doc_067.md > 关键材料`
- best_topk_coverage: 0.354
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_067.md::c0007` score=0.708006 cov=0.354 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_067.md::c0003` score=0.663978 cov=0.006 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_067.md::c0006` score=0.64739 cov=0.111 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_067.md::c0001` score=0.628648 cov=0.015 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_067.md::c0000` score=0.619936 cov=0.009 section=

### zh068 — zh_long_span_boundary_candidate
- question: 跳鬼步舞时手怎么动
- gold: `zh_doc_068.md > 关键材料`
- best_topk_coverage: 0.517
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_068.md::c0030` score=0.719597 cov=0.474 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_068.md::c0029` score=0.715803 cov=0.517 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_068.md::c0031` score=0.701744 cov=0.204 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_068.md::c0002` score=0.690452 cov=0.102 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_068.md::c0021` score=0.685765 cov=0.051 section=中文复杂检索文档 > 背景材料1

### zh069 — zh_long_span_boundary_candidate
- question: would like的回答
- gold: `zh_doc_069.md > 关键材料`
- best_topk_coverage: 0.275
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_069.md::c0001` score=0.763741 cov=0.125 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_069.md::c0002` score=0.75795 cov=0.125 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_069.md::c0009` score=0.756531 cov=0.105 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_069.md::c0003` score=0.755048 cov=0.13 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_069.md::c0021` score=0.753039 cov=0.275 section=中文复杂检索文档 > 关键材料

### zh070 — zh_long_span_boundary_candidate
- question: qq经常掉线怎么回事
- gold: `zh_doc_070.md > 关键材料`
- best_topk_coverage: 0.476
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_070.md::c0004` score=0.793285 cov=0.476 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_070.md::c0003` score=0.78626 cov=0.204 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_070.md::c0008` score=0.783861 cov=0.177 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_070.md::c0018` score=0.783769 cov=0.125 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_070.md::c0019` score=0.77532 cov=0.067 section=中文复杂检索文档 > 补充材料2

### zh072 — zh_long_span_boundary_candidate
- question: 我的世界手机版0.12.1末地传送门怎么做
- gold: `zh_doc_072.md > 关键材料`
- best_topk_coverage: 0.358
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_072.md::c0005` score=0.797804 cov=0.358 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_072.md::c0013` score=0.793745 cov=0.176 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_072.md::c0004` score=0.790813 cov=0.163 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_072.md::c0012` score=0.784813 cov=0.195 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_072.md::c0011` score=0.776798 cov=0.199 section=中文复杂检索文档 > 补充材料1

### zh073 — zh_long_span_boundary_candidate
- question: 三壬行化妆学校好吗
- gold: `zh_doc_073.md > 关键材料`
- best_topk_coverage: 0.557
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_073.md::c0005` score=0.804533 cov=0.557 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_073.md::c0009` score=0.783882 cov=0.086 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_073.md::c0004` score=0.775237 cov=0.383 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_073.md::c0006` score=0.772691 cov=0.544 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_073.md::c0007` score=0.772398 cov=0.511 section=中文复杂检索文档 > 关键材料

### zh074 — zh_long_span_boundary_candidate
- question: 胃功能
- gold: `zh_doc_074.md > 关键材料`
- best_topk_coverage: 0.601
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_074.md::c0005` score=0.711229 cov=0.412 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_074.md::c0006` score=0.711209 cov=0.601 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_074.md::c0007` score=0.698295 cov=0.559 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_074.md::c0008` score=0.697907 cov=0.487 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_074.md::c0004` score=0.688329 cov=0.204 section=中文复杂检索文档 > 背景材料2

### zh075 — zh_long_span_boundary_candidate
- question: 艾俐缇陶瓷怎么样
- gold: `zh_doc_075.md > 关键材料`
- best_topk_coverage: 0.384
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_075.md::c0011` score=0.740568 cov=0.02 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_075.md::c0004` score=0.692823 cov=0.244 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_075.md::c0001` score=0.683349 cov=0.026 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_075.md::c0010` score=0.682324 cov=0.067 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_075.md::c0008` score=0.669624 cov=0.384 section=中文复杂检索文档 > 关键材料

### zh076 — zh_long_span_boundary_candidate
- question: 公共事业管理属于什么专业类别
- gold: `zh_doc_076.md > 关键材料`
- best_topk_coverage: 0.627
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_076.md::c0003` score=0.806903 cov=0.465 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_076.md::c0004` score=0.782774 cov=0.627 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_076.md::c0002` score=0.768819 cov=0.443 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_076.md::c0008` score=0.764195 cov=0.211 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_076.md::c0007` score=0.761998 cov=0.341 section=中文复杂检索文档 > 关键材料

### zh077 — zh_long_span_boundary_candidate
- question: 天然无添加的护肤品存在吗
- gold: `zh_doc_077.md > 关键材料`
- best_topk_coverage: 0.595
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_077.md::c0032` score=0.765612 cov=0.595 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_077.md::c0033` score=0.762698 cov=0.584 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_077.md::c0034` score=0.742637 cov=0.53 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_077.md::c0035` score=0.734916 cov=0.33 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_077.md::c0037` score=0.706349 cov=0.171 section=中文复杂检索文档 > 补充材料1

### zh078 — zh_long_span_boundary_candidate
- question: 旅行发票 可以报吗
- gold: `zh_doc_078.md > 关键材料`
- best_topk_coverage: 0.462
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_078.md::c0000` score=0.764365 cov=0.067 section=
  - rank 2: `zh_doc_078.md::c0008` score=0.756509 cov=0.462 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_078.md::c0001` score=0.748204 cov=0.113 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_078.md::c0009` score=0.745813 cov=0.129 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_078.md::c0004` score=0.724106 cov=0.349 section=中文复杂检索文档 > 背景材料2

### zh079 — zh_long_span_boundary_candidate
- question: 种子可以用百度云下载吗
- gold: `zh_doc_079.md > 关键材料`
- best_topk_coverage: 0.591
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_079.md::c0005` score=0.708832 cov=0.548 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_079.md::c0012` score=0.699713 cov=0.255 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_079.md::c0006` score=0.698036 cov=0.591 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_079.md::c0011` score=0.683756 cov=0.182 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_079.md::c0008` score=0.675344 cov=0.485 section=中文复杂检索文档 > 关键材料

### zh080 — zh_long_span_boundary_candidate
- question: ipad能否连接打印机
- gold: `zh_doc_080.md > 关键材料`
- best_topk_coverage: 0.556
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_080.md::c0015` score=0.741404 cov=0.556 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_080.md::c0000` score=0.735667 cov=0.206 section=
  - rank 3: `zh_doc_080.md::c0006` score=0.726428 cov=0.177 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_080.md::c0002` score=0.72108 cov=0.206 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_080.md::c0004` score=0.714664 cov=0.206 section=中文复杂检索文档 > 背景材料1

### zh081 — zh_long_span_boundary_candidate
- question: 手机钢化保护膜怎么贴
- gold: `zh_doc_081.md > 关键材料`
- best_topk_coverage: 0.593
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_081.md::c0024` score=0.786097 cov=0.593 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_027.md::c0016` score=0.778139 cov=0.0 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_081.md::c0004` score=0.762409 cov=0.127 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_081.md::c0011` score=0.753031 cov=0.155 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_027.md::c0015` score=0.750728 cov=0.0 section=中文复杂检索文档 > 关键材料

### zh082 — zh_long_span_boundary_candidate
- question: 中国古代最繁荣的朝代
- gold: `zh_doc_082.md > 关键材料`
- best_topk_coverage: 0.093
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_082.md::c0001` score=0.751638 cov=0.047 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_082.md::c0000` score=0.714721 cov=0.053 section=
  - rank 3: `zh_doc_082.md::c0013` score=0.695516 cov=0.072 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_082.md::c0012` score=0.671868 cov=0.075 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_082.md::c0002` score=0.669408 cov=0.093 section=中文复杂检索文档 > 背景材料1

### zh085 — zh_long_span_boundary_candidate
- question: 白带有酸奶味
- gold: `zh_doc_085.md > 关键材料`
- best_topk_coverage: 0.278
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_085.md::c0041` score=0.748206 cov=0.099 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_085.md::c0001` score=0.744474 cov=0.075 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_085.md::c0000` score=0.733913 cov=0.111 section=
  - rank 4: `zh_doc_085.md::c0040` score=0.732909 cov=0.099 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_085.md::c0028` score=0.727094 cov=0.278 section=中文复杂检索文档 > 关键材料

### zh086 — zh_long_span_boundary_candidate
- question: mathematica怎么求积分
- gold: `zh_doc_086.md > 关键材料`
- best_topk_coverage: 0.42
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_086.md::c0000` score=0.723876 cov=0.125 section=
  - rank 2: `zh_doc_086.md::c0007` score=0.711869 cov=0.42 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_086.md::c0003` score=0.693247 cov=0.138 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_086.md::c0001` score=0.690612 cov=0.098 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_086.md::c0006` score=0.687668 cov=0.116 section=中文复杂检索文档 > 背景材料2

### zh087 — zh_long_span_boundary_candidate
- question: 晾衣架材质
- gold: `zh_doc_087.md > 关键材料`
- best_topk_coverage: 0.542
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_087.md::c0010` score=0.788689 cov=0.304 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_087.md::c0009` score=0.766397 cov=0.119 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_087.md::c0007` score=0.758767 cov=0.137 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_087.md::c0011` score=0.746943 cov=0.542 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_087.md::c0015` score=0.741686 cov=0.116 section=中文复杂检索文档 > 补充材料1

### zh088 — zh_long_span_boundary_candidate
- question: 如何遮盖唇色
- gold: `zh_doc_088.md > 关键材料`
- best_topk_coverage: 0.599
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_088.md::c0004` score=0.75164 cov=0.599 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_088.md::c0003` score=0.724207 cov=0.413 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_088.md::c0002` score=0.697968 cov=0.162 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_088.md::c0000` score=0.660335 cov=0.12 section=
  - rank 5: `zh_doc_088.md::c0001` score=0.656613 cov=0.153 section=中文复杂检索文档 > 背景材料1

### zh089 — zh_long_span_boundary_candidate
- question: 部落冲突怎么搜死鱼
- gold: `zh_doc_089.md > 关键材料`
- best_topk_coverage: 0.556
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_089.md::c0000` score=0.799365 cov=0.092 section=
  - rank 2: `zh_doc_089.md::c0001` score=0.77906 cov=0.103 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_089.md::c0004` score=0.770466 cov=0.556 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_089.md::c0002` score=0.753357 cov=0.092 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_089.md::c0010` score=0.716396 cov=0.072 section=中文复杂检索文档 > 补充材料1

### zh090 — zh_long_span_boundary_candidate
- question: 牛剖层移膜皮是什么
- gold: `zh_doc_090.md > 关键材料`
- best_topk_coverage: 0.552
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_090.md::c0030` score=0.748833 cov=0.545 section=中文复杂检索文档 > 关键
  - rank 2: `zh_doc_090.md::c0031` score=0.722358 cov=0.552 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_090.md::c0018` score=0.711799 cov=0.11 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_090.md::c0032` score=0.707553 cov=0.502 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_090.md::c0002` score=0.699705 cov=0.125 section=中文复杂检索文档 > 背景材料1

### zh092 — zh_long_span_boundary_candidate
- question: 北京市公务员一年考几次
- gold: `zh_doc_092.md > 关键材料`
- best_topk_coverage: 0.544
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_092.md::c0013` score=0.752175 cov=0.544 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_092.md::c0010` score=0.739672 cov=0.511 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_092.md::c0016` score=0.739211 cov=0.384 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_092.md::c0003` score=0.735677 cov=0.298 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_092.md::c0008` score=0.733756 cov=0.328 section=中文复杂检索文档 > 背景材料2

### zh093 — zh_long_span_boundary_candidate
- question: 成都审驾照需要什么
- gold: `zh_doc_093.md > 关键材料`
- best_topk_coverage: 0.154
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_093.md::c0036` score=0.737019 cov=0.139 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_093.md::c0029` score=0.734262 cov=0.099 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_093.md::c0009` score=0.732534 cov=0.147 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_093.md::c0021` score=0.730621 cov=0.136 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_093.md::c0015` score=0.721677 cov=0.154 section=中文复杂检索文档 > 背景材料2

### zh094 — zh_long_span_boundary_candidate
- question: 霜是怎么形成的
- gold: `zh_doc_094.md > 关键材料`
- best_topk_coverage: 0.057
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_094.md::c0020` score=0.702547 cov=0.04 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_094.md::c0000` score=0.696477 cov=0.043 section=
  - rank 3: `zh_doc_094.md::c0021` score=0.68717 cov=0.034 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_094.md::c0003` score=0.63356 cov=0.045 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_094.md::c0002` score=0.632289 cov=0.057 section=中文复杂检索文档 > 背景材料1

### zh095 — zh_long_span_boundary_candidate
- question: 卫生间铺什么地砖好
- gold: `zh_doc_095.md > 关键材料`
- best_topk_coverage: 0.537
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_095.md::c0014` score=0.669792 cov=0.303 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_095.md::c0003` score=0.662025 cov=0.163 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_095.md::c0013` score=0.638402 cov=0.537 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_095.md::c0004` score=0.635004 cov=0.142 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_095.md::c0002` score=0.625661 cov=0.16 section=中文复杂检索文档 > 背景材料1

### zh096 — zh_long_span_boundary_candidate
- question: 肠结核的症状
- gold: `zh_doc_096.md > 关键材料`
- best_topk_coverage: 0.586
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_096.md::c0009` score=0.765153 cov=0.571 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_096.md::c0002` score=0.755022 cov=0.126 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_096.md::c0008` score=0.744631 cov=0.586 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_096.md::c0003` score=0.728316 cov=0.14 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_096.md::c0014` score=0.693982 cov=0.097 section=中文复杂检索文档 > 补充材料1

### zh097 — zh_long_span_boundary_candidate
- question: 表带怎么打孔
- gold: `zh_doc_097.md > 关键材料`
- best_topk_coverage: 0.526
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_097.md::c0010` score=0.780622 cov=0.221 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_097.md::c0008` score=0.757276 cov=0.526 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_097.md::c0001` score=0.749635 cov=0.099 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_097.md::c0015` score=0.744421 cov=0.064 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_097.md::c0005` score=0.735515 cov=0.119 section=中文复杂检索文档 > 背景材料2

### zh099 — zh_long_span_boundary_candidate
- question: 水土流失是什么意思
- gold: `zh_doc_099.md > 关键材料`
- best_topk_coverage: 0.615
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_099.md::c0041` score=0.711336 cov=0.615 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_099.md::c0040` score=0.701034 cov=0.365 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_099.md::c0053` score=0.665129 cov=0.497 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_099.md::c0000` score=0.656504 cov=0.147 section=
  - rank 5: `zh_doc_099.md::c0054` score=0.612723 cov=0.338 section=中文复杂检索文档 > 补充材料2

### zh100 — zh_long_span_boundary_candidate
- question: 红枣表面有层白色粉末
- gold: `zh_doc_100.md > 关键材料`
- best_topk_coverage: 0.586
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_100.md::c0007` score=0.829946 cov=0.396 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_100.md::c0006` score=0.796195 cov=0.586 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_100.md::c0008` score=0.796017 cov=0.141 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_100.md::c0012` score=0.794084 cov=0.057 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_100.md::c0011` score=0.782271 cov=0.066 section=中文复杂检索文档 > 补充材料1

### zh101 — zh_long_span_boundary_candidate
- question: 小米的平板好用吗
- gold: `zh_doc_101.md > 关键材料`
- best_topk_coverage: 0.574
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_101.md::c0019` score=0.777279 cov=0.574 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_101.md::c0002` score=0.729794 cov=0.066 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_101.md::c0029` score=0.711303 cov=0.044 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_101.md::c0024` score=0.703782 cov=0.088 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_101.md::c0000` score=0.696379 cov=0.096 section=

### zh102 — zh_long_span_boundary_candidate
- question: 尺神经麻痹治疗
- gold: `zh_doc_102.md > 关键材料`
- best_topk_coverage: 0.17
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_102.md::c0004` score=0.776246 cov=0.11 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_102.md::c0008` score=0.750097 cov=0.115 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_102.md::c0009` score=0.738457 cov=0.17 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_102.md::c0020` score=0.721967 cov=0.075 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_102.md::c0019` score=0.721713 cov=0.078 section=中文复杂检索文档 > 补充材料1

### zh103 — zh_long_span_boundary_candidate
- question: 北京出国体检在哪里
- gold: `zh_doc_103.md > 关键材料`
- best_topk_coverage: 0.616
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_103.md::c0007` score=0.802836 cov=0.566 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_103.md::c0008` score=0.799892 cov=0.616 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_103.md::c0013` score=0.790888 cov=0.308 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_103.md::c0010` score=0.780334 cov=0.417 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_103.md::c0001` score=0.779867 cov=0.222 section=中文复杂检索文档 > 背景材料1

### zh106 — zh_long_span_boundary_candidate
- question: 原地跑步能减肚子吗
- gold: `zh_doc_106.md > 关键材料`
- best_topk_coverage: 0.241
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_106.md::c0028` score=0.736181 cov=0.079 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_106.md::c0002` score=0.728593 cov=0.241 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_106.md::c0029` score=0.727269 cov=0.086 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_106.md::c0001` score=0.723479 cov=0.082 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_106.md::c0022` score=0.715898 cov=0.058 section=中文复杂检索文档 > 补充材料1

### zh107 — zh_long_span_boundary_candidate
- question: 金匮肾气丸要吃多长时间
- gold: `zh_doc_107.md > 关键材料`
- best_topk_coverage: 0.637
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_107.md::c0031` score=0.820321 cov=0.48 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_107.md::c0034` score=0.810509 cov=0.483 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_107.md::c0032` score=0.810144 cov=0.637 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_107.md::c0035` score=0.805513 cov=0.249 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_107.md::c0025` score=0.800969 cov=0.191 section=中文复杂检索文档 > 背景材料1

### zh108 — zh_long_span_boundary_candidate
- question: 肩颈僵硬
- gold: `zh_doc_108.md > 关键材料`
- best_topk_coverage: 0.573
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_108.md::c0000` score=0.729817 cov=0.045 section=
  - rank 2: `zh_doc_108.md::c0001` score=0.717911 cov=0.052 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_108.md::c0005` score=0.715644 cov=0.573 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_108.md::c0004` score=0.714687 cov=0.292 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_108.md::c0003` score=0.704364 cov=0.076 section=中文复杂检索文档 > 背景材料2

### zh110 — zh_long_span_boundary_candidate
- question: 完美世界出过什么游戏
- gold: `zh_doc_110.md > 关键材料`
- best_topk_coverage: 0.491
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_110.md::c0012` score=0.629423 cov=0.061 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_110.md::c0000` score=0.627388 cov=0.061 section=
  - rank 3: `zh_doc_110.md::c0001` score=0.58004 cov=0.079 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_110.md::c0011` score=0.560045 cov=0.067 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_110.md::c0005` score=0.557977 cov=0.491 section=中文复杂检索文档 > 背景材料2

### zh111 — zh_long_span_boundary_candidate
- question: 张家港大千装饰怎样
- gold: `zh_doc_111.md > 关键材料`
- best_topk_coverage: 0.507
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_111.md::c0004` score=0.785093 cov=0.483 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_111.md::c0000` score=0.765436 cov=0.216 section=
  - rank 3: `zh_doc_111.md::c0007` score=0.750063 cov=0.507 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_111.md::c0008` score=0.724241 cov=0.318 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_111.md::c0003` score=0.71186 cov=0.22 section=中文复杂检索文档 > 背景材料1

### zh112 — zh_long_span_boundary_candidate
- question: 为什么qq打不开图片
- gold: `zh_doc_112.md > 关键材料`
- best_topk_coverage: 0.613
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_112.md::c0007` score=0.759417 cov=0.459 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_112.md::c0005` score=0.755585 cov=0.613 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_112.md::c0008` score=0.743688 cov=0.142 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_112.md::c0012` score=0.720809 cov=0.106 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_112.md::c0004` score=0.716483 cov=0.338 section=中文复杂检索文档 > 背景材料2

### zh113 — zh_long_span_boundary_candidate
- question: 辅酶q10的服用方法
- gold: `zh_doc_113.md > 关键材料`
- best_topk_coverage: 0.16
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_113.md::c0004` score=0.781229 cov=0.113 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_113.md::c0015` score=0.769769 cov=0.127 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_113.md::c0017` score=0.762224 cov=0.127 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_113.md::c0005` score=0.759901 cov=0.131 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_113.md::c0014` score=0.75586 cov=0.16 section=中文复杂检索文档 > 关键材料

### zh117 — zh_long_span_boundary_candidate
- question: 德国红铁元和绿铁元有什么区别
- gold: `zh_doc_117.md > 关键材料`
- best_topk_coverage: 0.245
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_117.md::c0001` score=0.765831 cov=0.234 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_117.md::c0002` score=0.759632 cov=0.192 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_117.md::c0004` score=0.75443 cov=0.245 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_117.md::c0003` score=0.748432 cov=0.224 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_117.md::c0011` score=0.736702 cov=0.224 section=中文复杂检索文档 > 补充材料1

### zh118 — zh_long_span_boundary_candidate
- question: 诛仙法宝技能怎么洗
- gold: `zh_doc_118.md > 关键材料`
- best_topk_coverage: 0.433
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_118.md::c0007` score=0.731133 cov=0.433 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_118.md::c0001` score=0.713277 cov=0.061 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_118.md::c0010` score=0.709283 cov=0.084 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_118.md::c0002` score=0.704592 cov=0.053 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_118.md::c0000` score=0.702288 cov=0.046 section=

### zh119 — zh_long_span_boundary_candidate
- question: 神秘博士clara是谁
- gold: `zh_doc_119.md > 关键材料`
- best_topk_coverage: 0.553
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_119.md::c0006` score=0.755995 cov=0.553 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_119.md::c0004` score=0.72172 cov=0.504 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_119.md::c0000` score=0.71033 cov=0.045 section=
  - rank 4: `zh_doc_119.md::c0003` score=0.699536 cov=0.162 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_119.md::c0005` score=0.68005 cov=0.534 section=中文复杂检索文档 > 背景材料2

### zh120 — zh_long_span_boundary_candidate
- question: 保妇康栓要用多久
- gold: `zh_doc_120.md > 关键材料`
- best_topk_coverage: 0.409
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_120.md::c0003` score=0.766716 cov=0.228 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_120.md::c0001` score=0.765311 cov=0.29 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_120.md::c0002` score=0.761964 cov=0.228 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_120.md::c0000` score=0.755642 cov=0.264 section=
  - rank 5: `zh_doc_120.md::c0004` score=0.718427 cov=0.409 section=中文复杂检索文档 > 背景材料2

## All Query Summary

| qid | expected type | success | rank | best cov | gold rank hint |
|---|---|---:|---:|---:|---:|
| zh001 | zh_long_span_boundary_candidate | False | None | 0.646 | 1 |
| zh002 | zh_long_span_boundary_candidate | False | None | 0.267 | 1 |
| zh003 | zh_long_span_boundary_candidate | False | None | 0.222 | 1 |
| zh004 | zh_long_span_boundary_candidate | False | None | 0.277 | 1 |
| zh005 | zh_long_span_boundary_candidate | False | None | 0.371 | 1 |
| zh006 | zh_long_span_boundary_candidate | False | None | 0.357 | 1 |
| zh007 | zh_long_span_boundary_candidate | False | None | 0.335 | 1 |
| zh008 | zh_long_span_boundary_candidate | False | None | 0.275 | 1 |
| zh009 | zh_long_span_boundary_candidate | False | None | 0.42 | 1 |
| zh010 | zh_long_span_boundary_candidate | False | None | 0.065 | 1 |
| zh011 | zh_long_span_boundary_candidate | False | None | 0.173 | 1 |
| zh012 | zh_long_span_boundary_candidate | False | None | 0.112 | 1 |
| zh013 | zh_long_span_boundary_candidate | False | None | 0.373 | 1 |
| zh014 | zh_long_span_boundary_candidate | False | None | 0.38 | 1 |
| zh015 | zh_long_span_boundary_candidate | False | None | 0.433 | 1 |
| zh016 | zh_long_span_boundary_candidate | False | None | 0.391 | 1 |
| zh017 | zh_long_span_boundary_candidate | False | None | 0.234 | 1 |
| zh018 | zh_long_span_boundary_candidate | False | None | 0.375 | 1 |
| zh019 | zh_long_span_boundary_candidate | False | None | 0.481 | 1 |
| zh020 | zh_long_span_boundary_candidate | False | None | 0.3 | 1 |
| zh021 | zh_long_span_boundary_candidate | False | None | 0.335 | 1 |
| zh022 | zh_long_span_boundary_candidate | False | None | 0.391 | 1 |
| zh023 | zh_long_span_boundary_candidate | False | None | 0.503 | 1 |
| zh024 | zh_long_span_boundary_candidate | False | None | 0.382 | 1 |
| zh025 | zh_long_span_boundary_candidate | False | None | 0.347 | 1 |
| zh026 | zh_long_span_boundary_candidate | False | None | 0.56 | 1 |
| zh027 | zh_long_span_boundary_candidate | False | None | 0.078 | 1 |
| zh028 | zh_long_span_boundary_candidate | False | None | 0.403 | 1 |
| zh029 | zh_long_span_boundary_candidate | False | None | 0.342 | 1 |
| zh030 | zh_long_span_boundary_candidate | False | None | 0.262 | 1 |
| zh031 | zh_long_span_boundary_candidate | False | None | 0.483 | 1 |
| zh032 | zh_long_span_boundary_candidate | False | None | 0.324 | 1 |
| zh033 | zh_long_span_boundary_candidate | False | None | 0.325 | 1 |
| zh034 | zh_long_span_boundary_candidate | False | None | 0.433 | 1 |
| zh035 | zh_long_span_boundary_candidate | False | None | 0.432 | 1 |
| zh036 | zh_long_span_boundary_candidate | False | None | 0.591 | 1 |
| zh037 | zh_long_span_boundary_candidate | False | None | 0.438 | 1 |
| zh038 | zh_long_span_boundary_candidate | False | None | 0.315 | 1 |
| zh039 | zh_long_span_boundary_candidate | False | None | 0.302 | 1 |
| zh040 | zh_long_span_boundary_candidate | False | None | 0.137 | 1 |
| zh041 | zh_long_span_boundary_candidate | False | None | 0.44 | 1 |
| zh042 | zh_long_span_boundary_candidate | False | None | 0.408 | 1 |
| zh043 | zh_long_span_boundary_candidate | False | None | 0.47 | 1 |
| zh044 | zh_long_span_boundary_candidate | False | None | 0.276 | 1 |
| zh045 | zh_long_span_boundary_candidate | False | None | 0.581 | 1 |
| zh046 | zh_long_span_boundary_candidate | False | None | 0.121 | 1 |
| zh047 | zh_long_span_boundary_candidate | False | None | 0.576 | 1 |
| zh048 | zh_long_span_boundary_candidate | False | None | 0.405 | 1 |
| zh049 | zh_long_span_boundary_candidate | False | None | 0.548 | 1 |
| zh050 | zh_long_span_boundary_candidate | False | None | 0.462 | 1 |
| zh051 | zh_long_span_boundary_candidate | False | None | 0.551 | 1 |
| zh052 | zh_long_span_boundary_candidate | False | None | 0.525 | 1 |
| zh053 | zh_long_span_boundary_candidate | False | None | 0.164 | 1 |
| zh054 | zh_long_span_boundary_candidate | False | None | 0.599 | 1 |
| zh055 | zh_long_span_boundary_candidate | False | None | 0.535 | 1 |
| zh056 | zh_long_span_boundary_candidate | False | None | 0.53 | 1 |
| zh057 | zh_long_span_boundary_candidate | False | None | 0.166 | 1 |
| zh058 | zh_long_span_boundary_candidate | True | 1 | 0.697 | 1 |
| zh059 | zh_long_span_boundary_candidate | False | None | 0.637 | 1 |
| zh060 | zh_long_span_boundary_candidate | False | None | 0.327 | 1 |
| zh061 | zh_long_span_boundary_candidate | False | None | 0.342 | 1 |
| zh062 | zh_long_span_boundary_candidate | False | None | 0.253 | 1 |
| zh063 | zh_long_span_boundary_candidate | False | None | 0.49 | 1 |
| zh064 | zh_long_span_boundary_candidate | False | None | 0.639 | 1 |
| zh065 | zh_long_span_boundary_candidate | False | None | 0.571 | 1 |
| zh066 | zh_long_span_boundary_candidate | False | None | 0.582 | 1 |
| zh067 | zh_long_span_boundary_candidate | False | None | 0.354 | 1 |
| zh068 | zh_long_span_boundary_candidate | False | None | 0.517 | 1 |
| zh069 | zh_long_span_boundary_candidate | False | None | 0.275 | 1 |
| zh070 | zh_long_span_boundary_candidate | False | None | 0.476 | 1 |
| zh071 | zh_long_span_boundary_candidate | True | 1 | 0.669 | 1 |
| zh072 | zh_long_span_boundary_candidate | False | None | 0.358 | 1 |
| zh073 | zh_long_span_boundary_candidate | False | None | 0.557 | 1 |
| zh074 | zh_long_span_boundary_candidate | False | None | 0.601 | 1 |
| zh075 | zh_long_span_boundary_candidate | False | None | 0.384 | 1 |
| zh076 | zh_long_span_boundary_candidate | False | None | 0.627 | 1 |
| zh077 | zh_long_span_boundary_candidate | False | None | 0.595 | 1 |
| zh078 | zh_long_span_boundary_candidate | False | None | 0.462 | 1 |
| zh079 | zh_long_span_boundary_candidate | False | None | 0.591 | 1 |
| zh080 | zh_long_span_boundary_candidate | False | None | 0.556 | 1 |
| zh081 | zh_long_span_boundary_candidate | False | None | 0.593 | 1 |
| zh082 | zh_long_span_boundary_candidate | False | None | 0.093 | 1 |
| zh083 | zh_long_span_boundary_candidate | True | 2 | 0.696 | 1 |
| zh084 | zh_long_span_boundary_candidate | True | 1 | 0.74 | 1 |
| zh085 | zh_long_span_boundary_candidate | False | None | 0.278 | 1 |
| zh086 | zh_long_span_boundary_candidate | False | None | 0.42 | 1 |
| zh087 | zh_long_span_boundary_candidate | False | None | 0.542 | 1 |
| zh088 | zh_long_span_boundary_candidate | False | None | 0.599 | 1 |
| zh089 | zh_long_span_boundary_candidate | False | None | 0.556 | 1 |
| zh090 | zh_long_span_boundary_candidate | False | None | 0.552 | 1 |
| zh091 | zh_long_span_boundary_candidate | True | 1 | 0.664 | 1 |
| zh092 | zh_long_span_boundary_candidate | False | None | 0.544 | 1 |
| zh093 | zh_long_span_boundary_candidate | False | None | 0.154 | 1 |
| zh094 | zh_long_span_boundary_candidate | False | None | 0.057 | 1 |
| zh095 | zh_long_span_boundary_candidate | False | None | 0.537 | 1 |
| zh096 | zh_long_span_boundary_candidate | False | None | 0.586 | 1 |
| zh097 | zh_long_span_boundary_candidate | False | None | 0.526 | 1 |
| zh098 | zh_long_span_boundary_candidate | True | 1 | 0.696 | 1 |
| zh099 | zh_long_span_boundary_candidate | False | None | 0.615 | 1 |
| zh100 | zh_long_span_boundary_candidate | False | None | 0.586 | 1 |
| zh101 | zh_long_span_boundary_candidate | False | None | 0.574 | 1 |
| zh102 | zh_long_span_boundary_candidate | False | None | 0.17 | 1 |
| zh103 | zh_long_span_boundary_candidate | False | None | 0.616 | 1 |
| zh104 | zh_long_span_boundary_candidate | True | 5 | 0.726 | 1 |
| zh105 | zh_long_span_boundary_candidate | True | 1 | 0.672 | 1 |
| zh106 | zh_long_span_boundary_candidate | False | None | 0.241 | 1 |
| zh107 | zh_long_span_boundary_candidate | False | None | 0.637 | 1 |
| zh108 | zh_long_span_boundary_candidate | False | None | 0.573 | 1 |
| zh109 | zh_long_span_boundary_candidate | True | 2 | 0.678 | 1 |
| zh110 | zh_long_span_boundary_candidate | False | None | 0.491 | 1 |
| zh111 | zh_long_span_boundary_candidate | False | None | 0.507 | 1 |
| zh112 | zh_long_span_boundary_candidate | False | None | 0.613 | 1 |
| zh113 | zh_long_span_boundary_candidate | False | None | 0.16 | 1 |
| zh114 | zh_long_span_boundary_candidate | True | 1 | 0.669 | 1 |
| zh115 | zh_long_span_boundary_candidate | True | 3 | 0.692 | 1 |
| zh116 | zh_long_span_boundary_candidate | True | 2 | 0.771 | 1 |
| zh117 | zh_long_span_boundary_candidate | False | None | 0.245 | 1 |
| zh118 | zh_long_span_boundary_candidate | False | None | 0.433 | 1 |
| zh119 | zh_long_span_boundary_candidate | False | None | 0.553 | 1 |
| zh120 | zh_long_span_boundary_candidate | False | None | 0.409 | 1 |
