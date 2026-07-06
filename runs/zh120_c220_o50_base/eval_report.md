# Baseline Retrieval Report

## Config

- **docs**: `case_zh_dureader_120/docs`
- **questions**: `case_zh_dureader_120/eval/questions_patch_source.jsonl`
- **chunk_size**: `220`
- **overlap**: `50`
- **keep_heading**: `True`
- **top_k**: `5`
- **coverage_threshold**: `0.65`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`

## Metrics

- **total**: 120
- **recall@5**: 0.0917
- **mrr**: 0.0475
- **hits**: 11
- **failed**: 109
- **coverage_threshold**: 0.6500

## Failed Queries

### zh001 — zh_long_span_boundary_candidate
- question: 高速公路超速20以上不足50扣几分
- gold: `zh_doc_001.md > 关键材料`
- best_topk_coverage: 0.547
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_001.md::c0015` score=0.798784 cov=0.547 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_001.md::c0049` score=0.790286 cov=0.429 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_001.md::c0027` score=0.787532 cov=0.359 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_001.md::c0014` score=0.787017 cov=0.35 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_001.md::c0035` score=0.778142 cov=0.364 section=中文复杂检索文档 > 补充材料1

### zh002 — zh_long_span_boundary_candidate
- question: 空气净化器哪种净化方式好
- gold: `zh_doc_002.md > 关键材料`
- best_topk_coverage: 0.264
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_002.md::c0007` score=0.728084 cov=0.264 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_002.md::c0004` score=0.712365 cov=0.15 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_002.md::c0001` score=0.710192 cov=0.134 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_002.md::c0002` score=0.700583 cov=0.112 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_002.md::c0000` score=0.688329 cov=0.139 section=

### zh003 — zh_long_span_boundary_candidate
- question: 黄山风景古诗赞
- gold: `zh_doc_003.md > 关键材料`
- best_topk_coverage: 0.211
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_003.md::c0012` score=0.66983 cov=0.033 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_003.md::c0008` score=0.649258 cov=0.211 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_003.md::c0006` score=0.642356 cov=0.206 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_003.md::c0004` score=0.63456 cov=0.192 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_003.md::c0007` score=0.62877 cov=0.193 section=中文复杂检索文档 > 关键材料

### zh004 — zh_long_span_boundary_candidate
- question: 一天放很多屁
- gold: `zh_doc_004.md > 关键材料`
- best_topk_coverage: 0.256
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_004.md::c0027` score=0.728063 cov=0.256 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_004.md::c0003` score=0.716317 cov=0.054 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_004.md::c0019` score=0.715067 cov=0.23 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_004.md::c0000` score=0.711929 cov=0.084 section=
  - rank 5: `zh_doc_004.md::c0002` score=0.699273 cov=0.063 section=中文复杂检索文档 > 背景材料1

### zh005 — zh_long_span_boundary_candidate
- question: 叉车有几种
- gold: `zh_doc_005.md > 关键材料`
- best_topk_coverage: 0.367
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_005.md::c0020` score=0.754724 cov=0.367 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_005.md::c0019` score=0.753611 cov=0.254 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_005.md::c0023` score=0.745096 cov=0.366 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_005.md::c0030` score=0.738996 cov=0.107 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_005.md::c0022` score=0.726236 cov=0.318 section=中文复杂检索文档 > 关键材料

### zh006 — zh_long_span_boundary_candidate
- question: 春光成语
- gold: `zh_doc_006.md > 关键材料`
- best_topk_coverage: 0.386
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_006.md::c0010` score=0.761691 cov=0.272 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_006.md::c0005` score=0.737132 cov=0.336 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_006.md::c0004` score=0.716377 cov=0.298 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_006.md::c0006` score=0.711014 cov=0.386 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_006.md::c0012` score=0.699529 cov=0.2 section=中文复杂检索文档 > 补充材料1

### zh007 — zh_long_span_boundary_candidate
- question: 经常用肥皂洗脸好吗
- gold: `zh_doc_007.md > 关键材料`
- best_topk_coverage: 0.314
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_007.md::c0014` score=0.793166 cov=0.139 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_007.md::c0006` score=0.772962 cov=0.314 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_007.md::c0013` score=0.763366 cov=0.105 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_007.md::c0012` score=0.758503 cov=0.114 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_007.md::c0003` score=0.757627 cov=0.128 section=中文复杂检索文档 > 背景材料1

### zh008 — zh_long_span_boundary_candidate
- question: 冬天怎样养鹦鹉
- gold: `zh_doc_008.md > 关键材料`
- best_topk_coverage: 0.282
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_008.md::c0004` score=0.717434 cov=0.06 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_008.md::c0014` score=0.711735 cov=0.099 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_008.md::c0005` score=0.695179 cov=0.156 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_008.md::c0003` score=0.694081 cov=0.061 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_008.md::c0006` score=0.668121 cov=0.282 section=中文复杂检索文档 > 关键材料

### zh009 — zh_long_span_boundary_candidate
- question: 附睾肿胀
- gold: `zh_doc_009.md > 关键材料`
- best_topk_coverage: 0.444
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_009.md::c0008` score=0.765268 cov=0.398 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_009.md::c0007` score=0.754173 cov=0.289 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_009.md::c0016` score=0.745107 cov=0.116 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_009.md::c0017` score=0.738028 cov=0.092 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_009.md::c0009` score=0.729414 cov=0.444 section=中文复杂检索文档 > 关键材料

### zh010 — zh_long_span_boundary_candidate
- question: 硫磺皂能长期用吗
- gold: `zh_doc_010.md > 关键材料`
- best_topk_coverage: 0.057
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_010.md::c0010` score=0.783066 cov=0.046 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_010.md::c0011` score=0.780968 cov=0.056 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_010.md::c0012` score=0.77396 cov=0.057 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_010.md::c0000` score=0.764083 cov=0.054 section=
  - rank 5: `zh_doc_010.md::c0013` score=0.710962 cov=0.057 section=中文复杂检索文档 > 补充材料2

### zh011 — zh_long_span_boundary_candidate
- question: 比较好看的电视剧
- gold: `zh_doc_011.md > 关键材料`
- best_topk_coverage: 0.2
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_011.md::c0000` score=0.618039 cov=0.078 section=
  - rank 2: `zh_doc_011.md::c0012` score=0.615748 cov=0.026 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_011.md::c0011` score=0.608845 cov=0.033 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_011.md::c0009` score=0.583629 cov=0.2 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_011.md::c0010` score=0.578786 cov=0.034 section=中文复杂检索文档 > 补充材料1

### zh012 — zh_long_span_boundary_candidate
- question: 夏天喝什么饮品好
- gold: `zh_doc_012.md > 关键材料`
- best_topk_coverage: 0.368
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_012.md::c0000` score=0.653822 cov=0.112 section=
  - rank 2: `zh_doc_012.md::c0001` score=0.638064 cov=0.104 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_012.md::c0003` score=0.636665 cov=0.368 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_012.md::c0009` score=0.626694 cov=0.087 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_012.md::c0011` score=0.594028 cov=0.085 section=中文复杂检索文档 > 补充材料1

### zh013 — zh_long_span_boundary_candidate
- question: workgroup是什么
- gold: `zh_doc_013.md > 关键材料`
- best_topk_coverage: 0.304
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_013.md::c0000` score=0.707351 cov=0.093 section=
  - rank 2: `zh_doc_013.md::c0001` score=0.629034 cov=0.141 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_013.md::c0008` score=0.528831 cov=0.304 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_013.md::c0010` score=0.492872 cov=0.07 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_013.md::c0011` score=0.486784 cov=0.047 section=中文复杂检索文档 > 补充材料1

### zh014 — zh_long_span_boundary_candidate
- question: 怎样锻炼肺活量
- gold: `zh_doc_014.md > 关键材料`
- best_topk_coverage: 0.341
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_014.md::c0012` score=0.723591 cov=0.253 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_014.md::c0015` score=0.722627 cov=0.074 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_014.md::c0008` score=0.715987 cov=0.341 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_014.md::c0007` score=0.715128 cov=0.322 section=中文复杂检索文档 > 关
  - rank 5: `zh_doc_014.md::c0014` score=0.704144 cov=0.124 section=中文复杂检索文档 > 补充材料1

### zh015 — zh_long_span_boundary_candidate
- question: 做胃镜注意
- gold: `zh_doc_015.md > 关键材料`
- best_topk_coverage: 0.443
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_015.md::c0007` score=0.706079 cov=0.443 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_015.md::c0010` score=0.693097 cov=0.332 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_015.md::c0011` score=0.689547 cov=0.229 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_015.md::c0009` score=0.688933 cov=0.286 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_015.md::c0013` score=0.681348 cov=0.075 section=中文复杂检索文档 > 补充材料1

