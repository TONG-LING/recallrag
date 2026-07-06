# Dense + BM25 -> RRF -> Rerank Report

## Config

- **index**: `runs/zh120_base`
- **questions**: `case_zh_dureader_120/eval/questions_patch_source.jsonl`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`
- **top_k**: `5`
- **dense_k**: `20`
- **bm25_k**: `20`
- **candidate_k**: `20`
- **rrf_k**: `60`
- **coverage_threshold**: `0.65`
- **reranker_model_path**: `/mnt/d/projects/hf_models/BAAI__bge-reranker-v2-m3`
- **reranker_device**: `cuda:0`
- **reranker_batch_size**: `8`
- **reranker_max_length**: `512`
- **hyde_enabled**: `False`
- **hyde_model**: ``
- **hyde_endpoint**: ``
- **hyde_protocol**: ``
- **hyde_auth_mode**: ``
- **hyde_disable_thinking**: `False`

## Metrics

- **total**: 120
- **fusion_recall@5**: 0.1083
- **recall@5**: 0.1333
- **fusion_mrr**: 0.0390
- **mrr**: 0.0822
- **fusion_hits_before_rerank**: 13
- **hits**: 16
- **failed**: 104
- **rerank_fixed**: 4
- **rerank_improved**: 11
- **dense_k**: 20
- **bm25_k**: 20
- **candidate_k**: 20
- **rrf_k**: 60
- **coverage_threshold**: 0.6500
- **hyde_enabled**: False

## Fixed By Rerank

### zh086 — zh_long_span_boundary_candidate
- question: mathematica怎么求积分
- before rank: None
- after rank: 2
- before best_topk_coverage: 0.482
- after best_topk_coverage: 0.656
- top results after rerank:
  - rank 1: `zh_doc_086.md::c0004` rerank_score=4.761719 pre_rerank_rank=2 cov=0.482
  - rank 2: `zh_doc_086.md::c0005` rerank_score=3.677734 pre_rerank_rank=7 cov=0.656
  - rank 3: `zh_doc_086.md::c0006` rerank_score=2.949219 pre_rerank_rank=6 cov=0.527
  - rank 4: `zh_doc_086.md::c0007` rerank_score=2.542969 pre_rerank_rank=8 cov=0.192
  - rank 5: `zh_doc_086.md::c0003` rerank_score=1.264648 pre_rerank_rank=3 cov=0.121

### zh092 — zh_long_span_boundary_candidate
- question: 北京市公务员一年考几次
- before rank: None
- after rank: 2
- before best_topk_coverage: 0.567
- after best_topk_coverage: 0.662
- top results after rerank:
  - rank 1: `zh_doc_092.md::c0003` rerank_score=3.609375 pre_rerank_rank=3 cov=0.567
  - rank 2: `zh_doc_092.md::c0006` rerank_score=3.310547 pre_rerank_rank=8 cov=0.662
  - rank 3: `zh_doc_092.md::c0004` rerank_score=2.634766 pre_rerank_rank=1 cov=0.393
  - rank 4: `zh_doc_092.md::c0001` rerank_score=2.574219 pre_rerank_rank=9 cov=0.279
  - rank 5: `zh_doc_092.md::c0008` rerank_score=2.523438 pre_rerank_rank=7 cov=0.59

### zh107 — zh_long_span_boundary_candidate
- question: 金匮肾气丸要吃多长时间
- before rank: None
- after rank: 2
- before best_topk_coverage: 0.529
- after best_topk_coverage: 0.665
- top results after rerank:
  - rank 1: `zh_doc_107.md::c0007` rerank_score=7.238281 pre_rerank_rank=5 cov=0.16
  - rank 2: `zh_doc_107.md::c0018` rerank_score=7.222656 pre_rerank_rank=7 cov=0.665
  - rank 3: `zh_doc_107.md::c0005` rerank_score=6.421875 pre_rerank_rank=10 cov=0.28
  - rank 4: `zh_doc_107.md::c0019` rerank_score=5.800781 pre_rerank_rank=1 cov=0.271
  - rank 5: `zh_doc_107.md::c0001` rerank_score=5.410156 pre_rerank_rank=19 cov=0.354

### zh108 — zh_long_span_boundary_candidate
- question: 肩颈僵硬
- before rank: None
- after rank: 3
- before best_topk_coverage: 0.205
- after best_topk_coverage: 0.674
- top results after rerank:
  - rank 1: `zh_doc_108.md::c0002` rerank_score=4.058594 pre_rerank_rank=2 cov=0.205
  - rank 2: `zh_doc_108.md::c0000` rerank_score=3.095703 pre_rerank_rank=1 cov=0.045
  - rank 3: `zh_doc_108.md::c0003` rerank_score=2.195312 pre_rerank_rank=9 cov=0.674
  - rank 4: `zh_doc_108.md::c0007` rerank_score=1.446289 pre_rerank_rank=6 cov=0.087
  - rank 5: `zh_doc_108.md::c0001` rerank_score=1.358398 pre_rerank_rank=4 cov=0.056

## Still Failed After Rerank

### zh001 — zh_long_span_boundary_candidate
- question: 高速公路超速20以上不足50扣几分
- before rank: None
- after rank: None
- before best_topk_coverage: 0.646
- after best_topk_coverage: 0.646

### zh002 — zh_long_span_boundary_candidate
- question: 空气净化器哪种净化方式好
- before rank: None
- after rank: None
- before best_topk_coverage: 0.19
- after best_topk_coverage: 0.19

### zh003 — zh_long_span_boundary_candidate
- question: 黄山风景古诗赞
- before rank: None
- after rank: None
- before best_topk_coverage: 0.206
- after best_topk_coverage: 0.206

### zh004 — zh_long_span_boundary_candidate
- question: 一天放很多屁
- before rank: None
- after rank: None
- before best_topk_coverage: 0.274
- after best_topk_coverage: 0.274

### zh005 — zh_long_span_boundary_candidate
- question: 叉车有几种
- before rank: None
- after rank: None
- before best_topk_coverage: 0.361
- after best_topk_coverage: 0.361

### zh006 — zh_long_span_boundary_candidate
- question: 春光成语
- before rank: None
- after rank: None
- before best_topk_coverage: 0.31
- after best_topk_coverage: 0.337

### zh007 — zh_long_span_boundary_candidate
- question: 经常用肥皂洗脸好吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.33
- after best_topk_coverage: 0.346

### zh008 — zh_long_span_boundary_candidate
- question: 冬天怎样养鹦鹉
- before rank: None
- after rank: None
- before best_topk_coverage: 0.183
- after best_topk_coverage: 0.276

### zh009 — zh_long_span_boundary_candidate
- question: 附睾肿胀
- before rank: None
- after rank: None
- before best_topk_coverage: 0.446
- after best_topk_coverage: 0.446

### zh010 — zh_long_span_boundary_candidate
- question: 硫磺皂能长期用吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.075
- after best_topk_coverage: 0.075

### zh011 — zh_long_span_boundary_candidate
- question: 比较好看的电视剧
- before rank: None
- after rank: None
- before best_topk_coverage: 0.19
- after best_topk_coverage: 0.19

### zh012 — zh_long_span_boundary_candidate
- question: 夏天喝什么饮品好
- before rank: None
- after rank: None
- before best_topk_coverage: 0.401
- after best_topk_coverage: 0.307

### zh013 — zh_long_span_boundary_candidate
- question: workgroup是什么
- before rank: None
- after rank: None
- before best_topk_coverage: 0.351
- after best_topk_coverage: 0.42

### zh014 — zh_long_span_boundary_candidate
- question: 怎样锻炼肺活量
- before rank: None
- after rank: None
- before best_topk_coverage: 0.336
- after best_topk_coverage: 0.336

### zh015 — zh_long_span_boundary_candidate
- question: 做胃镜注意
- before rank: None
- after rank: None
- before best_topk_coverage: 0.462
- after best_topk_coverage: 0.433

### zh016 — zh_long_span_boundary_candidate
- question: 油电混合动力汽车购置税优惠吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.405
- after best_topk_coverage: 0.405

### zh017 — zh_long_span_boundary_candidate
- question: 阴部变白
- before rank: None
- after rank: None
- before best_topk_coverage: 0.321
- after best_topk_coverage: 0.339

### zh018 — zh_long_span_boundary_candidate
- question: 如何买卖etf基金
- before rank: None
- after rank: None
- before best_topk_coverage: 0.289
- after best_topk_coverage: 0.289

### zh019 — zh_long_span_boundary_candidate
- question: 在实习期内的驾驶证扣分会怎样
- before rank: None
- after rank: None
- before best_topk_coverage: 0.579
- after best_topk_coverage: 0.432

### zh020 — zh_long_span_boundary_candidate
- question: 私立大学和公立大学的区别
- before rank: None
- after rank: None
- before best_topk_coverage: 0.124
- after best_topk_coverage: 0.101

### zh021 — zh_long_span_boundary_candidate
- question: 如何调水表数字
- before rank: None
- after rank: None
- before best_topk_coverage: 0.325
- after best_topk_coverage: 0.325

### zh022 — zh_long_span_boundary_candidate
- question: 怎样种香菜
- before rank: None
- after rank: None
- before best_topk_coverage: 0.386
- after best_topk_coverage: 0.386

### zh023 — zh_long_span_boundary_candidate
- question: 如何把电脑上的东西传到ipad上
- before rank: None
- after rank: None
- before best_topk_coverage: 0.472
- after best_topk_coverage: 0.472

### zh024 — zh_long_span_boundary_candidate
- question: c1扣12分怎么办
- before rank: None
- after rank: None
- before best_topk_coverage: 0.41
- after best_topk_coverage: 0.375

### zh025 — zh_long_span_boundary_candidate
- question: tf与sd卡的区别
- before rank: None
- after rank: None
- before best_topk_coverage: 0.429
- after best_topk_coverage: 0.33

### zh026 — zh_long_span_boundary_candidate
- question: 左肾部位疼痛
- before rank: None
- after rank: None
- before best_topk_coverage: 0.487
- after best_topk_coverage: 0.487

### zh027 — zh_long_span_boundary_candidate
- question: 小米平板钢化膜怎么贴
- before rank: None
- after rank: None
- before best_topk_coverage: 0.037
- after best_topk_coverage: 0.395

### zh028 — zh_long_span_boundary_candidate
- question: 怎么控制路由器把蹭wifi的人给踢了
- before rank: None
- after rank: None
- before best_topk_coverage: 0.264
- after best_topk_coverage: 0.606

### zh029 — zh_long_span_boundary_candidate
- question: 怎么做卫浴销售
- before rank: None
- after rank: None
- before best_topk_coverage: 0.445
- after best_topk_coverage: 0.524

### zh030 — zh_long_span_boundary_candidate
- question: 外伤缝针不能吃什么
- before rank: None
- after rank: None
- before best_topk_coverage: 0.226
- after best_topk_coverage: 0.289

### zh031 — zh_long_span_boundary_candidate
- question: 超级会员是什么
- before rank: None
- after rank: None
- before best_topk_coverage: 0.517
- after best_topk_coverage: 0.552

### zh032 — zh_long_span_boundary_candidate
- question: 杭州劳动仲裁电话
- before rank: None
- after rank: None
- before best_topk_coverage: 0.236
- after best_topk_coverage: 0.236

### zh033 — zh_long_span_boundary_candidate
- question: 电暖桌哪个牌子好
- before rank: None
- after rank: None
- before best_topk_coverage: 0.349
- after best_topk_coverage: 0.349

### zh034 — zh_long_span_boundary_candidate
- question: 板栗可以蒸着吃吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.49
- after best_topk_coverage: 0.49

### zh035 — zh_long_span_boundary_candidate
- question: 没越狱的iphone怎么清理垃圾
- before rank: None
- after rank: None
- before best_topk_coverage: 0.424
- after best_topk_coverage: 0.424

### zh036 — zh_long_span_boundary_candidate
- question: 苹果系统怎么查看隐藏文件
- before rank: None
- after rank: None
- before best_topk_coverage: 0.525
- after best_topk_coverage: 0.525

### zh037 — zh_long_span_boundary_candidate
- question: 海淀医院孕前检查
- before rank: None
- after rank: None
- before best_topk_coverage: 0.44
- after best_topk_coverage: 0.44

### zh038 — zh_long_span_boundary_candidate
- question: 玩梦幻西游怎么赚钱
- before rank: None
- after rank: None
- before best_topk_coverage: 0.494
- after best_topk_coverage: 0.279

### zh039 — zh_long_span_boundary_candidate
- question: 跟庐山有关的诗句
- before rank: None
- after rank: None
- before best_topk_coverage: 0.486
- after best_topk_coverage: 0.267

### zh040 — zh_long_span_boundary_candidate
- question: 现在去哪里下载音乐
- before rank: None
- after rank: None
- before best_topk_coverage: 0.456
- after best_topk_coverage: 0.493

### zh041 — zh_long_span_boundary_candidate
- question: 治疗颈椎病药物
- before rank: None
- after rank: None
- before best_topk_coverage: 0.419
- after best_topk_coverage: 0.419

### zh042 — zh_long_span_boundary_candidate
- question: 户外手电筒什么牌子好
- before rank: None
- after rank: None
- before best_topk_coverage: 0.411
- after best_topk_coverage: 0.411

### zh044 — zh_long_span_boundary_candidate
- question: 换外汇哪个银行好
- before rank: None
- after rank: None
- before best_topk_coverage: 0.541
- after best_topk_coverage: 0.541

### zh045 — zh_long_span_boundary_candidate
- question: 轻型羽绒服什么牌子好
- before rank: None
- after rank: None
- before best_topk_coverage: 0.536
- after best_topk_coverage: 0.521

### zh046 — zh_long_span_boundary_candidate
- question: 手机外放进水
- before rank: None
- after rank: None
- before best_topk_coverage: 0.316
- after best_topk_coverage: 0.454

### zh047 — zh_long_span_boundary_candidate
- question: 什么样的借条不具法律效力
- before rank: None
- after rank: None
- before best_topk_coverage: 0.6
- after best_topk_coverage: 0.422

### zh048 — zh_long_span_boundary_candidate
- question: m8a1用什么炮
- before rank: None
- after rank: None
- before best_topk_coverage: 0.472
- after best_topk_coverage: 0.472

### zh049 — zh_long_span_boundary_candidate
- question: 西安人流手术费用要多少
- before rank: None
- after rank: None
- before best_topk_coverage: 0.583
- after best_topk_coverage: 0.583

### zh050 — zh_long_span_boundary_candidate
- question: xm外汇平台怎么样
- before rank: None
- after rank: None
- before best_topk_coverage: 0.265
- after best_topk_coverage: 0.265

### zh051 — zh_long_span_boundary_candidate
- question: 双人床最小宽度
- before rank: None
- after rank: None
- before best_topk_coverage: 0.533
- after best_topk_coverage: 0.316

### zh052 — zh_long_span_boundary_candidate
- question: 生气时喂奶
- before rank: None
- after rank: None
- before best_topk_coverage: 0.482
- after best_topk_coverage: 0.5

### zh053 — zh_long_span_boundary_candidate
- question: 龟头敏感度低怎么办
- before rank: None
- after rank: None
- before best_topk_coverage: 0.241
- after best_topk_coverage: 0.481

### zh054 — zh_long_span_boundary_candidate
- question: 沪陕高速限速多少
- before rank: None
- after rank: None
- before best_topk_coverage: 0.552
- after best_topk_coverage: 0.552

### zh055 — zh_long_span_boundary_candidate
- question: ios9 如何关闭搜索最近联系人
- before rank: None
- after rank: None
- before best_topk_coverage: 0.611
- after best_topk_coverage: 0.611

### zh056 — zh_long_span_boundary_candidate
- question: 尸兄主角能力
- before rank: None
- after rank: None
- before best_topk_coverage: 0.51
- after best_topk_coverage: 0.51

### zh057 — zh_long_span_boundary_candidate
- question: word怎么不能修改
- before rank: None
- after rank: None
- before best_topk_coverage: 0.234
- after best_topk_coverage: 0.546

### zh058 — zh_long_span_boundary_candidate
- question: 我国古代第一个有伟大成就的爱国诗人是( )
- before rank: None
- after rank: None
- before best_topk_coverage: 0.25
- after best_topk_coverage: 0.25

### zh060 — zh_long_span_boundary_candidate
- question: 氨端聚二甲基硅氧烷是硅油吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.27
- after best_topk_coverage: 0.619

### zh061 — zh_long_span_boundary_candidate
- question: 为什么中国必须守住18亿亩耕地红线
- before rank: None
- after rank: None
- before best_topk_coverage: 0.342
- after best_topk_coverage: 0.497

### zh062 — zh_long_span_boundary_candidate
- question: 如何取消电脑的自动休眠
- before rank: None
- after rank: None
- before best_topk_coverage: 0.506
- after best_topk_coverage: 0.253

### zh063 — zh_long_span_boundary_candidate
- question: 象征孩子纯洁的花
- before rank: None
- after rank: None
- before best_topk_coverage: 0.526
- after best_topk_coverage: 0.581

### zh064 — zh_long_span_boundary_candidate
- question: 血清甘油三脂偏低
- before rank: None
- after rank: None
- before best_topk_coverage: 0.639
- after best_topk_coverage: 0.639

### zh065 — zh_long_span_boundary_candidate
- question: 哪种制氧机好
- before rank: None
- after rank: None
- before best_topk_coverage: 0.581
- after best_topk_coverage: 0.581

### zh066 — zh_long_span_boundary_candidate
- question: 电动牙刷刷的干净吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.567
- after best_topk_coverage: 0.567

### zh067 — zh_long_span_boundary_candidate
- question: 武松属什么
- before rank: None
- after rank: None
- before best_topk_coverage: 0.432
- after best_topk_coverage: 0.432

### zh068 — zh_long_span_boundary_candidate
- question: 跳鬼步舞时手怎么动
- before rank: None
- after rank: None
- before best_topk_coverage: 0.553
- after best_topk_coverage: 0.553

### zh069 — zh_long_span_boundary_candidate
- question: would like的回答
- before rank: None
- after rank: None
- before best_topk_coverage: 0.64
- after best_topk_coverage: 0.64

### zh070 — zh_long_span_boundary_candidate
- question: qq经常掉线怎么回事
- before rank: None
- after rank: None
- before best_topk_coverage: 0.095
- after best_topk_coverage: 0.375

### zh071 — zh_long_span_boundary_candidate
- question: 还珠格格第一部背景音乐
- before rank: None
- after rank: None
- before best_topk_coverage: 0.244
- after best_topk_coverage: 0.617

### zh072 — zh_long_span_boundary_candidate
- question: 我的世界手机版0.12.1末地传送门怎么做
- before rank: None
- after rank: None
- before best_topk_coverage: 0.466
- after best_topk_coverage: 0.57

### zh073 — zh_long_span_boundary_candidate
- question: 三壬行化妆学校好吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.534
- after best_topk_coverage: 0.534

### zh074 — zh_long_span_boundary_candidate
- question: 胃功能
- before rank: None
- after rank: None
- before best_topk_coverage: 0.17
- after best_topk_coverage: 0.595

### zh075 — zh_long_span_boundary_candidate
- question: 艾俐缇陶瓷怎么样
- before rank: None
- after rank: None
- before best_topk_coverage: 0.137
- after best_topk_coverage: 0.137

### zh076 — zh_long_span_boundary_candidate
- question: 公共事业管理属于什么专业类别
- before rank: None
- after rank: None
- before best_topk_coverage: 0.567
- after best_topk_coverage: 0.567

### zh077 — zh_long_span_boundary_candidate
- question: 天然无添加的护肤品存在吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.584
- after best_topk_coverage: 0.584

### zh078 — zh_long_span_boundary_candidate
- question: 旅行发票 可以报吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.578
- after best_topk_coverage: 0.559

### zh079 — zh_long_span_boundary_candidate
- question: 种子可以用百度云下载吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.527
- after best_topk_coverage: 0.527

### zh080 — zh_long_span_boundary_candidate
- question: ipad能否连接打印机
- before rank: None
- after rank: None
- before best_topk_coverage: 0.545
- after best_topk_coverage: 0.545

### zh081 — zh_long_span_boundary_candidate
- question: 手机钢化保护膜怎么贴
- before rank: None
- after rank: None
- before best_topk_coverage: 0.588
- after best_topk_coverage: 0.588

### zh082 — zh_long_span_boundary_candidate
- question: 中国古代最繁荣的朝代
- before rank: None
- after rank: None
- before best_topk_coverage: 0.498
- after best_topk_coverage: 0.09

### zh083 — zh_long_span_boundary_candidate
- question: 怎么改民族
- before rank: None
- after rank: None
- before best_topk_coverage: 0.428
- after best_topk_coverage: 0.637

### zh085 — zh_long_span_boundary_candidate
- question: 白带有酸奶味
- before rank: None
- after rank: None
- before best_topk_coverage: 0.371
- after best_topk_coverage: 0.111

### zh087 — zh_long_span_boundary_candidate
- question: 晾衣架材质
- before rank: None
- after rank: None
- before best_topk_coverage: 0.542
- after best_topk_coverage: 0.542

### zh088 — zh_long_span_boundary_candidate
- question: 如何遮盖唇色
- before rank: None
- after rank: None
- before best_topk_coverage: 0.605
- after best_topk_coverage: 0.605

### zh089 — zh_long_span_boundary_candidate
- question: 部落冲突怎么搜死鱼
- before rank: None
- after rank: None
- before best_topk_coverage: 0.456
- after best_topk_coverage: 0.456

### zh090 — zh_long_span_boundary_candidate
- question: 牛剖层移膜皮是什么
- before rank: None
- after rank: None
- before best_topk_coverage: 0.404
- after best_topk_coverage: 0.404

### zh093 — zh_long_span_boundary_candidate
- question: 成都审驾照需要什么
- before rank: None
- after rank: None
- before best_topk_coverage: 0.333
- after best_topk_coverage: 0.333

### zh094 — zh_long_span_boundary_candidate
- question: 霜是怎么形成的
- before rank: None
- after rank: None
- before best_topk_coverage: 0.159
- after best_topk_coverage: 0.528

### zh095 — zh_long_span_boundary_candidate
- question: 卫生间铺什么地砖好
- before rank: None
- after rank: None
- before best_topk_coverage: 0.576
- after best_topk_coverage: 0.576

### zh096 — zh_long_span_boundary_candidate
- question: 肠结核的症状
- before rank: None
- after rank: None
- before best_topk_coverage: 0.557
- after best_topk_coverage: 0.557

### zh097 — zh_long_span_boundary_candidate
- question: 表带怎么打孔
- before rank: None
- after rank: None
- before best_topk_coverage: 0.407
- after best_topk_coverage: 0.526

### zh099 — zh_long_span_boundary_candidate
- question: 水土流失是什么意思
- before rank: None
- after rank: None
- before best_topk_coverage: 0.626
- after best_topk_coverage: 0.626

### zh100 — zh_long_span_boundary_candidate
- question: 红枣表面有层白色粉末
- before rank: None
- after rank: None
- before best_topk_coverage: 0.58
- after best_topk_coverage: 0.58

### zh101 — zh_long_span_boundary_candidate
- question: 小米的平板好用吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.096
- after best_topk_coverage: 0.577

### zh102 — zh_long_span_boundary_candidate
- question: 尺神经麻痹治疗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.164
- after best_topk_coverage: 0.524

### zh103 — zh_long_span_boundary_candidate
- question: 北京出国体检在哪里
- before rank: None
- after rank: None
- before best_topk_coverage: 0.623
- after best_topk_coverage: 0.623

### zh106 — zh_long_span_boundary_candidate
- question: 原地跑步能减肚子吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.361
- after best_topk_coverage: 0.361

### zh110 — zh_long_span_boundary_candidate
- question: 完美世界出过什么游戏
- before rank: None
- after rank: None
- before best_topk_coverage: 0.607
- after best_topk_coverage: 0.607

### zh112 — zh_long_span_boundary_candidate
- question: 为什么qq打不开图片
- before rank: None
- after rank: None
- before best_topk_coverage: 0.35
- after best_topk_coverage: 0.613

### zh113 — zh_long_span_boundary_candidate
- question: 辅酶q10的服用方法
- before rank: None
- after rank: None
- before best_topk_coverage: 0.52
- after best_topk_coverage: 0.625

### zh117 — zh_long_span_boundary_candidate
- question: 德国红铁元和绿铁元有什么区别
- before rank: None
- after rank: None
- before best_topk_coverage: 0.227
- after best_topk_coverage: 0.626

### zh118 — zh_long_span_boundary_candidate
- question: 诛仙法宝技能怎么洗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.354
- after best_topk_coverage: 0.274

### zh119 — zh_long_span_boundary_candidate
- question: 神秘博士clara是谁
- before rank: None
- after rank: None
- before best_topk_coverage: 0.534
- after best_topk_coverage: 0.534

### zh120 — zh_long_span_boundary_candidate
- question: 保妇康栓要用多久
- before rank: 3
- after rank: None
- before best_topk_coverage: 0.67
- after best_topk_coverage: 0.399

## All Query Summary

| qid | success before | success after | rank before | rank after | rerank fixed | rerank improved |
|---|---:|---:|---:|---:|---:|---:|
| zh001 | False | False | None | None | False | False |
| zh002 | False | False | None | None | False | False |
| zh003 | False | False | None | None | False | False |
| zh004 | False | False | None | None | False | False |
| zh005 | False | False | None | None | False | False |
| zh006 | False | False | None | None | False | False |
| zh007 | False | False | None | None | False | False |
| zh008 | False | False | None | None | False | False |
| zh009 | False | False | None | None | False | False |
| zh010 | False | False | None | None | False | False |
| zh011 | False | False | None | None | False | False |
| zh012 | False | False | None | None | False | False |
| zh013 | False | False | None | None | False | False |
| zh014 | False | False | None | None | False | False |
| zh015 | False | False | None | None | False | False |
| zh016 | False | False | None | None | False | False |
| zh017 | False | False | None | None | False | False |
| zh018 | False | False | None | None | False | False |
| zh019 | False | False | None | None | False | False |
| zh020 | False | False | None | None | False | False |
| zh021 | False | False | None | None | False | False |
| zh022 | False | False | None | None | False | False |
| zh023 | False | False | None | None | False | False |
| zh024 | False | False | None | None | False | False |
| zh025 | False | False | None | None | False | False |
| zh026 | False | False | None | None | False | False |
| zh027 | False | False | None | None | False | False |
| zh028 | False | False | None | None | False | False |
| zh029 | False | False | None | None | False | False |
| zh030 | False | False | None | None | False | False |
| zh031 | False | False | None | None | False | False |
| zh032 | False | False | None | None | False | False |
| zh033 | False | False | None | None | False | False |
| zh034 | False | False | None | None | False | False |
| zh035 | False | False | None | None | False | False |
| zh036 | False | False | None | None | False | False |
| zh037 | False | False | None | None | False | False |
| zh038 | False | False | None | None | False | False |
| zh039 | False | False | None | None | False | False |
| zh040 | False | False | None | None | False | False |
| zh041 | False | False | None | None | False | False |
| zh042 | False | False | None | None | False | False |
| zh043 | True | True | 4 | 1 | False | True |
| zh044 | False | False | None | None | False | False |
| zh045 | False | False | None | None | False | False |
| zh046 | False | False | None | None | False | False |
| zh047 | False | False | None | None | False | False |
| zh048 | False | False | None | None | False | False |
| zh049 | False | False | None | None | False | False |
| zh050 | False | False | None | None | False | False |
| zh051 | False | False | None | None | False | False |
| zh052 | False | False | None | None | False | False |
| zh053 | False | False | None | None | False | False |
| zh054 | False | False | None | None | False | False |
| zh055 | False | False | None | None | False | False |
| zh056 | False | False | None | None | False | False |
| zh057 | False | False | None | None | False | False |
| zh058 | False | False | None | None | False | False |
| zh059 | True | True | 5 | 3 | False | True |
| zh060 | False | False | None | None | False | False |
| zh061 | False | False | None | None | False | False |
| zh062 | False | False | None | None | False | False |
| zh063 | False | False | None | None | False | False |
| zh064 | False | False | None | None | False | False |
| zh065 | False | False | None | None | False | False |
| zh066 | False | False | None | None | False | False |
| zh067 | False | False | None | None | False | False |
| zh068 | False | False | None | None | False | False |
| zh069 | False | False | None | None | False | False |
| zh070 | False | False | None | None | False | False |
| zh071 | False | False | None | None | False | False |
| zh072 | False | False | None | None | False | False |
| zh073 | False | False | None | None | False | False |
| zh074 | False | False | None | None | False | False |
| zh075 | False | False | None | None | False | False |
| zh076 | False | False | None | None | False | False |
| zh077 | False | False | None | None | False | False |
| zh078 | False | False | None | None | False | False |
| zh079 | False | False | None | None | False | False |
| zh080 | False | False | None | None | False | False |
| zh081 | False | False | None | None | False | False |
| zh082 | False | False | None | None | False | False |
| zh083 | False | False | None | None | False | False |
| zh084 | True | True | 3 | 1 | False | True |
| zh085 | False | False | None | None | False | False |
| zh086 | False | True | None | 2 | True | True |
| zh087 | False | False | None | None | False | False |
| zh088 | False | False | None | None | False | False |
| zh089 | False | False | None | None | False | False |
| zh090 | False | False | None | None | False | False |
| zh091 | True | True | 3 | 1 | False | True |
| zh092 | False | True | None | 2 | True | True |
| zh093 | False | False | None | None | False | False |
| zh094 | False | False | None | None | False | False |
| zh095 | False | False | None | None | False | False |
| zh096 | False | False | None | None | False | False |
| zh097 | False | False | None | None | False | False |
| zh098 | True | True | 2 | 4 | False | False |
| zh099 | False | False | None | None | False | False |
| zh100 | False | False | None | None | False | False |
| zh101 | False | False | None | None | False | False |
| zh102 | False | False | None | None | False | False |
| zh103 | False | False | None | None | False | False |
| zh104 | True | True | 5 | 5 | False | False |
| zh105 | True | True | 3 | 2 | False | True |
| zh106 | False | False | None | None | False | False |
| zh107 | False | True | None | 2 | True | True |
| zh108 | False | True | None | 3 | True | True |
| zh109 | True | True | 1 | 1 | False | False |
| zh110 | False | False | None | None | False | False |
| zh111 | True | True | 4 | 4 | False | False |
| zh112 | False | False | None | None | False | False |
| zh113 | False | False | None | None | False | False |
| zh114 | True | True | 2 | 2 | False | False |
| zh115 | True | True | 4 | 1 | False | True |
| zh116 | True | True | 5 | 1 | False | True |
| zh117 | False | False | None | None | False | False |
| zh118 | False | False | None | None | False | False |
| zh119 | False | False | None | None | False | False |
| zh120 | True | False | 3 | None | False | False |
