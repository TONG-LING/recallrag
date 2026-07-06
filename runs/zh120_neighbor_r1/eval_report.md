# Neighbor Expansion Report

## Config

- **index**: `runs/zh120_base`
- **questions**: `case_zh_dureader_120/eval/questions_patch_source.jsonl`
- **top_k**: `5`
- **coverage_threshold**: `0.65`
- **neighbor_radius**: `1`
- **endpoint**: `http://localhost:1234/v1/embeddings`
- **model**: `text-embedding-bge-large-zh-v1.5`

## Metrics

- **total**: 120
- **dense_recall@5**: 0.1417
- **recall@5**: 0.8750
- **dense_mrr**: 0.0651
- **mrr**: 0.5582
- **dense_hits_before_expansion**: 17
- **hits**: 105
- **failed**: 15
- **fixed_by_expansion**: 88
- **coverage_threshold**: 0.6500
- **neighbor_radius**: 1
- **avg_top5_total_chars**: 3414.1750
- **avg_top5_chars_per_item**: 682.8350
- **avg_top5_merged_chunks**: 2.8267

## Fixed By Neighbor Expansion

### zh001
- question: 高速公路超速20以上不足50扣几分
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.646
- best_topk_coverage after: 0.785

### zh005
- question: 叉车有几种
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.361
- best_topk_coverage after: 0.75

### zh006
- question: 春光成语
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.31
- best_topk_coverage after: 0.678

### zh007
- question: 经常用肥皂洗脸好吗
- rank before expansion: None
- rank after expansion: 5
- best_topk_coverage before: 0.33
- best_topk_coverage after: 0.688

### zh008
- question: 冬天怎样养鹦鹉
- rank before expansion: None
- rank after expansion: 5
- best_topk_coverage before: 0.276
- best_topk_coverage after: 0.681

### zh010
- question: 硫磺皂能长期用吗
- rank before expansion: None
- rank after expansion: 5
- best_topk_coverage before: 0.277
- best_topk_coverage after: 0.678

### zh012
- question: 夏天喝什么饮品好
- rank before expansion: None
- rank after expansion: 5
- best_topk_coverage before: 0.365
- best_topk_coverage after: 0.702

### zh013
- question: workgroup是什么
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.395
- best_topk_coverage after: 0.711

### zh014
- question: 怎样锻炼肺活量
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.336
- best_topk_coverage after: 0.718

### zh015
- question: 做胃镜注意
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.462
- best_topk_coverage after: 0.92

### zh016
- question: 油电混合动力汽车购置税优惠吗
- rank before expansion: None
- rank after expansion: 5
- best_topk_coverage before: 0.405
- best_topk_coverage after: 0.778

### zh017
- question: 阴部变白
- rank before expansion: None
- rank after expansion: 5
- best_topk_coverage before: 0.321
- best_topk_coverage after: 0.661

### zh018
- question: 如何买卖etf基金
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.429
- best_topk_coverage after: 0.785

### zh019
- question: 在实习期内的驾驶证扣分会怎样
- rank before expansion: None
- rank after expansion: 5
- best_topk_coverage before: 0.553
- best_topk_coverage after: 0.922

### zh021
- question: 如何调水表数字
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.325
- best_topk_coverage after: 0.692

### zh022
- question: 怎样种香菜
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.386
- best_topk_coverage after: 0.755

### zh023
- question: 如何把电脑上的东西传到ipad上
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.472
- best_topk_coverage after: 0.879

### zh024
- question: c1扣12分怎么办
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.41
- best_topk_coverage after: 0.752

### zh025
- question: tf与sd卡的区别
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.448
- best_topk_coverage after: 0.913

### zh026
- question: 左肾部位疼痛
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.487
- best_topk_coverage after: 0.921

### zh028
- question: 怎么控制路由器把蹭wifi的人给踢了
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.606
- best_topk_coverage after: 0.845

### zh029
- question: 怎么做卫浴销售
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.524
- best_topk_coverage after: 0.812

