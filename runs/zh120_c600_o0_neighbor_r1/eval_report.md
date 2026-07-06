# Neighbor Expansion Report

## Config

- **index**: `runs/zh120_c600_o0_base`
- **questions**: `case_zh_dureader_120/eval/questions_patch_source.jsonl`
- **top_k**: `5`
- **coverage_threshold**: `0.65`
- **neighbor_radius**: `1`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`

## Metrics

- **total**: 120
- **dense_recall@5**: 0.8833
- **recall@5**: 1.0000
- **dense_mrr**: 0.5508
- **mrr**: 0.9153
- **dense_hits_before_expansion**: 106
- **hits**: 120
- **failed**: 0
- **fixed_by_expansion**: 14
- **coverage_threshold**: 0.6500
- **neighbor_radius**: 1
- **avg_top5_total_chars**: 7597.7833
- **avg_top5_chars_per_item**: 1519.5567
- **avg_top5_merged_chunks**: 2.6017

## Fixed By Neighbor Expansion

### zh002
- question: 空气净化器哪种净化方式好
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.578
- best_topk_coverage after: 0.998

### zh003
- question: 黄山风景古诗赞
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.511
- best_topk_coverage after: 0.999

### zh004
- question: 一天放很多屁
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.576
- best_topk_coverage after: 0.999

### zh006
- question: 春光成语
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.605
- best_topk_coverage after: 0.999

### zh007
- question: 经常用肥皂洗脸好吗
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.648
- best_topk_coverage after: 0.999

### zh008
- question: 冬天怎样养鹦鹉
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.623
- best_topk_coverage after: 1.0

### zh010
- question: 硫磺皂能长期用吗
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.587
- best_topk_coverage after: 1.0

### zh011
- question: 比较好看的电视剧
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.623
- best_topk_coverage after: 1.0

### zh017
- question: 阴部变白
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.629
- best_topk_coverage after: 1.0

### zh027
- question: 小米平板钢化膜怎么贴
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.305
- best_topk_coverage after: 1.0

### zh033
- question: 电暖桌哪个牌子好
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.574
- best_topk_coverage after: 0.998

### zh057
- question: word怎么不能修改
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.423
- best_topk_coverage after: 1.0

### zh067
- question: 武松属什么
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.646
- best_topk_coverage after: 0.997

### zh101
- question: 小米的平板好用吗
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.592
- best_topk_coverage after: 1.0

## Still Failed

No failed queries after neighbor expansion.
## All Query Summary

| qid | success before | success after | rank before | rank after | total chars top-5 |
|---|---:|---:|---:|---:|---:|
| zh001 | True | True | 2 | 2 | 7667 |
| zh002 | False | True | None | 1 | 8258 |
| zh003 | False | True | None | 2 | 8150 |
| zh004 | False | True | None | 1 | 8742 |
| zh005 | True | True | 2 | 1 | 8417 |
| zh006 | False | True | None | 1 | 7926 |
| zh007 | False | True | None | 2 | 7232 |
| zh008 | False | True | None | 1 | 7310 |
| zh009 | True | True | 3 | 1 | 8188 |
| zh010 | False | True | None | 3 | 7567 |
| zh011 | False | True | None | 3 | 7723 |
| zh012 | True | True | 3 | 1 | 8021 |
| zh013 | True | True | 2 | 1 | 8079 |
| zh014 | True | True | 4 | 1 | 7464 |
| zh015 | True | True | 1 | 1 | 7632 |
| zh016 | True | True | 5 | 1 | 7775 |
| zh017 | False | True | None | 1 | 6797 |
| zh018 | True | True | 2 | 1 | 7540 |
| zh019 | True | True | 2 | 1 | 8227 |
| zh020 | True | True | 5 | 1 | 7465 |
| zh021 | True | True | 1 | 1 | 7724 |
| zh022 | True | True | 1 | 1 | 7835 |
| zh023 | True | True | 4 | 1 | 7905 |
| zh024 | True | True | 5 | 2 | 8227 |
| zh025 | True | True | 2 | 1 | 8734 |
| zh026 | True | True | 1 | 1 | 7145 |
| zh027 | False | True | None | 1 | 7136 |
| zh028 | True | True | 3 | 1 | 7046 |
| zh029 | True | True | 2 | 1 | 7584 |
| zh030 | True | True | 5 | 2 | 7935 |
| zh031 | True | True | 1 | 1 | 7023 |
| zh032 | True | True | 5 | 2 | 8272 |
| zh033 | False | True | None | 1 | 7887 |
| zh034 | True | True | 4 | 1 | 7143 |
| zh035 | True | True | 3 | 2 | 6785 |
| zh036 | True | True | 1 | 1 | 7473 |
| zh037 | True | True | 2 | 1 | 6693 |
| zh038 | True | True | 3 | 2 | 7542 |
| zh039 | True | True | 1 | 1 | 7942 |
| zh040 | True | True | 2 | 1 | 7137 |
| zh041 | True | True | 3 | 1 | 7997 |
| zh042 | True | True | 1 | 1 | 7153 |
| zh043 | True | True | 3 | 1 | 8457 |
| zh044 | True | True | 2 | 1 | 6707 |
| zh045 | True | True | 2 | 1 | 8147 |
| zh046 | True | True | 3 | 1 | 7376 |
| zh047 | True | True | 5 | 2 | 7197 |
| zh048 | True | True | 2 | 2 | 7488 |
| zh049 | True | True | 3 | 1 | 7805 |
| zh050 | True | True | 1 | 1 | 6595 |
| zh051 | True | True | 1 | 1 | 8254 |
| zh052 | True | True | 1 | 1 | 6640 |
| zh053 | True | True | 1 | 1 | 8094 |
| zh054 | True | True | 2 | 1 | 8012 |
| zh055 | True | True | 1 | 1 | 6528 |
| zh056 | True | True | 4 | 1 | 7794 |
| zh057 | False | True | None | 2 | 8104 |
| zh058 | True | True | 3 | 1 | 7463 |
| zh059 | True | True | 1 | 1 | 8010 |
| zh060 | True | True | 1 | 1 | 7662 |
| zh061 | True | True | 2 | 1 | 7269 |
| zh062 | True | True | 1 | 1 | 8178 |
| zh063 | True | True | 4 | 1 | 7640 |
| zh064 | True | True | 1 | 1 | 7112 |
| zh065 | True | True | 2 | 1 | 7099 |
| zh066 | True | True | 3 | 1 | 7813 |
| zh067 | False | True | None | 1 | 7115 |
| zh068 | True | True | 2 | 1 | 8741 |
| zh069 | True | True | 2 | 1 | 9037 |
| zh070 | True | True | 4 | 2 | 7320 |
| zh071 | True | True | 1 | 1 | 8743 |
| zh072 | True | True | 1 | 1 | 7271 |
| zh073 | True | True | 1 | 1 | 7562 |
| zh074 | True | True | 1 | 1 | 7964 |
| zh075 | True | True | 3 | 1 | 7464 |
| zh076 | True | True | 1 | 1 | 8031 |
| zh077 | True | True | 1 | 1 | 7794 |
| zh078 | True | True | 3 | 1 | 6889 |
| zh079 | True | True | 1 | 1 | 7226 |
| zh080 | True | True | 1 | 1 | 8743 |
| zh081 | True | True | 3 | 3 | 8268 |
| zh082 | True | True | 4 | 1 | 7286 |
| zh083 | True | True | 1 | 1 | 8070 |
| zh084 | True | True | 1 | 1 | 7706 |
| zh085 | True | True | 3 | 3 | 7628 |
| zh086 | True | True | 3 | 1 | 7255 |
| zh087 | True | True | 1 | 1 | 7820 |
| zh088 | True | True | 2 | 1 | 7769 |
| zh089 | True | True | 2 | 1 | 6295 |
| zh090 | True | True | 1 | 1 | 8736 |
| zh091 | True | True | 1 | 1 | 7977 |
| zh092 | True | True | 1 | 1 | 7375 |
| zh093 | True | True | 1 | 1 | 7662 |
| zh094 | True | True | 3 | 2 | 7471 |
| zh095 | True | True | 2 | 2 | 7464 |
| zh096 | True | True | 2 | 1 | 6908 |
| zh097 | True | True | 1 | 1 | 7084 |
| zh098 | True | True | 2 | 1 | 6962 |
| zh099 | True | True | 1 | 1 | 8195 |
| zh100 | True | True | 1 | 1 | 7807 |
| zh101 | False | True | None | 1 | 8168 |
| zh102 | True | True | 5 | 1 | 7343 |
| zh103 | True | True | 1 | 1 | 7148 |
| zh104 | True | True | 4 | 2 | 7095 |
| zh105 | True | True | 1 | 1 | 8048 |
| zh106 | True | True | 5 | 1 | 8371 |
| zh107 | True | True | 1 | 1 | 8358 |
| zh108 | True | True | 3 | 1 | 6890 |
| zh109 | True | True | 1 | 1 | 8771 |
| zh110 | True | True | 2 | 1 | 6729 |
| zh111 | True | True | 1 | 1 | 6486 |
| zh112 | True | True | 1 | 1 | 6591 |
| zh113 | True | True | 3 | 1 | 7775 |
| zh114 | True | True | 1 | 1 | 5557 |
| zh115 | True | True | 2 | 1 | 7699 |
| zh116 | True | True | 3 | 1 | 7461 |
| zh117 | True | True | 3 | 1 | 6879 |
| zh118 | True | True | 2 | 1 | 6511 |
| zh119 | True | True | 2 | 1 | 7121 |
| zh120 | True | True | 2 | 1 | 7153 |
