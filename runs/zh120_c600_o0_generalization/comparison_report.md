# Fixed Patch Held-out Generalization Report

## Setup

- questions: `case_zh_dureader_120/eval/questions_heldout.jsonl`
- main index: `runs/zh120_c600_o0_base`
- fixed patch source: `runs/zh120_c600_o0_patches`
- selected patch chunks: `6`
- top_k: `5`
- coverage_threshold: `0.65`

## Metrics

| Route | Recall@5 | MRR | Hits |
|---|---:|---:|---:|
| main | 0.8917 | 0.5696 | 107 / 120 |
| main + fixed patch | 0.9333 | 0.5938 | 112 / 120 |

- fixed: ['zh002_holdout', 'zh004_holdout', 'zh007_holdout', 'zh008_holdout', 'zh067_holdout']
- regressed: []
- unchanged_failure: ['zh003_holdout', 'zh006_holdout', 'zh010_holdout', 'zh011_holdout', 'zh017_holdout', 'zh027_holdout', 'zh033_holdout', 'zh101_holdout']
- unchanged_success_count: 107

## Why This Report Matters

- Patch selection is frozen before this evaluation.
- This report tests whether the already selected patch set still helps on unseen query wording.
- It is not a claim of document-level universal generalization. It is a query-held-out check for the same repaired evidence windows.

## Query Movement