### zh031
- question: 超级会员是什么
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.517
- best_topk_coverage after: 0.836

### zh032
- question: 杭州劳动仲裁电话
- rank before expansion: None
- rank after expansion: 5
- best_topk_coverage before: 0.396
- best_topk_coverage after: 0.669

### zh033
- question: 电暖桌哪个牌子好
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.349
- best_topk_coverage after: 0.729

### zh034
- question: 板栗可以蒸着吃吗
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.49
- best_topk_coverage after: 0.755

### zh035
- question: 没越狱的iphone怎么清理垃圾
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.424
- best_topk_coverage after: 0.772

### zh036
- question: 苹果系统怎么查看隐藏文件
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.525
- best_topk_coverage after: 0.916

### zh037
- question: 海淀医院孕前检查
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.44
- best_topk_coverage after: 0.877

### zh038
- question: 玩梦幻西游怎么赚钱
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.494
- best_topk_coverage after: 0.97

### zh039
- question: 跟庐山有关的诗句
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.486
- best_topk_coverage after: 0.859

### zh040
- question: 现在去哪里下载音乐
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.493
- best_topk_coverage after: 0.887

### zh041
- question: 治疗颈椎病药物
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.419
- best_topk_coverage after: 0.813

### zh042
- question: 户外手电筒什么牌子好
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.411
- best_topk_coverage after: 0.842

### zh044
- question: 换外汇哪个银行好
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.296
- best_topk_coverage after: 0.706

### zh045
- question: 轻型羽绒服什么牌子好
- rank before expansion: None
- rank after expansion: 5
- best_topk_coverage before: 0.536
- best_topk_coverage after: 0.835

### zh046
- question: 手机外放进水
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.491
- best_topk_coverage after: 0.993

### zh047
- question: 什么样的借条不具法律效力
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.6
- best_topk_coverage after: 0.85

### zh048
- question: m8a1用什么炮
- rank before expansion: None
- rank after expansion: 5
- best_topk_coverage before: 0.472
- best_topk_coverage after: 0.898

### zh049
- question: 西安人流手术费用要多少
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.583
- best_topk_coverage after: 0.998

### zh050
- question: xm外汇平台怎么样
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.265
- best_topk_coverage after: 0.721

### zh051
- question: 双人床最小宽度
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.533
- best_topk_coverage after: 0.878

### zh052
- question: 生气时喂奶
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.482
- best_topk_coverage after: 0.857

### zh053
- question: 龟头敏感度低怎么办
- rank before expansion: None
- rank after expansion: 5
- best_topk_coverage before: 0.481
- best_topk_coverage after: 0.871

### zh054
- question: 沪陕高速限速多少
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.552
- best_topk_coverage after: 0.955

### zh055
- question: ios9 如何关闭搜索最近联系人
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.611
- best_topk_coverage after: 0.915

### zh056
- question: 尸兄主角能力
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.51
- best_topk_coverage after: 0.908

### zh060
- question: 氨端聚二甲基硅氧烷是硅油吗
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.27
- best_topk_coverage after: 0.717

### zh061
- question: 为什么中国必须守住18亿亩耕地红线
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.342
- best_topk_coverage after: 0.723

### zh062
- question: 如何取消电脑的自动休眠
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.253
- best_topk_coverage after: 0.735

### zh063
- question: 象征孩子纯洁的花
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.526
- best_topk_coverage after: 0.992

### zh064
- question: 血清甘油三脂偏低
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.639
- best_topk_coverage after: 0.985

### zh065
- question: 哪种制氧机好
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.581
- best_topk_coverage after: 0.995

### zh066
- question: 电动牙刷刷的干净吗
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.567
- best_topk_coverage after: 0.993

### zh067
- question: 武松属什么
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.432
- best_topk_coverage after: 0.886

### zh068
- question: 跳鬼步舞时手怎么动
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.553
- best_topk_coverage after: 0.985

### zh069
- question: would like的回答
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.64
- best_topk_coverage after: 1.0

