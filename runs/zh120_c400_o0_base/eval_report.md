# Baseline Retrieval Report

## Config

- **docs**: `case_zh_dureader_120/docs`
- **questions**: `case_zh_dureader_120/eval/questions_patch_source.jsonl`
- **chunk_size**: `400`
- **overlap**: `0`
- **keep_heading**: `True`
- **top_k**: `5`
- **coverage_threshold**: `0.65`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`

## Metrics

- **total**: 120
- **recall@5**: 0.5750
- **mrr**: 0.3279
- **hits**: 69
- **failed**: 51
- **coverage_threshold**: 0.6500

## Failed Queries

### zh002 — zh_long_span_boundary_candidate
- question: 空气净化器哪种净化方式好
- gold: `zh_doc_002.md > 关键材料`
- best_topk_coverage: 0.416
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_002.md::c0003` score=0.711625 cov=0.409 section=中文复杂检索文档 > 关
  - rank 2: `zh_doc_002.md::c0001` score=0.711355 cov=0.201 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_002.md::c0000` score=0.707085 cov=0.184 section=
  - rank 4: `zh_doc_002.md::c0006` score=0.677525 cov=0.223 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_002.md::c0004` score=0.65132 cov=0.416 section=中文复杂检索文档 > 关键材料

### zh003 — zh_long_span_boundary_candidate
- question: 黄山风景古诗赞
- gold: `zh_doc_003.md > 关键材料`
- best_topk_coverage: 0.356
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_003.md::c0005` score=0.632158 cov=0.037 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_003.md::c0003` score=0.628075 cov=0.344 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_003.md::c0002` score=0.618128 cov=0.356 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_003.md::c0001` score=0.608304 cov=0.116 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_003.md::c0004` score=0.575998 cov=0.334 section=中文复杂检索文档 > 关键材料

### zh004 — zh_long_span_boundary_candidate
- question: 一天放很多屁
- gold: `zh_doc_004.md > 关键材料`
- best_topk_coverage: 0.431
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_004.md::c0001` score=0.711854 cov=0.078 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_004.md::c0012` score=0.706551 cov=0.431 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_004.md::c0011` score=0.703064 cov=0.373 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_004.md::c0000` score=0.702522 cov=0.105 section=
  - rank 5: `zh_doc_004.md::c0006` score=0.691073 cov=0.079 section=中文复杂检索文档 > 背景材料1

### zh005 — zh_long_span_boundary_candidate
- question: 叉车有几种
- gold: `zh_doc_005.md > 关键材料`
- best_topk_coverage: 0.528
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_005.md::c0008` score=0.757776 cov=0.466 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_005.md::c0009` score=0.731599 cov=0.481 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_005.md::c0010` score=0.73131 cov=0.528 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_005.md::c0013` score=0.696323 cov=0.11 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_005.md::c0000` score=0.691924 cov=0.457 section=

### zh006 — zh_long_span_boundary_candidate
- question: 春光成语
- gold: `zh_doc_006.md > 关键材料`
- best_topk_coverage: 0.523
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_006.md::c0004` score=0.751909 cov=0.451 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_006.md::c0002` score=0.745288 cov=0.523 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_006.md::c0001` score=0.736543 cov=0.31 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_006.md::c0000` score=0.687245 cov=0.162 section=
  - rank 5: `zh_doc_006.md::c0005` score=0.680866 cov=0.224 section=中文复杂检索文档 > 补充材料1

### zh007 — zh_long_span_boundary_candidate
- question: 经常用肥皂洗脸好吗
- gold: `zh_doc_007.md > 关键材料`
- best_topk_coverage: 0.413
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_007.md::c0006` score=0.797595 cov=0.137 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_007.md::c0005` score=0.774475 cov=0.152 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_007.md::c0001` score=0.760555 cov=0.165 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_007.md::c0002` score=0.757015 cov=0.413 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_007.md::c0000` score=0.732686 cov=0.168 section=

### zh008 — zh_long_span_boundary_candidate
- question: 冬天怎样养鹦鹉
- gold: `zh_doc_008.md > 关键材料`
- best_topk_coverage: 0.429
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_008.md::c0002` score=0.704235 cov=0.319 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_008.md::c0005` score=0.692075 cov=0.202 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_008.md::c0001` score=0.691483 cov=0.072 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_008.md::c0006` score=0.682045 cov=0.097 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_008.md::c0003` score=0.608856 cov=0.429 section=中文复杂检索文档 > 关键材料

