# Main-only vs Main+Patch Comparison

## Metrics

| Metric | Main-only | Main+Patch | Delta |
|---|---:|---:|---:|
| Recall@5 | 0.1417 | 0.3417 | +0.2000 |
| MRR | 0.0651 | 0.1501 | +0.0850 |
| Hits | 17 / 120 | 41 / 120 | +24 |

- main_chunks: 1634
- patch_chunks: 24
- patch/main ratio: 1.47%

## Query Movement

- fixed: ['zh015', 'zh021', 'zh026', 'zh035', 'zh042', 'zh045', 'zh049', 'zh052', 'zh056', 'zh060', 'zh061', 'zh063', 'zh065', 'zh068', 'zh069', 'zh073', 'zh080', 'zh087', 'zh088', 'zh099', 'zh106', 'zh112', 'zh118', 'zh119']
- regressed: []
- unchanged_failure: ['zh001', 'zh002', 'zh003', 'zh004', 'zh005', 'zh006', 'zh007', 'zh008', 'zh009', 'zh010', 'zh011', 'zh012', 'zh013', 'zh014', 'zh016', 'zh017', 'zh018', 'zh019', 'zh020', 'zh022', 'zh023', 'zh024', 'zh025', 'zh027', 'zh028', 'zh029', 'zh030', 'zh031', 'zh032', 'zh033', 'zh034', 'zh036', 'zh037', 'zh038', 'zh039', 'zh040', 'zh041', 'zh044', 'zh046', 'zh047', 'zh048', 'zh050', 'zh051', 'zh053', 'zh054', 'zh055', 'zh057', 'zh058', 'zh062', 'zh064', 'zh066', 'zh067', 'zh070', 'zh071', 'zh072', 'zh074', 'zh075', 'zh076', 'zh077', 'zh078', 'zh079', 'zh081', 'zh082', 'zh083', 'zh085', 'zh089', 'zh090', 'zh093', 'zh094', 'zh095', 'zh096', 'zh097', 'zh100', 'zh101', 'zh102', 'zh103', 'zh110', 'zh113', 'zh117']
- unchanged_success_count: 17