### zh070
- question: qq经常掉线怎么回事
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.375
- best_topk_coverage after: 0.866

### zh071
- question: 还珠格格第一部背景音乐
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.617
- best_topk_coverage after: 0.892

### zh072
- question: 我的世界手机版0.12.1末地传送门怎么做
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.42
- best_topk_coverage after: 0.86

### zh073
- question: 三壬行化妆学校好吗
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.534
- best_topk_coverage after: 0.997

### zh074
- question: 胃功能
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.595
- best_topk_coverage after: 0.982

### zh076
- question: 公共事业管理属于什么专业类别
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.567
- best_topk_coverage after: 0.963

### zh077
- question: 天然无添加的护肤品存在吗
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.584
- best_topk_coverage after: 1.0

### zh078
- question: 旅行发票 可以报吗
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.578
- best_topk_coverage after: 0.957

### zh079
- question: 种子可以用百度云下载吗
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.527
- best_topk_coverage after: 0.982

### zh080
- question: ipad能否连接打印机
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.545
- best_topk_coverage after: 0.996

### zh081
- question: 手机钢化保护膜怎么贴
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.588
- best_topk_coverage after: 0.997

### zh083
- question: 怎么改民族
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.637
- best_topk_coverage after: 1.0

### zh085
- question: 白带有酸奶味
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.371
- best_topk_coverage after: 0.886

### zh087
- question: 晾衣架材质
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.542
- best_topk_coverage after: 1.0

### zh088
- question: 如何遮盖唇色
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.605
- best_topk_coverage after: 1.0

### zh089
- question: 部落冲突怎么搜死鱼
- rank before expansion: None
- rank after expansion: 2
- best_topk_coverage before: 0.456
- best_topk_coverage after: 0.888

### zh090
- question: 牛剖层移膜皮是什么
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.545
- best_topk_coverage after: 0.994

### zh095
- question: 卫生间铺什么地砖好
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.576
- best_topk_coverage after: 0.997

### zh096
- question: 肠结核的症状
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.557
- best_topk_coverage after: 0.997

### zh097
- question: 表带怎么打孔
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.407
- best_topk_coverage after: 0.881

### zh099
- question: 水土流失是什么意思
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.626
- best_topk_coverage after: 0.997

### zh100
- question: 红枣表面有层白色粉末
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.58
- best_topk_coverage after: 1.0

### zh101
- question: 小米的平板好用吗
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.577
- best_topk_coverage after: 1.0

### zh103
- question: 北京出国体检在哪里
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.623
- best_topk_coverage after: 0.997

### zh106
- question: 原地跑步能减肚子吗
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.361
- best_topk_coverage after: 0.883

### zh110
- question: 完美世界出过什么游戏
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.607
- best_topk_coverage after: 0.997

### zh112
- question: 为什么qq打不开图片
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.613
- best_topk_coverage after: 0.994

### zh113
- question: 辅酶q10的服用方法
- rank before expansion: None
- rank after expansion: 3
- best_topk_coverage before: 0.52
- best_topk_coverage after: 0.982

### zh117
- question: 德国红铁元和绿铁元有什么区别
- rank before expansion: None
- rank after expansion: 4
- best_topk_coverage before: 0.227
- best_topk_coverage after: 0.654

### zh118
- question: 诛仙法宝技能怎么洗
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.354
- best_topk_coverage after: 0.897

### zh119
- question: 神秘博士clara是谁
- rank before expansion: None
- rank after expansion: 1
- best_topk_coverage before: 0.534
- best_topk_coverage after: 0.959

## Still Failed

### zh002
- question: 空气净化器哪种净化方式好
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.163
- best_topk_coverage after: 0.236

### zh003
- question: 黄山风景古诗赞
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.206
- best_topk_coverage after: 0.554

### zh004
- question: 一天放很多屁
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.276
- best_topk_coverage after: 0.618

### zh009
- question: 附睾肿胀
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.42
- best_topk_coverage after: 0.622

### zh011
- question: 比较好看的电视剧
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.19
- best_topk_coverage after: 0.439