### zh016 — zh_long_span_boundary_candidate
- question: 油电混合动力汽车购置税优惠吗
- gold: `zh_doc_016.md > 关键材料`
- best_topk_coverage: 0.399
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_016.md::c0008` score=0.792376 cov=0.385 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_016.md::c0010` score=0.778618 cov=0.398 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_016.md::c0013` score=0.767977 cov=0.399 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_016.md::c0007` score=0.75102 cov=0.394 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_016.md::c0005` score=0.748809 cov=0.274 section=中文复杂检索文档 > 背景材料1

### zh017 — zh_long_span_boundary_candidate
- question: 阴部变白
- gold: `zh_doc_017.md > 关键材料`
- best_topk_coverage: 0.356
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_017.md::c0004` score=0.700588 cov=0.162 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_017.md::c0013` score=0.693999 cov=0.025 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_017.md::c0006` score=0.684328 cov=0.356 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_017.md::c0000` score=0.680065 cov=0.036 section=
  - rank 5: `zh_doc_017.md::c0012` score=0.663119 cov=0.024 section=中文复杂检索文档 > 补充材料2

### zh018 — zh_long_span_boundary_candidate
- question: 如何买卖etf基金
- gold: `zh_doc_018.md > 关键材料`
- best_topk_coverage: 0.406
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_018.md::c0005` score=0.764168 cov=0.406 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_018.md::c0004` score=0.750387 cov=0.305 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_018.md::c0011` score=0.742363 cov=0.15 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_018.md::c0000` score=0.730025 cov=0.176 section=
  - rank 5: `zh_doc_018.md::c0002` score=0.720062 cov=0.14 section=中文复杂检索文档 > 背景材料1

### zh019 — zh_long_span_boundary_candidate
- question: 在实习期内的驾驶证扣分会怎样
- gold: `zh_doc_019.md > 关键材料`
- best_topk_coverage: 0.649
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_019.md::c0011` score=0.802466 cov=0.413 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_019.md::c0010` score=0.78263 cov=0.426 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_019.md::c0013` score=0.78018 cov=0.291 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_019.md::c0012` score=0.777944 cov=0.416 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_019.md::c0007` score=0.7599 cov=0.649 section=中文复杂检索文档 > 关键材料

### zh020 — zh_long_span_boundary_candidate
- question: 私立大学和公立大学的区别
- gold: `zh_doc_020.md > 关键材料`
- best_topk_coverage: 0.217
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_020.md::c0015` score=0.7996 cov=0.217 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_020.md::c0016` score=0.786962 cov=0.087 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_020.md::c0017` score=0.776061 cov=0.096 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_020.md::c0001` score=0.774019 cov=0.094 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_020.md::c0004` score=0.764117 cov=0.101 section=中文复杂检索文档 > 背景材料2

### zh021 — zh_long_span_boundary_candidate
- question: 如何调水表数字
- gold: `zh_doc_021.md > 关键材料`
- best_topk_coverage: 0.385
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_021.md::c0007` score=0.82115 cov=0.211 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_021.md::c0006` score=0.748823 cov=0.015 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_021.md::c0008` score=0.720412 cov=0.321 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_021.md::c0009` score=0.716339 cov=0.385 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_021.md::c0015` score=0.682509 cov=0.055 section=中文复杂检索文档 > 补充材料1

### zh022 — zh_long_span_boundary_candidate
- question: 怎样种香菜
- gold: `zh_doc_022.md > 关键材料`
- best_topk_coverage: 0.186
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_022.md::c0020` score=0.707329 cov=0.106 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_022.md::c0021` score=0.706137 cov=0.093 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_022.md::c0002` score=0.699466 cov=0.095 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_022.md::c0023` score=0.698339 cov=0.085 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_022.md::c0003` score=0.69038 cov=0.186 section=中文复杂检索文档 > 背景材料1

### zh023 — zh_long_span_boundary_candidate
- question: 如何把电脑上的东西传到ipad上
- gold: `zh_doc_023.md > 关键材料`
- best_topk_coverage: 0.38
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_023.md::c0005` score=0.788307 cov=0.38 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_023.md::c0011` score=0.753114 cov=0.186 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_023.md::c0001` score=0.751813 cov=0.125 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_023.md::c0002` score=0.745883 cov=0.104 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_023.md::c0004` score=0.742199 cov=0.112 section=中文复杂检索文档 > 背景材料2

### zh024 — zh_long_span_boundary_candidate
- question: c1扣12分怎么办
- gold: `zh_doc_024.md > 关键材料`
- best_topk_coverage: 0.407
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_024.md::c0015` score=0.810068 cov=0.119 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_024.md::c0006` score=0.794243 cov=0.215 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_024.md::c0003` score=0.783571 cov=0.331 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_024.md::c0013` score=0.771056 cov=0.407 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_024.md::c0001` score=0.770937 cov=0.25 section=中文复杂检索文档 > 背景材料1

### zh025 — zh_long_span_boundary_candidate
- question: tf与sd卡的区别
- gold: `zh_doc_025.md > 关键材料`
- best_topk_coverage: 0.347
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_025.md::c0013` score=0.834158 cov=0.333 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_025.md::c0014` score=0.819989 cov=0.328 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_025.md::c0018` score=0.814253 cov=0.347 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_025.md::c0023` score=0.809916 cov=0.277 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_025.md::c0009` score=0.80509 cov=0.34 section=中文复杂检索文档 > 背景材料2

### zh026 — zh_long_span_boundary_candidate
- question: 左肾部位疼痛
- gold: `zh_doc_026.md > 关键材料`
- best_topk_coverage: 0.63
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_026.md::c0004` score=0.802002 cov=0.427 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_026.md::c0006` score=0.78153 cov=0.63 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_026.md::c0005` score=0.781084 cov=0.482 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_026.md::c0000` score=0.751057 cov=0.125 section=
  - rank 5: `zh_doc_026.md::c0001` score=0.737709 cov=0.106 section=中文复杂检索文档 > 背景材料1

### zh027 — zh_long_span_boundary_candidate
- question: 小米平板钢化膜怎么贴
- gold: `zh_doc_027.md > 关键材料`
- best_topk_coverage: 0.145
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_027.md::c0012` score=0.779979 cov=0.078 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_027.md::c0013` score=0.713508 cov=0.037 section=中文复杂检索文档 > 补充
  - rank 3: `zh_doc_027.md::c0014` score=0.694968 cov=0.01 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_027.md::c0011` score=0.673527 cov=0.145 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_081.md::c0003` score=0.670335 cov=0.0 section=中文复杂检索文档 > 背景材料1

### zh028 — zh_long_span_boundary_candidate
- question: 怎么控制路由器把蹭wifi的人给踢了
- gold: `zh_doc_028.md > 关键材料`
- best_topk_coverage: 0.417
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_028.md::c0003` score=0.780045 cov=0.37 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_028.md::c0001` score=0.748929 cov=0.185 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_028.md::c0007` score=0.748082 cov=0.417 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_028.md::c0002` score=0.734773 cov=0.183 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_028.md::c0008` score=0.728947 cov=0.178 section=中文复杂检索文档 > 补充材料1

### zh029 — zh_long_span_boundary_candidate
- question: 怎么做卫浴销售
- gold: `zh_doc_029.md > 关键材料`
- best_topk_coverage: 0.531
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_029.md::c0003` score=0.75652 cov=0.051 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_029.md::c0001` score=0.731459 cov=0.091 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_029.md::c0000` score=0.700068 cov=0.065 section=
  - rank 4: `zh_doc_029.md::c0005` score=0.693718 cov=0.531 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_029.md::c0004` score=0.675422 cov=0.295 section=中文复杂检索文档 > 背景材料2

### zh030 — zh_long_span_boundary_candidate
- question: 外伤缝针不能吃什么
- gold: `zh_doc_030.md > 关键材料`
- best_topk_coverage: 0.285
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_030.md::c0015` score=0.719026 cov=0.171 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_030.md::c0003` score=0.718701 cov=0.114 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_030.md::c0013` score=0.712914 cov=0.285 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_030.md::c0000` score=0.702306 cov=0.136 section=
  - rank 5: `zh_doc_030.md::c0002` score=0.700168 cov=0.268 section=中文复杂检索文档 > 背景材料2

### zh031 — zh_long_span_boundary_candidate
- question: 超级会员是什么
- gold: `zh_doc_031.md > 关键材料`
- best_topk_coverage: 0.522
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_031.md::c0004` score=0.710419 cov=0.522 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_031.md::c0007` score=0.686428 cov=0.384 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_031.md::c0009` score=0.685726 cov=0.244 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_031.md::c0003` score=0.677762 cov=0.338 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_031.md::c0008` score=0.653871 cov=0.237 section=中文复杂检索文档 > 补充材料1

### zh032 — zh_long_span_boundary_candidate
- question: 杭州劳动仲裁电话
- gold: `zh_doc_032.md > 关键材料`
- best_topk_coverage: 0.352
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_032.md::c0003` score=0.777695 cov=0.352 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_032.md::c0021` score=0.763819 cov=0.122 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_032.md::c0008` score=0.743846 cov=0.122 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_032.md::c0009` score=0.73925 cov=0.173 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_032.md::c0002` score=0.736555 cov=0.05 section=中文复杂检索文档 > 背景材料2

### zh033 — zh_long_span_boundary_candidate
- question: 电暖桌哪个牌子好
- gold: `zh_doc_033.md > 关键材料`
- best_topk_coverage: 0.335
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_033.md::c0005` score=0.802844 cov=0.335 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_033.md::c0002` score=0.778131 cov=0.107 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_033.md::c0009` score=0.772853 cov=0.093 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_033.md::c0001` score=0.765069 cov=0.103 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_033.md::c0004` score=0.763083 cov=0.123 section=中文复杂检索文档 > 背景材料2

