# Paired Significance Report

## Summary

- n: `120`
- before hits: `17`
- after hits: `41`
- wins (0->1): `24`
- losses (1->0): `0`
- ties: `96`
- recall delta: `0.2000`
- recall 95% bootstrap CI: `[0.1333, 0.2750]`
- MRR delta: `0.0850`
- MRR 95% bootstrap CI: `[0.0501, 0.1247]`
- exact McNemar p-value: `0.000000`

## Interpretation

- `wins` 看的是原来失败、后来成功的 query 数。
- `losses` 看的是原来成功、后来失败的 query 数。
- McNemar 只针对 paired 二分类成功/失败，不是看小数漂不漂亮。
- bootstrap CI 更适合解释增益区间，不代表严格因果证明。

## Per Query

| qid | before_success | after_success | before_rank | after_rank | mrr_delta |
|---|---|---|---:|---:|---:|
| zh001 | False | False | None | None | 0.000000 |
| zh002 | False | False | None | None | 0.000000 |
| zh003 | False | False | None | None | 0.000000 |
| zh004 | False | False | None | None | 0.000000 |
| zh005 | False | False | None | None | 0.000000 |
| zh006 | False | False | None | None | 0.000000 |
| zh007 | False | False | None | None | 0.000000 |
| zh008 | False | False | None | None | 0.000000 |
| zh009 | False | False | None | None | 0.000000 |
| zh010 | False | False | None | None | 0.000000 |
| zh011 | False | False | None | None | 0.000000 |
| zh012 | False | False | None | None | 0.000000 |
| zh013 | False | False | None | None | 0.000000 |
| zh014 | False | False | None | None | 0.000000 |
| zh015 | False | True | None | 5 | 0.200000 |
| zh016 | False | False | None | None | 0.000000 |
| zh017 | False | False | None | None | 0.000000 |
| zh018 | False | False | None | None | 0.000000 |
| zh019 | False | False | None | None | 0.000000 |
| zh020 | False | False | None | None | 0.000000 |
| zh021 | False | True | None | 3 | 0.333333 |
| zh022 | False | False | None | None | 0.000000 |
| zh023 | False | False | None | None | 0.000000 |
| zh024 | False | False | None | None | 0.000000 |
| zh025 | False | False | None | None | 0.000000 |
| zh026 | False | True | None | 4 | 0.250000 |
| zh027 | False | False | None | None | 0.000000 |
| zh028 | False | False | None | None | 0.000000 |
| zh029 | False | False | None | None | 0.000000 |
| zh030 | False | False | None | None | 0.000000 |
| zh031 | False | False | None | None | 0.000000 |
| zh032 | False | False | None | None | 0.000000 |
| zh033 | False | False | None | None | 0.000000 |
| zh034 | False | False | None | None | 0.000000 |
| zh035 | False | True | None | 3 | 0.333333 |
| zh036 | False | False | None | None | 0.000000 |
| zh037 | False | False | None | None | 0.000000 |
| zh038 | False | False | None | None | 0.000000 |
| zh039 | False | False | None | None | 0.000000 |
| zh040 | False | False | None | None | 0.000000 |
| zh041 | False | False | None | None | 0.000000 |
| zh042 | False | True | None | 2 | 0.500000 |
| zh043 | True | True | 3 | 3 | 0.000000 |
| zh044 | False | False | None | None | 0.000000 |
| zh045 | False | True | None | 3 | 0.333333 |
| zh046 | False | False | None | None | 0.000000 |
| zh047 | False | False | None | None | 0.000000 |
| zh048 | False | False | None | None | 0.000000 |
| zh049 | False | True | None | 4 | 0.250000 |
| zh050 | False | False | None | None | 0.000000 |
| zh051 | False | False | None | None | 0.000000 |
| zh052 | False | True | None | 5 | 0.200000 |
| zh053 | False | False | None | None | 0.000000 |
| zh054 | False | False | None | None | 0.000000 |
| zh055 | False | False | None | None | 0.000000 |
| zh056 | False | True | None | 4 | 0.250000 |
| zh057 | False | False | None | None | 0.000000 |
| zh058 | False | False | None | None | 0.000000 |
| zh059 | True | True | 2 | 2 | 0.000000 |
| zh060 | False | True | None | 1 | 1.000000 |
| zh061 | False | True | None | 1 | 1.000000 |
| zh062 | False | False | None | None | 0.000000 |
| zh063 | False | True | None | 5 | 0.200000 |
| zh064 | False | False | None | None | 0.000000 |
| zh065 | False | True | None | 5 | 0.200000 |
| zh066 | False | False | None | None | 0.000000 |
| zh067 | False | False | None | None | 0.000000 |
| zh068 | False | True | None | 2 | 0.500000 |
| zh069 | False | True | None | 1 | 1.000000 |
| zh070 | False | False | None | None | 0.000000 |
| zh071 | False | False | None | None | 0.000000 |
| zh072 | False | False | None | None | 0.000000 |
| zh073 | False | True | None | 3 | 0.333333 |
| zh074 | False | False | None | None | 0.000000 |
| zh075 | False | False | None | None | 0.000000 |
| zh076 | False | False | None | None | 0.000000 |
| zh077 | False | False | None | None | 0.000000 |
| zh078 | False | False | None | None | 0.000000 |
| zh079 | False | False | None | None | 0.000000 |
| zh080 | False | True | None | 1 | 1.000000 |
| zh081 | False | False | None | None | 0.000000 |
| zh082 | False | False | None | None | 0.000000 |
| zh083 | False | False | None | None | 0.000000 |
| zh084 | True | True | 1 | 1 | 0.000000 |
| zh085 | False | False | None | None | 0.000000 |
| zh086 | True | True | 5 | 5 | 0.000000 |
| zh087 | False | True | None | 5 | 0.200000 |
| zh088 | False | True | None | 3 | 0.333333 |
| zh089 | False | False | None | None | 0.000000 |
| zh090 | False | False | None | None | 0.000000 |
| zh091 | True | True | 1 | 1 | 0.000000 |
| zh092 | True | True | 5 | 5 | 0.000000 |
| zh093 | False | False | None | None | 0.000000 |
| zh094 | False | False | None | None | 0.000000 |
| zh095 | False | False | None | None | 0.000000 |
| zh096 | False | False | None | None | 0.000000 |
| zh097 | False | False | None | None | 0.000000 |
| zh098 | True | True | 1 | 1 | 0.000000 |
| zh099 | False | True | None | 2 | 0.500000 |
| zh100 | False | False | None | None | 0.000000 |
| zh101 | False | False | None | None | 0.000000 |
| zh102 | False | False | None | None | 0.000000 |
| zh103 | False | False | None | None | 0.000000 |
| zh104 | True | True | 5 | 5 | 0.000000 |
| zh105 | True | True | 3 | 3 | 0.000000 |
| zh106 | False | True | None | 3 | 0.333333 |
| zh107 | True | True | 5 | 5 | 0.000000 |
| zh108 | True | True | 5 | 5 | 0.000000 |
| zh109 | True | True | 2 | 2 | 0.000000 |
| zh110 | False | False | None | None | 0.000000 |
| zh111 | True | True | 5 | 5 | 0.000000 |
| zh112 | False | True | None | 2 | 0.500000 |
| zh113 | False | False | None | None | 0.000000 |
| zh114 | True | True | 1 | 1 | 0.000000 |
| zh115 | True | True | 2 | 2 | 0.000000 |
| zh116 | True | True | 4 | 4 | 0.000000 |
| zh117 | False | False | None | None | 0.000000 |
| zh118 | False | True | None | 5 | 0.200000 |
| zh119 | False | True | None | 4 | 0.250000 |
| zh120 | True | True | 5 | 5 | 0.000000 |