| qid | movement | before rank | after rank | before coverage | after coverage |
|---|---|---:|---:|---:|---:|
| zh001 | unchanged_failure | None | None | 0.646 | 0.646 |
| zh002 | unchanged_failure | None | None | 0.163 | 0.163 |
| zh003 | unchanged_failure | None | None | 0.206 | 0.206 |
| zh004 | unchanged_failure | None | None | 0.276 | 0.276 |
| zh005 | unchanged_failure | None | None | 0.361 | 0.361 |
| zh006 | unchanged_failure | None | None | 0.31 | 0.31 |
| zh007 | unchanged_failure | None | None | 0.33 | 0.33 |
| zh008 | unchanged_failure | None | None | 0.276 | 0.276 |
| zh009 | unchanged_failure | None | None | 0.42 | 0.42 |
| zh010 | unchanged_failure | None | None | 0.277 | 0.277 |
| zh011 | unchanged_failure | None | None | 0.19 | 0.19 |
| zh012 | unchanged_failure | None | None | 0.365 | 0.365 |
| zh013 | unchanged_failure | None | None | 0.395 | 0.395 |
| zh014 | unchanged_failure | None | None | 0.336 | 0.336 |
| zh015 | fixed | None | 5 | 0.462 | 0.775 |
| zh016 | unchanged_failure | None | None | 0.405 | 0.405 |
| zh017 | unchanged_failure | None | None | 0.321 | 0.321 |
| zh018 | unchanged_failure | None | None | 0.429 | 0.429 |
| zh019 | unchanged_failure | None | None | 0.553 | 0.553 |
| zh020 | unchanged_failure | None | None | 0.124 | 0.124 |
| zh021 | fixed | None | 3 | 0.325 | 0.692 |
| zh022 | unchanged_failure | None | None | 0.386 | 0.386 |
| zh023 | unchanged_failure | None | None | 0.472 | 0.472 |
| zh024 | unchanged_failure | None | None | 0.41 | 0.41 |
| zh025 | unchanged_failure | None | None | 0.448 | 0.448 |
| zh026 | fixed | None | 4 | 0.487 | 0.921 |
| zh027 | unchanged_failure | None | None | 0.041 | 0.041 |
| zh028 | unchanged_failure | None | None | 0.606 | 0.606 |
| zh029 | unchanged_failure | None | None | 0.524 | 0.524 |
| zh030 | unchanged_failure | None | None | 0.289 | 0.289 |
| zh031 | unchanged_failure | None | None | 0.517 | 0.517 |
| zh032 | unchanged_failure | None | None | 0.396 | 0.396 |
| zh033 | unchanged_failure | None | None | 0.349 | 0.349 |
| zh034 | unchanged_failure | None | None | 0.49 | 0.49 |
| zh035 | fixed | None | 3 | 0.424 | 0.772 |
| zh036 | unchanged_failure | None | None | 0.525 | 0.525 |
| zh037 | unchanged_failure | None | None | 0.44 | 0.44 |
| zh038 | unchanged_failure | None | None | 0.494 | 0.494 |
| zh039 | unchanged_failure | None | None | 0.486 | 0.486 |
| zh040 | unchanged_failure | None | None | 0.493 | 0.493 |
| zh041 | unchanged_failure | None | None | 0.419 | 0.419 |
| zh042 | fixed | None | 2 | 0.411 | 0.842 |
| zh043 | unchanged_success | 3 | 3 | 0.702 | 0.702 |
| zh044 | unchanged_failure | None | None | 0.296 | 0.296 |
| zh045 | fixed | None | 3 | 0.536 | 0.835 |
| zh046 | unchanged_failure | None | None | 0.491 | 0.491 |
| zh047 | unchanged_failure | None | None | 0.6 | 0.6 |
| zh048 | unchanged_failure | None | None | 0.472 | 0.472 |
| zh049 | fixed | None | 4 | 0.583 | 0.753 |
| zh050 | unchanged_failure | None | None | 0.265 | 0.265 |
| zh051 | unchanged_failure | None | None | 0.533 | 0.533 |
| zh052 | fixed | None | 5 | 0.482 | 0.733 |
| zh053 | unchanged_failure | None | None | 0.481 | 0.481 |
| zh054 | unchanged_failure | None | None | 0.552 | 0.552 |
| zh055 | unchanged_failure | None | None | 0.611 | 0.611 |
| zh056 | fixed | None | 4 | 0.51 | 0.908 |
| zh057 | unchanged_failure | None | None | 0.166 | 0.166 |
| zh058 | unchanged_failure | None | None | 0.25 | 0.25 |
| zh059 | unchanged_success | 2 | 2 | 0.656 | 0.656 |
| zh060 | fixed | None | 1 | 0.27 | 0.717 |
| zh061 | fixed | None | 1 | 0.342 | 0.723 |
| zh062 | unchanged_failure | None | None | 0.253 | 0.253 |
| zh063 | fixed | None | 5 | 0.526 | 0.66 |
| zh064 | unchanged_failure | None | None | 0.639 | 0.639 |
| zh065 | fixed | None | 5 | 0.581 | 0.825 |
| zh066 | unchanged_failure | None | None | 0.567 | 0.567 |
| zh067 | unchanged_failure | None | None | 0.432 | 0.432 |
| zh068 | fixed | None | 2 | 0.553 | 0.67 |
| zh069 | fixed | None | 1 | 0.64 | 1.0 |
| zh070 | unchanged_failure | None | None | 0.375 | 0.375 |
| zh071 | unchanged_failure | None | None | 0.617 | 0.617 |
| zh072 | unchanged_failure | None | None | 0.42 | 0.42 |
| zh073 | fixed | None | 3 | 0.534 | 0.854 |
| zh074 | unchanged_failure | None | None | 0.595 | 0.595 |
| zh075 | unchanged_failure | None | None | 0.137 | 0.137 |
| zh076 | unchanged_failure | None | None | 0.567 | 0.567 |
| zh077 | unchanged_failure | None | None | 0.584 | 0.584 |
| zh078 | unchanged_failure | None | None | 0.578 | 0.578 |
| zh079 | unchanged_failure | None | None | 0.527 | 0.527 |
| zh080 | fixed | None | 1 | 0.545 | 0.848 |
| zh081 | unchanged_failure | None | None | 0.588 | 0.588 |
| zh082 | unchanged_failure | None | None | 0.09 | 0.09 |
| zh083 | unchanged_failure | None | None | 0.637 | 0.637 |
| zh084 | unchanged_success | 1 | 1 | 0.71 | 0.71 |
| zh085 | unchanged_failure | None | None | 0.371 | 0.371 |
| zh086 | unchanged_success | 5 | 5 | 0.656 | 0.656 |
| zh087 | fixed | None | 5 | 0.542 | 0.676 |
| zh088 | fixed | None | 3 | 0.605 | 0.949 |
| zh089 | unchanged_failure | None | None | 0.456 | 0.456 |
| zh090 | unchanged_failure | None | None | 0.545 | 0.545 |
| zh091 | unchanged_success | 1 | 1 | 0.668 | 0.668 |
| zh092 | unchanged_success | 5 | 5 | 0.662 | 0.662 |
| zh093 | unchanged_failure | None | None | 0.179 | 0.179 |
| zh094 | unchanged_failure | None | None | 0.077 | 0.077 |
| zh095 | unchanged_failure | None | None | 0.576 | 0.576 |
| zh096 | unchanged_failure | None | None | 0.557 | 0.557 |
| zh097 | unchanged_failure | None | None | 0.407 | 0.407 |
| zh098 | unchanged_success | 1 | 1 | 0.682 | 0.682 |
| zh099 | fixed | None | 2 | 0.626 | 0.906 |
| zh100 | unchanged_failure | None | None | 0.58 | 0.58 |
| zh101 | unchanged_failure | None | None | 0.577 | 0.577 |
| zh102 | unchanged_failure | None | None | 0.164 | 0.164 |
| zh103 | unchanged_failure | None | None | 0.623 | 0.623 |
| zh104 | unchanged_success | 5 | 5 | 0.722 | 0.722 |
| zh105 | unchanged_success | 3 | 3 | 0.669 | 0.669 |
| zh106 | fixed | None | 3 | 0.361 | 0.773 |
| zh107 | unchanged_success | 5 | 5 | 0.665 | 0.665 |
| zh108 | unchanged_success | 5 | 5 | 0.674 | 0.674 |
| zh109 | unchanged_success | 2 | 2 | 0.656 | 0.656 |
| zh110 | unchanged_failure | None | None | 0.607 | 0.607 |
| zh111 | unchanged_success | 5 | 5 | 0.689 | 0.689 |
| zh112 | fixed | None | 2 | 0.613 | 0.849 |
| zh113 | unchanged_failure | None | None | 0.52 | 0.52 |
| zh114 | unchanged_success | 1 | 1 | 0.656 | 0.656 |
| zh115 | unchanged_success | 2 | 2 | 0.711 | 0.711 |
| zh116 | unchanged_success | 4 | 4 | 0.671 | 0.671 |
| zh117 | unchanged_failure | None | None | 0.227 | 0.227 |
| zh118 | fixed | None | 5 | 0.354 | 0.897 |
| zh119 | fixed | None | 4 | 0.534 | 0.959 |
| zh120 | unchanged_success | 5 | 5 | 0.67 | 0.67 |

