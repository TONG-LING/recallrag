# Main-only vs Main+Patch Comparison

## Metrics

| Metric | Main-only | Main+Patch | Delta |
|---|---:|---:|---:|
| Recall@5 | 0.8833 | 0.9333 | +0.0500 |
| MRR | 0.5508 | 0.5715 | +0.0207 |
| Hits | 106 / 120 | 112 / 120 | +6 |

- main_chunks: 634
- patch_chunks: 6
- patch/main ratio: 0.95%

## Query Movement

- fixed: ['zh002', 'zh004', 'zh007', 'zh008', 'zh057', 'zh067']
- regressed: []
- unchanged_failure: ['zh003', 'zh006', 'zh010', 'zh011', 'zh017', 'zh027', 'zh033', 'zh101']
- unchanged_success_count: 106

| qid | movement | before rank | after rank | before coverage | after coverage |
|---|---|---:|---:|---:|---:|
| zh001 | unchanged_success | 2 | 2 | 0.778 | 0.778 |
| zh002 | fixed | None | 1 | 0.578 | 0.952 |
| zh003 | unchanged_failure | None | None | 0.511 | 0.511 |
| zh004 | fixed | None | 2 | 0.576 | 0.786 |
| zh005 | unchanged_success | 2 | 2 | 0.661 | 0.661 |
| zh006 | unchanged_failure | None | None | 0.605 | 0.605 |
| zh007 | fixed | None | 4 | 0.648 | 0.886 |
| zh008 | fixed | None | 5 | 0.623 | 0.834 |
| zh009 | unchanged_success | 3 | 3 | 0.732 | 0.732 |
| zh010 | unchanged_failure | None | None | 0.587 | 0.587 |
| zh011 | unchanged_failure | None | None | 0.623 | 0.623 |
| zh012 | unchanged_success | 3 | 3 | 0.708 | 0.708 |
| zh013 | unchanged_success | 2 | 2 | 0.786 | 0.786 |
| zh014 | unchanged_success | 4 | 4 | 0.755 | 0.755 |
| zh015 | unchanged_success | 1 | 1 | 0.777 | 0.777 |
| zh016 | unchanged_success | 5 | 5 | 0.797 | 0.797 |
| zh017 | unchanged_failure | None | None | 0.629 | 0.629 |
| zh018 | unchanged_success | 2 | 2 | 0.736 | 0.736 |
| zh019 | unchanged_success | 2 | 2 | 0.885 | 0.885 |
| zh020 | unchanged_success | 5 | 5 | 0.824 | 0.824 |
| zh021 | unchanged_success | 1 | 1 | 0.73 | 0.73 |
| zh022 | unchanged_success | 1 | 1 | 0.653 | 0.653 |
| zh023 | unchanged_success | 4 | 4 | 0.765 | 0.765 |
| zh024 | unchanged_success | 5 | 5 | 0.879 | 0.879 |
| zh025 | unchanged_success | 2 | 2 | 0.841 | 0.841 |
| zh026 | unchanged_success | 1 | 1 | 0.705 | 0.705 |
| zh027 | unchanged_failure | None | None | 0.305 | 0.305 |
| zh028 | unchanged_success | 3 | 3 | 0.947 | 0.947 |
| zh029 | unchanged_success | 2 | 2 | 0.712 | 0.712 |
| zh030 | unchanged_success | 5 | 5 | 0.833 | 0.833 |
| zh031 | unchanged_success | 1 | 1 | 0.94 | 0.94 |
| zh032 | unchanged_success | 5 | 5 | 0.914 | 0.914 |
| zh033 | unchanged_failure | None | None | 0.574 | 0.574 |
| zh034 | unchanged_success | 4 | 4 | 0.856 | 0.856 |
| zh035 | unchanged_success | 3 | 3 | 0.897 | 0.897 |
| zh036 | unchanged_success | 1 | 1 | 0.946 | 0.946 |
| zh037 | unchanged_success | 2 | 2 | 0.711 | 0.711 |
| zh038 | unchanged_success | 3 | 3 | 0.7 | 0.7 |
| zh039 | unchanged_success | 1 | 1 | 0.945 | 0.945 |
| zh040 | unchanged_success | 2 | 2 | 0.998 | 0.998 |
| zh041 | unchanged_success | 3 | 3 | 0.733 | 0.733 |
| zh042 | unchanged_success | 1 | 1 | 0.98 | 0.98 |
| zh043 | unchanged_success | 3 | 3 | 0.833 | 0.833 |
| zh044 | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh045 | unchanged_success | 2 | 2 | 0.869 | 0.869 |
| zh046 | unchanged_success | 3 | 3 | 0.657 | 0.657 |
| zh047 | unchanged_success | 5 | 5 | 0.792 | 0.792 |
| zh048 | unchanged_success | 2 | 2 | 0.744 | 0.744 |
| zh049 | unchanged_success | 3 | 3 | 0.982 | 0.982 |
| zh050 | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh051 | unchanged_success | 1 | 1 | 0.896 | 0.896 |
| zh052 | unchanged_success | 1 | 1 | 0.928 | 0.928 |
| zh053 | unchanged_success | 1 | 1 | 0.914 | 0.914 |
| zh054 | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh055 | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh056 | unchanged_success | 4 | 4 | 0.833 | 0.833 |
| zh057 | fixed | None | 5 | 0.423 | 0.854 |
| zh058 | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh059 | unchanged_success | 1 | 1 | 0.871 | 0.871 |
| zh060 | unchanged_success | 1 | 1 | 0.678 | 0.678 |
| zh061 | unchanged_success | 2 | 2 | 0.782 | 0.782 |
| zh062 | unchanged_success | 1 | 1 | 0.8 | 0.8 |
| zh063 | unchanged_success | 4 | 4 | 1.0 | 1.0 |
| zh064 | unchanged_success | 1 | 1 | 0.995 | 0.995 |
| zh065 | unchanged_success | 2 | 2 | 0.683 | 0.683 |
| zh066 | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh067 | fixed | None | 3 | 0.646 | 0.997 |
| zh068 | unchanged_success | 2 | 2 | 0.7 | 0.7 |
| zh069 | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh070 | unchanged_success | 4 | 4 | 0.878 | 0.878 |
| zh071 | unchanged_success | 1 | 1 | 0.948 | 0.948 |
| zh072 | unchanged_success | 1 | 1 | 0.984 | 0.984 |
| zh073 | unchanged_success | 1 | 1 | 0.942 | 0.942 |
| zh074 | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh075 | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh076 | unchanged_success | 1 | 1 | 0.781 | 0.781 |
| zh077 | unchanged_success | 1 | 1 | 0.852 | 0.852 |
| zh078 | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh079 | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh080 | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh081 | unchanged_success | 3 | 3 | 0.726 | 0.726 |
| zh082 | unchanged_success | 4 | 4 | 1.0 | 1.0 |
| zh083 | unchanged_success | 1 | 1 | 0.776 | 0.776 |
| zh084 | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh085 | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh086 | unchanged_success | 3 | 3 | 0.79 | 0.79 |
| zh087 | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh088 | unchanged_success | 2 | 2 | 0.79 | 0.79 |
| zh089 | unchanged_success | 2 | 2 | 0.791 | 0.791 |
| zh090 | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh091 | unchanged_success | 1 | 1 | 0.808 | 0.808 |
| zh092 | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh093 | unchanged_success | 1 | 1 | 0.846 | 0.846 |
| zh094 | unchanged_success | 3 | 3 | 0.886 | 0.886 |
| zh095 | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh096 | unchanged_success | 2 | 2 | 0.72 | 0.72 |
| zh097 | unchanged_success | 1 | 1 | 0.89 | 0.89 |
| zh098 | unchanged_success | 2 | 2 | 0.873 | 0.873 |
| zh099 | unchanged_success | 1 | 1 | 1.0 | 1.0 |
| zh100 | unchanged_success | 1 | 1 | 0.913 | 0.913 |
| zh101 | unchanged_failure | None | None | 0.592 | 0.592 |
| zh102 | unchanged_success | 5 | 5 | 0.807 | 0.807 |
| zh103 | unchanged_success | 1 | 1 | 0.874 | 0.874 |
| zh104 | unchanged_success | 4 | 4 | 0.859 | 0.859 |
| zh105 | unchanged_success | 1 | 1 | 0.789 | 0.789 |
| zh106 | unchanged_success | 5 | 5 | 0.653 | 0.653 |
| zh107 | unchanged_success | 1 | 1 | 0.982 | 0.982 |
| zh108 | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh109 | unchanged_success | 1 | 1 | 0.94 | 0.94 |
| zh110 | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh111 | unchanged_success | 1 | 1 | 0.986 | 0.986 |
| zh112 | unchanged_success | 1 | 1 | 0.982 | 0.982 |
| zh113 | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh114 | unchanged_success | 1 | 1 | 0.867 | 0.867 |
| zh115 | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh116 | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh117 | unchanged_success | 3 | 3 | 1.0 | 1.0 |
| zh118 | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh119 | unchanged_success | 2 | 2 | 1.0 | 1.0 |
| zh120 | unchanged_success | 2 | 2 | 1.0 | 1.0 |

