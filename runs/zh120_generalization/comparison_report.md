# Fixed Patch Held-out Generalization Report

## Setup

- questions: `case_zh_dureader_120/eval/questions_heldout.jsonl`
- main index: `runs/zh120_base`
- fixed patch source: `runs/zh120_patches`
- selected patch chunks: `24`
- top_k: `5`
- coverage_threshold: `0.65`

## Metrics

| Route | Recall@5 | MRR | Hits |
|---|---:|---:|---:|
| main | 0.1417 | 0.0608 | 17 / 120 |
| main + fixed patch | 0.3250 | 0.1374 | 39 / 120 |

- fixed: ['zh015_holdout', 'zh021_holdout', 'zh026_holdout', 'zh035_holdout', 'zh042_holdout', 'zh045_holdout', 'zh049_holdout', 'zh052_holdout', 'zh060_holdout', 'zh061_holdout', 'zh063_holdout', 'zh065_holdout', 'zh068_holdout', 'zh069_holdout', 'zh073_holdout', 'zh080_holdout', 'zh087_holdout', 'zh088_holdout', 'zh099_holdout', 'zh106_holdout', 'zh112_holdout', 'zh119_holdout']
- regressed: []
- unchanged_failure: ['zh001_holdout', 'zh002_holdout', 'zh003_holdout', 'zh004_holdout', 'zh005_holdout', 'zh006_holdout', 'zh007_holdout', 'zh008_holdout', 'zh009_holdout', 'zh010_holdout', 'zh011_holdout', 'zh012_holdout', 'zh013_holdout', 'zh014_holdout', 'zh016_holdout', 'zh017_holdout', 'zh018_holdout', 'zh019_holdout', 'zh020_holdout', 'zh022_holdout', 'zh023_holdout', 'zh024_holdout', 'zh025_holdout', 'zh027_holdout', 'zh028_holdout', 'zh029_holdout', 'zh030_holdout', 'zh031_holdout', 'zh032_holdout', 'zh033_holdout', 'zh034_holdout', 'zh036_holdout', 'zh037_holdout', 'zh038_holdout', 'zh039_holdout', 'zh040_holdout', 'zh041_holdout', 'zh044_holdout', 'zh046_holdout', 'zh047_holdout', 'zh048_holdout', 'zh050_holdout', 'zh051_holdout', 'zh053_holdout', 'zh054_holdout', 'zh055_holdout', 'zh056_holdout', 'zh057_holdout', 'zh058_holdout', 'zh062_holdout', 'zh064_holdout', 'zh066_holdout', 'zh067_holdout', 'zh070_holdout', 'zh071_holdout', 'zh072_holdout', 'zh074_holdout', 'zh075_holdout', 'zh076_holdout', 'zh077_holdout', 'zh078_holdout', 'zh079_holdout', 'zh081_holdout', 'zh082_holdout', 'zh083_holdout', 'zh085_holdout', 'zh089_holdout', 'zh090_holdout', 'zh093_holdout', 'zh094_holdout', 'zh095_holdout', 'zh096_holdout', 'zh097_holdout', 'zh100_holdout', 'zh101_holdout', 'zh102_holdout', 'zh103_holdout', 'zh110_holdout', 'zh113_holdout', 'zh117_holdout', 'zh118_holdout']
- unchanged_success_count: 17

## Why This Report Matters

- Patch selection is frozen before this evaluation.
- This report tests whether the already selected patch set still helps on unseen query wording.
- It is not a claim of document-level universal generalization. It is a query-held-out check for the same repaired evidence windows.

## Query Movement

