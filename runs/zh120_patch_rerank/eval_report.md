# Dense -> Rerank Report

## Config

- **mode**: `main_plus_fixed_patch_rerank`
- **index**: `runs/zh120_base`
- **patch_dir**: `runs/zh120_patches`
- **questions**: `case_zh_dureader_120/eval/questions_patch_source.jsonl`
- **top_k**: `5`
- **candidate_k**: `20`
- **coverage_threshold**: `0.65`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`
- **reranker_model_path**: `/mnt/d/projects/hf_models/BAAI__bge-reranker-v2-m3`
- **reranker_device**: `cuda:0`
- **reranker_batch_size**: `8`
- **reranker_max_length**: `512`
- **reranker_use_fp16**: `True`
- **selected_patch_chunks**: `24`

## Metrics

- **total**: 120
- **dense_recall@5**: 0.3417
- **recall@5**: 0.3250
- **dense_mrr**: 0.1501
- **mrr**: 0.2001
- **dense_hits_before_rerank**: 41
- **hits**: 39
- **failed**: 81
- **rerank_fixed**: 0
- **rerank_improved**: 25
- **rerank_candidate_k**: 20
- **coverage_threshold**: 0.6500

## Fixed By Rerank

No query was fixed by reranking under current candidate_k.
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
- before best_topk_coverage: 0.163
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
- before best_topk_coverage: 0.276
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
- before best_topk_coverage: 0.276
- after best_topk_coverage: 0.276

### zh009 — zh_long_span_boundary_candidate
- question: 附睾肿胀
- before rank: None
- after rank: None
- before best_topk_coverage: 0.42
- after best_topk_coverage: 0.446

### zh010 — zh_long_span_boundary_candidate
- question: 硫磺皂能长期用吗
- before rank: None
- after rank: None
- before best_topk_coverage: 0.277
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
- before best_topk_coverage: 0.365
- after best_topk_coverage: 0.307

### zh013 — zh_long_span_boundary_candidate
- question: workgroup是什么
- before rank: None
- after rank: None
- before best_topk_coverage: 0.395
- after best_topk_coverage: 0.395

### zh014 — zh_long_span_boundary_candidate
- question: 怎样锻炼肺活量
- before rank: None
- after rank: None
- before best_topk_coverage: 0.336
- after best_topk_coverage: 0.336

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
- before best_topk_coverage: 0.429
- after best_topk_coverage: 0.289

### zh019 — zh_long_span_boundary_candidate
- question: 在实习期内的驾驶证扣分会怎样
- before rank: None
- after rank: None
- before best_topk_coverage: 0.553
- after best_topk_coverage: 0.432

### zh020 — zh_long_span_boundary_candidate
- question: 私立大学和公立大学的区别
- before rank: None
- after rank: None
- before best_topk_coverage: 0.124
- after best_topk_coverage: 0.101

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
- before best_topk_coverage: 0.448
- after best_topk_coverage: 0.33

### zh027 — zh_long_span_boundary_candidate
- question: 小米平板钢化膜怎么贴
- before rank: None
- after rank: None
- before best_topk_coverage: 0.041
- after best_topk_coverage: 0.395

### zh028 — zh_long_span_boundary_candidate
- question: 怎么控制路由器把蹭wifi的人给踢了
- before rank: None
- after rank: None
- before best_topk_coverage: 0.606
- after best_topk_coverage: 0.606

### zh029 — zh_long_span_boundary_candidate
- question: 怎么做卫浴销售
- before rank: None
- after rank: None
- before best_topk_coverage: 0.524
- after best_topk_coverage: 0.524

### zh030 — zh_long_span_boundary_candidate
- question: 外伤缝针不能吃什么
- before rank: None
- after rank: None
- before best_topk_coverage: 0.289
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
- before best_topk_coverage: 0.396
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
- before best_topk_coverage: 0.493
- after best_topk_coverage: 0.493

### zh041 — zh_long_span_boundary_candidate
- question: 治疗颈椎病药物
- before rank: None
- after rank: None
- before best_topk_coverage: 0.419
- after best_topk_coverage: 0.419

### zh044 — zh_long_span_boundary_candidate
- question: 换外汇哪个银行好
- before rank: None
- after rank: None
- before best_topk_coverage: 0.296
- after best_topk_coverage: 0.541

### zh045 — zh_long_span_boundary_candidate
- question: 轻型羽绒服什么牌子好
- before rank: 3
- after rank: None
- before best_topk_coverage: 0.835
- after best_topk_coverage: 0.521

### zh046 — zh_long_span_boundary_candidate
- question: 手机外放进水
- before rank: None
- after rank: None
- before best_topk_coverage: 0.491
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

### zh053 — zh_long_span_boundary_candidate
- question: 龟头敏感度低怎么办
- before rank: None
- after rank: None
- before best_topk_coverage: 0.481
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

### zh057 — zh_long_span_boundary_candidate
- question: word怎么不能修改
- before rank: None
- after rank: None
- before best_topk_coverage: 0.166
- after best_topk_coverage: 0.546

### zh058 — zh_long_span_boundary_candidate
- question: 我国古代第一个有伟大成就的爱国诗人是( )
- before rank: None
- after rank: None
- before best_topk_coverage: 0.25
- after best_topk_coverage: 0.25

### zh062 — zh_long_span_boundary_candidate
- question: 如何取消电脑的自动休眠
- before rank: None
- after rank: None
- before best_topk_coverage: 0.253
- after best_topk_coverage: 0.253

### zh064 — zh_long_span_boundary_candidate
- question: 血清甘油三脂偏低
- before rank: None
- after rank: None
- before best_topk_coverage: 0.639
- after best_topk_coverage: 0.639

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

### zh070 — zh_long_span_boundary_candidate
- question: qq经常掉线怎么回事
- before rank: None
- after rank: None
- before best_topk_coverage: 0.375
- after best_topk_coverage: 0.375

### zh071 — zh_long_span_boundary_candidate
- question: 还珠格格第一部背景音乐
- before rank: None
- after rank: None
- before best_topk_coverage: 0.617
- after best_topk_coverage: 0.617

### zh072 — zh_long_span_boundary_candidate
- question: 我的世界手机版0.12.1末地传送门怎么做
- before rank: None
- after rank: None
- before best_topk_coverage: 0.42
- after best_topk_coverage: 0.57

### zh074 — zh_long_span_boundary_candidate
- question: 胃功能
- before rank: None
- after rank: None
- before best_topk_coverage: 0.595
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
- before best_topk_coverage: 0.09
- after best_topk_coverage: 0.09

### zh083 — zh_long_span_boundary_candidate
- question: 怎么改民族
- before rank: None
- after rank: None
- before best_topk_coverage: 0.637
- after best_topk_coverage: 0.637

### zh085 — zh_long_span_boundary_candidate
- question: 白带有酸奶味
- before rank: None
- after rank: None
- before best_topk_coverage: 0.371
- after best_topk_coverage: 0.111

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
- before best_topk_coverage: 0.545
- after best_topk_coverage: 0.404

### zh093 — zh_long_span_boundary_candidate
- question: 成都审驾照需要什么
- before rank: None
- after rank: None
- before best_topk_coverage: 0.179
- after best_topk_coverage: 0.333

### zh094 — zh_long_span_boundary_candidate
- question: 霜是怎么形成的
- before rank: None
- after rank: None
- before best_topk_coverage: 0.077
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
- before best_topk_coverage: 0.577
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

### zh110 — zh_long_span_boundary_candidate
- question: 完美世界出过什么游戏
- before rank: None
- after rank: None
- before best_topk_coverage: 0.607
- after best_topk_coverage: 0.607

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

### zh120 — zh_long_span_boundary_candidate
- question: 保妇康栓要用多久
- before rank: 5
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
| zh015 | True | True | 5 | 2 | False | True |
| zh016 | False | False | None | None | False | False |
| zh017 | False | False | None | None | False | False |
| zh018 | False | False | None | None | False | False |
| zh019 | False | False | None | None | False | False |
| zh020 | False | False | None | None | False | False |
| zh021 | True | True | 3 | 2 | False | True |
| zh022 | False | False | None | None | False | False |
| zh023 | False | False | None | None | False | False |
| zh024 | False | False | None | None | False | False |
| zh025 | False | False | None | None | False | False |
| zh026 | True | True | 4 | 2 | False | True |
| zh027 | False | False | None | None | False | False |
| zh028 | False | False | None | None | False | False |
| zh029 | False | False | None | None | False | False |
| zh030 | False | False | None | None | False | False |
| zh031 | False | False | None | None | False | False |
| zh032 | False | False | None | None | False | False |
| zh033 | False | False | None | None | False | False |
| zh034 | False | False | None | None | False | False |
| zh035 | True | True | 3 | 4 | False | False |
| zh036 | False | False | None | None | False | False |
| zh037 | False | False | None | None | False | False |
| zh038 | False | False | None | None | False | False |
| zh039 | False | False | None | None | False | False |
| zh040 | False | False | None | None | False | False |
| zh041 | False | False | None | None | False | False |
| zh042 | True | True | 2 | 1 | False | True |
| zh043 | True | True | 3 | 1 | False | True |
| zh044 | False | False | None | None | False | False |
| zh045 | True | False | 3 | None | False | False |
| zh046 | False | False | None | None | False | False |
| zh047 | False | False | None | None | False | False |
| zh048 | False | False | None | None | False | False |
| zh049 | True | True | 4 | 1 | False | True |
| zh050 | False | False | None | None | False | False |
| zh051 | False | False | None | None | False | False |
| zh052 | True | True | 5 | 1 | False | True |
| zh053 | False | False | None | None | False | False |
| zh054 | False | False | None | None | False | False |
| zh055 | False | False | None | None | False | False |
| zh056 | True | True | 4 | 1 | False | True |
| zh057 | False | False | None | None | False | False |
| zh058 | False | False | None | None | False | False |
| zh059 | True | True | 2 | 3 | False | False |
| zh060 | True | True | 1 | 2 | False | False |
| zh061 | True | True | 1 | 4 | False | False |
| zh062 | False | False | None | None | False | False |
| zh063 | True | True | 5 | 4 | False | True |
| zh064 | False | False | None | None | False | False |
| zh065 | True | True | 5 | 2 | False | True |
| zh066 | False | False | None | None | False | False |
| zh067 | False | False | None | None | False | False |
| zh068 | True | True | 2 | 2 | False | False |
| zh069 | True | True | 1 | 3 | False | False |
| zh070 | False | False | None | None | False | False |
| zh071 | False | False | None | None | False | False |
| zh072 | False | False | None | None | False | False |
| zh073 | True | True | 3 | 1 | False | True |
| zh074 | False | False | None | None | False | False |
| zh075 | False | False | None | None | False | False |
| zh076 | False | False | None | None | False | False |
| zh077 | False | False | None | None | False | False |
| zh078 | False | False | None | None | False | False |
| zh079 | False | False | None | None | False | False |
| zh080 | True | True | 1 | 1 | False | False |
| zh081 | False | False | None | None | False | False |
| zh082 | False | False | None | None | False | False |
| zh083 | False | False | None | None | False | False |
| zh084 | True | True | 1 | 1 | False | False |
| zh085 | False | False | None | None | False | False |
| zh086 | True | True | 5 | 2 | False | True |
| zh087 | True | True | 5 | 3 | False | True |
| zh088 | True | True | 3 | 1 | False | True |
| zh089 | False | False | None | None | False | False |
| zh090 | False | False | None | None | False | False |
| zh091 | True | True | 1 | 1 | False | False |
| zh092 | True | True | 5 | 2 | False | True |
| zh093 | False | False | None | None | False | False |
| zh094 | False | False | None | None | False | False |
| zh095 | False | False | None | None | False | False |
| zh096 | False | False | None | None | False | False |
| zh097 | False | False | None | None | False | False |
| zh098 | True | True | 1 | 4 | False | False |
| zh099 | True | True | 2 | 1 | False | True |
| zh100 | False | False | None | None | False | False |
| zh101 | False | False | None | None | False | False |
| zh102 | False | False | None | None | False | False |
| zh103 | False | False | None | None | False | False |
| zh104 | True | True | 5 | 5 | False | False |
| zh105 | True | True | 3 | 2 | False | True |
| zh106 | True | True | 3 | 5 | False | False |
| zh107 | True | True | 5 | 2 | False | True |
| zh108 | True | True | 5 | 3 | False | True |
| zh109 | True | True | 2 | 1 | False | True |
| zh110 | False | False | None | None | False | False |
| zh111 | True | True | 5 | 4 | False | True |
| zh112 | True | True | 2 | 1 | False | True |
| zh113 | False | False | None | None | False | False |
| zh114 | True | True | 1 | 2 | False | False |
| zh115 | True | True | 2 | 1 | False | True |
| zh116 | True | True | 4 | 1 | False | True |
| zh117 | False | False | None | None | False | False |
| zh118 | True | True | 5 | 5 | False | False |
| zh119 | True | True | 4 | 3 | False | True |
| zh120 | True | False | 5 | None | False | False |