## Candidate Probe / Selected Patch

| qid | selected patch | type | individual rank | text_len |
|---|---|---|---:|---:|
| zh002 | `patch_zh002_001_adjacent_merge` | `adjacent_merge` | 1 | 1904 |
| zh004 | `patch_zh004_003_contextual` | `contextual` | 2 | 1048 |
| zh007 | `patch_zh007_005_adjacent_merge` | `adjacent_merge` | 4 | 1884 |
| zh008 | `patch_zh008_006_adjacent_merge` | `adjacent_merge` | 5 | 1884 |
| zh057 | `patch_zh057_012_contextual` | `contextual` | 5 | 1021 |
| zh067 | `patch_zh067_013_adjacent_merge` | `adjacent_merge` | 3 | 1884 |

## Patch Decisions

| patch_id | source qid | status | before rank | after rank | reason |
|---|---|---|---:|---:|---|
| patch_zh002_001_adjacent_merge | zh002 | accepted | None | 1 | source query fixed and no regression detected |
| patch_zh002_001_contextual | zh002 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh002_001_local_proposition | zh002 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh002_001_local_summary | zh002 | candidate_not_selected | None | 1 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh003_002_adjacent_merge | zh003 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh003_002_contextual | zh003 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh003_002_local_proposition | zh003 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh003_002_local_summary | zh003 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh004_003_adjacent_merge | zh004 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh004_003_contextual | zh004 | accepted | None | 2 | source query fixed and no regression detected |
| patch_zh004_003_local_proposition | zh004 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh004_003_local_summary | zh004 | candidate_not_selected | None | 2 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh006_004_adjacent_merge | zh006 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh006_004_contextual | zh006 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh006_004_local_proposition | zh006 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh006_004_local_summary | zh006 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh007_005_adjacent_merge | zh007 | accepted | None | 4 | source query fixed and no regression detected |
| patch_zh007_005_contextual | zh007 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh007_005_local_proposition | zh007 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh007_005_local_summary | zh007 | candidate_not_selected | None | 4 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh008_006_adjacent_merge | zh008 | accepted | None | 5 | source query fixed and no regression detected |
| patch_zh008_006_contextual | zh008 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh008_006_local_proposition | zh008 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh008_006_local_summary | zh008 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh010_007_adjacent_merge | zh010 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh010_007_contextual | zh010 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh010_007_local_proposition | zh010 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh010_007_local_summary | zh010 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh011_008_adjacent_merge | zh011 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh011_008_contextual | zh011 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh011_008_local_proposition | zh011 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh011_008_local_summary | zh011 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh017_009_adjacent_merge | zh017 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh017_009_contextual | zh017 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh017_009_local_proposition | zh017 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh017_009_local_summary | zh017 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh027_010_adjacent_merge | zh027 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh027_010_contextual | zh027 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh027_010_local_proposition | zh027 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh027_010_local_summary | zh027 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh033_011_adjacent_merge | zh033 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh033_011_contextual | zh033 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh033_011_local_proposition | zh033 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh033_011_local_summary | zh033 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh057_012_adjacent_merge | zh057 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh057_012_contextual | zh057 | accepted | None | 5 | source query fixed and no regression detected |
| patch_zh057_012_local_proposition | zh057 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh057_012_local_summary | zh057 | candidate_not_selected | None | 5 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh067_013_adjacent_merge | zh067 | accepted | None | 3 | source query fixed and no regression detected |
| patch_zh067_013_contextual | zh067 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh067_013_local_proposition | zh067 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh067_013_local_summary | zh067 | candidate_not_selected | None | 3 | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh101_014_adjacent_merge | zh101 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh101_014_contextual | zh101 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh101_014_local_proposition | zh101 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |
| patch_zh101_014_local_summary | zh101 | candidate_not_selected | None | None | candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule |

## Safety Interpretation

- The main index was not modified.
- Patch chunks were stored in a small side Patch Index.
- A patch is accepted only when it fixes its source failure and no regression appears in the eval set.
- Rejected patches remain auditable but should not be merged into the main index.