### zh009 — zh_long_span_boundary_candidate
- question: 附睾肿胀
- gold: `zh_doc_009.md > 关键材料`
- best_topk_coverage: 0.572
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_009.md::c0003` score=0.753068 cov=0.456 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_009.md::c0007` score=0.728522 cov=0.107 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_009.md::c0004` score=0.696806 cov=0.572 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_009.md::c0005` score=0.684253 cov=0.566 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_009.md::c0006` score=0.679609 cov=0.154 section=中文复杂检索文档 > 补充

### zh010 — zh_long_span_boundary_candidate
- question: 硫磺皂能长期用吗
- gold: `zh_doc_010.md > 关键材料`
- best_topk_coverage: 0.448
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_010.md::c0004` score=0.781663 cov=0.171 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_010.md::c0005` score=0.774989 cov=0.078 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_010.md::c0000` score=0.739096 cov=0.072 section=
  - rank 4: `zh_doc_010.md::c0001` score=0.707306 cov=0.229 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_010.md::c0002` score=0.668995 cov=0.448 section=中文复杂检索文档 > 关键材料

### zh011 — zh_long_span_boundary_candidate
- question: 比较好看的电视剧
- gold: `zh_doc_011.md > 关键材料`
- best_topk_coverage: 0.471
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_011.md::c0005` score=0.623771 cov=0.026 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_011.md::c0000` score=0.567997 cov=0.094 section=
  - rank 3: `zh_doc_011.md::c0001` score=0.552383 cov=0.247 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_011.md::c0004` score=0.537734 cov=0.127 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_011.md::c0003` score=0.487226 cov=0.471 section=中文复杂检索文档 > 关键材料

### zh012 — zh_long_span_boundary_candidate
- question: 夏天喝什么饮品好
- gold: `zh_doc_012.md > 关键材料`
- best_topk_coverage: 0.578
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_012.md::c0000` score=0.651067 cov=0.142 section=
  - rank 2: `zh_doc_012.md::c0004` score=0.614288 cov=0.111 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_012.md::c0001` score=0.607507 cov=0.486 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_012.md::c0003` score=0.606043 cov=0.488 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_012.md::c0002` score=0.565051 cov=0.578 section=中文复杂检索文档 > 关键材料

### zh013 — zh_long_span_boundary_candidate
- question: workgroup是什么
- gold: `zh_doc_013.md > 关键材料`
- best_topk_coverage: 0.523
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_013.md::c0000` score=0.673989 cov=0.163 section=
  - rank 2: `zh_doc_013.md::c0003` score=0.512785 cov=0.523 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_013.md::c0004` score=0.493083 cov=0.072 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_013.md::c0005` score=0.480139 cov=0.106 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_013.md::c0009` score=0.476416 cov=0.104 section=中文复杂检索文档 > 补充材料1

### zh014 — zh_long_span_boundary_candidate
- question: 怎样锻炼肺活量
- gold: `zh_doc_014.md > 关键材料`
- best_topk_coverage: 0.507
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_014.md::c0006` score=0.709121 cov=0.118 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_014.md::c0000` score=0.707348 cov=0.169 section=
  - rank 3: `zh_doc_014.md::c0001` score=0.702455 cov=0.147 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_014.md::c0005` score=0.688656 cov=0.473 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_014.md::c0003` score=0.681403 cov=0.507 section=中文复杂检索文档 > 关键材料

### zh015 — zh_long_span_boundary_candidate
- question: 做胃镜注意
- gold: `zh_doc_015.md > 关键材料`
- best_topk_coverage: 0.583
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_015.md::c0003` score=0.726172 cov=0.583 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_015.md::c0004` score=0.725124 cov=0.517 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_015.md::c0002` score=0.66455 cov=0.194 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_015.md::c0005` score=0.64178 cov=0.179 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_015.md::c0006` score=0.641746 cov=0.113 section=中文复杂检索文档 > 补充材料1

### zh016 — zh_long_span_boundary_candidate
- question: 油电混合动力汽车购置税优惠吗
- gold: `zh_doc_016.md > 关键材料`
- best_topk_coverage: 0.628
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_016.md::c0003` score=0.791211 cov=0.538 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_016.md::c0005` score=0.756819 cov=0.628 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_016.md::c0006` score=0.748715 cov=0.345 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_016.md::c0004` score=0.748006 cov=0.609 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_016.md::c0002` score=0.746411 cov=0.394 section=中文复杂检索文档 > 背景材料1

### zh017 — zh_long_span_boundary_candidate
- question: 阴部变白
- gold: `zh_doc_017.md > 关键材料`
- best_topk_coverage: 0.536
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_017.md::c0000` score=0.702403 cov=0.076 section=
  - rank 2: `zh_doc_017.md::c0005` score=0.679193 cov=0.034 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_017.md::c0001` score=0.669556 cov=0.039 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_017.md::c0002` score=0.661145 cov=0.536 section=中文复杂检索文档 > 关键
  - rank 5: `zh_doc_017.md::c0004` score=0.623233 cov=0.188 section=中文复杂检索文档 > 关键材料

### zh020 — zh_long_span_boundary_candidate
- question: 私立大学和公立大学的区别
- gold: `zh_doc_020.md > 关键材料`
- best_topk_coverage: 0.456
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_020.md::c0006` score=0.800076 cov=0.456 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_020.md::c0008` score=0.785251 cov=0.071 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_020.md::c0007` score=0.77346 cov=0.119 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_020.md::c0001` score=0.767396 cov=0.11 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_020.md::c0000` score=0.757833 cov=0.113 section=

### zh021 — zh_long_span_boundary_candidate
- question: 如何调水表数字
- gold: `zh_doc_021.md > 关键材料`
- best_topk_coverage: 0.462
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_021.md::c0003` score=0.810636 cov=0.462 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_021.md::c0001` score=0.683072 cov=0.081 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_021.md::c0005` score=0.681208 cov=0.249 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_021.md::c0007` score=0.659652 cov=0.074 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_021.md::c0006` score=0.654836 cov=0.077 section=中文复杂检索文档 > 补充材料1