### zh034 — zh_long_span_boundary_candidate
- question: 板栗可以蒸着吃吗
- gold: `zh_doc_034.md > 关键材料`
- best_topk_coverage: 0.404
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_034.md::c0006` score=0.729524 cov=0.404 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_034.md::c0005` score=0.687607 cov=0.087 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_034.md::c0013` score=0.641474 cov=0.118 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_034.md::c0012` score=0.63818 cov=0.108 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_034.md::c0014` score=0.637014 cov=0.129 section=中文复杂检索文档 > 补充材料2

### zh035 — zh_long_span_boundary_candidate
- question: 没越狱的iphone怎么清理垃圾
- gold: `zh_doc_035.md > 关键材料`
- best_topk_coverage: 0.434
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_035.md::c0004` score=0.78901 cov=0.434 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_035.md::c0010` score=0.787285 cov=0.121 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_035.md::c0009` score=0.787197 cov=0.125 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_035.md::c0011` score=0.786069 cov=0.139 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_035.md::c0002` score=0.782169 cov=0.37 section=中文复杂检索文档 > 背景材料1

### zh036 — zh_long_span_boundary_candidate
- question: 苹果系统怎么查看隐藏文件
- gold: `zh_doc_036.md > 关键材料`
- best_topk_coverage: 0.543
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_036.md::c0006` score=0.768187 cov=0.543 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_036.md::c0004` score=0.744638 cov=0.501 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_036.md::c0005` score=0.733799 cov=0.43 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_036.md::c0000` score=0.704396 cov=0.221 section=
  - rank 5: `zh_doc_036.md::c0007` score=0.681007 cov=0.301 section=中文复杂检索文档 > 关键材料

### zh037 — zh_long_span_boundary_candidate
- question: 海淀医院孕前检查
- gold: `zh_doc_037.md > 关键材料`
- best_topk_coverage: 0.455
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_037.md::c0008` score=0.745576 cov=0.198 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_037.md::c0000` score=0.733445 cov=0.071 section=
  - rank 3: `zh_doc_037.md::c0004` score=0.72473 cov=0.253 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_037.md::c0005` score=0.706916 cov=0.455 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_037.md::c0009` score=0.632756 cov=0.061 section=中文复杂检索文档 > 补充材料1

### zh038 — zh_long_span_boundary_candidate
- question: 玩梦幻西游怎么赚钱
- gold: `zh_doc_038.md > 关键材料`
- best_topk_coverage: 0.491
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_038.md::c0003` score=0.724203 cov=0.049 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_038.md::c0004` score=0.723164 cov=0.087 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_038.md::c0000` score=0.720347 cov=0.074 section=
  - rank 4: `zh_doc_038.md::c0006` score=0.681325 cov=0.451 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_038.md::c0007` score=0.652516 cov=0.491 section=中文复杂检索文档 > 关键材料

### zh039 — zh_long_span_boundary_candidate
- question: 跟庐山有关的诗句
- gold: `zh_doc_039.md > 关键材料`
- best_topk_coverage: 0.476
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_039.md::c0007` score=0.697932 cov=0.121 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_039.md::c0003` score=0.688651 cov=0.343 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_039.md::c0006` score=0.688312 cov=0.35 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_039.md::c0004` score=0.687847 cov=0.476 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_039.md::c0008` score=0.682257 cov=0.045 section=中文复杂检索文档 > 补充材料1

### zh040 — zh_long_span_boundary_candidate
- question: 现在去哪里下载音乐
- gold: `zh_doc_040.md > 关键材料`
- best_topk_coverage: 0.493
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_040.md::c0000` score=0.631478 cov=0.137 section=
  - rank 2: `zh_doc_040.md::c0004` score=0.611937 cov=0.493 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_040.md::c0006` score=0.61014 cov=0.434 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_040.md::c0008` score=0.604544 cov=0.069 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_040.md::c0007` score=0.601418 cov=0.181 section=中文复杂检索文档 > 关键材料

### zh041 — zh_long_span_boundary_candidate
- question: 治疗颈椎病药物
- gold: `zh_doc_041.md > 关键材料`
- best_topk_coverage: 0.41
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_041.md::c0015` score=0.715337 cov=0.096 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_041.md::c0009` score=0.670315 cov=0.41 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_041.md::c0014` score=0.663198 cov=0.114 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_041.md::c0012` score=0.642157 cov=0.323 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_041.md::c0016` score=0.633728 cov=0.107 section=中文复杂检索文档 > 补充材料2

### zh042 — zh_long_span_boundary_candidate
- question: 户外手电筒什么牌子好
- gold: `zh_doc_042.md > 关键材料`
- best_topk_coverage: 0.42
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_042.md::c0003` score=0.743118 cov=0.315 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_042.md::c0001` score=0.693946 cov=0.071 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_042.md::c0007` score=0.688657 cov=0.123 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_042.md::c0008` score=0.684579 cov=0.109 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_042.md::c0004` score=0.677943 cov=0.42 section=中文复杂检索文档 > 关键材料

### zh043 — zh_long_span_boundary_candidate
- question: cfs和cy有什么不同
- gold: `zh_doc_043.md > 关键材料`
- best_topk_coverage: 0.418
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_043.md::c0002` score=0.605607 cov=0.418 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_043.md::c0015` score=0.487725 cov=0.01 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_043.md::c0000` score=0.475422 cov=0.024 section=
  - rank 4: `zh_doc_043.md::c0009` score=0.471878 cov=0.007 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_043.md::c0013` score=0.464672 cov=0.01 section=中文复杂检索文档 > 补充材料1

### zh044 — zh_long_span_boundary_candidate
- question: 换外汇哪个银行好
- gold: `zh_doc_044.md > 关键材料`
- best_topk_coverage: 0.412
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_044.md::c0000` score=0.838119 cov=0.079 section=
  - rank 2: `zh_doc_044.md::c0001` score=0.779867 cov=0.095 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_044.md::c0002` score=0.774435 cov=0.097 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_044.md::c0007` score=0.757932 cov=0.133 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_044.md::c0003` score=0.754461 cov=0.412 section=中文复杂检索文档 > 背景材料2

### zh045 — zh_long_span_boundary_candidate
- question: 轻型羽绒服什么牌子好
- gold: `zh_doc_045.md > 关键材料`
- best_topk_coverage: 0.57
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_045.md::c0003` score=0.65518 cov=0.57 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_045.md::c0014` score=0.638174 cov=0.125 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_045.md::c0010` score=0.63039 cov=0.114 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_045.md::c0000` score=0.630254 cov=0.1 section=
  - rank 5: `zh_doc_045.md::c0005` score=0.630052 cov=0.564 section=中文复杂检索文档 > 关键材料

### zh046 — zh_long_span_boundary_candidate
- question: 手机外放进水
- gold: `zh_doc_046.md > 关键材料`
- best_topk_coverage: 0.247
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_046.md::c0010` score=0.737852 cov=0.074 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_046.md::c0000` score=0.735881 cov=0.114 section=
  - rank 3: `zh_doc_046.md::c0008` score=0.732728 cov=0.247 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_046.md::c0001` score=0.723336 cov=0.111 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_046.md::c0002` score=0.717635 cov=0.116 section=中文复杂检索文档 > 背景材料1

### zh047 — zh_long_span_boundary_candidate
- question: 什么样的借条不具法律效力
- gold: `zh_doc_047.md > 关键材料`
- best_topk_coverage: 0.576
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_047.md::c0017` score=0.796887 cov=0.167 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_047.md::c0016` score=0.793086 cov=0.167 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_047.md::c0015` score=0.790735 cov=0.216 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_047.md::c0012` score=0.77774 cov=0.576 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_047.md::c0001` score=0.772817 cov=0.11 section=中文复杂检索文档 > 背景材料1

### zh048 — zh_long_span_boundary_candidate
- question: m8a1用什么炮
- gold: `zh_doc_048.md > 关键材料`
- best_topk_coverage: 0.507
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_048.md::c0010` score=0.695455 cov=0.123 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_048.md::c0004` score=0.666765 cov=0.205 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_048.md::c0009` score=0.66536 cov=0.102 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_048.md::c0008` score=0.664145 cov=0.207 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_048.md::c0005` score=0.661064 cov=0.507 section=中文复杂检索文档 > 关键材料

### zh049 — zh_long_span_boundary_candidate
- question: 西安人流手术费用要多少
- gold: `zh_doc_049.md > 关键材料`
- best_topk_coverage: 0.525
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_049.md::c0000` score=0.783485 cov=0.161 section=
  - rank 2: `zh_doc_049.md::c0007` score=0.776354 cov=0.295 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_049.md::c0008` score=0.766683 cov=0.224 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_049.md::c0006` score=0.760893 cov=0.525 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_049.md::c0001` score=0.74775 cov=0.141 section=中文复杂检索文档 > 背景材料1

### zh050 — zh_long_span_boundary_candidate
- question: xm外汇平台怎么样
- gold: `zh_doc_050.md > 关键材料`
- best_topk_coverage: 0.412
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_050.md::c0003` score=0.841643 cov=0.336 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_050.md::c0006` score=0.817092 cov=0.412 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_050.md::c0001` score=0.793856 cov=0.091 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_050.md::c0007` score=0.788463 cov=0.122 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_050.md::c0000` score=0.785202 cov=0.084 section=