| qid | movement | before rank | after rank | before coverage | after coverage |
|---|---|---:|---:|---:|---:|
| zh001_holdout | unchanged_success | 1 | 1 | 0.778 | 0.778 |
| zh002_holdout | fixed | None | 1 | 0.566 | 0.952 |
| zh003_holdout | unchanged_failure | None | None | 0.511 | 0.511 |
| zh004_holdout | fixed | None | 1 | 0.576 | 0.786 |
| zh005_holdout | unchanged_success | 2 | 2 | 0.661 | 0.661 |
| zh006_holdout | unchanged_failure | None | None | 0.605 | 0.605 |
| zh007_holdout | fixed | None | 5 | 0.648 | 0.886 |
| zh008_holdout | fixed | None | 5 | 0.623 | 0.834 |
| zh009_holdout | unchanged_success | 2 | 2 | 0.732 | 0.732 |
| zh010_holdout | unchanged_failure | None | None | 0.587 | 0.587 |
| zh011_holdout | unchanged_failure | None | None | 0.623 | 0.623 |
| zh012_holdout | unchanged_success | 3 | 3 | 0.708 | 0.708 |
| zh013_holdout | unchanged_success | 2 | 2 | 0.786 | 0.786 |
| zh014_holdout | unchanged_success | 2 | 2 | 0.755 | 0.755 |
| zh015_holdout | unchanged_success | 1 | 1 | 0.777 | 0.777 |
| zh016_holdout | unchanged_success | 5 | 5 | 0.797 | 0.797 |
| zh017_holdout | unchanged_failure | None | None | 0.629 | 0.629 |
| zh018_holdout | unchanged_success | 1 | 1 | 0.736 | 0.736 |
| zh019_holdout | unchanged_success | 2 | 2 | 0.885 | 0.885 |
| zh020_holdout | unchanged_success | 5 | 5 | 0.824 | 0.824 |
| zh021_holdout | unchanged_success | 1 | 1 | 0.73 | 0.73 |
| zh022_holdout | unchanged_success | 1 | 1 | 0.653 | 0.653 |
| zh023_holdout | unchanged_success | 4 | 4 | 0.765 | 0.765 |
| zh024_holdout | unchanged_success | 5 | 5 | 0.879 | 0.879 |
| zh025_holdout | unchanged_success | 2 | 2 | 0.841 | 0.841 |
| zh026_holdout | unchanged_success | 2 | 2 | 0.705 | 0.705 |
| zh027_holdout | unchanged_failure | None | None | 0.305 | 0.305 |
| zh028_holdout | unchanged_success | 3 | 3 | 0.947 | 0.947 |
| zh029_holdout | unchanged_success | 1 | 1 | 0.712 | 0.712 |
| zh030_holdout | unchanged_success | 5 | 5 | 0.833 | 0.833 |
| zh031_holdout | unchanged_success | 1 | 1 | 0.94 | 0.94 |
| zh032_holdout | unchanged_success | 4 | 4 | 0.914 | 0.914 |
| zh033_holdout | unchanged_failure | None | None | 0.574 | 0.574 |
| zh034_holdout | unchanged_success | 4 | 4 | 0.856 | 0.856 |
| zh035_holdout | unchanged_success | 3 | 3 | 0.897 | 0.897 |
| zh036_holdout | unchanged_success | 1 | 1 | 0.946 | 0.946 |
| zh037_holdout | unchanged_success | 1 | 1 | 0.711 | 0.711 |
| zh038_holdout | unchanged_success | 1 | 1 | 0.7 | 0.7 |
| zh039_holdout | unchanged_success | 1 | 1 | 0.945 | 0.945 |
| zh040_holdout | unchanged_success | 2 | 2 | 0.998 | 0.998 |
| zh041_holdout | unchanged_success | 3 | 3 | 0.733 | 0.733 |
| zh042_holdout | unchanged_success | 1 | 1 | 0.98 | 0.98 |
| zh043_holdout | unchanged_success | 3 | 3 | 0.833 | 0.833 |
| zh044_holdout | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh045_holdout | unchanged_success | 2 | 2 | 0.869 | 0.869 |
| zh046_holdout | unchanged_success | 4 | 4 | 0.657 | 0.657 |
| zh047_holdout | unchanged_success | 5 | 5 | 0.792 | 0.792 |
| zh048_holdout | unchanged_success | 3 | 3 | 0.744 | 0.744 |
| zh049_holdout | unchanged_success | 3 | 3 | 0.982 | 0.982 |
| zh050_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh051_holdout | unchanged_success | 1 | 1 | 0.896 | 0.896 |
| zh052_holdout | unchanged_success | 1 | 1 | 0.928 | 0.928 |
| zh053_holdout | unchanged_success | 1 | 1 | 0.914 | 0.914 |
| zh054_holdout | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh055_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh056_holdout | unchanged_success | 3 | 3 | 0.833 | 0.833 |
| zh057_holdout | unchanged_success | 3 | 3 | 0.851 | 0.854 |
| zh058_holdout | unchanged_success | 4 | 4 | 1.0 | 1.0 |
| zh059_holdout | unchanged_success | 1 | 1 | 0.871 | 0.871 |
| zh060_holdout | unchanged_success | 1 | 1 | 0.678 | 0.678 |
| zh061_holdout | unchanged_success | 2 | 2 | 0.782 | 0.782 |
| zh062_holdout | unchanged_success | 1 | 1 | 0.8 | 0.8 |
| zh063_holdout | unchanged_success | 4 | 4 | 1.0 | 1.0 |
| zh064_holdout | unchanged_success | 1 | 1 | 0.995 | 0.995 |
| zh065_holdout | unchanged_success | 2 | 2 | 0.683 | 0.683 |
| zh066_holdout | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh067_holdout | fixed | None | 2 | 0.646 | 0.997 |
| zh068_holdout | unchanged_success | 2 | 2 | 0.7 | 0.7 |
| zh069_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh070_holdout | unchanged_success | 4 | 4 | 0.878 | 0.878 |
| zh071_holdout | unchanged_success | 1 | 1 | 0.948 | 0.948 |
| zh072_holdout | unchanged_success | 1 | 1 | 0.984 | 0.984 |
| zh073_holdout | unchanged_success | 1 | 1 | 0.942 | 0.942 |
| zh074_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh075_holdout | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh076_holdout | unchanged_success | 1 | 1 | 0.781 | 0.781 |
| zh077_holdout | unchanged_success | 1 | 1 | 0.852 | 0.852 |
| zh078_holdout | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh079_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh080_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh081_holdout | unchanged_success | 3 | 3 | 0.726 | 0.726 |
| zh082_holdout | unchanged_success | 5 | 5 | 1.0 | 1.0 |
| zh083_holdout | unchanged_success | 1 | 1 | 0.776 | 0.776 |
| zh084_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh085_holdout | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh086_holdout | unchanged_success | 3 | 3 | 0.79 | 0.79 |
| zh087_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh088_holdout | unchanged_success | 2 | 2 | 0.79 | 0.79 |
| zh089_holdout | unchanged_success | 3 | 3 | 0.791 | 0.791 |
| zh090_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh091_holdout | unchanged_success | 1 | 1 | 0.808 | 0.808 |
| zh092_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh093_holdout | unchanged_success | 1 | 1 | 0.846 | 0.846 |
| zh094_holdout | unchanged_success | 4 | 4 | 0.886 | 0.886 |
| zh095_holdout | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh096_holdout | unchanged_success | 2 | 2 | 0.72 | 0.72 |
| zh097_holdout | unchanged_success | 2 | 2 | 0.89 | 0.89 |
| zh098_holdout | unchanged_success | 2 | 2 | 0.873 | 0.873 |
| zh099_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh100_holdout | unchanged_success | 1 | 1 | 0.913 | 0.913 |
| zh101_holdout | unchanged_failure | None | None | 0.592 | 0.592 |
| zh102_holdout | unchanged_success | 5 | 5 | 0.807 | 0.807 |
| zh103_holdout | unchanged_success | 1 | 1 | 0.874 | 0.874 |
| zh104_holdout | unchanged_success | 4 | 4 | 0.859 | 0.859 |
| zh105_holdout | unchanged_success | 1 | 1 | 0.789 | 0.789 |
| zh106_holdout | unchanged_success | 5 | 5 | 0.653 | 0.653 |
| zh107_holdout | unchanged_success | 1 | 1 | 0.982 | 0.982 |
| zh108_holdout | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh109_holdout | unchanged_success | 1 | 1 | 0.94 | 0.94 |
| zh110_holdout | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh111_holdout | unchanged_success | 2 | 2 | 0.986 | 0.986 |
| zh112_holdout | unchanged_success | 1 | 1 | 0.982 | 0.982 |
| zh113_holdout | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh114_holdout | unchanged_success | 2 | 2 | 0.867 | 0.867 |
| zh115_holdout | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh116_holdout | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh117_holdout | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh118_holdout | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh119_holdout | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh120_holdout | unchanged_success | 2 | 2 | 1.0 | 1.0 |