### zh022 — zh_long_span_boundary_candidate
- question: 怎样种香菜
- gold: `zh_doc_022.md > 关键材料`
- best_topk_coverage: 0.414
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_022.md::c0009` score=0.712762 cov=0.119 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_022.md::c0006` score=0.697272 cov=0.414 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_022.md::c0000` score=0.687842 cov=0.139 section=
  - rank 4: `zh_doc_022.md::c0008` score=0.683771 cov=0.38 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_022.md::c0001` score=0.681011 cov=0.221 section=中文复杂检索文档 > 背景材料1

### zh023 — zh_long_span_boundary_candidate
- question: 如何把电脑上的东西传到ipad上
- gold: `zh_doc_023.md > 关键材料`
- best_topk_coverage: 0.577
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_023.md::c0002` score=0.787246 cov=0.577 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_023.md::c0005` score=0.764443 cov=0.209 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_023.md::c0004` score=0.750548 cov=0.303 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_023.md::c0000` score=0.733359 cov=0.223 section=
  - rank 5: `zh_doc_023.md::c0001` score=0.731721 cov=0.162 section=中文复杂检索文档 > 背景材料2

### zh024 — zh_long_span_boundary_candidate
- question: c1扣12分怎么办
- gold: `zh_doc_024.md > 关键材料`
- best_topk_coverage: 0.494
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_024.md::c0006` score=0.793075 cov=0.307 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_024.md::c0001` score=0.783903 cov=0.494 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_024.md::c0002` score=0.782215 cov=0.337 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_024.md::c0000` score=0.754707 cov=0.291 section=
  - rank 5: `zh_doc_024.md::c0005` score=0.742999 cov=0.436 section=中文复杂检索文档 > 补充材料1

### zh025 — zh_long_span_boundary_candidate
- question: tf与sd卡的区别
- gold: `zh_doc_025.md > 关键材料`
- best_topk_coverage: 0.614
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_025.md::c0000` score=0.808512 cov=0.258 section=
  - rank 2: `zh_doc_025.md::c0007` score=0.807486 cov=0.542 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_025.md::c0004` score=0.807018 cov=0.52 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_025.md::c0005` score=0.806403 cov=0.588 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_025.md::c0008` score=0.802557 cov=0.614 section=中文复杂检索文档 > 补充材料1

### zh027 — zh_long_span_boundary_candidate
- question: 小米平板钢化膜怎么贴
- gold: `zh_doc_027.md > 关键材料`
- best_topk_coverage: 0.105
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_027.md::c0005` score=0.756379 cov=0.096 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_027.md::c0006` score=0.703079 cov=0.01 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_081.md::c0003` score=0.678025 cov=0.0 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_081.md::c0001` score=0.667689 cov=0.0 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_027.md::c0000` score=0.666691 cov=0.105 section=

### zh028 — zh_long_span_boundary_candidate
- question: 怎么控制路由器把蹭wifi的人给踢了
- gold: `zh_doc_028.md > 关键材料`
- best_topk_coverage: 0.567
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_028.md::c0001` score=0.788116 cov=0.567 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_028.md::c0003` score=0.763031 cov=0.451 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_028.md::c0000` score=0.751935 cov=0.194 section=
  - rank 4: `zh_doc_028.md::c0004` score=0.684436 cov=0.211 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_028.md::c0005` score=0.663564 cov=0.132 section=中文复杂检索文档 > 补充材料2

### zh030 — zh_long_span_boundary_candidate
- question: 外伤缝针不能吃什么
- gold: `zh_doc_030.md > 关键材料`
- best_topk_coverage: 0.577
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_030.md::c0001` score=0.716614 cov=0.268 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_030.md::c0000` score=0.711916 cov=0.24 section=
  - rank 3: `zh_doc_030.md::c0005` score=0.707345 cov=0.577 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_030.md::c0006` score=0.696865 cov=0.191 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_030.md::c0002` score=0.694622 cov=0.307 section=中文复杂检索文档 > 背景材料2

### zh032 — zh_long_span_boundary_candidate
- question: 杭州劳动仲裁电话
- gold: `zh_doc_032.md > 关键材料`
- best_topk_coverage: 0.444
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_032.md::c0001` score=0.762557 cov=0.444 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_032.md::c0009` score=0.739388 cov=0.215 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_032.md::c0008` score=0.73097 cov=0.202 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_032.md::c0003` score=0.729464 cov=0.274 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_032.md::c0004` score=0.709549 cov=0.29 section=中文复杂检索文档 > 补充材料1