### zh051 — zh_long_span_boundary_candidate
- question: 双人床最小宽度
- gold: `zh_doc_051.md > 关键材料`
- best_topk_coverage: 0.441
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_051.md::c0014` score=0.749722 cov=0.128 section=中文复杂检索文档 > 补充材料1
  - rank 2: `zh_doc_051.md::c0000` score=0.748644 cov=0.078 section=
  - rank 3: `zh_doc_051.md::c0010` score=0.745794 cov=0.441 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_051.md::c0002` score=0.742583 cov=0.064 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_051.md::c0001` score=0.741398 cov=0.067 section=中文复杂检索文档 > 背景材料1

### zh052 — zh_long_span_boundary_candidate
- question: 生气时喂奶
- gold: `zh_doc_052.md > 关键材料`
- best_topk_coverage: 0.522
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_052.md::c0003` score=0.759584 cov=0.469 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_052.md::c0002` score=0.741152 cov=0.238 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_052.md::c0006` score=0.739738 cov=0.224 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_052.md::c0005` score=0.734643 cov=0.522 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_052.md::c0001` score=0.714313 cov=0.33 section=中文复杂检索文档 > 背景材料1

### zh053 — zh_long_span_boundary_candidate
- question: 龟头敏感度低怎么办
- gold: `zh_doc_053.md > 关键材料`
- best_topk_coverage: 0.383
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_053.md::c0000` score=0.767137 cov=0.051 section=
  - rank 2: `zh_doc_053.md::c0016` score=0.75397 cov=0.383 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_053.md::c0022` score=0.748517 cov=0.117 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_053.md::c0018` score=0.744914 cov=0.227 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_053.md::c0005` score=0.743479 cov=0.119 section=中文复杂检索文档 > 背景材料2

### zh054 — zh_long_span_boundary_candidate
- question: 沪陕高速限速多少
- gold: `zh_doc_054.md > 关键材料`
- best_topk_coverage: 0.573
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_054.md::c0004` score=0.730194 cov=0.573 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_054.md::c0002` score=0.73009 cov=0.254 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_054.md::c0005` score=0.70315 cov=0.549 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_054.md::c0003` score=0.683152 cov=0.322 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_054.md::c0008` score=0.667017 cov=0.103 section=中文复杂检索文档 > 补充材料1

### zh055 — zh_long_span_boundary_candidate
- question: ios9 如何关闭搜索最近联系人
- gold: `zh_doc_055.md > 关键材料`
- best_topk_coverage: 0.589
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_055.md::c0000` score=0.806686 cov=0.459 section=
  - rank 2: `zh_doc_055.md::c0002` score=0.796994 cov=0.551 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_055.md::c0001` score=0.792618 cov=0.56 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_055.md::c0007` score=0.78891 cov=0.377 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_055.md::c0004` score=0.784691 cov=0.589 section=中文复杂检索文档 > 关键材料

### zh056 — zh_long_span_boundary_candidate
- question: 尸兄主角能力
- gold: `zh_doc_056.md > 关键材料`
- best_topk_coverage: 0.43
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_056.md::c0002` score=0.696141 cov=0.077 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_056.md::c0010` score=0.684792 cov=0.077 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_056.md::c0003` score=0.675866 cov=0.067 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_056.md::c0012` score=0.669564 cov=0.075 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_056.md::c0006` score=0.664923 cov=0.43 section=中文复杂检索文档 > 背景材料2

### zh057 — zh_long_span_boundary_candidate
- question: word怎么不能修改
- gold: `zh_doc_057.md > 关键材料`
- best_topk_coverage: 0.141
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_057.md::c0001` score=0.748066 cov=0.124 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_057.md::c0018` score=0.742401 cov=0.141 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_057.md::c0015` score=0.741791 cov=0.101 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_057.md::c0027` score=0.727379 cov=0.096 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_057.md::c0000` score=0.720023 cov=0.101 section=

### zh059 — zh_long_span_boundary_candidate
- question: 电热毯能烘干被子吗
- gold: `zh_doc_059.md > 关键材料`
- best_topk_coverage: 0.6
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_059.md::c0004` score=0.746697 cov=0.568 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_059.md::c0000` score=0.735688 cov=0.134 section=
  - rank 3: `zh_doc_059.md::c0005` score=0.735069 cov=0.6 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_059.md::c0001` score=0.721637 cov=0.185 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_059.md::c0006` score=0.719335 cov=0.585 section=中文复杂检索文档 > 关键材料

### zh060 — zh_long_span_boundary_candidate
- question: 氨端聚二甲基硅氧烷是硅油吗
- gold: `zh_doc_060.md > 关键材料`
- best_topk_coverage: 0.327
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_060.md::c0012` score=0.690918 cov=0.327 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_060.md::c0016` score=0.656166 cov=0.12 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_060.md::c0002` score=0.630446 cov=0.15 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_060.md::c0001` score=0.620996 cov=0.204 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_060.md::c0021` score=0.614064 cov=0.125 section=中文复杂检索文档 > 补充材料1

### zh061 — zh_long_span_boundary_candidate
- question: 为什么中国必须守住18亿亩耕地红线
- gold: `zh_doc_061.md > 关键材料`
- best_topk_coverage: 0.392
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_061.md::c0007` score=0.783064 cov=0.109 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_061.md::c0014` score=0.776171 cov=0.392 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_061.md::c0012` score=0.768683 cov=0.161 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_061.md::c0011` score=0.765852 cov=0.358 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_061.md::c0000` score=0.758872 cov=0.129 section=

### zh062 — zh_long_span_boundary_candidate
- question: 如何取消电脑的自动休眠
- gold: `zh_doc_062.md > 关键材料`
- best_topk_coverage: 0.426
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_062.md::c0007` score=0.843967 cov=0.103 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_062.md::c0006` score=0.804999 cov=0.135 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_062.md::c0000` score=0.782576 cov=0.203 section=
  - rank 4: `zh_doc_062.md::c0001` score=0.753111 cov=0.079 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_062.md::c0008` score=0.752247 cov=0.426 section=中文复杂检索文档 > 背景材料2

### zh063 — zh_long_span_boundary_candidate
- question: 象征孩子纯洁的花
- gold: `zh_doc_063.md > 关键材料`
- best_topk_coverage: 0.534
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_063.md::c0000` score=0.674036 cov=0.107 section=
  - rank 2: `zh_doc_063.md::c0004` score=0.644008 cov=0.067 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_063.md::c0006` score=0.642149 cov=0.534 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_063.md::c0011` score=0.641317 cov=0.055 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_063.md::c0010` score=0.635941 cov=0.451 section=中文复杂检索文档 > 补充材料1

### zh064 — zh_long_span_boundary_candidate
- question: 血清甘油三脂偏低
- gold: `zh_doc_064.md > 关键材料`
- best_topk_coverage: 0.639
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_064.md::c0005` score=0.794669 cov=0.639 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_064.md::c0003` score=0.77958 cov=0.541 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_064.md::c0002` score=0.774582 cov=0.556 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_064.md::c0004` score=0.769653 cov=0.511 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_064.md::c0013` score=0.758039 cov=0.203 section=中文复杂检索文档 > 补充材料1

### zh065 — zh_long_span_boundary_candidate
- question: 哪种制氧机好
- gold: `zh_doc_065.md > 关键材料`
- best_topk_coverage: 0.594
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_065.md::c0005` score=0.698737 cov=0.364 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_065.md::c0007` score=0.689641 cov=0.526 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_065.md::c0006` score=0.685158 cov=0.594 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_065.md::c0010` score=0.672032 cov=0.191 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_065.md::c0011` score=0.657021 cov=0.188 section=中文复杂检索文档 > 补充材料1

### zh066 — zh_long_span_boundary_candidate
- question: 电动牙刷刷的干净吗
- gold: `zh_doc_066.md > 关键材料`
- best_topk_coverage: 0.567
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_066.md::c0000` score=0.707145 cov=0.204 section=
  - rank 2: `zh_doc_066.md::c0003` score=0.697145 cov=0.345 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_066.md::c0006` score=0.676694 cov=0.26 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_066.md::c0004` score=0.673947 cov=0.567 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_066.md::c0001` score=0.669543 cov=0.192 section=中文复杂检索文档 > 背景材料1

### zh067 — zh_long_span_boundary_candidate
- question: 武松属什么
- gold: `zh_doc_067.md > 关键材料`
- best_topk_coverage: 0.372
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_067.md::c0005` score=0.709142 cov=0.372 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_067.md::c0002` score=0.668874 cov=0.009 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_067.md::c0001` score=0.634319 cov=0.015 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_067.md::c0000` score=0.619936 cov=0.009 section=
  - rank 5: `zh_doc_067.md::c0011` score=0.60921 cov=0.009 section=中文复杂检索文档 > 补充材料2

### zh068 — zh_long_span_boundary_candidate
- question: 跳鬼步舞时手怎么动
- gold: `zh_doc_068.md > 关键材料`
- best_topk_coverage: 0.526
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_068.md::c0021` score=0.719427 cov=0.526 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_068.md::c0022` score=0.701656 cov=0.15 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_068.md::c0015` score=0.679682 cov=0.078 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_068.md::c0019` score=0.676993 cov=0.486 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_068.md::c0011` score=0.666633 cov=0.081 section=中文复杂检索文档 > 背景材料1