### zh020
- question: 私立大学和公立大学的区别
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.124
- best_topk_coverage after: 0.443

### zh027
- question: 小米平板钢化膜怎么贴
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.041
- best_topk_coverage after: 0.113

### zh030
- question: 外伤缝针不能吃什么
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.289
- best_topk_coverage after: 0.622

### zh057
- question: word怎么不能修改
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.166
- best_topk_coverage after: 0.38

### zh058
- question: 我国古代第一个有伟大成就的爱国诗人是( )
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.25
- best_topk_coverage after: 0.394

### zh075
- question: 艾俐缇陶瓷怎么样
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.137
- best_topk_coverage after: 0.587

### zh082
- question: 中国古代最繁荣的朝代
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.09
- best_topk_coverage after: 0.542

### zh093
- question: 成都审驾照需要什么
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.179
- best_topk_coverage after: 0.451

### zh094
- question: 霜是怎么形成的
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.077
- best_topk_coverage after: 0.548

### zh102
- question: 尺神经麻痹治疗
- rank before expansion: None
- rank after expansion: None
- best_topk_coverage before: 0.164
- best_topk_coverage after: 0.573

## All Query Summary

| qid | success before | success after | rank before | rank after | total chars top-5 |
|---|---:|---:|---:|---:|---:|
| zh001 | False | True | None | 2 | 3424 |
| zh002 | False | False | None | None | 3424 |
| zh003 | False | False | None | None | 3718 |
| zh004 | False | False | None | None | 3445 |
| zh005 | False | True | None | 2 | 3717 |
| zh006 | False | True | None | 4 | 3693 |
| zh007 | False | True | None | 5 | 3315 |
| zh008 | False | True | None | 5 | 3396 |
| zh009 | False | False | None | None | 3420 |
| zh010 | False | True | None | 5 | 3006 |
| zh011 | False | False | None | None | 3207 |
| zh012 | False | True | None | 5 | 3422 |
| zh013 | False | True | None | 4 | 3421 |
| zh014 | False | True | None | 4 | 3266 |
| zh015 | False | True | None | 1 | 3715 |
| zh016 | False | True | None | 5 | 3419 |
| zh017 | False | True | None | 5 | 3085 |
| zh018 | False | True | None | 3 | 3169 |
| zh019 | False | True | None | 5 | 3296 |
| zh020 | False | False | None | None | 3676 |
| zh021 | False | True | None | 1 | 3473 |
| zh022 | False | True | None | 3 | 3330 |
| zh023 | False | True | None | 1 | 3575 |
| zh024 | False | True | None | 1 | 3701 |
| zh025 | False | True | None | 1 | 3726 |
| zh026 | False | True | None | 1 | 3419 |
| zh027 | False | False | None | None | 2916 |
| zh028 | False | True | None | 2 | 3419 |
| zh029 | False | True | None | 4 | 3421 |
| zh030 | False | False | None | None | 3282 |
| zh031 | False | True | None | 3 | 3202 |
| zh032 | False | True | None | 5 | 3727 |
| zh033 | False | True | None | 1 | 3693 |
| zh034 | False | True | None | 2 | 3571 |
| zh035 | False | True | None | 4 | 3265 |
| zh036 | False | True | None | 1 | 3444 |
| zh037 | False | True | None | 3 | 3448 |
| zh038 | False | True | None | 3 | 3129 |
| zh039 | False | True | None | 4 | 3693 |
| zh040 | False | True | None | 3 | 3356 |
| zh041 | False | True | None | 3 | 3589 |
| zh042 | False | True | None | 1 | 3325 |
| zh043 | True | True | 3 | 2 | 3408 |
| zh044 | False | True | None | 2 | 3421 |
| zh045 | False | True | None | 5 | 3128 |
| zh046 | False | True | None | 4 | 3447 |
| zh047 | False | True | None | 3 | 3290 |
| zh048 | False | True | None | 5 | 3626 |
| zh049 | False | True | None | 1 | 3445 |
| zh050 | False | True | None | 4 | 3348 |
| zh051 | False | True | None | 2 | 3421 |
| zh052 | False | True | None | 2 | 3296 |
| zh053 | False | True | None | 5 | 3448 |
| zh054 | False | True | None | 1 | 3446 |
| zh055 | False | True | None | 3 | 3372 |
| zh056 | False | True | None | 1 | 3726 |
| zh057 | False | False | None | None | 3373 |
| zh058 | False | False | None | None | 3727 |
| zh059 | True | True | 2 | 1 | 3206 |
| zh060 | False | True | None | 1 | 3699 |
| zh061 | False | True | None | 1 | 3389 |
| zh062 | False | True | None | 2 | 3452 |
| zh063 | False | True | None | 2 | 3413 |
| zh064 | False | True | None | 1 | 3696 |
| zh065 | False | True | None | 2 | 3725 |
| zh066 | False | True | None | 2 | 3164 |
| zh067 | False | True | None | 1 | 3220 |
| zh068 | False | True | None | 1 | 3696 |
| zh069 | False | True | None | 2 | 3720 |
| zh070 | False | True | None | 4 | 3171 |
| zh071 | False | True | None | 1 | 3690 |
| zh072 | False | True | None | 4 | 3259 |
| zh073 | False | True | None | 1 | 3418 |
| zh074 | False | True | None | 1 | 3445 |
| zh075 | False | False | None | None | 3323 |
| zh076 | False | True | None | 1 | 3728 |
| zh077 | False | True | None | 1 | 3563 |
| zh078 | False | True | None | 2 | 3345 |
| zh079 | False | True | None | 1 | 3386 |
| zh080 | False | True | None | 4 | 3450 |
| zh081 | False | True | None | 2 | 3725 |
| zh082 | False | False | None | None | 3424 |
| zh083 | False | True | None | 1 | 2964 |
| zh084 | True | True | 1 | 1 | 3414 |
| zh085 | False | True | None | 3 | 3312 |
| zh086 | True | True | 5 | 1 | 3420 |
| zh087 | False | True | None | 1 | 3635 |
| zh088 | False | True | None | 1 | 3090 |
| zh089 | False | True | None | 2 | 3247 |
| zh090 | False | True | None | 1 | 3697 |
| zh091 | True | True | 1 | 1 | 3420 |
| zh092 | True | True | 5 | 1 | 3725 |
| zh093 | False | False | None | None | 3453 |
| zh094 | False | False | None | None | 2813 |
| zh095 | False | True | None | 3 | 3410 |
| zh096 | False | True | None | 1 | 3420 |
| zh097 | False | True | None | 1 | 3140 |
| zh098 | True | True | 1 | 1 | 3420 |
| zh099 | False | True | None | 1 | 3251 |
| zh100 | False | True | None | 1 | 3350 |
| zh101 | False | True | None | 1 | 3060 |
| zh102 | False | False | None | None | 3452 |
| zh103 | False | True | None | 1 | 2971 |
| zh104 | True | True | 5 | 5 | 3024 |
| zh105 | True | True | 3 | 3 | 3317 |
| zh106 | False | True | None | 1 | 3699 |
| zh107 | True | True | 5 | 1 | 3725 |
| zh108 | True | True | 5 | 2 | 3421 |
| zh109 | True | True | 2 | 1 | 3725 |
| zh110 | False | True | None | 4 | 3316 |
| zh111 | True | True | 5 | 1 | 3420 |
| zh112 | False | True | None | 1 | 3274 |
| zh113 | False | True | None | 3 | 3699 |
| zh114 | True | True | 1 | 1 | 3296 |
| zh115 | True | True | 2 | 2 | 3420 |
| zh116 | True | True | 4 | 2 | 3296 |
| zh117 | False | True | None | 4 | 3254 |
| zh118 | False | True | None | 1 | 3421 |
| zh119 | False | True | None | 1 | 3142 |
| zh120 | True | True | 5 | 2 | 3421 |
