# Paired Significance Report

## Summary

- n: `120`
- before hits: `17`
- after hits: `39`
- wins (0->1): `22`
- losses (1->0): `0`
- ties: `98`
- recall delta: `0.1833`
- recall 95% bootstrap CI: `[0.1167, 0.2583]`
- MRR delta: `0.0765`
- MRR 95% bootstrap CI: `[0.0450, 0.1117]`
- exact McNemar p-value: `0.000000`

## Interpretation

- `wins` 看的是原来失败、后来成功的 query 数。
- `losses` 看的是原来成功、后来失败的 query 数。
- McNemar 只针对 paired 二分类成功/失败，不是看小数漂不漂亮。
- bootstrap CI 更适合解释增益区间，不代表严格因果证明。

## Per Query

| qid | before_success | after_success | before_rank | after_rank | mrr_delta |
|---|---|---|---:|---:|---:|
| zh001_holdout | False | False | None | None | 0.000000 |
| zh002_holdout | False | False | None | None | 0.000000 |
| zh003_holdout | False | False | None | None | 0.000000 |
| zh004_holdout | False | False | None | None | 0.000000 |
| zh005_holdout | False | False | None | None | 0.000000 |
| zh006_holdout | False | False | None | None | 0.000000 |
| zh007_holdout | False | False | None | None | 0.000000 |
| zh008_holdout | False | False | None | None | 0.000000 |
| zh009_holdout | False | False | None | None | 0.000000 |
| zh010_holdout | False | False | None | None | 0.000000 |
| zh011_holdout | False | False | None | None | 0.000000 |
| zh012_holdout | False | False | None | None | 0.000000 |
| zh013_holdout | False | False | None | None | 0.000000 |
| zh014_holdout | False | False | None | None | 0.000000 |
| zh015_holdout | False | True | None | 5 | 0.200000 |
| zh016_holdout | False | False | None | None | 0.000000 |
| zh017_holdout | False | False | None | None | 0.000000 |
| zh018_holdout | False | False | None | None | 0.000000 |
| zh019_holdout | False | False | None | None | 0.000000 |
| zh020_holdout | False | False | None | None | 0.000000 |
| zh021_holdout | False | True | None | 3 | 0.333333 |
| zh022_holdout | False | False | None | None | 0.000000 |
| zh023_holdout | False | False | None | None | 0.000000 |
| zh024_holdout | False | False | None | None | 0.000000 |
| zh025_holdout | False | False | None | None | 0.000000 |
| zh026_holdout | False | True | None | 2 | 0.500000 |
| zh027_holdout | False | False | None | None | 0.000000 |
| zh028_holdout | False | False | None | None | 0.000000 |
| zh029_holdout | False | False | None | None | 0.000000 |
| zh030_holdout | False | False | None | None | 0.000000 |
| zh031_holdout | False | False | None | None | 0.000000 |
| zh032_holdout | False | False | None | None | 0.000000 |
| zh033_holdout | False | False | None | None | 0.000000 |
| zh034_holdout | False | False | None | None | 0.000000 |
| zh035_holdout | False | True | None | 2 | 0.500000 |
| zh036_holdout | False | False | None | None | 0.000000 |
| zh037_holdout | False | False | None | None | 0.000000 |
| zh038_holdout | False | False | None | None | 0.000000 |
| zh039_holdout | False | False | None | None | 0.000000 |
| zh040_holdout | False | False | None | None | 0.000000 |
| zh041_holdout | False | False | None | None | 0.000000 |
| zh042_holdout | False | True | None | 2 | 0.500000 |
| zh043_holdout | True | True | 3 | 3 | 0.000000 |
| zh044_holdout | False | False | None | None | 0.000000 |
| zh045_holdout | False | True | None | 4 | 0.250000 |
| zh046_holdout | False | False | None | None | 0.000000 |
| zh047_holdout | False | False | None | None | 0.000000 |
| zh048_holdout | False | False | None | None | 0.000000 |
| zh049_holdout | False | True | None | 4 | 0.250000 |
| zh050_holdout | False | False | None | None | 0.000000 |
| zh051_holdout | False | False | None | None | 0.000000 |
| zh052_holdout | False | True | None | 5 | 0.200000 |
| zh053_holdout | False | False | None | None | 0.000000 |
| zh054_holdout | False | False | None | None | 0.000000 |
| zh055_holdout | False | False | None | None | 0.000000 |
| zh056_holdout | False | False | None | None | 0.000000 |
| zh057_holdout | False | False | None | None | 0.000000 |
| zh058_holdout | False | False | None | None | 0.000000 |
| zh059_holdout | True | True | 2 | 2 | 0.000000 |
| zh060_holdout | False | True | None | 2 | 0.500000 |
| zh061_holdout | False | True | None | 1 | 1.000000 |
| zh062_holdout | False | False | None | None | 0.000000 |
| zh063_holdout | False | True | None | 5 | 0.200000 |
| zh064_holdout | False | False | None | None | 0.000000 |
| zh065_holdout | False | True | None | 3 | 0.333333 |
| zh066_holdout | False | False | None | None | 0.000000 |
| zh067_holdout | False | False | None | None | 0.000000 |
| zh068_holdout | False | True | None | 3 | 0.333333 |
| zh069_holdout | False | True | None | 2 | 0.500000 |
| zh070_holdout | False | False | None | None | 0.000000 |
| zh071_holdout | False | False | None | None | 0.000000 |
| zh072_holdout | False | False | None | None | 0.000000 |
| zh073_holdout | False | True | None | 2 | 0.500000 |
| zh074_holdout | False | False | None | None | 0.000000 |
| zh075_holdout | False | False | None | None | 0.000000 |
| zh076_holdout | False | False | None | None | 0.000000 |
| zh077_holdout | False | False | None | None | 0.000000 |
| zh078_holdout | False | False | None | None | 0.000000 |
| zh079_holdout | False | False | None | None | 0.000000 |
| zh080_holdout | False | True | None | 1 | 1.000000 |
| zh081_holdout | False | False | None | None | 0.000000 |
| zh082_holdout | False | False | None | None | 0.000000 |
| zh083_holdout | False | False | None | None | 0.000000 |
| zh084_holdout | True | True | 2 | 2 | 0.000000 |
| zh085_holdout | False | False | None | None | 0.000000 |
| zh086_holdout | True | True | 5 | 5 | 0.000000 |
| zh087_holdout | False | True | None | 3 | 0.333333 |
| zh088_holdout | False | True | None | 3 | 0.333333 |
| zh089_holdout | False | False | None | None | 0.000000 |
| zh090_holdout | False | False | None | None | 0.000000 |
| zh091_holdout | True | True | 1 | 1 | 0.000000 |
| zh092_holdout | True | True | 4 | 4 | 0.000000 |
| zh093_holdout | False | False | None | None | 0.000000 |
| zh094_holdout | False | False | None | None | 0.000000 |
| zh095_holdout | False | False | None | None | 0.000000 |
| zh096_holdout | False | False | None | None | 0.000000 |
| zh097_holdout | False | False | None | None | 0.000000 |
| zh098_holdout | True | True | 1 | 1 | 0.000000 |
| zh099_holdout | False | True | None | 2 | 0.500000 |
| zh100_holdout | False | False | None | None | 0.000000 |
| zh101_holdout | False | False | None | None | 0.000000 |
| zh102_holdout | False | False | None | None | 0.000000 |
| zh103_holdout | False | False | None | None | 0.000000 |
| zh104_holdout | True | True | 5 | 5 | 0.000000 |
| zh105_holdout | True | True | 3 | 3 | 0.000000 |
| zh106_holdout | False | True | None | 4 | 0.250000 |
| zh107_holdout | True | True | 5 | 5 | 0.000000 |
| zh108_holdout | True | True | 3 | 3 | 0.000000 |
| zh109_holdout | True | True | 2 | 2 | 0.000000 |
| zh110_holdout | False | False | None | None | 0.000000 |
| zh111_holdout | True | True | 5 | 5 | 0.000000 |
| zh112_holdout | False | True | None | 3 | 0.333333 |
| zh113_holdout | False | False | None | None | 0.000000 |
| zh114_holdout | True | True | 2 | 2 | 0.000000 |
| zh115_holdout | True | True | 2 | 2 | 0.000000 |
| zh116_holdout | True | True | 2 | 2 | 0.000000 |
| zh117_holdout | False | False | None | None | 0.000000 |
| zh118_holdout | False | False | None | None | 0.000000 |
| zh119_holdout | False | True | None | 3 | 0.333333 |
| zh120_holdout | True | True | 4 | 4 | 0.000000 |
