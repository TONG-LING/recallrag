# Paired Significance Report

## Summary

- n: `120`
- before hits: `107`
- after hits: `112`
- wins (0->1): `5`
- losses (1->0): `0`
- ties: `115`
- recall delta: `0.0417`
- recall 95% bootstrap CI: `[0.0083, 0.0833]`
- MRR delta: `0.0242`
- MRR 95% bootstrap CI: `[0.0033, 0.0517]`
- exact McNemar p-value: `0.062500`

## Interpretation

- `wins` 看的是原来失败、后来成功的 query 数。
- `losses` 看的是原来成功、后来失败的 query 数。
- McNemar 只针对 paired 二分类成功/失败，不是看小数漂不漂亮。
- bootstrap CI 更适合解释增益区间，不代表严格因果证明。

## Per Query

| qid | before_success | after_success | before_rank | after_rank | mrr_delta |
|---|---|---|---:|---:|---:|
| zh001_holdout | True | True | 1 | 1 | 0.000000 |
| zh002_holdout | False | True | None | 1 | 1.000000 |
| zh003_holdout | False | False | None | None | 0.000000 |
| zh004_holdout | False | True | None | 1 | 1.000000 |
| zh005_holdout | True | True | 2 | 2 | 0.000000 |
| zh006_holdout | False | False | None | None | 0.000000 |
| zh007_holdout | False | True | None | 5 | 0.200000 |
| zh008_holdout | False | True | None | 5 | 0.200000 |
| zh009_holdout | True | True | 2 | 2 | 0.000000 |
| zh010_holdout | False | False | None | None | 0.000000 |
| zh011_holdout | False | False | None | None | 0.000000 |
| zh012_holdout | True | True | 3 | 3 | 0.000000 |
| zh013_holdout | True | True | 2 | 2 | 0.000000 |
| zh014_holdout | True | True | 2 | 2 | 0.000000 |
| zh015_holdout | True | True | 1 | 1 | 0.000000 |
| zh016_holdout | True | True | 5 | 5 | 0.000000 |
| zh017_holdout | False | False | None | None | 0.000000 |
| zh018_holdout | True | True | 1 | 1 | 0.000000 |
| zh019_holdout | True | True | 2 | 2 | 0.000000 |
| zh020_holdout | True | True | 5 | 5 | 0.000000 |
| zh021_holdout | True | True | 1 | 1 | 0.000000 |
| zh022_holdout | True | True | 1 | 1 | 0.000000 |
| zh023_holdout | True | True | 4 | 4 | 0.000000 |
| zh024_holdout | True | True | 5 | 5 | 0.000000 |
| zh025_holdout | True | True | 2 | 2 | 0.000000 |
| zh026_holdout | True | True | 2 | 2 | 0.000000 |
| zh027_holdout | False | False | None | None | 0.000000 |
| zh028_holdout | True | True | 3 | 3 | 0.000000 |
| zh029_holdout | True | True | 1 | 1 | 0.000000 |
| zh030_holdout | True | True | 5 | 5 | 0.000000 |
| zh031_holdout | True | True | 1 | 1 | 0.000000 |
| zh032_holdout | True | True | 4 | 4 | 0.000000 |
| zh033_holdout | False | False | None | None | 0.000000 |
| zh034_holdout | True | True | 4 | 4 | 0.000000 |
| zh035_holdout | True | True | 3 | 3 | 0.000000 |
| zh036_holdout | True | True | 1 | 1 | 0.000000 |
| zh037_holdout | True | True | 1 | 1 | 0.000000 |
| zh038_holdout | True | True | 1 | 1 | 0.000000 |
| zh039_holdout | True | True | 1 | 1 | 0.000000 |
| zh040_holdout | True | True | 2 | 2 | 0.000000 |
| zh041_holdout | True | True | 3 | 3 | 0.000000 |
| zh042_holdout | True | True | 1 | 1 | 0.000000 |
| zh043_holdout | True | True | 3 | 3 | 0.000000 |
| zh044_holdout | True | True | 2 | 2 | 0.000000 |
| zh045_holdout | True | True | 2 | 2 | 0.000000 |
| zh046_holdout | True | True | 4 | 4 | 0.000000 |
| zh047_holdout | True | True | 5 | 5 | 0.000000 |
| zh048_holdout | True | True | 3 | 3 | 0.000000 |
| zh049_holdout | True | True | 3 | 3 | 0.000000 |
| zh050_holdout | True | True | 1 | 1 | 0.000000 |
| zh051_holdout | True | True | 1 | 1 | 0.000000 |
| zh052_holdout | True | True | 1 | 1 | 0.000000 |
| zh053_holdout | True | True | 1 | 1 | 0.000000 |
| zh054_holdout | True | True | 2 | 2 | 0.000000 |
| zh055_holdout | True | True | 1 | 1 | 0.000000 |
| zh056_holdout | True | True | 3 | 3 | 0.000000 |
| zh057_holdout | True | True | 3 | 3 | 0.000000 |
| zh058_holdout | True | True | 4 | 4 | 0.000000 |
| zh059_holdout | True | True | 1 | 1 | 0.000000 |
| zh060_holdout | True | True | 1 | 1 | 0.000000 |
| zh061_holdout | True | True | 2 | 2 | 0.000000 |
| zh062_holdout | True | True | 1 | 1 | 0.000000 |
| zh063_holdout | True | True | 4 | 4 | 0.000000 |
| zh064_holdout | True | True | 1 | 1 | 0.000000 |
| zh065_holdout | True | True | 2 | 2 | 0.000000 |
| zh066_holdout | True | True | 2 | 2 | 0.000000 |
| zh067_holdout | False | True | None | 2 | 0.500000 |
| zh068_holdout | True | True | 2 | 2 | 0.000000 |
| zh069_holdout | True | True | 1 | 1 | 0.000000 |
| zh070_holdout | True | True | 4 | 4 | 0.000000 |
| zh071_holdout | True | True | 1 | 1 | 0.000000 |
| zh072_holdout | True | True | 1 | 1 | 0.000000 |
| zh073_holdout | True | True | 1 | 1 | 0.000000 |
| zh074_holdout | True | True | 1 | 1 | 0.000000 |
| zh075_holdout | True | True | 2 | 2 | 0.000000 |
| zh076_holdout | True | True | 1 | 1 | 0.000000 |
| zh077_holdout | True | True | 1 | 1 | 0.000000 |
| zh078_holdout | True | True | 3 | 3 | 0.000000 |
| zh079_holdout | True | True | 1 | 1 | 0.000000 |
| zh080_holdout | True | True | 1 | 1 | 0.000000 |
| zh081_holdout | True | True | 3 | 3 | 0.000000 |
| zh082_holdout | True | True | 5 | 5 | 0.000000 |
| zh083_holdout | True | True | 1 | 1 | 0.000000 |
| zh084_holdout | True | True | 1 | 1 | 0.000000 |
| zh085_holdout | True | True | 3 | 3 | 0.000000 |
| zh086_holdout | True | True | 3 | 3 | 0.000000 |
| zh087_holdout | True | True | 1 | 1 | 0.000000 |
| zh088_holdout | True | True | 2 | 2 | 0.000000 |
| zh089_holdout | True | True | 3 | 3 | 0.000000 |
| zh090_holdout | True | True | 1 | 1 | 0.000000 |
| zh091_holdout | True | True | 1 | 1 | 0.000000 |
| zh092_holdout | True | True | 1 | 1 | 0.000000 |
| zh093_holdout | True | True | 1 | 1 | 0.000000 |
| zh094_holdout | True | True | 4 | 4 | 0.000000 |
| zh095_holdout | True | True | 3 | 3 | 0.000000 |
| zh096_holdout | True | True | 2 | 2 | 0.000000 |
| zh097_holdout | True | True | 2 | 2 | 0.000000 |
| zh098_holdout | True | True | 2 | 2 | 0.000000 |
| zh099_holdout | True | True | 1 | 1 | 0.000000 |
| zh100_holdout | True | True | 1 | 1 | 0.000000 |
| zh101_holdout | False | False | None | None | 0.000000 |
| zh102_holdout | True | True | 5 | 5 | 0.000000 |
| zh103_holdout | True | True | 1 | 1 | 0.000000 |
| zh104_holdout | True | True | 4 | 4 | 0.000000 |
| zh105_holdout | True | True | 1 | 1 | 0.000000 |
| zh106_holdout | True | True | 5 | 5 | 0.000000 |
| zh107_holdout | True | True | 1 | 1 | 0.000000 |
| zh108_holdout | True | True | 3 | 3 | 0.000000 |
| zh109_holdout | True | True | 1 | 1 | 0.000000 |
| zh110_holdout | True | True | 2 | 2 | 0.000000 |
| zh111_holdout | True | True | 2 | 2 | 0.000000 |
| zh112_holdout | True | True | 1 | 1 | 0.000000 |
| zh113_holdout | True | True | 2 | 2 | 0.000000 |
| zh114_holdout | True | True | 2 | 2 | 0.000000 |
| zh115_holdout | True | True | 2 | 2 | 0.000000 |
| zh116_holdout | True | True | 2 | 2 | 0.000000 |
| zh117_holdout | True | True | 3 | 3 | 0.000000 |
| zh118_holdout | True | True | 3 | 3 | 0.000000 |
| zh119_holdout | True | True | 1 | 1 | 0.000000 |
| zh120_holdout | True | True | 2 | 2 | 0.000000 |