### zh069 — zh_long_span_boundary_candidate
- question: would like的回答
- gold: `zh_doc_069.md > 关键材料`
- best_topk_coverage: 0.64
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_069.md::c0002` score=0.765146 cov=0.13 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_069.md::c0016` score=0.748528 cov=0.145 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_069.md::c0013` score=0.746222 cov=0.64 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_069.md::c0015` score=0.746154 cov=0.195 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_069.md::c0006` score=0.745201 cov=0.125 section=中文复杂检索文档 > 背景材料1

### zh070 — zh_long_span_boundary_candidate
- question: qq经常掉线怎么回事
- gold: `zh_doc_070.md > 关键材料`
- best_topk_coverage: 0.54
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_070.md::c0003` score=0.786445 cov=0.54 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_070.md::c0013` score=0.782932 cov=0.088 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_070.md::c0012` score=0.775061 cov=0.101 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_070.md::c0008` score=0.766326 cov=0.104 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_070.md::c0009` score=0.762109 cov=0.07 section=中文复杂检索文档 > 补充材料1

### zh071 — zh_long_span_boundary_candidate
- question: 还珠格格第一部背景音乐
- gold: `zh_doc_071.md > 关键材料`
- best_topk_coverage: 0.596
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_071.md::c0018` score=0.680672 cov=0.596 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_071.md::c0002` score=0.630723 cov=0.22 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_071.md::c0004` score=0.619272 cov=0.16 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_071.md::c0003` score=0.617918 cov=0.223 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_071.md::c0005` score=0.59253 cov=0.279 section=中文复杂检索文档 > 背景材料2

### zh072 — zh_long_span_boundary_candidate
- question: 我的世界手机版0.12.1末地传送门怎么做
- gold: `zh_doc_072.md > 关键材料`
- best_topk_coverage: 0.43
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_072.md::c0009` score=0.79729 cov=0.182 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_072.md::c0003` score=0.79072 cov=0.169 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_072.md::c0002` score=0.76026 cov=0.163 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_072.md::c0007` score=0.755569 cov=0.28 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_072.md::c0004` score=0.752333 cov=0.43 section=中文复杂检索文档 > 背景材料2

### zh073 — zh_long_span_boundary_candidate
- question: 三壬行化妆学校好吗
- gold: `zh_doc_073.md > 关键材料`
- best_topk_coverage: 0.534
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_073.md::c0003` score=0.821664 cov=0.436 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_073.md::c0005` score=0.802191 cov=0.511 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_073.md::c0004` score=0.782251 cov=0.534 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_073.md::c0006` score=0.780576 cov=0.134 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_073.md::c0001` score=0.753278 cov=0.083 section=中文复杂检索文档 > 背景材料1

### zh074 — zh_long_span_boundary_candidate
- question: 胃功能
- gold: `zh_doc_074.md > 关键材料`
- best_topk_coverage: 0.572
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_074.md::c0004` score=0.708286 cov=0.572 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_074.md::c0003` score=0.700786 cov=0.263 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_074.md::c0002` score=0.686004 cov=0.075 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_074.md::c0000` score=0.666446 cov=0.124 section=
  - rank 5: `zh_doc_074.md::c0006` score=0.662083 cov=0.335 section=中文复杂检索文档 > 关键材料

### zh075 — zh_long_span_boundary_candidate
- question: 艾俐缇陶瓷怎么样
- gold: `zh_doc_075.md > 关键材料`
- best_topk_coverage: 0.311
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_075.md::c0003` score=0.694252 cov=0.311 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_075.md::c0007` score=0.672939 cov=0.07 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_075.md::c0006` score=0.669628 cov=0.253 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_075.md::c0001` score=0.668642 cov=0.032 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_075.md::c0008` score=0.665959 cov=0.02 section=中文复杂检索文档 > 补充材料1

### zh076 — zh_long_span_boundary_candidate
- question: 公共事业管理属于什么专业类别
- gold: `zh_doc_076.md > 关键材料`
- best_topk_coverage: 0.639
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_076.md::c0002` score=0.797809 cov=0.465 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_076.md::c0003` score=0.774177 cov=0.639 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_076.md::c0005` score=0.756544 cov=0.323 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_076.md::c0008` score=0.745121 cov=0.204 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_076.md::c0011` score=0.738151 cov=0.174 section=中文复杂检索文档 > 补充材料1

### zh077 — zh_long_span_boundary_candidate
- question: 天然无添加的护肤品存在吗
- gold: `zh_doc_077.md > 关键材料`
- best_topk_coverage: 0.604
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_077.md::c0023` score=0.759171 cov=0.604 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_077.md::c0024` score=0.742637 cov=0.53 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_077.md::c0025` score=0.71499 cov=0.242 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_077.md::c0026` score=0.6953 cov=0.162 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_077.md::c0017` score=0.691537 cov=0.134 section=中文复杂检索文档 > 背景材料1

### zh078 — zh_long_span_boundary_candidate
- question: 旅行发票 可以报吗
- gold: `zh_doc_078.md > 关键材料`
- best_topk_coverage: 0.583
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_078.md::c0000` score=0.764365 cov=0.067 section=
  - rank 2: `zh_doc_078.md::c0001` score=0.753588 cov=0.113 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_078.md::c0006` score=0.734924 cov=0.323 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_078.md::c0003` score=0.716969 cov=0.419 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_078.md::c0005` score=0.702011 cov=0.583 section=中文复杂检索文档 > 关键材料

### zh079 — zh_long_span_boundary_candidate
- question: 种子可以用百度云下载吗
- gold: `zh_doc_079.md > 关键材料`
- best_topk_coverage: 0.509
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_079.md::c0004` score=0.69929 cov=0.509 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_079.md::c0002` score=0.689142 cov=0.148 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_079.md::c0008` score=0.686946 cov=0.252 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_079.md::c0000` score=0.674459 cov=0.167 section=
  - rank 5: `zh_doc_079.md::c0006` score=0.659923 cov=0.367 section=中文复杂检索文档 > 关键材料

### zh081 — zh_long_span_boundary_candidate
- question: 手机钢化保护膜怎么贴
- gold: `zh_doc_081.md > 关键材料`
- best_topk_coverage: 0.599
- best_gold_rank_hint: 2
- top results:
  - rank 1: `zh_doc_027.md::c0011` score=0.763713 cov=0.0 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_081.md::c0003` score=0.763611 cov=0.136 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_081.md::c0004` score=0.761388 cov=0.209 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_081.md::c0021` score=0.761161 cov=0.15 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_081.md::c0017` score=0.760331 cov=0.599 section=中文复杂检索文档 > 关键材料

### zh082 — zh_long_span_boundary_candidate
- question: 中国古代最繁荣的朝代
- gold: `zh_doc_082.md > 关键材料`
- best_topk_coverage: 0.321
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_082.md::c0000` score=0.714721 cov=0.053 section=
  - rank 2: `zh_doc_082.md::c0001` score=0.680577 cov=0.081 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_082.md::c0008` score=0.670054 cov=0.059 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_082.md::c0009` score=0.664904 cov=0.072 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_082.md::c0003` score=0.635062 cov=0.321 section=中文复杂检索文档 > 背景材料2

### zh083 — zh_long_span_boundary_candidate
- question: 怎么改民族
- gold: `zh_doc_083.md > 关键材料`
- best_topk_coverage: 0.637
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_083.md::c0032` score=0.726345 cov=0.552 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_083.md::c0001` score=0.72604 cov=0.224 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_083.md::c0031` score=0.712309 cov=0.637 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_083.md::c0000` score=0.689758 cov=0.159 section=
  - rank 5: `zh_doc_083.md::c0041` score=0.669 cov=0.233 section=中文复杂检索文档 > 补充材料2

### zh085 — zh_long_span_boundary_candidate
- question: 白带有酸奶味
- gold: `zh_doc_085.md > 关键材料`
- best_topk_coverage: 0.207
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_085.md::c0001` score=0.756505 cov=0.039 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_085.md::c0029` score=0.734701 cov=0.099 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_085.md::c0000` score=0.733913 cov=0.111 section=
  - rank 4: `zh_doc_085.md::c0020` score=0.717853 cov=0.207 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_085.md::c0026` score=0.717211 cov=0.072 section=中文复杂检索文档 > 补充材料1