### zh033 — zh_long_span_boundary_candidate
- question: 电暖桌哪个牌子好
- gold: `zh_doc_033.md > 关键材料`
- best_topk_coverage: 0.558
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_033.md::c0002` score=0.779842 cov=0.558 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_033.md::c0006` score=0.766752 cov=0.131 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_033.md::c0004` score=0.76287 cov=0.101 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_033.md::c0005` score=0.761909 cov=0.093 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_033.md::c0007` score=0.758355 cov=0.04 section=中文复杂检索文档 > 补充材料2

### zh039 — zh_long_span_boundary_candidate
- question: 跟庐山有关的诗句
- gold: `zh_doc_039.md > 关键材料`
- best_topk_coverage: 0.635
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_039.md::c0003` score=0.710166 cov=0.108 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_039.md::c0001` score=0.707727 cov=0.501 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_039.md::c0002` score=0.692305 cov=0.635 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_039.md::c0000` score=0.679982 cov=0.068 section=
  - rank 5: `zh_doc_003.md::c0003` score=0.588906 cov=0.0 section=中文复杂检索文档 > 关键材料

### zh044 — zh_long_span_boundary_candidate
- question: 换外汇哪个银行好
- gold: `zh_doc_044.md > 关键材料`
- best_topk_coverage: 0.559
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_044.md::c0000` score=0.82836 cov=0.127 section=
  - rank 2: `zh_doc_044.md::c0001` score=0.77462 cov=0.552 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_044.md::c0003` score=0.755294 cov=0.299 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_044.md::c0004` score=0.748744 cov=0.559 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_050.md::c0001` score=0.670055 cov=0.0 section=中文复杂检索文档 > 背景材料2

### zh045 — zh_long_span_boundary_candidate
- question: 轻型羽绒服什么牌子好
- gold: `zh_doc_045.md > 关键材料`
- best_topk_coverage: 0.624
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_045.md::c0000` score=0.637518 cov=0.157 section=
  - rank 2: `zh_doc_045.md::c0006` score=0.629798 cov=0.137 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_045.md::c0004` score=0.626735 cov=0.14 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_045.md::c0002` score=0.623327 cov=0.624 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_045.md::c0007` score=0.623068 cov=0.105 section=中文复杂检索文档 > 补充材料2

### zh046 — zh_long_span_boundary_candidate
- question: 手机外放进水
- gold: `zh_doc_046.md > 关键材料`
- best_topk_coverage: 0.644
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_046.md::c0003` score=0.744629 cov=0.541 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_046.md::c0002` score=0.725259 cov=0.644 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_046.md::c0000` score=0.725138 cov=0.16 section=
  - rank 4: `zh_doc_046.md::c0001` score=0.724513 cov=0.131 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_046.md::c0004` score=0.696883 cov=0.119 section=中文复杂检索文档 > 补充材料1

### zh051 — zh_long_span_boundary_candidate
- question: 双人床最小宽度
- gold: `zh_doc_051.md > 关键材料`
- best_topk_coverage: 0.641
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_051.md::c0000` score=0.750193 cov=0.084 section=
  - rank 2: `zh_doc_051.md::c0004` score=0.747571 cov=0.609 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_051.md::c0005` score=0.739726 cov=0.641 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_051.md::c0001` score=0.723334 cov=0.142 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_051.md::c0008` score=0.714044 cov=0.159 section=中文复杂检索文档 > 补充材料2

### zh052 — zh_long_span_boundary_candidate
- question: 生气时喂奶
- gold: `zh_doc_052.md > 关键材料`
- best_topk_coverage: 0.648
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_052.md::c0004` score=0.784415 cov=0.108 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_052.md::c0002` score=0.751537 cov=0.648 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_052.md::c0001` score=0.733968 cov=0.599 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_052.md::c0003` score=0.706312 cov=0.22 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_052.md::c0000` score=0.704325 cov=0.565 section=