## Candidate Probe / Selected Patch

| qid | selected patch | type | individual rank | text_len |
|---|---|---|---:|---:|
| zh015 | `patch_zh015_015_adjacent_merge` | `adjacent_merge` | 5 | 769 |
| zh021 | `patch_zh021_021_adjacent_merge` | `adjacent_merge` | 3 | 770 |
| zh026 | `patch_zh026_026_adjacent_merge` | `adjacent_merge` | 4 | 769 |
| zh035 | `patch_zh035_035_adjacent_merge` | `adjacent_merge` | 3 | 769 |
| zh042 | `patch_zh042_042_contextual` | `contextual` | 2 | 678 |
| zh045 | `patch_zh045_044_local_proposition` | `local_proposition` | 3 | 670 |
| zh049 | `patch_zh049_048_adjacent_merge` | `adjacent_merge` | 4 | 770 |
| zh052 | `patch_zh052_051_adjacent_merge` | `adjacent_merge` | 5 | 745 |
| zh056 | `patch_zh056_055_adjacent_merge` | `adjacent_merge` | 4 | 770 |
| zh060 | `patch_zh060_058_local_proposition` | `local_proposition` | 1 | 556 |
| zh061 | `patch_zh061_059_adjacent_merge` | `adjacent_merge` | 1 | 772 |
| zh063 | `patch_zh063_061_adjacent_merge` | `adjacent_merge` | 5 | 772 |
| zh065 | `patch_zh065_063_local_summary` | `local_summary` | 5 | 456 |
| zh068 | `patch_zh068_066_adjacent_merge` | `adjacent_merge` | 2 | 770 |
| zh069 | `patch_zh069_067_adjacent_merge` | `adjacent_merge` | 1 | 769 |
| zh073 | `patch_zh073_071_adjacent_merge` | `adjacent_merge` | 3 | 770 |
| zh080 | `patch_zh080_078_adjacent_merge` | `adjacent_merge` | 1 | 772 |
| zh087 | `patch_zh087_083_adjacent_merge` | `adjacent_merge` | 5 | 768 |
| zh088 | `patch_zh088_084_contextual` | `contextual` | 3 | 657 |
| zh099 | `patch_zh099_092_adjacent_merge` | `adjacent_merge` | 2 | 772 |
| zh106 | `patch_zh106_097_adjacent_merge` | `adjacent_merge` | 3 | 744 |
| zh112 | `patch_zh112_099_local_summary` | `local_summary` | 2 | 456 |
| zh118 | `patch_zh118_102_adjacent_merge` | `adjacent_merge` | 5 | 770 |
| zh119 | `patch_zh119_103_contextual` | `contextual` | 4 | 680 |

