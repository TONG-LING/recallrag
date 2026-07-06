# Paired Significance Report

## Summary

- n: `120`
- before hits: `106`
- after hits: `112`
- wins (0->1): `6`
- losses (1->0): `0`
- ties: `114`
- recall delta: `0.0500`
- recall 95% bootstrap CI: `[0.0167, 0.0917]`
- MRR delta: `0.0207`
- MRR 95% bootstrap CI: `[0.0044, 0.0433]`
- exact McNemar p-value: `0.031250`

## Interpretation

- `wins` 看的是原来失败、后来成功的 query 数。
- `losses` 看的是原来成功、后来失败的 query 数。
- McNemar 只针对 paired 二分类成功/失败，不是看小数漂不漂亮。
- bootstrap CI 更适合解释增益区间，不代表严格因果证明。

## Per Query

| qid | before_success | after_success | before_rank | after_rank | mrr_delta |
|---|---|---|---:|---:|---:|
| zh001 | True | True | 2 | 2 | 0.000000 |
| zh002 | False | True | None | 1 | 1.000000 |
| zh003 | False | False | None | None | 0.000000 |
| zh004 | False | True | None | 2 | 0.500000 |
| zh005 | True | True | 2 | 2 | 0.000000 |
| zh006 | False | False | None | None | 0.000000 |
| zh007 | False | True | None | 4 | 0.250000 |
| zh008 | False | True | None | 5 | 0.200000 |
| zh009 | True | True | 3 | 3 | 0.000000 |
| zh010 | False | False | None | None | 0.000000 |
| zh011 | False | False | None | None | 0.000000 |
| zh012 | True | True | 3 | 3 | 0.000000 |
| zh013 | True | True | 2 | 2 | 0.000000 |
| zh014 | True | True | 4 | 4 | 0.000000 |
| zh015 | True | True | 1 | 1 | 0.000000 |
| zh016 | True | True | 5 | 5 | 0.000000 |
| zh017 | False | False | None | None | 0.000000 |
| zh018 | True | True | 2 | 2 | 0.000000 |
| zh019 | True | True | 2 | 2 | 0.000000 |
| zh020 | True | True | 5 | 5 | 0.000000 |
| zh021 | True | True | 1 | 1 | 0.000000 |
| zh022 | True | True | 1 | 1 | 0.000000 |
| zh023 | True | True | 4 | 4 | 0.000000 |
| zh024 | True | True | 5 | 5 | 0.000000 |
| zh025 | True | True | 2 | 2 | 0.000000 |
| zh026 | True | True | 1 | 1 | 0.000000 |
| zh027 | False | False | None | None | 0.000000 |
| zh028 | True | True | 3 | 3 | 0.000000 |
| zh029 | True | True | 2 | 2 | 0.000000 |
| zh030 | True | True | 5 | 5 | 0.000000 |
| zh031 | True | True | 1 | 1 | 0.000000 |
| zh032 | True | True | 5 | 5 | 0.000000 |
| zh033 | False | False | None | None | 0.000000 |
| zh034 | True | True | 4 | 4 | 0.000000 |
| zh035 | True | True | 3 | 3 | 0.000000 |
| zh036 | True | True | 1 | 1 | 0.000000 |
| zh037 | True | True | 2 | 2 | 0.000000 |
| zh038 | True | True | 3 | 3 | 0.000000 |
| zh039 | True | True | 1 | 1 | 0.000000 |
| zh040 | True | True | 2 | 2 | 0.000000 |
| zh041 | True | True | 3 | 3 | 0.000000 |
| zh042 | True | True | 1 | 1 | 0.000000 |
| zh043 | True | True | 3 | 3 | 0.000000 |
| zh044 | True | True | 2 | 2 | 0.000000 |
| zh045 | True | True | 2 | 2 | 0.000000 |
| zh046 | True | True | 3 | 3 | 0.000000 |
| zh047 | True | True | 5 | 5 | 0.000000 |
| zh048 | True | True | 2 | 2 | 0.000000 |
| zh049 | True | True | 3 | 3 | 0.000000 |
| zh050 | True | True | 1 | 1 | 0.000000 |
| zh051 | True | True | 1 | 1 | 0.000000 |
| zh052 | True | True | 1 | 1 | 0.000000 |
| zh053 | True | True | 1 | 1 | 0.000000 |
| zh054 | True | True | 2 | 2 | 0.000000 |
| zh055 | True | True | 1 | 1 | 0.000000 |
| zh056 | True | True | 4 | 4 | 0.000000 |
| zh057 | False | True | None | 5 | 0.200000 |
| zh058 | True | True | 3 | 3 | 0.000000 |
| zh059 | True | True | 1 | 1 | 0.000000 |
| zh060 | True | True | 1 | 1 | 0.000000 |
| zh061 | True | True | 2 | 2 | 0.000000 |
| zh062 | True | True | 1 | 1 | 0.000000 |
| zh063 | True | True | 4 | 4 | 0.000000 |
| zh064 | True | True | 1 | 1 | 0.000000 |
| zh065 | True | True | 2 | 2 | 0.000000 |
| zh066 | True | True | 3 | 3 | 0.000000 |
| zh067 | False | True | None | 3 | 0.333333 |
| zh068 | True | True | 2 | 2 | 0.000000 |
| zh069 | True | True | 2 | 2 | 0.000000 |
| zh070 | True | True | 4 | 4 | 0.000000 |
| zh071 | True | True | 1 | 1 | 0.000000 |
| zh072 | True | True | 1 | 1 | 0.000000 |
| zh073 | True | True | 1 | 1 | 0.000000 |
| zh074 | True | True | 1 | 1 | 0.000000 |
| zh075 | True | True | 3 | 3 | 0.000000 |
| zh076 | True | True | 1 | 1 | 0.000000 |
| zh077 | True | True | 1 | 1 | 0.000000 |
| zh078 | True | True | 3 | 3 | 0.000000 |
| zh079 | True | True | 1 | 1 | 0.000000 |
| zh080 | True | True | 1 | 1 | 0.000000 |
| zh081 | True | True | 3 | 3 | 0.000000 |
| zh082 | True | True | 4 | 4 | 0.000000 |
| zh083 | True | True | 1 | 1 | 0.000000 |
| zh084 | True | True | 1 | 1 | 0.000000 |
| zh085 | True | True | 3 | 3 | 0.000000 |
| zh086 | True | True | 3 | 3 | 0.000000 |
| zh087 | True | True | 1 | 1 | 0.000000 |
| zh088 | True | True | 2 | 2 | 0.000000 |
| zh089 | True | True | 2 | 2 | 0.000000 |
| zh090 | True | True | 1 | 1 | 0.000000 |
| zh091 | True | True | 1 | 1 | 0.000000 |
| zh092 | True | True | 1 | 1 | 0.000000 |
| zh093 | True | True | 1 | 1 | 0.000000 |
| zh094 | True | True | 3 | 3 | 0.000000 |
| zh095 | True | True | 2 | 2 | 0.000000 |
| zh096 | True | True | 2 | 2 | 0.000000 |
| zh097 | True | True | 1 | 1 | 0.000000 |
| zh098 | True | True | 2 | 2 | 0.000000 |
| zh099 | True | True | 1 | 1 | 0.000000 |
| zh100 | True | True | 1 | 1 | 0.000000 |
| zh101 | False | False | None | None | 0.000000 |
| zh102 | True | True | 5 | 5 | 0.000000 |
| zh103 | True | True | 1 | 1 | 0.000000 |
| zh104 | True | True | 4 | 4 | 0.000000 |
| zh105 | True | True | 1 | 1 | 0.000000 |
| zh106 | True | True | 5 | 5 | 0.000000 |
| zh107 | True | True | 1 | 1 | 0.000000 |
| zh108 | True | True | 3 | 3 | 0.000000 |
| zh109 | True | True | 1 | 1 | 0.000000 |
| zh110 | True | True | 2 | 2 | 0.000000 |
| zh111 | True | True | 1 | 1 | 0.000000 |
| zh112 | True | True | 1 | 1 | 0.000000 |
| zh113 | True | True | 3 | 3 | 0.000000 |
| zh114 | True | True | 1 | 1 | 0.000000 |
| zh115 | True | True | 2 | 2 | 0.000000 |
| zh116 | True | True | 3 | 3 | 0.000000 |
| zh117 | True | True | 3 | 3 | 0.000000 |
| zh118 | True | True | 2 | 2 | 0.000000 |
| zh119 | True | True | 2 | 2 | 0.000000 |
| zh120 | True | True | 2 | 2 | 0.000000 |