### zh056 — zh_long_span_boundary_candidate
- question: 尸兄主角能力
- gold: `zh_doc_056.md > 关键材料`
- best_topk_coverage: 0.363
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_056.md::c0005` score=0.680796 cov=0.112 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_056.md::c0004` score=0.678593 cov=0.139 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_056.md::c0002` score=0.669676 cov=0.363 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_056.md::c0001` score=0.647982 cov=0.087 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_056.md::c0000` score=0.645714 cov=0.072 section=

### zh057 — zh_long_span_boundary_candidate
- question: word怎么不能修改
- gold: `zh_doc_057.md > 关键材料`
- best_topk_coverage: 0.403
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_057.md::c0000` score=0.735138 cov=0.166 section=
  - rank 2: `zh_doc_057.md::c0006` score=0.71752 cov=0.115 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_057.md::c0008` score=0.712869 cov=0.403 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_057.md::c0011` score=0.699355 cov=0.2 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_057.md::c0010` score=0.697497 cov=0.276 section=中文复杂检索文档 > 关键材料

### zh060 — zh_long_span_boundary_candidate
- question: 氨端聚二甲基硅氧烷是硅油吗
- gold: `zh_doc_060.md > 关键材料`
- best_topk_coverage: 0.206
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_060.md::c0007` score=0.658574 cov=0.113 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_060.md::c0000` score=0.630606 cov=0.206 section=
  - rank 3: `zh_doc_060.md::c0009` score=0.61356 cov=0.179 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_060.md::c0008` score=0.61252 cov=0.106 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_060.md::c0002` score=0.592631 cov=0.155 section=中文复杂检索文档 > 背景材料2

### zh062 — zh_long_span_boundary_candidate
- question: 如何取消电脑的自动休眠
- gold: `zh_doc_062.md > 关键材料`
- best_topk_coverage: 0.471
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_062.md::c0003` score=0.805086 cov=0.471 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_062.md::c0000` score=0.769439 cov=0.221 section=
  - rank 3: `zh_doc_062.md::c0002` score=0.759898 cov=0.291 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_062.md::c0006` score=0.743822 cov=0.238 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_062.md::c0007` score=0.713107 cov=0.171 section=中文复杂检索文档 > 补充材料2

### zh067 — zh_long_span_boundary_candidate
- question: 武松属什么
- gold: `zh_doc_067.md > 关键材料`
- best_topk_coverage: 0.646
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_067.md::c0002` score=0.695659 cov=0.646 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_067.md::c0000` score=0.628509 cov=0.018 section=
  - rank 3: `zh_doc_067.md::c0004` score=0.601148 cov=0.018 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_067.md::c0001` score=0.561191 cov=0.012 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_067.md::c0003` score=0.514031 cov=0.375 section=中文复杂检索文档 > 关键材料

### zh071 — zh_long_span_boundary_candidate
- question: 还珠格格第一部背景音乐
- gold: `zh_doc_071.md > 关键材料`
- best_topk_coverage: 0.387
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_071.md::c0001` score=0.637402 cov=0.258 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_071.md::c0007` score=0.620019 cov=0.185 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_071.md::c0009` score=0.607714 cov=0.387 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_071.md::c0002` score=0.605722 cov=0.317 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_071.md::c0000` score=0.571891 cov=0.348 section=

### zh073 — zh_long_span_boundary_candidate
- question: 三壬行化妆学校好吗
- gold: `zh_doc_073.md > 关键材料`
- best_topk_coverage: 0.617
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_073.md::c0002` score=0.813038 cov=0.617 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_073.md::c0001` score=0.792519 cov=0.587 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_073.md::c0000` score=0.742997 cov=0.091 section=
  - rank 4: `zh_doc_073.md::c0003` score=0.678619 cov=0.081 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_068.md::c0003` score=0.501456 cov=0.0 section=中文复杂检索文档 > 背景材料1

### zh082 — zh_long_span_boundary_candidate
- question: 中国古代最繁荣的朝代
- gold: `zh_doc_082.md > 关键材料`
- best_topk_coverage: 0.645
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_082.md::c0000` score=0.715936 cov=0.106 section=
  - rank 2: `zh_doc_082.md::c0003` score=0.666671 cov=0.084 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_082.md::c0004` score=0.660453 cov=0.087 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_082.md::c0002` score=0.637734 cov=0.645 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_082.md::c0001` score=0.628461 cov=0.502 section=中文复杂检索文档 > 背景材料2

### zh085 — zh_long_span_boundary_candidate
- question: 白带有酸奶味
- gold: `zh_doc_085.md > 关键材料`
- best_topk_coverage: 0.647
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_085.md::c0000` score=0.754353 cov=0.138 section=
  - rank 2: `zh_doc_085.md::c0012` score=0.750942 cov=0.111 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_085.md::c0008` score=0.698584 cov=0.647 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_085.md::c0002` score=0.69683 cov=0.144 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_085.md::c0003` score=0.695779 cov=0.117 section=中文复杂检索文档 > 背景材料2

### zh087 — zh_long_span_boundary_candidate
- question: 晾衣架材质
- gold: `zh_doc_087.md > 关键材料`
- best_topk_coverage: 0.649
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_087.md::c0003` score=0.763472 cov=0.649 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_087.md::c0004` score=0.743272 cov=0.488 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_087.md::c0002` score=0.736877 cov=0.152 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_087.md::c0005` score=0.692694 cov=0.217 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_087.md::c0000` score=0.675871 cov=0.125 section=

### zh093 — zh_long_span_boundary_candidate
- question: 成都审驾照需要什么
- gold: `zh_doc_093.md > 关键材料`
- best_topk_coverage: 0.205
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_093.md::c0008` score=0.736263 cov=0.205 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_093.md::c0002` score=0.73553 cov=0.176 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_093.md::c0009` score=0.724611 cov=0.205 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_093.md::c0011` score=0.711707 cov=0.04 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_093.md::c0000` score=0.708966 cov=0.19 section=