## Patch Decisions

| patch_id | source qid | status | before rank | after rank | reason |
|---|---|---|---:|---:|---|
| patch_zh001_001_adjacent_merge | zh001 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh001_001_contextual | zh001 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh001_001_local_proposition | zh001 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh001_001_local_summary | zh001 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh002_002_adjacent_merge | zh002 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh002_002_contextual | zh002 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh002_002_local_proposition | zh002 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh002_002_local_summary | zh002 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh003_003_adjacent_merge | zh003 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh003_003_contextual | zh003 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh003_003_local_proposition | zh003 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh003_003_local_summary | zh003 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh004_004_adjacent_merge | zh004 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh004_004_contextual | zh004 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh004_004_local_proposition | zh004 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh004_004_local_summary | zh004 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh005_005_adjacent_merge | zh005 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh005_005_contextual | zh005 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh005_005_local_proposition | zh005 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh005_005_local_summary | zh005 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh006_006_adjacent_merge | zh006 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh006_006_contextual | zh006 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh006_006_local_proposition | zh006 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh006_006_local_summary | zh006 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh007_007_adjacent_merge | zh007 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh007_007_contextual | zh007 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh007_007_local_proposition | zh007 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh007_007_local_summary | zh007 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh008_008_adjacent_merge | zh008 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh008_008_contextual | zh008 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh008_008_local_proposition | zh008 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh008_008_local_summary | zh008 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh009_009_adjacent_merge | zh009 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh009_009_contextual | zh009 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh009_009_local_proposition | zh009 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh009_009_local_summary | zh009 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh010_010_adjacent_merge | zh010 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh010_010_contextual | zh010 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh010_010_local_proposition | zh010 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh010_010_local_summary | zh010 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh011_011_adjacent_merge | zh011 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh011_011_contextual | zh011 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh011_011_local_proposition | zh011 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh011_011_local_summary | zh011 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh012_012_adjacent_merge | zh012 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh012_012_contextual | zh012 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh012_012_local_proposition | zh012 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh012_012_local_summary | zh012 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh013_013_adjacent_merge | zh013 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh013_013_contextual | zh013 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh013_013_local_proposition | zh013 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh013_013_local_summary | zh013 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh014_014_adjacent_merge | zh014 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh014_014_contextual | zh014 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh014_014_local_proposition | zh014 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh014_014_local_summary | zh014 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh015_015_adjacent_merge | zh015 | accepted | None | 5 | source query fixed and no regression detected |
| patch_zh015_015_contextual | zh015 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh015_015_local_proposition | zh015 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh015_015_local_summary | zh015 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh016_016_adjacent_merge | zh016 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh016_016_contextual | zh016 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh016_016_local_proposition | zh016 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh016_016_local_summary | zh016 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh017_017_adjacent_merge | zh017 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh017_017_contextual | zh017 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh017_017_local_proposition | zh017 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh017_017_local_summary | zh017 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh018_018_adjacent_merge | zh018 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh018_018_contextual | zh018 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh018_018_local_proposition | zh018 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh018_018_local_summary | zh018 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh019_019_adjacent_merge | zh019 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh019_019_contextual | zh019 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh019_019_local_proposition | zh019 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh019_019_local_summary | zh019 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh020_020_adjacent_merge | zh020 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh020_020_contextual | zh020 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh020_020_local_proposition | zh020 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh020_020_local_summary | zh020 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh021_021_adjacent_merge | zh021 | accepted | None | 3 | source query fixed and no regression detected |
| patch_zh021_021_contextual | zh021 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh021_021_local_proposition | zh021 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh021_021_local_summary | zh021 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh022_022_adjacent_merge | zh022 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh022_022_contextual | zh022 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh022_022_local_proposition | zh022 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh022_022_local_summary | zh022 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh023_023_adjacent_merge | zh023 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh023_023_contextual | zh023 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh023_023_local_proposition | zh023 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh023_023_local_summary | zh023 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh024_024_adjacent_merge | zh024 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh024_024_contextual | zh024 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh024_024_local_proposition | zh024 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh024_024_local_summary | zh024 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh025_025_adjacent_merge | zh025 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh025_025_contextual | zh025 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh025_025_local_proposition | zh025 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh025_025_local_summary | zh025 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh026_026_adjacent_merge | zh026 | accepted | None | 4 | source query fixed and no regression detected |
| patch_zh026_026_contextual | zh026 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh026_026_local_proposition | zh026 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh026_026_local_summary | zh026 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh027_027_adjacent_merge | zh027 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh027_027_contextual | zh027 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh027_027_local_proposition | zh027 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh027_027_local_summary | zh027 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh028_028_adjacent_merge | zh028 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh028_028_contextual | zh028 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh028_028_local_proposition | zh028 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh028_028_local_summary | zh028 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh029_029_adjacent_merge | zh029 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh029_029_contextual | zh029 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh029_029_local_proposition | zh029 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh029_029_local_summary | zh029 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh030_030_adjacent_merge | zh030 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh030_030_contextual | zh030 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh030_030_local_proposition | zh030 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh030_030_local_summary | zh030 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh031_031_adjacent_merge | zh031 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh031_031_contextual | zh031 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh031_031_local_proposition | zh031 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh031_031_local_summary | zh031 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh032_032_adjacent_merge | zh032 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh032_032_contextual | zh032 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh032_032_local_proposition | zh032 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh032_032_local_summary | zh032 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh033_033_adjacent_merge | zh033 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh033_033_contextual | zh033 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh033_033_local_proposition | zh033 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh033_033_local_summary | zh033 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh034_034_adjacent_merge | zh034 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh034_034_contextual | zh034 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh034_034_local_proposition | zh034 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh034_034_local_summary | zh034 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh035_035_adjacent_merge | zh035 | accepted | None | 3 | source query fixed and no regression detected |
| patch_zh035_035_contextual | zh035 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh035_035_local_proposition | zh035 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh035_035_local_summary | zh035 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh036_036_adjacent_merge | zh036 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh036_036_contextual | zh036 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh036_036_local_proposition | zh036 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh036_036_local_summary | zh036 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh037_037_adjacent_merge | zh037 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh037_037_contextual | zh037 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh037_037_local_proposition | zh037 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh037_037_local_summary | zh037 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh038_038_adjacent_merge | zh038 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh038_038_contextual | zh038 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh038_038_local_proposition | zh038 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh038_038_local_summary | zh038 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh039_039_adjacent_merge | zh039 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh039_039_contextual | zh039 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh039_039_local_proposition | zh039 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh039_039_local_summary | zh039 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh040_040_adjacent_merge | zh040 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh040_040_contextual | zh040 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh040_040_local_proposition | zh040 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh040_040_local_summary | zh040 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh041_041_adjacent_merge | zh041 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh041_041_contextual | zh041 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh041_041_local_proposition | zh041 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh041_041_local_summary | zh041 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh042_042_adjacent_merge | zh042 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh042_042_contextual | zh042 | accepted | None | 2 | source query fixed and no regression detected |
| patch_zh042_042_local_proposition | zh042 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh042_042_local_summary | zh042 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh044_043_adjacent_merge | zh044 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh044_043_contextual | zh044 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh044_043_local_proposition | zh044 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh044_043_local_summary | zh044 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh045_044_adjacent_merge | zh045 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh045_044_contextual | zh045 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh045_044_local_proposition | zh045 | accepted | None | 3 | source query fixed and no regression detected |
| patch_zh045_044_local_summary | zh045 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh046_045_adjacent_merge | zh046 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh046_045_contextual | zh046 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh046_045_local_proposition | zh046 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh046_045_local_summary | zh046 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh047_046_adjacent_merge | zh047 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh047_046_contextual | zh047 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh047_046_local_proposition | zh047 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh047_046_local_summary | zh047 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh048_047_adjacent_merge | zh048 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh048_047_contextual | zh048 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh048_047_local_proposition | zh048 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh048_047_local_summary | zh048 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh049_048_adjacent_merge | zh049 | accepted | None | 4 | source query fixed and no regression detected |
| patch_zh049_048_contextual | zh049 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh049_048_local_proposition | zh049 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh049_048_local_summary | zh049 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh050_049_adjacent_merge | zh050 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh050_049_contextual | zh050 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh050_049_local_proposition | zh050 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh050_049_local_summary | zh050 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh051_050_adjacent_merge | zh051 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh051_050_contextual | zh051 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh051_050_local_proposition | zh051 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh051_050_local_summary | zh051 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh052_051_adjacent_merge | zh052 | accepted | None | 5 | source query fixed and no regression detected |
| patch_zh052_051_contextual | zh052 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh052_051_local_proposition | zh052 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh052_051_local_summary | zh052 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh053_052_adjacent_merge | zh053 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh053_052_contextual | zh053 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh053_052_local_proposition | zh053 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh053_052_local_summary | zh053 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh054_053_adjacent_merge | zh054 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh054_053_contextual | zh054 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh054_053_local_proposition | zh054 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh054_053_local_summary | zh054 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh055_054_adjacent_merge | zh055 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh055_054_contextual | zh055 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh055_054_local_proposition | zh055 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh055_054_local_summary | zh055 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh056_055_adjacent_merge | zh056 | accepted | None | 4 | source query fixed and no regression detected |
| patch_zh056_055_contextual | zh056 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh056_055_local_proposition | zh056 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh056_055_local_summary | zh056 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh057_056_adjacent_merge | zh057 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh057_056_contextual | zh057 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh057_056_local_proposition | zh057 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh057_056_local_summary | zh057 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh058_057_adjacent_merge | zh058 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh058_057_contextual | zh058 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh058_057_local_proposition | zh058 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh058_057_local_summary | zh058 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh060_058_adjacent_merge | zh060 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh060_058_contextual | zh060 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh060_058_local_proposition | zh060 | accepted | None | 1 | source query fixed and no regression detected |
| patch_zh060_058_local_summary | zh060 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh061_059_adjacent_merge | zh061 | accepted | None | 1 | source query fixed and no regression detected |
| patch_zh061_059_contextual | zh061 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh061_059_local_proposition | zh061 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh061_059_local_summary | zh061 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh062_060_adjacent_merge | zh062 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh062_060_contextual | zh062 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh062_060_local_proposition | zh062 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh062_060_local_summary | zh062 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh063_061_adjacent_merge | zh063 | accepted | None | 5 | source query fixed and no regression detected |
| patch_zh063_061_contextual | zh063 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh063_061_local_proposition | zh063 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh063_061_local_summary | zh063 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh064_062_adjacent_merge | zh064 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh064_062_contextual | zh064 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh064_062_local_proposition | zh064 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh064_062_local_summary | zh064 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh065_063_adjacent_merge | zh065 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh065_063_contextual | zh065 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh065_063_local_proposition | zh065 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh065_063_local_summary | zh065 | accepted | None | 5 | source query fixed and no regression detected |
| patch_zh066_064_adjacent_merge | zh066 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh066_064_contextual | zh066 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh066_064_local_proposition | zh066 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh066_064_local_summary | zh066 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh067_065_adjacent_merge | zh067 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh067_065_contextual | zh067 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh067_065_local_proposition | zh067 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh067_065_local_summary | zh067 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh068_066_adjacent_merge | zh068 | accepted | None | 2 | source query fixed and no regression detected |
| patch_zh068_066_contextual | zh068 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh068_066_local_proposition | zh068 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh068_066_local_summary | zh068 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh069_067_adjacent_merge | zh069 | accepted | None | 1 | source query fixed and no regression detected |
| patch_zh069_067_contextual | zh069 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh069_067_local_proposition | zh069 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh069_067_local_summary | zh069 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh070_068_adjacent_merge | zh070 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh070_068_contextual | zh070 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh070_068_local_proposition | zh070 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh070_068_local_summary | zh070 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh071_069_adjacent_merge | zh071 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh071_069_contextual | zh071 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh071_069_local_proposition | zh071 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh071_069_local_summary | zh071 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh072_070_adjacent_merge | zh072 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh072_070_contextual | zh072 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh072_070_local_proposition | zh072 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh072_070_local_summary | zh072 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh073_071_adjacent_merge | zh073 | accepted | None | 3 | source query fixed and no regression detected |
| patch_zh073_071_contextual | zh073 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh073_071_local_proposition | zh073 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh073_071_local_summary | zh073 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh074_072_adjacent_merge | zh074 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh074_072_contextual | zh074 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh074_072_local_proposition | zh074 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh074_072_local_summary | zh074 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh075_073_adjacent_merge | zh075 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh075_073_contextual | zh075 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh075_073_local_proposition | zh075 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh075_073_local_summary | zh075 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh076_074_adjacent_merge | zh076 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh076_074_contextual | zh076 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh076_074_local_proposition | zh076 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh076_074_local_summary | zh076 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh077_075_adjacent_merge | zh077 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh077_075_contextual | zh077 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh077_075_local_proposition | zh077 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh077_075_local_summary | zh077 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh078_076_adjacent_merge | zh078 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh078_076_contextual | zh078 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh078_076_local_proposition | zh078 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh078_076_local_summary | zh078 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh079_077_adjacent_merge | zh079 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh079_077_contextual | zh079 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh079_077_local_proposition | zh079 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh079_077_local_summary | zh079 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh080_078_adjacent_merge | zh080 | accepted | None | 1 | source query fixed and no regression detected |
| patch_zh080_078_contextual | zh080 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh080_078_local_proposition | zh080 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh080_078_local_summary | zh080 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh081_079_adjacent_merge | zh081 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh081_079_contextual | zh081 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh081_079_local_proposition | zh081 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh081_079_local_summary | zh081 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh082_080_adjacent_merge | zh082 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh082_080_contextual | zh082 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh082_080_local_proposition | zh082 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh082_080_local_summary | zh082 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh083_081_adjacent_merge | zh083 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh083_081_contextual | zh083 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh083_081_local_proposition | zh083 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh083_081_local_summary | zh083 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh085_082_adjacent_merge | zh085 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh085_082_contextual | zh085 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh085_082_local_proposition | zh085 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh085_082_local_summary | zh085 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh087_083_adjacent_merge | zh087 | accepted | None | 5 | source query fixed and no regression detected |
| patch_zh087_083_contextual | zh087 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh087_083_local_proposition | zh087 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh087_083_local_summary | zh087 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh088_084_adjacent_merge | zh088 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh088_084_contextual | zh088 | accepted | None | 3 | source query fixed and no regression detected |
| patch_zh088_084_local_proposition | zh088 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh088_084_local_summary | zh088 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh089_085_adjacent_merge | zh089 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh089_085_contextual | zh089 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh089_085_local_proposition | zh089 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh089_085_local_summary | zh089 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh090_086_adjacent_merge | zh090 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh090_086_contextual | zh090 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh090_086_local_proposition | zh090 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh090_086_local_summary | zh090 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh093_087_adjacent_merge | zh093 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh093_087_contextual | zh093 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh093_087_local_proposition | zh093 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh093_087_local_summary | zh093 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh094_088_adjacent_merge | zh094 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh094_088_contextual | zh094 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh094_088_local_proposition | zh094 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh094_088_local_summary | zh094 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh095_089_adjacent_merge | zh095 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh095_089_contextual | zh095 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh095_089_local_proposition | zh095 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh095_089_local_summary | zh095 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh096_090_adjacent_merge | zh096 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh096_090_contextual | zh096 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh096_090_local_proposition | zh096 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh096_090_local_summary | zh096 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh097_091_adjacent_merge | zh097 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh097_091_contextual | zh097 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh097_091_local_proposition | zh097 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh097_091_local_summary | zh097 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh099_092_adjacent_merge | zh099 | accepted | None | 2 | source query fixed and no regression detected |
| patch_zh099_092_contextual | zh099 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh099_092_local_proposition | zh099 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh099_092_local_summary | zh099 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh100_093_adjacent_merge | zh100 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh100_093_contextual | zh100 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh100_093_local_proposition | zh100 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh100_093_local_summary | zh100 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh101_094_adjacent_merge | zh101 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh101_094_contextual | zh101 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh101_094_local_proposition | zh101 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh101_094_local_summary | zh101 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh102_095_adjacent_merge | zh102 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh102_095_contextual | zh102 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh102_095_local_proposition | zh102 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh102_095_local_summary | zh102 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh103_096_adjacent_merge | zh103 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh103_096_contextual | zh103 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh103_096_local_proposition | zh103 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh103_096_local_summary | zh103 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh106_097_adjacent_merge | zh106 | accepted | None | 3 | source query fixed and no regression detected |
| patch_zh106_097_contextual | zh106 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh106_097_local_proposition | zh106 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh106_097_local_summary | zh106 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh110_098_adjacent_merge | zh110 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh110_098_contextual | zh110 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh110_098_local_proposition | zh110 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh110_098_local_summary | zh110 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh112_099_adjacent_merge | zh112 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh112_099_contextual | zh112 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh112_099_local_proposition | zh112 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh112_099_local_summary | zh112 | accepted | None | 2 | source query fixed and no regression detected |
| patch_zh113_100_adjacent_merge | zh113 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh113_100_contextual | zh113 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh113_100_local_proposition | zh113 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh113_100_local_summary | zh113 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh117_101_adjacent_merge | zh117 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh117_101_contextual | zh117 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh117_101_local_proposition | zh117 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh117_101_local_summary | zh117 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh118_102_adjacent_merge | zh118 | accepted | None | 5 | source query fixed and no regression detected |
| patch_zh118_102_contextual | zh118 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh118_102_local_proposition | zh118 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh118_102_local_summary | zh118 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh119_103_adjacent_merge | zh119 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh119_103_contextual | zh119 | accepted | None | 4 | source query fixed and no regression detected |
| patch_zh119_103_local_proposition | zh119 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh119_103_local_summary | zh119 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |

## Safety Interpretation

- The main index was not modified.
- Patch chunks were stored in a small side Patch Index.
- A patch is accepted only when it fixes its source failure and no regression appears in the eval set.
- Rejected patches remain auditable but should not be merged into the main index.
