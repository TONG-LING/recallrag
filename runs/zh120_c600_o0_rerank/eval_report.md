# Dense -> Rerank Report

## Config

- **index**: `runs/zh120_c600_o0_base`
- **questions**: `case_zh_dureader_120/eval/questions_patch_source.jsonl`
- **top_k**: `5`
- **candidate_k**: `20`
- **coverage_threshold**: `0.65`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`
- **reranker_model_path**: `None`
- **reranker_device**: `None`
- **reranker_batch_size**: `8`
- **reranker_max_length**: `512`
- **reranker_use_fp16**: `True`

## Metrics

- **total**: 120
- **dense_recall@5**: 0.8833
- **recall@5**: 0.8750
- **dense_mrr**: 0.5508
- **mrr**: 0.6004
- **dense_hits_before_rerank**: 106
- **hits**: 105
- **failed**: 15
- **rerank_fixed**: 2
- **rerank_improved**: 37
- **rerank_candidate_k**: 20
- **coverage_threshold**: 0.6500

## Fixed By Rerank

### zh027 — zh_long_span_boundary_candidate
- question: 小米平板钢化膜怎么贴
- before rank: None
- after rank: 3
- before best_topk_coverage: 0.305
- after best_topk_coverage: 0.904
- top results after rerank:
  - rank 1: `zh_doc_027.md::c0003` rerank_score=8.46875 dense_rank=1 cov=0.305
  - rank 2: `zh_doc_027.md::c0000` rerank_score=3.673828 dense_rank=3 cov=0.139
  - rank 3: `zh_doc_027.md::c0002` rerank_score=3.205078 dense_rank=11 cov=0.904
  - rank 4: `zh_doc_081.md::c0002` rerank_score=2.603516 dense_rank=4 cov=0.0
  - rank 5: `zh_doc_027.md::c0001` rerank_score=2.505859 dense_rank=9 cov=0.172

### zh057 — zh_long_span_boundary_candidate
- question: word怎么不能修改
- before rank: None
- after rank: 2
- before best_topk_coverage: 0.423
- after best_topk_coverage: 0.851
- top results after rerank:
  - rank 1: `zh_doc_057.md::c0000` rerank_score=6.15625 dense_rank=1 cov=0.214
  - rank 2: `zh_doc_057.md::c0006` rerank_score=5.664062 dense_rank=6 cov=0.851
  - rank 3: `zh_doc_057.md::c0005` rerank_score=5.351562 dense_rank=4 cov=0.423
  - rank 4: `zh_doc_057.md::c0007` rerank_score=4.082031 dense_rank=2 cov=0.228
  - rank 5: `zh_doc_057.md::c0004` rerank_score=2.507812 dense_rank=3 cov=0.228

## Still Failed After Rerank

### zh002 — zh_long_span_boundary_candidate
- question: 空气净化器哪种净化方式好
- before rank: None
- after rank: None
- before best_topk_coverage: 0.578
- after best_topk_coverage: 0.578

### zh003 — zh_long_span_boundary_candidate
- question: 黄山风景古诗赞
- before rank: None
- after rank: None
- before best_topk_coverage: 0.511
- after best_topk_coverage: 0.511

### zh004 — zh_long_span_boundary_candidate
- question: 一天放很多屁
- before rank: None
- after rank: None
- before best_topk_coverage: 0.576
- after best_topk_coverage: 0.576

### zh006 — zh_long_span_boundary_candidate
- question: 春光成语
- before rank: None
- after rank: None
- before best_topk_coverage: 0.605
- after best_topk_coverage: 0.605

### zh007 — zh_long_span_boundary_candidate
- question: 经常用肥皂洗脸好吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.648
- after best_topk_coverage: 0.648

### zh008 — zh_long_span_boundary_candidate
- question: 冬天怎样养鹦鹉
- before rank: None
- after rank: None
- before best_topk_coverage: 0.623
- after best_topk_coverage: 0.623

### zh010 — zh_long_span_boundary_candidate
- question: 硫磺皂能长期用吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.587
- after best_topk_coverage: 0.587

### zh011 — zh_long_span_boundary_candidate
- question: 比较好看的电视剧
- before rank: None
- after rank: None
- before best_topk_coverage: 0.623
- after best_topk_coverage: 0.623

### zh017 — zh_long_span_boundary_candidate
- question: 阴部变白
- before rank: None
- after rank: None
- before best_topk_coverage: 0.629
- after best_topk_coverage: 0.629

### zh024 — zh_long_span_boundary_candidate
- question: c1扣12分怎么办
- before rank: 5
- after rank: None
- before best_topk_coverage: 0.879
- after best_topk_coverage: 0.539

### zh033 — zh_long_span_boundary_candidate
- question: 电暖桌哪个牌子好
- before rank: None
- after rank: None
- before best_topk_coverage: 0.574
- after best_topk_coverage: 0.574

### zh043 — zh_long_span_boundary_candidate
- question: cfs和cy有什么不同
- before rank: 3
- after rank: None
- before best_topk_coverage: 0.833
- after best_topk_coverage: 0.616

### zh067 — zh_long_span_boundary_candidate
- question: 武松属什么
- before rank: None
- after rank: None
- before best_topk_coverage: 0.646
- after best_topk_coverage: 0.646

### zh081 — zh_long_span_boundary_candidate
- question: 手机钢化保护膜怎么贴
- before rank: 3
- after rank: None
- before best_topk_coverage: 0.726
- after best_topk_coverage: 0.494

### zh101 — zh_long_span_boundary_candidate
- question: 小米的平板好用吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.592
- after best_topk_coverage: 0.592

## All Query Summary

| qid | success before | success after | rank before | rank after | rerank fixed | rerank improved |
|---|---:|---:|---:|---:|---:|---:|
| zh001 | True | True | 2 | 2 | False | False |
| zh002 | False | False | None | None | False | False |
| zh003 | False | False | None | None | False | False |
| zh004 | False | False | None | None | False | False |
| zh005 | True | True | 2 | 4 | False | False |
| zh006 | False | False | None | None | False | False |
| zh007 | False | False | None | None | False | False |
| zh008 | False | False | None | None | False | False |
| zh009 | True | True | 3 | 5 | False | False |
| zh010 | False | False | None | None | False | False |
| zh011 | False | False | None | None | False | False |
| zh012 | True | True | 3 | 4 | False | False |
| zh013 | True | True | 2 | 2 | False | False |
| zh014 | True | True | 4 | 1 | False | True |
| zh015 | True | True | 1 | 1 | False | False |
| zh016 | True | True | 5 | 2 | False | True |
| zh017 | False | False | None | None | False | False |
| zh018 | True | True | 2 | 1 | False | True |
| zh019 | True | True | 2 | 1 | False | True |
| zh020 | True | True | 5 | 5 | False | False |
| zh021 | True | True | 1 | 1 | False | False |
| zh022 | True | True | 1 | 4 | False | False |
| zh023 | True | True | 4 | 2 | False | True |
| zh024 | True | False | 5 | None | False | False |
| zh025 | True | True | 2 | 1 | False | True |
| zh026 | True | True | 1 | 1 | False | False |
| zh027 | False | True | None | 3 | True | True |
| zh028 | True | True | 3 | 3 | False | False |
| zh029 | True | True | 2 | 3 | False | False |
| zh030 | True | True | 5 | 3 | False | True |
| zh031 | True | True | 1 | 1 | False | False |
| zh032 | True | True | 5 | 4 | False | True |
| zh033 | False | False | None | None | False | False |
| zh034 | True | True | 4 | 3 | False | True |
| zh035 | True | True | 3 | 1 | False | True |
| zh036 | True | True | 1 | 1 | False | False |
| zh037 | True | True | 2 | 2 | False | False |
| zh038 | True | True | 3 | 3 | False | False |
| zh039 | True | True | 1 | 3 | False | False |
| zh040 | True | True | 2 | 1 | False | True |
| zh041 | True | True | 3 | 2 | False | True |
| zh042 | True | True | 1 | 1 | False | False |
| zh043 | True | False | 3 | None | False | False |
| zh044 | True | True | 2 | 2 | False | False |
| zh045 | True | True | 2 | 1 | False | True |
| zh046 | True | True | 3 | 2 | False | True |
| zh047 | True | True | 5 | 5 | False | False |
| zh048 | True | True | 2 | 2 | False | False |
| zh049 | True | True | 3 | 2 | False | True |
| zh050 | True | True | 1 | 2 | False | False |
| zh051 | True | True | 1 | 1 | False | False |
| zh052 | True | True | 1 | 1 | False | False |
| zh053 | True | True | 1 | 3 | False | False |
| zh054 | True | True | 2 | 1 | False | True |
| zh055 | True | True | 1 | 1 | False | False |
| zh056 | True | True | 4 | 1 | False | True |
| zh057 | False | True | None | 2 | True | True |
| zh058 | True | True | 3 | 1 | False | True |
| zh059 | True | True | 1 | 3 | False | False |
| zh060 | True | True | 1 | 1 | False | False |
| zh061 | True | True | 2 | 1 | False | True |
| zh062 | True | True | 1 | 1 | False | False |
| zh063 | True | True | 4 | 2 | False | True |
| zh064 | True | True | 1 | 1 | False | False |
| zh065 | True | True | 2 | 3 | False | False |
| zh066 | True | True | 3 | 1 | False | True |
| zh067 | False | False | None | None | False | False |
| zh068 | True | True | 2 | 3 | False | False |
| zh069 | True | True | 2 | 1 | False | True |
| zh070 | True | True | 4 | 2 | False | True |
| zh071 | True | True | 1 | 2 | False | False |
| zh072 | True | True | 1 | 1 | False | False |
| zh073 | True | True | 1 | 1 | False | False |
| zh074 | True | True | 1 | 2 | False | False |
| zh075 | True | True | 3 | 1 | False | True |
| zh076 | True | True | 1 | 1 | False | False |
| zh077 | True | True | 1 | 1 | False | False |
| zh078 | True | True | 3 | 2 | False | True |
| zh079 | True | True | 1 | 1 | False | False |
| zh080 | True | True | 1 | 1 | False | False |
| zh081 | True | False | 3 | None | False | False |
| zh082 | True | True | 4 | 3 | False | True |
| zh083 | True | True | 1 | 1 | False | False |
| zh084 | True | True | 1 | 2 | False | False |
| zh085 | True | True | 3 | 4 | False | False |
| zh086 | True | True | 3 | 2 | False | True |
| zh087 | True | True | 1 | 1 | False | False |
| zh088 | True | True | 2 | 2 | False | False |
| zh089 | True | True | 2 | 2 | False | False |
| zh090 | True | True | 1 | 1 | False | False |
| zh091 | True | True | 1 | 1 | False | False |
| zh092 | True | True | 1 | 2 | False | False |
| zh093 | True | True | 1 | 2 | False | False |
| zh094 | True | True | 3 | 3 | False | False |
| zh095 | True | True | 2 | 3 | False | False |
| zh096 | True | True | 2 | 1 | False | True |
| zh097 | True | True | 1 | 1 | False | False |
| zh098 | True | True | 2 | 2 | False | False |
| zh099 | True | True | 1 | 1 | False | False |
| zh100 | True | True | 1 | 1 | False | False |
| zh101 | False | False | None | None | False | False |
| zh102 | True | True | 5 | 5 | False | False |
| zh103 | True | True | 1 | 1 | False | False |
| zh104 | True | True | 4 | 2 | False | True |
| zh105 | True | True | 1 | 1 | False | False |
| zh106 | True | True | 5 | 2 | False | True |
| zh107 | True | True | 1 | 3 | False | False |
| zh108 | True | True | 3 | 1 | False | True |
| zh109 | True | True | 1 | 1 | False | False |
| zh110 | True | True | 2 | 2 | False | False |
| zh111 | True | True | 1 | 1 | False | False |
| zh112 | True | True | 1 | 1 | False | False |
| zh113 | True | True | 3 | 2 | False | True |
| zh114 | True | True | 1 | 1 | False | False |
| zh115 | True | True | 2 | 1 | False | True |
| zh116 | True | True | 3 | 2 | False | True |
| zh117 | True | True | 3 | 1 | False | True |
| zh118 | True | True | 2 | 2 | False | False |
| zh119 | True | True | 2 | 2 | False | False |
| zh120 | True | True | 2 | 2 | False | False |