### zh101 — zh_long_span_boundary_candidate
- question: 小米的平板好用吗
- gold: `zh_doc_101.md > 关键材料`
- best_topk_coverage: 0.588
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_101.md::c0005` score=0.767461 cov=0.518 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_101.md::c0008` score=0.719296 cov=0.103 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_101.md::c0000` score=0.719063 cov=0.121 section=
  - rank 4: `zh_doc_101.md::c0006` score=0.694057 cov=0.588 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_101.md::c0003` score=0.691818 cov=0.103 section=中文复杂检索文档 > 背景材料1

### zh106 — zh_long_span_boundary_candidate
- question: 原地跑步能减肚子吗
- gold: `zh_doc_106.md > 关键材料`
- best_topk_coverage: 0.131
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_106.md::c0000` score=0.716439 cov=0.131 section=
  - rank 2: `zh_doc_106.md::c0008` score=0.711926 cov=0.093 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_106.md::c0002` score=0.702437 cov=0.107 section=中文复杂检索文档 > 补
  - rank 4: `zh_doc_106.md::c0003` score=0.702102 cov=0.076 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_106.md::c0009` score=0.701956 cov=0.103 section=中文复杂检索文档 > 补充材料2

### zh108 — zh_long_span_boundary_candidate
- question: 肩颈僵硬
- gold: `zh_doc_108.md > 关键材料`
- best_topk_coverage: 0.576
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_108.md::c0001` score=0.734703 cov=0.531 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_108.md::c0000` score=0.718627 cov=0.073 section=
  - rank 3: `zh_doc_108.md::c0003` score=0.673293 cov=0.083 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_108.md::c0004` score=0.652272 cov=0.104 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_108.md::c0002` score=0.635282 cov=0.576 section=中文复杂检索文档 > 关键材料

### zh110 — zh_long_span_boundary_candidate
- question: 完美世界出过什么游戏
- gold: `zh_doc_110.md > 关键材料`
- best_topk_coverage: 0.646
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_110.md::c0000` score=0.606625 cov=0.091 section=
  - rank 2: `zh_doc_110.md::c0002` score=0.5936 cov=0.646 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_110.md::c0001` score=0.57059 cov=0.463 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_110.md::c0003` score=0.541599 cov=0.067 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_011.md::c0003` score=0.444865 cov=0.0 section=中文复杂检索文档 > 关键材料

### zh112 — zh_long_span_boundary_candidate
- question: 为什么qq打不开图片
- gold: `zh_doc_112.md > 关键材料`
- best_topk_coverage: 0.589
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_112.md::c0004` score=0.761196 cov=0.069 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_112.md::c0001` score=0.71449 cov=0.589 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_112.md::c0003` score=0.710216 cov=0.112 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_112.md::c0000` score=0.689369 cov=0.127 section=
  - rank 5: `zh_doc_112.md::c0002` score=0.664599 cov=0.538 section=中文复杂检索文档 > 关键材料

### zh118 — zh_long_span_boundary_candidate
- question: 诛仙法宝技能怎么洗
- gold: `zh_doc_118.md > 关键材料`
- best_topk_coverage: 0.635
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_118.md::c0003` score=0.738848 cov=0.137 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_118.md::c0002` score=0.709068 cov=0.536 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_118.md::c0000` score=0.70249 cov=0.076 section=
  - rank 4: `zh_doc_118.md::c0001` score=0.686402 cov=0.635 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_118.md::c0004` score=0.523759 cov=0.008 section=中文复杂检索文档 > 补充材料2

### zh120 — zh_long_span_boundary_candidate
- question: 保妇康栓要用多久
- gold: `zh_doc_120.md > 关键材料`
- best_topk_coverage: 0.627
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_120.md::c0000` score=0.769763 cov=0.337 section=
  - rank 2: `zh_doc_120.md::c0001` score=0.762879 cov=0.612 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_120.md::c0002` score=0.730356 cov=0.627 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_120.md::c0003` score=0.699948 cov=0.207 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_107.md::c0007` score=0.502908 cov=0.0 section=中文复杂检索文档 > 背景材料1

## All Query Summary

| qid | expected type | success | rank | best cov | gold rank hint |
|---|---|---:|---:|---:|---:|
| zh001 | zh_long_span_boundary_candidate | True | 2 | 0.668 | 1 |
| zh002 | zh_long_span_boundary_candidate | False | None | 0.416 | 1 |
| zh003 | zh_long_span_boundary_candidate | False | None | 0.356 | 1 |
| zh004 | zh_long_span_boundary_candidate | False | None | 0.431 | 1 |
| zh005 | zh_long_span_boundary_candidate | False | None | 0.528 | 1 |
| zh006 | zh_long_span_boundary_candidate | False | None | 0.523 | 1 |
| zh007 | zh_long_span_boundary_candidate | False | None | 0.413 | 1 |
| zh008 | zh_long_span_boundary_candidate | False | None | 0.429 | 1 |
| zh009 | zh_long_span_boundary_candidate | False | None | 0.572 | 1 |
| zh010 | zh_long_span_boundary_candidate | False | None | 0.448 | 1 |
| zh011 | zh_long_span_boundary_candidate | False | None | 0.471 | 1 |
| zh012 | zh_long_span_boundary_candidate | False | None | 0.578 | 1 |
| zh013 | zh_long_span_boundary_candidate | False | None | 0.523 | 1 |
| zh014 | zh_long_span_boundary_candidate | False | None | 0.507 | 1 |
| zh015 | zh_long_span_boundary_candidate | False | None | 0.583 | 1 |
| zh016 | zh_long_span_boundary_candidate | False | None | 0.628 | 1 |
| zh017 | zh_long_span_boundary_candidate | False | None | 0.536 | 1 |
| zh018 | zh_long_span_boundary_candidate | True | 1 | 0.685 | 1 |
| zh019 | zh_long_span_boundary_candidate | True | 3 | 0.788 | 1 |
| zh020 | zh_long_span_boundary_candidate | False | None | 0.456 | 1 |
| zh021 | zh_long_span_boundary_candidate | False | None | 0.462 | 1 |
| zh022 | zh_long_span_boundary_candidate | False | None | 0.414 | 1 |
| zh023 | zh_long_span_boundary_candidate | False | None | 0.577 | 1 |
| zh024 | zh_long_span_boundary_candidate | False | None | 0.494 | 1 |
| zh025 | zh_long_span_boundary_candidate | False | None | 0.614 | 1 |
| zh026 | zh_long_span_boundary_candidate | True | 2 | 0.681 | 1 |
| zh027 | zh_long_span_boundary_candidate | False | None | 0.105 | 1 |
| zh028 | zh_long_span_boundary_candidate | False | None | 0.567 | 1 |
| zh029 | zh_long_span_boundary_candidate | True | 3 | 0.705 | 1 |
| zh030 | zh_long_span_boundary_candidate | False | None | 0.577 | 1 |
| zh031 | zh_long_span_boundary_candidate | True | 5 | 0.759 | 1 |
| zh032 | zh_long_span_boundary_candidate | False | None | 0.444 | 1 |
| zh033 | zh_long_span_boundary_candidate | False | None | 0.558 | 1 |
| zh034 | zh_long_span_boundary_candidate | True | 5 | 0.668 | 1 |
| zh035 | zh_long_span_boundary_candidate | True | 4 | 0.721 | 1 |
| zh036 | zh_long_span_boundary_candidate | True | 1 | 0.657 | 1 |
| zh037 | zh_long_span_boundary_candidate | True | 4 | 0.693 | 1 |
| zh038 | zh_long_span_boundary_candidate | True | 3 | 0.691 | 1 |
| zh039 | zh_long_span_boundary_candidate | False | None | 0.635 | 1 |
| zh040 | zh_long_span_boundary_candidate | True | 5 | 0.728 | 1 |
| zh041 | zh_long_span_boundary_candidate | True | 2 | 0.797 | 1 |
| zh042 | zh_long_span_boundary_candidate | True | 5 | 0.703 | 1 |
| zh043 | zh_long_span_boundary_candidate | True | 1 | 0.907 | 1 |
| zh044 | zh_long_span_boundary_candidate | False | None | 0.559 | 1 |
| zh045 | zh_long_span_boundary_candidate | False | None | 0.624 | 1 |
| zh046 | zh_long_span_boundary_candidate | False | None | 0.644 | 1 |
| zh047 | zh_long_span_boundary_candidate | True | 4 | 0.787 | 1 |
| zh048 | zh_long_span_boundary_candidate | True | 3 | 0.735 | 1 |
| zh049 | zh_long_span_boundary_candidate | True | 3 | 0.804 | 1 |
| zh050 | zh_long_span_boundary_candidate | True | 4 | 0.77 | 1 |
| zh051 | zh_long_span_boundary_candidate | False | None | 0.641 | 1 |
| zh052 | zh_long_span_boundary_candidate | False | None | 0.648 | 1 |
| zh053 | zh_long_span_boundary_candidate | True | 5 | 0.787 | 1 |
| zh054 | zh_long_span_boundary_candidate | True | 3 | 0.784 | 1 |
| zh055 | zh_long_span_boundary_candidate | True | 1 | 0.816 | 1 |
| zh056 | zh_long_span_boundary_candidate | False | None | 0.363 | 1 |
| zh057 | zh_long_span_boundary_candidate | False | None | 0.403 | 1 |
| zh058 | zh_long_span_boundary_candidate | True | 1 | 1.0 | 1 |
| zh059 | zh_long_span_boundary_candidate | True | 1 | 0.834 | 1 |
| zh060 | zh_long_span_boundary_candidate | False | None | 0.206 | 1 |
| zh061 | zh_long_span_boundary_candidate | True | 5 | 0.785 | 1 |
| zh062 | zh_long_span_boundary_candidate | False | None | 0.471 | 1 |
| zh063 | zh_long_span_boundary_candidate | True | 3 | 0.854 | 1 |
| zh064 | zh_long_span_boundary_candidate | True | 1 | 0.82 | 1 |
| zh065 | zh_long_span_boundary_candidate | True | 2 | 0.67 | 1 |
| zh066 | zh_long_span_boundary_candidate | True | 4 | 0.71 | 1 |
| zh067 | zh_long_span_boundary_candidate | False | None | 0.646 | 1 |
| zh068 | zh_long_span_boundary_candidate | True | 2 | 0.697 | 1 |
| zh069 | zh_long_span_boundary_candidate | True | 4 | 0.745 | 1 |
| zh070 | zh_long_span_boundary_candidate | True | 4 | 0.707 | 1 |
| zh071 | zh_long_span_boundary_candidate | False | None | 0.387 | 1 |
| zh072 | zh_long_span_boundary_candidate | True | 4 | 0.883 | 1 |
| zh073 | zh_long_span_boundary_candidate | False | None | 0.617 | 1 |
| zh074 | zh_long_span_boundary_candidate | True | 2 | 0.791 | 1 |
| zh075 | zh_long_span_boundary_candidate | True | 3 | 0.677 | 1 |
| zh076 | zh_long_span_boundary_candidate | True | 1 | 0.833 | 1 |
| zh077 | zh_long_span_boundary_candidate | True | 1 | 0.735 | 1 |
| zh078 | zh_long_span_boundary_candidate | True | 3 | 0.75 | 1 |
| zh079 | zh_long_span_boundary_candidate | True | 1 | 0.697 | 1 |
| zh080 | zh_long_span_boundary_candidate | True | 1 | 0.733 | 1 |
| zh081 | zh_long_span_boundary_candidate | True | 1 | 0.901 | 1 |
| zh082 | zh_long_span_boundary_candidate | False | None | 0.645 | 1 |
| zh083 | zh_long_span_boundary_candidate | True | 1 | 0.897 | 1 |
| zh084 | zh_long_span_boundary_candidate | True | 1 | 0.866 | 1 |
| zh085 | zh_long_span_boundary_candidate | False | None | 0.647 | 1 |
| zh086 | zh_long_span_boundary_candidate | True | 5 | 0.79 | 1 |
| zh087 | zh_long_span_boundary_candidate | False | None | 0.649 | 1 |
| zh088 | zh_long_span_boundary_candidate | True | 1 | 0.781 | 1 |
| zh089 | zh_long_span_boundary_candidate | True | 2 | 0.711 | 1 |
| zh090 | zh_long_span_boundary_candidate | True | 1 | 0.918 | 1 |
| zh091 | zh_long_span_boundary_candidate | True | 2 | 0.877 | 1 |
| zh092 | zh_long_span_boundary_candidate | True | 1 | 0.902 | 1 |
| zh093 | zh_long_span_boundary_candidate | False | None | 0.205 | 1 |
| zh094 | zh_long_span_boundary_candidate | True | 3 | 0.884 | 1 |
| zh095 | zh_long_span_boundary_candidate | True | 4 | 0.706 | 1 |
| zh096 | zh_long_span_boundary_candidate | True | 1 | 0.711 | 1 |
| zh097 | zh_long_span_boundary_candidate | True | 2 | 0.884 | 1 |
| zh098 | zh_long_span_boundary_candidate | True | 1 | 0.826 | 1 |
| zh099 | zh_long_span_boundary_candidate | True | 1 | 0.741 | 1 |
| zh100 | zh_long_span_boundary_candidate | True | 3 | 0.661 | 1 |
| zh101 | zh_long_span_boundary_candidate | False | None | 0.588 | 1 |
| zh102 | zh_long_span_boundary_candidate | True | 3 | 0.867 | 1 |
| zh103 | zh_long_span_boundary_candidate | True | 1 | 0.858 | 1 |
| zh104 | zh_long_span_boundary_candidate | True | 5 | 0.863 | 1 |
| zh105 | zh_long_span_boundary_candidate | True | 1 | 0.898 | 1 |
| zh106 | zh_long_span_boundary_candidate | False | None | 0.131 | 1 |
| zh107 | zh_long_span_boundary_candidate | True | 1 | 0.671 | 1 |
| zh108 | zh_long_span_boundary_candidate | False | None | 0.576 | 1 |
| zh109 | zh_long_span_boundary_candidate | True | 1 | 0.94 | 1 |
| zh110 | zh_long_span_boundary_candidate | False | None | 0.646 | 1 |
| zh111 | zh_long_span_boundary_candidate | True | 1 | 0.706 | 1 |
| zh112 | zh_long_span_boundary_candidate | False | None | 0.589 | 1 |
| zh113 | zh_long_span_boundary_candidate | True | 3 | 0.811 | 1 |
| zh114 | zh_long_span_boundary_candidate | True | 3 | 0.765 | 1 |
| zh115 | zh_long_span_boundary_candidate | True | 4 | 0.722 | 1 |
| zh116 | zh_long_span_boundary_candidate | True | 2 | 0.932 | 1 |
| zh117 | zh_long_span_boundary_candidate | True | 4 | 0.766 | 1 |
| zh118 | zh_long_span_boundary_candidate | False | None | 0.635 | 1 |
| zh119 | zh_long_span_boundary_candidate | True | 3 | 0.865 | 1 |
| zh120 | zh_long_span_boundary_candidate | False | None | 0.627 | 1 |