### zh086 — zh_long_span_boundary_candidate
- question: mathematica怎么求积分
- gold: `zh_doc_086.md > 关键材料`
- best_topk_coverage: 0.433
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_086.md::c0005` score=0.733704 cov=0.433 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_086.md::c0000` score=0.723876 cov=0.125 section=
  - rank 3: `zh_doc_086.md::c0001` score=0.71011 cov=0.116 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_086.md::c0002` score=0.672759 cov=0.116 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_086.md::c0004` score=0.65401 cov=0.112 section=中文复杂检索文档 > 背景材料2

### zh087 — zh_long_span_boundary_candidate
- question: 晾衣架材质
- gold: `zh_doc_087.md > 关键材料`
- best_topk_coverage: 0.292
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_087.md::c0007` score=0.765481 cov=0.292 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_087.md::c0005` score=0.757819 cov=0.137 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_087.md::c0010` score=0.754014 cov=0.262 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_087.md::c0006` score=0.737417 cov=0.101 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_087.md::c0011` score=0.737347 cov=0.092 section=中文复杂检索文档 > 补充材料1

### zh088 — zh_long_span_boundary_candidate
- question: 如何遮盖唇色
- gold: `zh_doc_088.md > 关键材料`
- best_topk_coverage: 0.617
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_088.md::c0002` score=0.721712 cov=0.389 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_088.md::c0003` score=0.682457 cov=0.617 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_088.md::c0001` score=0.673643 cov=0.177 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_088.md::c0000` score=0.660335 cov=0.12 section=
  - rank 5: `zh_doc_088.md::c0004` score=0.659169 cov=0.563 section=中文复杂检索文档 > 关键材料

### zh089 — zh_long_span_boundary_candidate
- question: 部落冲突怎么搜死鱼
- gold: `zh_doc_089.md > 关键材料`
- best_topk_coverage: 0.536
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_089.md::c0000` score=0.799365 cov=0.092 section=
  - rank 2: `zh_doc_089.md::c0001` score=0.767165 cov=0.103 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_089.md::c0005` score=0.726568 cov=0.252 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_089.md::c0007` score=0.716111 cov=0.072 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_089.md::c0003` score=0.693872 cov=0.536 section=中文复杂检索文档 > 关键材料

### zh090 — zh_long_span_boundary_candidate
- question: 牛剖层移膜皮是什么
- gold: `zh_doc_090.md > 关键材料`
- best_topk_coverage: 0.545
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_090.md::c0021` score=0.723909 cov=0.52 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_090.md::c0025` score=0.696287 cov=0.122 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_090.md::c0023` score=0.695033 cov=0.376 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_090.md::c0022` score=0.688208 cov=0.545 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_090.md::c0015` score=0.686974 cov=0.132 section=中文复杂检索文档 > 背景材料2

### zh092 — zh_long_span_boundary_candidate
- question: 北京市公务员一年考几次
- gold: `zh_doc_092.md > 关键材料`
- best_topk_coverage: 0.567
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_092.md::c0004` score=0.743398 cov=0.567 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_092.md::c0009` score=0.739536 cov=0.567 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_092.md::c0010` score=0.736974 cov=0.564 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_092.md::c0006` score=0.731198 cov=0.397 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_092.md::c0002` score=0.730543 cov=0.302 section=中文复杂检索文档 > 背景材料1

### zh093 — zh_long_span_boundary_candidate
- question: 成都审驾照需要什么
- gold: `zh_doc_093.md > 关键材料`
- best_topk_coverage: 0.19
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_093.md::c0025` score=0.732509 cov=0.19 section=中文复杂检索文档 > 补充材料2
  - rank 2: `zh_doc_093.md::c0015` score=0.730521 cov=0.147 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_093.md::c0011` score=0.728682 cov=0.088 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_093.md::c0006` score=0.725907 cov=0.125 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_093.md::c0021` score=0.722258 cov=0.147 section=中文复杂检索文档 > 补充材料2

### zh094 — zh_long_span_boundary_candidate
- question: 霜是怎么形成的
- gold: `zh_doc_094.md > 关键材料`
- best_topk_coverage: 0.062
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_094.md::c0000` score=0.696477 cov=0.043 section=
  - rank 2: `zh_doc_094.md::c0014` score=0.695244 cov=0.04 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_094.md::c0015` score=0.664854 cov=0.023 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_094.md::c0002` score=0.65021 cov=0.045 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_094.md::c0001` score=0.635613 cov=0.062 section=中文复杂检索文档 > 背景材料1

### zh095 — zh_long_span_boundary_candidate
- question: 卫生间铺什么地砖好
- gold: `zh_doc_095.md > 关键材料`
- best_topk_coverage: 0.605
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_095.md::c0002` score=0.649322 cov=0.172 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_095.md::c0008` score=0.644557 cov=0.605 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_095.md::c0003` score=0.643977 cov=0.131 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_095.md::c0009` score=0.633307 cov=0.585 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_095.md::c0001` score=0.61622 cov=0.139 section=中文复杂检索文档 > 背景材料1

### zh096 — zh_long_span_boundary_candidate
- question: 肠结核的症状
- gold: `zh_doc_096.md > 关键材料`
- best_topk_coverage: 0.574
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_096.md::c0006` score=0.74785 cov=0.574 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_096.md::c0002` score=0.728027 cov=0.137 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_096.md::c0007` score=0.693993 cov=0.463 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_096.md::c0008` score=0.693419 cov=0.137 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_096.md::c0000` score=0.681931 cov=0.123 section=

### zh097 — zh_long_span_boundary_candidate
- question: 表带怎么打孔
- gold: `zh_doc_097.md > 关键材料`
- best_topk_coverage: 0.549
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_097.md::c0004` score=0.785853 cov=0.27 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_097.md::c0007` score=0.782435 cov=0.241 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_097.md::c0006` score=0.744578 cov=0.549 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_097.md::c0010` score=0.733056 cov=0.096 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_097.md::c0008` score=0.729614 cov=0.099 section=中文复杂检索文档 > 补充材料1

### zh099 — zh_long_span_boundary_candidate
- question: 水土流失是什么意思
- gold: `zh_doc_099.md > 关键材料`
- best_topk_coverage: 0.606
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_099.md::c0028` score=0.721933 cov=0.253 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_099.md::c0029` score=0.686342 cov=0.606 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_099.md::c0000` score=0.656504 cov=0.147 section=
  - rank 4: `zh_doc_099.md::c0038` score=0.629934 cov=0.382 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_099.md::c0030` score=0.61751 cov=0.597 section=中文复杂检索文档 > 关键材料

### zh100 — zh_long_span_boundary_candidate
- question: 红枣表面有层白色粉末
- gold: `zh_doc_100.md > 关键材料`
- best_topk_coverage: 0.559
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_100.md::c0005` score=0.836307 cov=0.369 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_100.md::c0006` score=0.792295 cov=0.072 section=中文复杂检索文档 > 补充材料1
  - rank 3: `zh_doc_100.md::c0008` score=0.789325 cov=0.072 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_100.md::c0009` score=0.784032 cov=0.051 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_100.md::c0004` score=0.783685 cov=0.559 section=中文复杂检索文档 > 关键材料

### zh101 — zh_long_span_boundary_candidate
- question: 小米的平板好用吗
- gold: `zh_doc_101.md > 关键材料`
- best_topk_coverage: 0.599
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_101.md::c0013` score=0.774478 cov=0.599 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_101.md::c0014` score=0.734412 cov=0.518 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_101.md::c0020` score=0.726887 cov=0.059 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_101.md::c0017` score=0.711242 cov=0.092 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_101.md::c0019` score=0.70583 cov=0.085 section=中文复杂检索文档 > 补充材料1

### zh102 — zh_long_span_boundary_candidate
- question: 尺神经麻痹治疗
- gold: `zh_doc_102.md > 关键材料`
- best_topk_coverage: 0.631
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_102.md::c0006` score=0.751212 cov=0.159 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_102.md::c0014` score=0.716649 cov=0.081 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_102.md::c0011` score=0.71317 cov=0.262 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_102.md::c0005` score=0.707589 cov=0.072 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_102.md::c0010` score=0.702307 cov=0.631 section=中文复杂检索文档 > 关键材料