| qid | movement | before rank | after rank | before coverage | after coverage |
|---|---|---:|---:|---:|---:|
| zh001_holdout | unchanged_failure | None | None | 0.646 | 0.646 |
| zh002_holdout | unchanged_failure | None | None | 0.163 | 0.163 |
| zh003_holdout | unchanged_failure | None | None | 0.206 | 0.206 |
| zh004_holdout | unchanged_failure | None | None | 0.276 | 0.276 |
| zh005_holdout | unchanged_failure | None | None | 0.38 | 0.38 |
| zh006_holdout | unchanged_failure | None | None | 0.337 | 0.337 |
| zh007_holdout | unchanged_failure | None | None | 0.346 | 0.346 |
| zh008_holdout | unchanged_failure | None | None | 0.276 | 0.276 |
| zh009_holdout | unchanged_failure | None | None | 0.446 | 0.446 |
| zh010_holdout | unchanged_failure | None | None | 0.277 | 0.277 |
| zh011_holdout | unchanged_failure | None | None | 0.19 | 0.19 |
| zh012_holdout | unchanged_failure | None | None | 0.365 | 0.365 |
| zh013_holdout | unchanged_failure | None | None | 0.395 | 0.395 |
| zh014_holdout | unchanged_failure | None | None | 0.38 | 0.38 |
| zh015_holdout | fixed | None | 5 | 0.462 | 0.775 |
| zh016_holdout | unchanged_failure | None | None | 0.405 | 0.405 |
| zh017_holdout | unchanged_failure | None | None | 0.321 | 0.321 |
| zh018_holdout | unchanged_failure | None | None | 0.429 | 0.429 |
| zh019_holdout | unchanged_failure | None | None | 0.553 | 0.553 |
| zh020_holdout | unchanged_failure | None | None | 0.409 | 0.409 |
| zh021_holdout | fixed | None | 3 | 0.325 | 0.692 |
| zh022_holdout | unchanged_failure | None | None | 0.386 | 0.386 |
| zh023_holdout | unchanged_failure | None | None | 0.472 | 0.472 |
| zh024_holdout | unchanged_failure | None | None | 0.575 | 0.575 |
| zh025_holdout | unchanged_failure | None | None | 0.448 | 0.448 |
| zh026_holdout | fixed | None | 2 | 0.487 | 0.921 |
| zh027_holdout | unchanged_failure | None | None | 0.041 | 0.041 |
| zh028_holdout | unchanged_failure | None | None | 0.606 | 0.606 |
| zh029_holdout | unchanged_failure | None | None | 0.524 | 0.524 |
| zh030_holdout | unchanged_failure | None | None | 0.289 | 0.289 |
| zh031_holdout | unchanged_failure | None | None | 0.517 | 0.517 |
| zh032_holdout | unchanged_failure | None | None | 0.396 | 0.396 |
| zh033_holdout | unchanged_failure | None | None | 0.349 | 0.349 |
| zh034_holdout | unchanged_failure | None | None | 0.49 | 0.49 |
| zh035_holdout | fixed | None | 2 | 0.394 | 0.772 |
| zh036_holdout | unchanged_failure | None | None | 0.525 | 0.525 |
| zh037_holdout | unchanged_failure | None | None | 0.44 | 0.44 |
| zh038_holdout | unchanged_failure | None | None | 0.494 | 0.494 |
| zh039_holdout | unchanged_failure | None | None | 0.486 | 0.486 |
| zh040_holdout | unchanged_failure | None | None | 0.493 | 0.493 |
| zh041_holdout | unchanged_failure | None | None | 0.419 | 0.419 |
| zh042_holdout | fixed | None | 2 | 0.411 | 0.842 |
| zh043_holdout | unchanged_success | 3 | 3 | 0.702 | 0.702 |
| zh044_holdout | unchanged_failure | None | None | 0.296 | 0.296 |
| zh045_holdout | fixed | None | 4 | 0.521 | 0.835 |
| zh046_holdout | unchanged_failure | None | None | 0.491 | 0.491 |
| zh047_holdout | unchanged_failure | None | None | 0.422 | 0.422 |
| zh048_holdout | unchanged_failure | None | None | 0.477 | 0.477 |
| zh049_holdout | fixed | None | 4 | 0.583 | 0.753 |
| zh050_holdout | unchanged_failure | None | None | 0.265 | 0.265 |
| zh051_holdout | unchanged_failure | None | None | 0.533 | 0.533 |
| zh052_holdout | fixed | None | 5 | 0.482 | 0.733 |
| zh053_holdout | unchanged_failure | None | None | 0.481 | 0.481 |
| zh054_holdout | unchanged_failure | None | None | 0.552 | 0.552 |
| zh055_holdout | unchanged_failure | None | None | 0.611 | 0.611 |
| zh056_holdout | unchanged_failure | None | None | 0.51 | 0.51 |
| zh057_holdout | unchanged_failure | None | None | 0.546 | 0.546 |
| zh058_holdout | unchanged_failure | None | None | 0.25 | 0.25 |
| zh059_holdout | unchanged_success | 2 | 2 | 0.656 | 0.656 |
| zh060_holdout | fixed | None | 2 | 0.27 | 0.717 |
| zh061_holdout | fixed | None | 1 | 0.342 | 0.723 |
| zh062_holdout | unchanged_failure | None | None | 0.506 | 0.506 |
| zh063_holdout | fixed | None | 5 | 0.526 | 0.66 |
| zh064_holdout | unchanged_failure | None | None | 0.639 | 0.639 |
| zh065_holdout | fixed | None | 3 | 0.581 | 0.825 |
| zh066_holdout | unchanged_failure | None | None | 0.567 | 0.567 |
| zh067_holdout | unchanged_failure | None | None | 0.432 | 0.432 |
| zh068_holdout | fixed | None | 3 | 0.553 | 0.67 |
| zh069_holdout | fixed | None | 2 | 0.24 | 1.0 |
| zh070_holdout | unchanged_failure | None | None | 0.375 | 0.375 |
| zh071_holdout | unchanged_failure | None | None | 0.617 | 0.617 |
| zh072_holdout | unchanged_failure | None | None | 0.42 | 0.42 |
| zh073_holdout | fixed | None | 2 | 0.534 | 0.854 |
| zh074_holdout | unchanged_failure | None | None | 0.595 | 0.595 |
| zh075_holdout | unchanged_failure | None | None | 0.137 | 0.137 |
| zh076_holdout | unchanged_failure | None | None | 0.567 | 0.567 |
| zh077_holdout | unchanged_failure | None | None | 0.584 | 0.584 |
| zh078_holdout | unchanged_failure | None | None | 0.578 | 0.578 |
| zh079_holdout | unchanged_failure | None | None | 0.527 | 0.527 |
| zh080_holdout | fixed | None | 1 | 0.545 | 0.848 |
| zh081_holdout | unchanged_failure | None | None | 0.588 | 0.588 |
| zh082_holdout | unchanged_failure | None | None | 0.09 | 0.09 |
| zh083_holdout | unchanged_failure | None | None | 0.637 | 0.637 |
| zh084_holdout | unchanged_success | 2 | 2 | 0.71 | 0.71 |
| zh085_holdout | unchanged_failure | None | None | 0.371 | 0.371 |
| zh086_holdout | unchanged_success | 5 | 5 | 0.656 | 0.656 |
| zh087_holdout | fixed | None | 3 | 0.542 | 0.676 |
| zh088_holdout | fixed | None | 3 | 0.605 | 0.949 |
| zh089_holdout | unchanged_failure | None | None | 0.456 | 0.456 |
| zh090_holdout | unchanged_failure | None | None | 0.404 | 0.404 |
| zh091_holdout | unchanged_success | 1 | 1 | 0.668 | 0.668 |
| zh092_holdout | unchanged_success | 4 | 4 | 0.662 | 0.662 |
| zh093_holdout | unchanged_failure | None | None | 0.256 | 0.256 |
| zh094_holdout | unchanged_failure | None | None | 0.077 | 0.077 |
| zh095_holdout | unchanged_failure | None | None | 0.576 | 0.576 |
| zh096_holdout | unchanged_failure | None | None | 0.557 | 0.557 |
| zh097_holdout | unchanged_failure | None | None | 0.526 | 0.526 |
| zh098_holdout | unchanged_success | 1 | 1 | 0.682 | 0.682 |
| zh099_holdout | fixed | None | 2 | 0.626 | 0.906 |
| zh100_holdout | unchanged_failure | None | None | 0.58 | 0.58 |
| zh101_holdout | unchanged_failure | None | None | 0.577 | 0.577 |
| zh102_holdout | unchanged_failure | None | None | 0.164 | 0.164 |
| zh103_holdout | unchanged_failure | None | None | 0.623 | 0.623 |
| zh104_holdout | unchanged_success | 5 | 5 | 0.722 | 0.722 |
| zh105_holdout | unchanged_success | 3 | 3 | 0.669 | 0.669 |
| zh106_holdout | fixed | None | 4 | 0.361 | 0.773 |
| zh107_holdout | unchanged_success | 5 | 5 | 0.665 | 0.665 |
| zh108_holdout | unchanged_success | 3 | 3 | 0.674 | 0.674 |
| zh109_holdout | unchanged_success | 2 | 2 | 0.656 | 0.656 |
| zh110_holdout | unchanged_failure | None | None | 0.607 | 0.607 |
| zh111_holdout | unchanged_success | 5 | 5 | 0.689 | 0.689 |
| zh112_holdout | fixed | None | 3 | 0.613 | 0.849 |
| zh113_holdout | unchanged_failure | None | None | 0.625 | 0.625 |
| zh114_holdout | unchanged_success | 2 | 2 | 0.656 | 0.656 |
| zh115_holdout | unchanged_success | 2 | 2 | 0.711 | 0.711 |
| zh116_holdout | unchanged_success | 2 | 2 | 0.671 | 0.671 |
| zh117_holdout | unchanged_failure | None | None | 0.227 | 0.227 |
| zh118_holdout | unchanged_failure | None | None | 0.354 | 0.354 |
| zh119_holdout | fixed | None | 3 | 0.534 | 0.959 |
| zh120_holdout | unchanged_success | 4 | 4 | 0.67 | 0.67 |