### zh103 — zh_long_span_boundary_candidate
- question: 北京出国体检在哪里
- gold: `zh_doc_103.md > 关键材料`
- best_topk_coverage: 0.593
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_103.md::c0005` score=0.792588 cov=0.593 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_103.md::c0001` score=0.787741 cov=0.222 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_103.md::c0007` score=0.776884 cov=0.43 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_103.md::c0009` score=0.769671 cov=0.384 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_103.md::c0002` score=0.749345 cov=0.235 section=中文复杂检索文档 > 背景材料2

### zh106 — zh_long_span_boundary_candidate
- question: 原地跑步能减肚子吗
- gold: `zh_doc_106.md > 关键材料`
- best_topk_coverage: 0.313
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_106.md::c0020` score=0.723172 cov=0.096 section=中文复杂检索文档 > 补充
  - rank 2: `zh_doc_106.md::c0004` score=0.722042 cov=0.313 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_106.md::c0007` score=0.720373 cov=0.062 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_106.md::c0001` score=0.719127 cov=0.093 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_106.md::c0008` score=0.712521 cov=0.058 section=中文复杂检索文档 > 补充材料1

### zh108 — zh_long_span_boundary_candidate
- question: 肩颈僵硬
- gold: `zh_doc_108.md > 关键材料`
- best_topk_coverage: 0.372
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_108.md::c0001` score=0.738817 cov=0.059 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_108.md::c0000` score=0.729817 cov=0.045 section=
  - rank 3: `zh_doc_108.md::c0003` score=0.72293 cov=0.372 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_108.md::c0002` score=0.700447 cov=0.083 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_108.md::c0009` score=0.686006 cov=0.087 section=中文复杂检索文档 > 补充材料1

### zh109 — zh_long_span_boundary_candidate
- question: 借书的好处
- gold: `zh_doc_109.md > 关键材料`
- best_topk_coverage: 0.647
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_109.md::c0029` score=0.792814 cov=0.647 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_109.md::c0028` score=0.784136 cov=0.596 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_109.md::c0019` score=0.734954 cov=0.114 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_109.md::c0020` score=0.712626 cov=0.117 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_109.md::c0018` score=0.684618 cov=0.129 section=中文复杂检索文档 > 背景材料1

### zh110 — zh_long_span_boundary_candidate
- question: 完美世界出过什么游戏
- gold: `zh_doc_110.md > 关键材料`
- best_topk_coverage: 0.61
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_110.md::c0000` score=0.627388 cov=0.061 section=
  - rank 2: `zh_doc_110.md::c0008` score=0.581928 cov=0.061 section=中文复杂检索文档 > 补充
  - rank 3: `zh_doc_110.md::c0001` score=0.577032 cov=0.085 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_110.md::c0004` score=0.573472 cov=0.61 section=中文复杂检索文档 > 关键材料
  - rank 5: `zh_doc_110.md::c0003` score=0.551317 cov=0.277 section=中文复杂检索文档 > 背景材料2

### zh111 — zh_long_span_boundary_candidate
- question: 张家港大千装饰怎样
- gold: `zh_doc_111.md > 关键材料`
- best_topk_coverage: 0.544
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_111.md::c0003` score=0.800424 cov=0.544 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_111.md::c0000` score=0.765436 cov=0.216 section=
  - rank 3: `zh_doc_111.md::c0005` score=0.743473 cov=0.49 section=中文复杂检索文档 > 关键材料
  - rank 4: `zh_doc_111.md::c0002` score=0.719785 cov=0.216 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_111.md::c0001` score=0.689913 cov=0.216 section=中文复杂检索文档 > 背景材料1

### zh112 — zh_long_span_boundary_candidate
- question: 为什么qq打不开图片
- gold: `zh_doc_112.md > 关键材料`
- best_topk_coverage: 0.429
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_112.md::c0005` score=0.763187 cov=0.429 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_112.md::c0009` score=0.760611 cov=0.088 section=中文复杂检索文档 > 补充材料2
  - rank 3: `zh_doc_112.md::c0003` score=0.747258 cov=0.423 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_112.md::c0008` score=0.712808 cov=0.097 section=中文复杂检索文档 > 补充材料1
  - rank 5: `zh_doc_112.md::c0001` score=0.695837 cov=0.115 section=中文复杂检索文档 > 背景材料1

### zh113 — zh_long_span_boundary_candidate
- question: 辅酶q10的服用方法
- gold: `zh_doc_113.md > 关键材料`
- best_topk_coverage: 0.138
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_113.md::c0003` score=0.775853 cov=0.116 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_113.md::c0004` score=0.772348 cov=0.138 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_113.md::c0002` score=0.76304 cov=0.116 section=中文复杂检索文档 > 背景材料1
  - rank 4: `zh_doc_113.md::c0012` score=0.762224 cov=0.127 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_113.md::c0010` score=0.759979 cov=0.127 section=中文复杂检索文档 > 补充

### zh114 — zh_long_span_boundary_candidate
- question: 杀人剑没了?
- gold: `zh_doc_114.md > 关键材料`
- best_topk_coverage: 0.628
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_114.md::c0004` score=0.608225 cov=0.628 section=中文复杂检索文档 > 关键材料
  - rank 2: `zh_doc_114.md::c0003` score=0.605708 cov=0.582 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_114.md::c0008` score=0.560231 cov=0.096 section=中文复杂检索文档 > 补充材料2
  - rank 4: `zh_doc_114.md::c0002` score=0.550132 cov=0.201 section=中文复杂检索文档 > 背景材料2
  - rank 5: `zh_doc_114.md::c0001` score=0.539687 cov=0.139 section=中文复杂检索文档 > 背景材料1

### zh117 — zh_long_span_boundary_candidate
- question: 德国红铁元和绿铁元有什么区别
- gold: `zh_doc_117.md > 关键材料`
- best_topk_coverage: 0.287
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_117.md::c0001` score=0.761551 cov=0.213 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_117.md::c0002` score=0.75375 cov=0.227 section=中文复杂检索文档 > 背景材料1
  - rank 3: `zh_doc_117.md::c0003` score=0.724838 cov=0.287 section=中文复杂检索文档 > 背景材料2
  - rank 4: `zh_doc_117.md::c0008` score=0.718693 cov=0.231 section=中文复杂检索文档 > 补充材料2
  - rank 5: `zh_doc_117.md::c0007` score=0.714122 cov=0.217 section=中文复杂检索文档 > 补充材料1

### zh118 — zh_long_span_boundary_candidate
- question: 诛仙法宝技能怎么洗
- gold: `zh_doc_118.md > 关键材料`
- best_topk_coverage: 0.433
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_118.md::c0001` score=0.72214 cov=0.042 section=中文复杂检索文档 > 背景材料1
  - rank 2: `zh_doc_118.md::c0005` score=0.721235 cov=0.407 section=中文复杂检索文档 > 关键材料
  - rank 3: `zh_doc_118.md::c0007` score=0.720277 cov=0.084 section=中文复杂检索文档 > 补充材料1
  - rank 4: `zh_doc_118.md::c0000` score=0.702288 cov=0.046 section=
  - rank 5: `zh_doc_118.md::c0003` score=0.70102 cov=0.433 section=中文复杂检索文档 > 背景材料2

### zh119 — zh_long_span_boundary_candidate
- question: 神秘博士clara是谁
- gold: `zh_doc_119.md > 关键材料`
- best_topk_coverage: 0.534
- best_gold_rank_hint: 1
- top results:
  - rank 1: `zh_doc_119.md::c0004` score=0.745136 cov=0.534 section=中文复杂检索文档 > 背景材料2
  - rank 2: `zh_doc_119.md::c0003` score=0.733338 cov=0.534 section=中文复杂检索文档 > 背景材料2
  - rank 3: `zh_doc_119.md::c0000` score=0.71033 cov=0.045 section=
  - rank 4: `zh_doc_119.md::c0002` score=0.618085 cov=0.086 section=中文复杂检索文档 > 背景材料1
  - rank 5: `zh_doc_119.md::c0001` score=0.587523 cov=0.038 section=中文复杂检索文档 > 背景材料1

## All Query Summary

| qid | expected type | success | rank | best cov | gold rank hint |
|---|---|---:|---:|---:|---:|
| zh001 | zh_long_span_boundary_candidate | False | None | 0.547 | 1 |
| zh002 | zh_long_span_boundary_candidate | False | None | 0.264 | 1 |
| zh003 | zh_long_span_boundary_candidate | False | None | 0.211 | 1 |
| zh004 | zh_long_span_boundary_candidate | False | None | 0.256 | 1 |
| zh005 | zh_long_span_boundary_candidate | False | None | 0.367 | 1 |
| zh006 | zh_long_span_boundary_candidate | False | None | 0.386 | 1 |
| zh007 | zh_long_span_boundary_candidate | False | None | 0.314 | 1 |
| zh008 | zh_long_span_boundary_candidate | False | None | 0.282 | 1 |
| zh009 | zh_long_span_boundary_candidate | False | None | 0.444 | 1 |
| zh010 | zh_long_span_boundary_candidate | False | None | 0.057 | 1 |
| zh011 | zh_long_span_boundary_candidate | False | None | 0.2 | 1 |
| zh012 | zh_long_span_boundary_candidate | False | None | 0.368 | 1 |
| zh013 | zh_long_span_boundary_candidate | False | None | 0.304 | 1 |
| zh014 | zh_long_span_boundary_candidate | False | None | 0.341 | 1 |
| zh015 | zh_long_span_boundary_candidate | False | None | 0.443 | 1 |
| zh016 | zh_long_span_boundary_candidate | False | None | 0.399 | 1 |
| zh017 | zh_long_span_boundary_candidate | False | None | 0.356 | 1 |
| zh018 | zh_long_span_boundary_candidate | False | None | 0.406 | 1 |
| zh019 | zh_long_span_boundary_candidate | False | None | 0.649 | 1 |
| zh020 | zh_long_span_boundary_candidate | False | None | 0.217 | 1 |
| zh021 | zh_long_span_boundary_candidate | False | None | 0.385 | 1 |
| zh022 | zh_long_span_boundary_candidate | False | None | 0.186 | 1 |
| zh023 | zh_long_span_boundary_candidate | False | None | 0.38 | 1 |
| zh024 | zh_long_span_boundary_candidate | False | None | 0.407 | 1 |
| zh025 | zh_long_span_boundary_candidate | False | None | 0.347 | 1 |
| zh026 | zh_long_span_boundary_candidate | False | None | 0.63 | 1 |
| zh027 | zh_long_span_boundary_candidate | False | None | 0.145 | 1 |
| zh028 | zh_long_span_boundary_candidate | False | None | 0.417 | 1 |
| zh029 | zh_long_span_boundary_candidate | False | None | 0.531 | 1 |
| zh030 | zh_long_span_boundary_candidate | False | None | 0.285 | 1 |
| zh031 | zh_long_span_boundary_candidate | False | None | 0.522 | 1 |
| zh032 | zh_long_span_boundary_candidate | False | None | 0.352 | 1 |
| zh033 | zh_long_span_boundary_candidate | False | None | 0.335 | 1 |
| zh034 | zh_long_span_boundary_candidate | False | None | 0.404 | 1 |
| zh035 | zh_long_span_boundary_candidate | False | None | 0.434 | 1 |
| zh036 | zh_long_span_boundary_candidate | False | None | 0.543 | 1 |
| zh037 | zh_long_span_boundary_candidate | False | None | 0.455 | 1 |
| zh038 | zh_long_span_boundary_candidate | False | None | 0.491 | 1 |
| zh039 | zh_long_span_boundary_candidate | False | None | 0.476 | 1 |
| zh040 | zh_long_span_boundary_candidate | False | None | 0.493 | 1 |
| zh041 | zh_long_span_boundary_candidate | False | None | 0.41 | 1 |
| zh042 | zh_long_span_boundary_candidate | False | None | 0.42 | 1 |
| zh043 | zh_long_span_boundary_candidate | False | None | 0.418 | 1 |
| zh044 | zh_long_span_boundary_candidate | False | None | 0.412 | 1 |
| zh045 | zh_long_span_boundary_candidate | False | None | 0.57 | 1 |
| zh046 | zh_long_span_boundary_candidate | False | None | 0.247 | 1 |
| zh047 | zh_long_span_boundary_candidate | False | None | 0.576 | 1 |
| zh048 | zh_long_span_boundary_candidate | False | None | 0.507 | 1 |
| zh049 | zh_long_span_boundary_candidate | False | None | 0.525 | 1 |
| zh050 | zh_long_span_boundary_candidate | False | None | 0.412 | 1 |
| zh051 | zh_long_span_boundary_candidate | False | None | 0.441 | 1 |
| zh052 | zh_long_span_boundary_candidate | False | None | 0.522 | 1 |
| zh053 | zh_long_span_boundary_candidate | False | None | 0.383 | 1 |
| zh054 | zh_long_span_boundary_candidate | False | None | 0.573 | 1 |
| zh055 | zh_long_span_boundary_candidate | False | None | 0.589 | 1 |
| zh056 | zh_long_span_boundary_candidate | False | None | 0.43 | 1 |
| zh057 | zh_long_span_boundary_candidate | False | None | 0.141 | 1 |
| zh058 | zh_long_span_boundary_candidate | True | 1 | 0.726 | 1 |
| zh059 | zh_long_span_boundary_candidate | False | None | 0.6 | 1 |
| zh060 | zh_long_span_boundary_candidate | False | None | 0.327 | 1 |
| zh061 | zh_long_span_boundary_candidate | False | None | 0.392 | 1 |
| zh062 | zh_long_span_boundary_candidate | False | None | 0.426 | 1 |
| zh063 | zh_long_span_boundary_candidate | False | None | 0.534 | 1 |
| zh064 | zh_long_span_boundary_candidate | False | None | 0.639 | 1 |
| zh065 | zh_long_span_boundary_candidate | False | None | 0.594 | 1 |
| zh066 | zh_long_span_boundary_candidate | False | None | 0.567 | 1 |
| zh067 | zh_long_span_boundary_candidate | False | None | 0.372 | 1 |
| zh068 | zh_long_span_boundary_candidate | False | None | 0.526 | 1 |
| zh069 | zh_long_span_boundary_candidate | False | None | 0.64 | 1 |
| zh070 | zh_long_span_boundary_candidate | False | None | 0.54 | 1 |
| zh071 | zh_long_span_boundary_candidate | False | None | 0.596 | 1 |
| zh072 | zh_long_span_boundary_candidate | False | None | 0.43 | 1 |
| zh073 | zh_long_span_boundary_candidate | False | None | 0.534 | 1 |
| zh074 | zh_long_span_boundary_candidate | False | None | 0.572 | 1 |
| zh075 | zh_long_span_boundary_candidate | False | None | 0.311 | 1 |
| zh076 | zh_long_span_boundary_candidate | False | None | 0.639 | 1 |
| zh077 | zh_long_span_boundary_candidate | False | None | 0.604 | 1 |
| zh078 | zh_long_span_boundary_candidate | False | None | 0.583 | 1 |
| zh079 | zh_long_span_boundary_candidate | False | None | 0.509 | 1 |
| zh080 | zh_long_span_boundary_candidate | True | 2 | 0.657 | 1 |
| zh081 | zh_long_span_boundary_candidate | False | None | 0.599 | 2 |
| zh082 | zh_long_span_boundary_candidate | False | None | 0.321 | 1 |
| zh083 | zh_long_span_boundary_candidate | False | None | 0.637 | 1 |
| zh084 | zh_long_span_boundary_candidate | True | 1 | 0.752 | 1 |
| zh085 | zh_long_span_boundary_candidate | False | None | 0.207 | 1 |
| zh086 | zh_long_span_boundary_candidate | False | None | 0.433 | 1 |
| zh087 | zh_long_span_boundary_candidate | False | None | 0.292 | 1 |
| zh088 | zh_long_span_boundary_candidate | False | None | 0.617 | 1 |
| zh089 | zh_long_span_boundary_candidate | False | None | 0.536 | 1 |
| zh090 | zh_long_span_boundary_candidate | False | None | 0.545 | 1 |
| zh091 | zh_long_span_boundary_candidate | True | 3 | 0.675 | 1 |
| zh092 | zh_long_span_boundary_candidate | False | None | 0.567 | 1 |
| zh093 | zh_long_span_boundary_candidate | False | None | 0.19 | 1 |
| zh094 | zh_long_span_boundary_candidate | False | None | 0.062 | 1 |
| zh095 | zh_long_span_boundary_candidate | False | None | 0.605 | 1 |
| zh096 | zh_long_span_boundary_candidate | False | None | 0.574 | 1 |
| zh097 | zh_long_span_boundary_candidate | False | None | 0.549 | 1 |
| zh098 | zh_long_span_boundary_candidate | True | 3 | 0.713 | 1 |
| zh099 | zh_long_span_boundary_candidate | False | None | 0.606 | 1 |
| zh100 | zh_long_span_boundary_candidate | False | None | 0.559 | 1 |
| zh101 | zh_long_span_boundary_candidate | False | None | 0.599 | 1 |
| zh102 | zh_long_span_boundary_candidate | False | None | 0.631 | 1 |
| zh103 | zh_long_span_boundary_candidate | False | None | 0.593 | 1 |
| zh104 | zh_long_span_boundary_candidate | True | 4 | 0.73 | 1 |
| zh105 | zh_long_span_boundary_candidate | True | 1 | 0.659 | 1 |
| zh106 | zh_long_span_boundary_candidate | False | None | 0.313 | 1 |
| zh107 | zh_long_span_boundary_candidate | True | 3 | 0.668 | 1 |
| zh108 | zh_long_span_boundary_candidate | False | None | 0.372 | 1 |
| zh109 | zh_long_span_boundary_candidate | False | None | 0.647 | 1 |
| zh110 | zh_long_span_boundary_candidate | False | None | 0.61 | 1 |
| zh111 | zh_long_span_boundary_candidate | False | None | 0.544 | 1 |
| zh112 | zh_long_span_boundary_candidate | False | None | 0.429 | 1 |
| zh113 | zh_long_span_boundary_candidate | False | None | 0.138 | 1 |
| zh114 | zh_long_span_boundary_candidate | False | None | 0.628 | 1 |
| zh115 | zh_long_span_boundary_candidate | True | 5 | 0.678 | 1 |
| zh116 | zh_long_span_boundary_candidate | True | 2 | 0.782 | 1 |
| zh117 | zh_long_span_boundary_candidate | False | None | 0.287 | 1 |
| zh118 | zh_long_span_boundary_candidate | False | None | 0.433 | 1 |
| zh119 | zh_long_span_boundary_candidate | False | None | 0.534 | 1 |
| zh120 | zh_long_span_boundary_candidate | True | 4 | 0.725 | 1 |
