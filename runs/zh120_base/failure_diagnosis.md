# Production-style Failure Diagnosis Report

## Summary

- failed queries diagnosed: 103
- chunking/local-context candidates: 103
- uncertain/non-chunk: 0
- patch_allowed: 103

> Localization does not use `gold_doc` or `gold_span`; gold fields are only retained for offline evaluation readability.

## zh001 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 高速公路超速20以上不足50扣几分
- offline gold: `zh_doc_001.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_001.md::c0038` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_001.md::c0038`
- anchor_doc_id: `zh_doc_001.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.833`
- anchor_localization_score: `0.85`
- candidate_window_chunk_ids: `['zh_doc_001.md::c0037', 'zh_doc_001.md::c0038']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh002 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 空气净化器哪种净化方式好
- offline gold: `zh_doc_002.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_002.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_002.md::c0001`
- anchor_doc_id: `zh_doc_002.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.7`
- anchor_localization_score: `0.73`
- candidate_window_chunk_ids: `['zh_doc_002.md::c0000', 'zh_doc_002.md::c0001', 'zh_doc_002.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh003 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 黄山风景古诗赞
- offline gold: `zh_doc_003.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_003.md::c0009` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_003.md::c0009`
- anchor_doc_id: `zh_doc_003.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.5`
- anchor_localization_score: `0.55`
- candidate_window_chunk_ids: `['zh_doc_003.md::c0008', 'zh_doc_003.md::c0009', 'zh_doc_003.md::c0010']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh004 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 一天放很多屁
- offline gold: `zh_doc_004.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_004.md::c0028` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_004.md::c0028`
- anchor_doc_id: `zh_doc_004.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料2`
- anchor_rank_in_trace: `22`
- anchor_query_overlap: `0.4`
- anchor_localization_score: `0.365`
- candidate_window_chunk_ids: `['zh_doc_004.md::c0027', 'zh_doc_004.md::c0028']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh005 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 叉车有几种
- offline gold: `zh_doc_005.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_005.md::c0010` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_005.md::c0010`
- anchor_doc_id: `zh_doc_005.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `12`
- anchor_query_overlap: `0.75`
- anchor_localization_score: `0.683`
- candidate_window_chunk_ids: `['zh_doc_005.md::c0009', 'zh_doc_005.md::c0010', 'zh_doc_005.md::c0011']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh006 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 春光成语
- offline gold: `zh_doc_006.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_006.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_006.md::c0000`
- anchor_doc_id: `zh_doc_006.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `8`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.912`
- candidate_window_chunk_ids: `['zh_doc_006.md::c0000', 'zh_doc_006.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh007 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 经常用肥皂洗脸好吗
- offline gold: `zh_doc_007.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_007.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_007.md::c0003`
- anchor_doc_id: `zh_doc_007.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `6`
- anchor_query_overlap: `0.875`
- anchor_localization_score: `0.804`
- candidate_window_chunk_ids: `['zh_doc_007.md::c0002', 'zh_doc_007.md::c0003', 'zh_doc_007.md::c0004']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh008 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 冬天怎样养鹦鹉
- offline gold: `zh_doc_008.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_008.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_008.md::c0003`
- anchor_doc_id: `zh_doc_008.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.5`
- anchor_localization_score: `0.55`
- candidate_window_chunk_ids: `['zh_doc_008.md::c0002', 'zh_doc_008.md::c0003', 'zh_doc_008.md::c0004']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh009 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 附睾肿胀
- offline gold: `zh_doc_009.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_009.md::c0006` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_009.md::c0006`
- anchor_doc_id: `zh_doc_009.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_009.md::c0005', 'zh_doc_009.md::c0006', 'zh_doc_009.md::c0007']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh010 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 硫磺皂能长期用吗
- offline gold: `zh_doc_010.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_010.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_010.md::c0000`
- anchor_doc_id: `zh_doc_010.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `3`
- anchor_query_overlap: `0.714`
- anchor_localization_score: `0.676`
- candidate_window_chunk_ids: `['zh_doc_010.md::c0000', 'zh_doc_010.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh011 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 比较好看的电视剧
- offline gold: `zh_doc_011.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_011.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_011.md::c0000`
- anchor_doc_id: `zh_doc_011.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.714`
- anchor_localization_score: `0.743`
- candidate_window_chunk_ids: `['zh_doc_011.md::c0000', 'zh_doc_011.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh012 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 夏天喝什么饮品好
- offline gold: `zh_doc_012.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_012.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_012.md::c0000`
- anchor_doc_id: `zh_doc_012.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.95`
- candidate_window_chunk_ids: `['zh_doc_012.md::c0000', 'zh_doc_012.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh013 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: workgroup是什么
- offline gold: `zh_doc_013.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_013.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_013.md::c0000`
- anchor_doc_id: `zh_doc_013.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_013.md::c0000', 'zh_doc_013.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh014 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 怎样锻炼肺活量
- offline gold: `zh_doc_014.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_014.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_014.md::c0000`
- anchor_doc_id: `zh_doc_014.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.667`
- anchor_localization_score: `0.7`
- candidate_window_chunk_ids: `['zh_doc_014.md::c0000', 'zh_doc_014.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh015 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 做胃镜注意
- offline gold: `zh_doc_015.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_015.md::c0006` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_015.md::c0006`
- anchor_doc_id: `zh_doc_015.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.75`
- anchor_localization_score: `0.775`
- candidate_window_chunk_ids: `['zh_doc_015.md::c0005', 'zh_doc_015.md::c0006', 'zh_doc_015.md::c0007']`
- topk_same_doc_count: `5`
- topk_same_section_count: `3`

## zh016 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 油电混合动力汽车购置税优惠吗
- offline gold: `zh_doc_016.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_016.md::c0006` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_016.md::c0006`
- anchor_doc_id: `zh_doc_016.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.692`
- anchor_localization_score: `0.723`
- candidate_window_chunk_ids: `['zh_doc_016.md::c0005', 'zh_doc_016.md::c0006', 'zh_doc_016.md::c0007']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh017 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 阴部变白
- offline gold: `zh_doc_017.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_017.md::c0010` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_017.md::c0010`
- anchor_doc_id: `zh_doc_017.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料2`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.667`
- anchor_localization_score: `0.65`
- candidate_window_chunk_ids: `['zh_doc_017.md::c0009', 'zh_doc_017.md::c0010']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh018 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 如何买卖etf基金
- offline gold: `zh_doc_018.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_018.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_018.md::c0003`
- anchor_doc_id: `zh_doc_018.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_018.md::c0002', 'zh_doc_018.md::c0003', 'zh_doc_018.md::c0004']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh019 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 在实习期内的驾驶证扣分会怎样
- offline gold: `zh_doc_019.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_019.md::c0008` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_019.md::c0008`
- anchor_doc_id: `zh_doc_019.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.615`
- anchor_localization_score: `0.654`
- candidate_window_chunk_ids: `['zh_doc_019.md::c0007', 'zh_doc_019.md::c0008', 'zh_doc_019.md::c0009']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh020 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 私立大学和公立大学的区别
- offline gold: `zh_doc_020.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_020.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_020.md::c0000`
- anchor_doc_id: `zh_doc_020.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `6`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.917`
- candidate_window_chunk_ids: `['zh_doc_020.md::c0000', 'zh_doc_020.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh021 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 如何调水表数字
- offline gold: `zh_doc_021.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_021.md::c0006` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_021.md::c0006`
- anchor_doc_id: `zh_doc_021.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.667`
- anchor_localization_score: `0.7`
- candidate_window_chunk_ids: `['zh_doc_021.md::c0005', 'zh_doc_021.md::c0006', 'zh_doc_021.md::c0007']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh022 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 怎样种香菜
- offline gold: `zh_doc_022.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_022.md::c0018` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_022.md::c0018`
- anchor_doc_id: `zh_doc_022.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.5`
- anchor_localization_score: `0.55`
- candidate_window_chunk_ids: `['zh_doc_022.md::c0017', 'zh_doc_022.md::c0018']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh023 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 如何把电脑上的东西传到ipad上
- offline gold: `zh_doc_023.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_023.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_023.md::c0001`
- anchor_doc_id: `zh_doc_023.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.833`
- anchor_localization_score: `0.8`
- candidate_window_chunk_ids: `['zh_doc_023.md::c0000', 'zh_doc_023.md::c0001', 'zh_doc_023.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh024 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: c1扣12分怎么办
- offline gold: `zh_doc_024.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_024.md::c0012` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_024.md::c0012`
- anchor_doc_id: `zh_doc_024.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.667`
- anchor_localization_score: `0.65`
- candidate_window_chunk_ids: `['zh_doc_024.md::c0011', 'zh_doc_024.md::c0012', 'zh_doc_024.md::c0013']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh025 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: tf与sd卡的区别
- offline gold: `zh_doc_025.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_025.md::c0014` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_025.md::c0014`
- anchor_doc_id: `zh_doc_025.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `4`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.925`
- candidate_window_chunk_ids: `['zh_doc_025.md::c0013', 'zh_doc_025.md::c0014', 'zh_doc_025.md::c0015']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh026 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 左肾部位疼痛
- offline gold: `zh_doc_026.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_026.md::c0005` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_026.md::c0005`
- anchor_doc_id: `zh_doc_026.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_026.md::c0004', 'zh_doc_026.md::c0005', 'zh_doc_026.md::c0006']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh027 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 小米平板钢化膜怎么贴
- offline gold: `zh_doc_027.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_027.md::c0010` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_027.md::c0010`
- anchor_doc_id: `zh_doc_027.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.556`
- anchor_localization_score: `0.6`
- candidate_window_chunk_ids: `['zh_doc_027.md::c0009', 'zh_doc_027.md::c0010', 'zh_doc_027.md::c0011']`
- topk_same_doc_count: `3`
- topk_same_section_count: `1`

## zh028 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 怎么控制路由器把蹭wifi的人给踢了
- offline gold: `zh_doc_028.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_028.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_028.md::c0001`
- anchor_doc_id: `zh_doc_028.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.462`
- anchor_localization_score: `0.515`
- candidate_window_chunk_ids: `['zh_doc_028.md::c0000', 'zh_doc_028.md::c0001', 'zh_doc_028.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh029 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 怎么做卫浴销售
- offline gold: `zh_doc_029.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_029.md::c0002` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_029.md::c0002`
- anchor_doc_id: `zh_doc_029.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.5`
- anchor_localization_score: `0.55`
- candidate_window_chunk_ids: `['zh_doc_029.md::c0001', 'zh_doc_029.md::c0002', 'zh_doc_029.md::c0003']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh030 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 外伤缝针不能吃什么
- offline gold: `zh_doc_030.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_030.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_030.md::c0000`
- anchor_doc_id: `zh_doc_030.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `5`
- anchor_query_overlap: `0.875`
- anchor_localization_score: `0.807`
- candidate_window_chunk_ids: `['zh_doc_030.md::c0000', 'zh_doc_030.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh031 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 超级会员是什么
- offline gold: `zh_doc_031.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_031.md::c0007` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_031.md::c0007`
- anchor_doc_id: `zh_doc_031.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_031.md::c0006', 'zh_doc_031.md::c0007', 'zh_doc_031.md::c0008']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh032 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 杭州劳动仲裁电话
- offline gold: `zh_doc_032.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_032.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_032.md::c0001`
- anchor_doc_id: `zh_doc_032.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `8`
- anchor_query_overlap: `0.857`
- anchor_localization_score: `0.784`
- candidate_window_chunk_ids: `['zh_doc_032.md::c0000', 'zh_doc_032.md::c0001', 'zh_doc_032.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh033 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 电暖桌哪个牌子好
- offline gold: `zh_doc_033.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_033.md::c0002` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_033.md::c0002`
- anchor_doc_id: `zh_doc_033.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `6`
- anchor_query_overlap: `0.571`
- anchor_localization_score: `0.531`
- candidate_window_chunk_ids: `['zh_doc_033.md::c0001', 'zh_doc_033.md::c0002', 'zh_doc_033.md::c0003']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh034 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 板栗可以蒸着吃吗
- offline gold: `zh_doc_034.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_034.md::c0010` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_034.md::c0010`
- anchor_doc_id: `zh_doc_034.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料2`
- anchor_rank_in_trace: `3`
- anchor_query_overlap: `0.571`
- anchor_localization_score: `0.548`
- candidate_window_chunk_ids: `['zh_doc_034.md::c0009', 'zh_doc_034.md::c0010', 'zh_doc_034.md::c0011']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh035 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 没越狱的iphone怎么清理垃圾
- offline gold: `zh_doc_035.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_035.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_035.md::c0003`
- anchor_doc_id: `zh_doc_035.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `4`
- anchor_query_overlap: `0.667`
- anchor_localization_score: `0.625`
- candidate_window_chunk_ids: `['zh_doc_035.md::c0002', 'zh_doc_035.md::c0003', 'zh_doc_035.md::c0004']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh036 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 苹果系统怎么查看隐藏文件
- offline gold: `zh_doc_036.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_036.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_036.md::c0000`
- anchor_doc_id: `zh_doc_036.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `4`
- anchor_query_overlap: `0.727`
- anchor_localization_score: `0.68`
- candidate_window_chunk_ids: `['zh_doc_036.md::c0000', 'zh_doc_036.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh037 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 海淀医院孕前检查
- offline gold: `zh_doc_037.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_037.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_037.md::c0003`
- anchor_doc_id: `zh_doc_037.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `4`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.925`
- candidate_window_chunk_ids: `['zh_doc_037.md::c0002', 'zh_doc_037.md::c0003', 'zh_doc_037.md::c0004']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh038 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 玩梦幻西游怎么赚钱
- offline gold: `zh_doc_038.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_038.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_038.md::c0003`
- anchor_doc_id: `zh_doc_038.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.875`
- anchor_localization_score: `0.887`
- candidate_window_chunk_ids: `['zh_doc_038.md::c0002', 'zh_doc_038.md::c0003', 'zh_doc_038.md::c0004']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh039 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 跟庐山有关的诗句
- offline gold: `zh_doc_039.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_039.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_039.md::c0000`
- anchor_doc_id: `zh_doc_039.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `6`
- anchor_query_overlap: `0.571`
- anchor_localization_score: `0.531`
- candidate_window_chunk_ids: `['zh_doc_039.md::c0000', 'zh_doc_039.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh040 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 现在去哪里下载音乐
- offline gold: `zh_doc_040.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_040.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_040.md::c0001`
- anchor_doc_id: `zh_doc_040.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.625`
- anchor_localization_score: `0.613`
- candidate_window_chunk_ids: `['zh_doc_040.md::c0000', 'zh_doc_040.md::c0001', 'zh_doc_040.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh041 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 治疗颈椎病药物
- offline gold: `zh_doc_041.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_041.md::c0011` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_041.md::c0011`
- anchor_doc_id: `zh_doc_041.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.833`
- anchor_localization_score: `0.85`
- candidate_window_chunk_ids: `['zh_doc_041.md::c0010', 'zh_doc_041.md::c0011', 'zh_doc_041.md::c0012']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh042 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 户外手电筒什么牌子好
- offline gold: `zh_doc_042.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_042.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_042.md::c0003`
- anchor_doc_id: `zh_doc_042.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_042.md::c0002', 'zh_doc_042.md::c0003', 'zh_doc_042.md::c0004']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh044 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 换外汇哪个银行好
- offline gold: `zh_doc_044.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_044.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_044.md::c0000`
- anchor_doc_id: `zh_doc_044.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.857`
- anchor_localization_score: `0.871`
- candidate_window_chunk_ids: `['zh_doc_044.md::c0000', 'zh_doc_044.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh045 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 轻型羽绒服什么牌子好
- offline gold: `zh_doc_045.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_045.md::c0002` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_045.md::c0002`
- anchor_doc_id: `zh_doc_045.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `5`
- anchor_query_overlap: `0.889`
- anchor_localization_score: `0.82`
- candidate_window_chunk_ids: `['zh_doc_045.md::c0001', 'zh_doc_045.md::c0002', 'zh_doc_045.md::c0003']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh046 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 手机外放进水
- offline gold: `zh_doc_046.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_046.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_046.md::c0003`
- anchor_doc_id: `zh_doc_046.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `8`
- anchor_query_overlap: `0.6`
- anchor_localization_score: `0.552`
- candidate_window_chunk_ids: `['zh_doc_046.md::c0002', 'zh_doc_046.md::c0003', 'zh_doc_046.md::c0004']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh047 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 什么样的借条不具法律效力
- offline gold: `zh_doc_047.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_047.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_047.md::c0000`
- anchor_doc_id: `zh_doc_047.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `5`
- anchor_query_overlap: `0.909`
- anchor_localization_score: `0.838`
- candidate_window_chunk_ids: `['zh_doc_047.md::c0000', 'zh_doc_047.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh048 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: m8a1用什么炮
- offline gold: `zh_doc_048.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_048.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_048.md::c0003`
- anchor_doc_id: `zh_doc_048.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.5`
- anchor_localization_score: `0.5`
- candidate_window_chunk_ids: `['zh_doc_048.md::c0002', 'zh_doc_048.md::c0003', 'zh_doc_048.md::c0004']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh049 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 西安人流手术费用要多少
- offline gold: `zh_doc_049.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_049.md::c0005` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_049.md::c0005`
- anchor_doc_id: `zh_doc_049.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.8`
- anchor_localization_score: `0.82`
- candidate_window_chunk_ids: `['zh_doc_049.md::c0004', 'zh_doc_049.md::c0005', 'zh_doc_049.md::c0006']`
- topk_same_doc_count: `5`
- topk_same_section_count: `3`

## zh050 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: xm外汇平台怎么样
- offline gold: `zh_doc_050.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_050.md::c0002` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_050.md::c0002`
- anchor_doc_id: `zh_doc_050.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_050.md::c0001', 'zh_doc_050.md::c0002', 'zh_doc_050.md::c0003']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh051 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 双人床最小宽度
- offline gold: `zh_doc_051.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_051.md::c0014` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_051.md::c0014`
- anchor_doc_id: `zh_doc_051.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.5`
- anchor_localization_score: `0.55`
- candidate_window_chunk_ids: `['zh_doc_051.md::c0013', 'zh_doc_051.md::c0014', 'zh_doc_051.md::c0015']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh052 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 生气时喂奶
- offline gold: `zh_doc_052.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_052.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_052.md::c0001`
- anchor_doc_id: `zh_doc_052.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `6`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.917`
- candidate_window_chunk_ids: `['zh_doc_052.md::c0000', 'zh_doc_052.md::c0001', 'zh_doc_052.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh053 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 龟头敏感度低怎么办
- offline gold: `zh_doc_053.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_053.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_053.md::c0000`
- anchor_doc_id: `zh_doc_053.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.75`
- anchor_localization_score: `0.775`
- candidate_window_chunk_ids: `['zh_doc_053.md::c0000', 'zh_doc_053.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh054 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 沪陕高速限速多少
- offline gold: `zh_doc_054.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_054.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_054.md::c0000`
- anchor_doc_id: `zh_doc_054.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `5`
- anchor_query_overlap: `0.714`
- anchor_localization_score: `0.663`
- candidate_window_chunk_ids: `['zh_doc_054.md::c0000', 'zh_doc_054.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh055 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: ios9 如何关闭搜索最近联系人
- offline gold: `zh_doc_055.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_055.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_055.md::c0000`
- anchor_doc_id: `zh_doc_055.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.636`
- anchor_localization_score: `0.673`
- candidate_window_chunk_ids: `['zh_doc_055.md::c0000', 'zh_doc_055.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh056 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 尸兄主角能力
- offline gold: `zh_doc_056.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_056.md::c0005` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_056.md::c0005`
- anchor_doc_id: `zh_doc_056.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.4`
- anchor_localization_score: `0.46`
- candidate_window_chunk_ids: `['zh_doc_056.md::c0004', 'zh_doc_056.md::c0005', 'zh_doc_056.md::c0006']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh057 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: word怎么不能修改
- offline gold: `zh_doc_057.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_057.md::c0012` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_057.md::c0012`
- anchor_doc_id: `zh_doc_057.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.833`
- anchor_localization_score: `0.85`
- candidate_window_chunk_ids: `['zh_doc_057.md::c0011', 'zh_doc_057.md::c0012', 'zh_doc_057.md::c0013']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh058 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 我国古代第一个有伟大成就的爱国诗人是( )
- offline gold: `zh_doc_058.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_058.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_058.md::c0003`
- anchor_doc_id: `zh_doc_058.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `6`
- anchor_query_overlap: `0.941`
- anchor_localization_score: `0.864`
- candidate_window_chunk_ids: `['zh_doc_058.md::c0002', 'zh_doc_058.md::c0003', 'zh_doc_058.md::c0004']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh060 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 氨端聚二甲基硅氧烷是硅油吗
- offline gold: `zh_doc_060.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_060.md::c0009` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_060.md::c0009`
- anchor_doc_id: `zh_doc_060.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.75`
- anchor_localization_score: `0.775`
- candidate_window_chunk_ids: `['zh_doc_060.md::c0008', 'zh_doc_060.md::c0009', 'zh_doc_060.md::c0010']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh061 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 为什么中国必须守住18亿亩耕地红线
- offline gold: `zh_doc_061.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_061.md::c0006` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_061.md::c0006`
- anchor_doc_id: `zh_doc_061.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.714`
- anchor_localization_score: `0.743`
- candidate_window_chunk_ids: `['zh_doc_061.md::c0005', 'zh_doc_061.md::c0006', 'zh_doc_061.md::c0007']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh062 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 如何取消电脑的自动休眠
- offline gold: `zh_doc_062.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_062.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_062.md::c0000`
- anchor_doc_id: `zh_doc_062.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `3`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.933`
- candidate_window_chunk_ids: `['zh_doc_062.md::c0000', 'zh_doc_062.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh063 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 象征孩子纯洁的花
- offline gold: `zh_doc_063.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_063.md::c0004` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_063.md::c0004`
- anchor_doc_id: `zh_doc_063.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `5`
- anchor_query_overlap: `0.714`
- anchor_localization_score: `0.663`
- candidate_window_chunk_ids: `['zh_doc_063.md::c0003', 'zh_doc_063.md::c0004', 'zh_doc_063.md::c0005']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh064 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 血清甘油三脂偏低
- offline gold: `zh_doc_064.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_064.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_064.md::c0000`
- anchor_doc_id: `zh_doc_064.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `7`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.914`
- candidate_window_chunk_ids: `['zh_doc_064.md::c0000', 'zh_doc_064.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh065 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 哪种制氧机好
- offline gold: `zh_doc_065.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_065.md::c0006` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_065.md::c0006`
- anchor_doc_id: `zh_doc_065.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `4`
- anchor_query_overlap: `0.6`
- anchor_localization_score: `0.565`
- candidate_window_chunk_ids: `['zh_doc_065.md::c0005', 'zh_doc_065.md::c0006', 'zh_doc_065.md::c0007']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh066 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 电动牙刷刷的干净吗
- offline gold: `zh_doc_066.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_066.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_066.md::c0000`
- anchor_doc_id: `zh_doc_066.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.875`
- anchor_localization_score: `0.887`
- candidate_window_chunk_ids: `['zh_doc_066.md::c0000', 'zh_doc_066.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh067 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 武松属什么
- offline gold: `zh_doc_067.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_067.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_067.md::c0000`
- anchor_doc_id: `zh_doc_067.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.5`
- anchor_localization_score: `0.5`
- candidate_window_chunk_ids: `['zh_doc_067.md::c0000', 'zh_doc_067.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh068 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 跳鬼步舞时手怎么动
- offline gold: `zh_doc_068.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_068.md::c0017` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_068.md::c0017`
- anchor_doc_id: `zh_doc_068.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.5`
- anchor_localization_score: `0.5`
- candidate_window_chunk_ids: `['zh_doc_068.md::c0016', 'zh_doc_068.md::c0017', 'zh_doc_068.md::c0018']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh069 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: would like的回答
- offline gold: `zh_doc_069.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_069.md::c0010` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_069.md::c0010`
- anchor_doc_id: `zh_doc_069.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.95`
- candidate_window_chunk_ids: `['zh_doc_069.md::c0009', 'zh_doc_069.md::c0010', 'zh_doc_069.md::c0011']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh070 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: qq经常掉线怎么回事
- offline gold: `zh_doc_070.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_070.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_070.md::c0000`
- anchor_doc_id: `zh_doc_070.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `5`
- anchor_query_overlap: `0.875`
- anchor_localization_score: `0.807`
- candidate_window_chunk_ids: `['zh_doc_070.md::c0000', 'zh_doc_070.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh071 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 还珠格格第一部背景音乐
- offline gold: `zh_doc_071.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_071.md::c0004` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_071.md::c0004`
- anchor_doc_id: `zh_doc_071.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `6`
- anchor_query_overlap: `0.8`
- anchor_localization_score: `0.737`
- candidate_window_chunk_ids: `['zh_doc_071.md::c0003', 'zh_doc_071.md::c0004', 'zh_doc_071.md::c0005']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh072 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 我的世界手机版0.12.1末地传送门怎么做
- offline gold: `zh_doc_072.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_072.md::c0007` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_072.md::c0007`
- anchor_doc_id: `zh_doc_072.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_072.md::c0006', 'zh_doc_072.md::c0007', 'zh_doc_072.md::c0008']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh073 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 三壬行化妆学校好吗
- offline gold: `zh_doc_073.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_073.md::c0004` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_073.md::c0004`
- anchor_doc_id: `zh_doc_073.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `3`
- anchor_query_overlap: `0.625`
- anchor_localization_score: `0.596`
- candidate_window_chunk_ids: `['zh_doc_073.md::c0003', 'zh_doc_073.md::c0004', 'zh_doc_073.md::c0005']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh074 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 胃功能
- offline gold: `zh_doc_074.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_074.md::c0002` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_074.md::c0002`
- anchor_doc_id: `zh_doc_074.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.95`
- candidate_window_chunk_ids: `['zh_doc_074.md::c0001', 'zh_doc_074.md::c0002', 'zh_doc_074.md::c0003']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh075 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 艾俐缇陶瓷怎么样
- offline gold: `zh_doc_075.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_075.md::c0006` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_075.md::c0006`
- anchor_doc_id: `zh_doc_075.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.571`
- anchor_localization_score: `0.614`
- candidate_window_chunk_ids: `['zh_doc_075.md::c0005', 'zh_doc_075.md::c0006', 'zh_doc_075.md::c0007']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh076 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 公共事业管理属于什么专业类别
- offline gold: `zh_doc_076.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_076.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_076.md::c0001`
- anchor_doc_id: `zh_doc_076.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `6`
- anchor_query_overlap: `0.769`
- anchor_localization_score: `0.709`
- candidate_window_chunk_ids: `['zh_doc_076.md::c0000', 'zh_doc_076.md::c0001', 'zh_doc_076.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh077 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 天然无添加的护肤品存在吗
- offline gold: `zh_doc_077.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_077.md::c0021` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_077.md::c0021`
- anchor_doc_id: `zh_doc_077.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料2`
- anchor_rank_in_trace: `4`
- anchor_query_overlap: `0.636`
- anchor_localization_score: `0.598`
- candidate_window_chunk_ids: `['zh_doc_077.md::c0020', 'zh_doc_077.md::c0021', 'zh_doc_077.md::c0022']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh078 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 旅行发票 可以报吗
- offline gold: `zh_doc_078.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_078.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_078.md::c0000`
- anchor_doc_id: `zh_doc_078.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.833`
- anchor_localization_score: `0.85`
- candidate_window_chunk_ids: `['zh_doc_078.md::c0000', 'zh_doc_078.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh079 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 种子可以用百度云下载吗
- offline gold: `zh_doc_079.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_079.md::c0002` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_079.md::c0002`
- anchor_doc_id: `zh_doc_079.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `3`
- anchor_query_overlap: `0.6`
- anchor_localization_score: `0.573`
- candidate_window_chunk_ids: `['zh_doc_079.md::c0001', 'zh_doc_079.md::c0002', 'zh_doc_079.md::c0003']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh080 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: ipad能否连接打印机
- offline gold: `zh_doc_080.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_080.md::c0008` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_080.md::c0008`
- anchor_doc_id: `zh_doc_080.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `5`
- anchor_query_overlap: `0.714`
- anchor_localization_score: `0.663`
- candidate_window_chunk_ids: `['zh_doc_080.md::c0007', 'zh_doc_080.md::c0008', 'zh_doc_080.md::c0009']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh081 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 手机钢化保护膜怎么贴
- offline gold: `zh_doc_081.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_027.md::c0004` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_027.md::c0004`
- anchor_doc_id: `zh_doc_027.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `3`
- anchor_query_overlap: `0.889`
- anchor_localization_score: `0.833`
- candidate_window_chunk_ids: `['zh_doc_027.md::c0003', 'zh_doc_027.md::c0004', 'zh_doc_027.md::c0005']`
- topk_same_doc_count: `1`
- topk_same_section_count: `1`

## zh082 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 中国古代最繁荣的朝代
- offline gold: `zh_doc_082.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_082.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_082.md::c0000`
- anchor_doc_id: `zh_doc_082.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_082.md::c0000', 'zh_doc_082.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh083 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 怎么改民族
- offline gold: `zh_doc_083.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_083.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_083.md::c0000`
- anchor_doc_id: `zh_doc_083.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `4`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.925`
- candidate_window_chunk_ids: `['zh_doc_083.md::c0000', 'zh_doc_083.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh085 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 白带有酸奶味
- offline gold: `zh_doc_085.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_085.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_085.md::c0000`
- anchor_doc_id: `zh_doc_085.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.8`
- anchor_localization_score: `0.77`
- candidate_window_chunk_ids: `['zh_doc_085.md::c0000', 'zh_doc_085.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh087 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 晾衣架材质
- offline gold: `zh_doc_087.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_087.md::c0008` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_087.md::c0008`
- anchor_doc_id: `zh_doc_087.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_087.md::c0007', 'zh_doc_087.md::c0008', 'zh_doc_087.md::c0009']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh088 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 如何遮盖唇色
- offline gold: `zh_doc_088.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_088.md::c0002` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_088.md::c0002`
- anchor_doc_id: `zh_doc_088.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.6`
- anchor_localization_score: `0.64`
- candidate_window_chunk_ids: `['zh_doc_088.md::c0001', 'zh_doc_088.md::c0002', 'zh_doc_088.md::c0003']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh089 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 部落冲突怎么搜死鱼
- offline gold: `zh_doc_089.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_089.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_089.md::c0000`
- anchor_doc_id: `zh_doc_089.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_089.md::c0000', 'zh_doc_089.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh090 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 牛剖层移膜皮是什么
- offline gold: `zh_doc_090.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_090.md::c0023` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_090.md::c0023`
- anchor_doc_id: `zh_doc_090.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `7`
- anchor_query_overlap: `0.875`
- anchor_localization_score: `0.802`
- candidate_window_chunk_ids: `['zh_doc_090.md::c0022', 'zh_doc_090.md::c0023', 'zh_doc_090.md::c0024']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh093 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 成都审驾照需要什么
- offline gold: `zh_doc_093.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_093.md::c0016` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_093.md::c0016`
- anchor_doc_id: `zh_doc_093.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.625`
- anchor_localization_score: `0.662`
- candidate_window_chunk_ids: `['zh_doc_093.md::c0015', 'zh_doc_093.md::c0016', 'zh_doc_093.md::c0017']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh094 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 霜是怎么形成的
- offline gold: `zh_doc_094.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_094.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_094.md::c0000`
- anchor_doc_id: `zh_doc_094.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.95`
- candidate_window_chunk_ids: `['zh_doc_094.md::c0000', 'zh_doc_094.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh095 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 卫生间铺什么地砖好
- offline gold: `zh_doc_095.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_095.md::c0002` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_095.md::c0002`
- anchor_doc_id: `zh_doc_095.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.625`
- anchor_localization_score: `0.613`
- candidate_window_chunk_ids: `['zh_doc_095.md::c0001', 'zh_doc_095.md::c0002', 'zh_doc_095.md::c0003']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh096 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 肠结核的症状
- offline gold: `zh_doc_096.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_096.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_096.md::c0001`
- anchor_doc_id: `zh_doc_096.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.8`
- anchor_localization_score: `0.77`
- candidate_window_chunk_ids: `['zh_doc_096.md::c0000', 'zh_doc_096.md::c0001', 'zh_doc_096.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh097 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 表带怎么打孔
- offline gold: `zh_doc_097.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_097.md::c0006` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_097.md::c0006`
- anchor_doc_id: `zh_doc_097.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `4`
- anchor_query_overlap: `0.8`
- anchor_localization_score: `0.745`
- candidate_window_chunk_ids: `['zh_doc_097.md::c0005', 'zh_doc_097.md::c0006', 'zh_doc_097.md::c0007']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh099 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 水土流失是什么意思
- offline gold: `zh_doc_099.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_099.md::c0022` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_099.md::c0022`
- anchor_doc_id: `zh_doc_099.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_099.md::c0021', 'zh_doc_099.md::c0022', 'zh_doc_099.md::c0023']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh100 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 红枣表面有层白色粉末
- offline gold: `zh_doc_100.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_100.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_100.md::c0000`
- anchor_doc_id: `zh_doc_100.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `5`
- anchor_query_overlap: `0.778`
- anchor_localization_score: `0.72`
- candidate_window_chunk_ids: `['zh_doc_100.md::c0000', 'zh_doc_100.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh101 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 小米的平板好用吗
- offline gold: `zh_doc_101.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_101.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_101.md::c0001`
- anchor_doc_id: `zh_doc_101.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `4`
- anchor_query_overlap: `0.571`
- anchor_localization_score: `0.539`
- candidate_window_chunk_ids: `['zh_doc_101.md::c0000', 'zh_doc_101.md::c0001', 'zh_doc_101.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh102 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 尺神经麻痹治疗
- offline gold: `zh_doc_102.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_102.md::c0004` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_102.md::c0004`
- anchor_doc_id: `zh_doc_102.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.833`
- anchor_localization_score: `0.85`
- candidate_window_chunk_ids: `['zh_doc_102.md::c0003', 'zh_doc_102.md::c0004', 'zh_doc_102.md::c0005']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh103 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 北京出国体检在哪里
- offline gold: `zh_doc_103.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_103.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_103.md::c0000`
- anchor_doc_id: `zh_doc_103.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `5`
- anchor_query_overlap: `0.875`
- anchor_localization_score: `0.807`
- candidate_window_chunk_ids: `['zh_doc_103.md::c0000', 'zh_doc_103.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh106 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 原地跑步能减肚子吗
- offline gold: `zh_doc_106.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_106.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_106.md::c0001`
- anchor_doc_id: `zh_doc_106.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.75`
- anchor_localization_score: `0.775`
- candidate_window_chunk_ids: `['zh_doc_106.md::c0000', 'zh_doc_106.md::c0001', 'zh_doc_106.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh110 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 完美世界出过什么游戏
- offline gold: `zh_doc_110.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_110.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_110.md::c0000`
- anchor_doc_id: `zh_doc_110.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.667`
- anchor_localization_score: `0.7`
- candidate_window_chunk_ids: `['zh_doc_110.md::c0000', 'zh_doc_110.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh112 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 为什么qq打不开图片
- offline gold: `zh_doc_112.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_112.md::c0004` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_112.md::c0004`
- anchor_doc_id: `zh_doc_112.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.857`
- anchor_localization_score: `0.871`
- candidate_window_chunk_ids: `['zh_doc_112.md::c0003', 'zh_doc_112.md::c0004', 'zh_doc_112.md::c0005']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh113 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 辅酶q10的服用方法
- offline gold: `zh_doc_113.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_113.md::c0008` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_113.md::c0008`
- anchor_doc_id: `zh_doc_113.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `1.0`
- candidate_window_chunk_ids: `['zh_doc_113.md::c0007', 'zh_doc_113.md::c0008', 'zh_doc_113.md::c0009']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh117 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 德国红铁元和绿铁元有什么区别
- offline gold: `zh_doc_117.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_117.md::c0006` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_117.md::c0006`
- anchor_doc_id: `zh_doc_117.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `3`
- anchor_query_overlap: `0.833`
- anchor_localization_score: `0.783`
- candidate_window_chunk_ids: `['zh_doc_117.md::c0005', 'zh_doc_117.md::c0006', 'zh_doc_117.md::c0007']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`

## zh118 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 诛仙法宝技能怎么洗
- offline gold: `zh_doc_118.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_118.md::c0004` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_118.md::c0004`
- anchor_doc_id: `zh_doc_118.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.75`
- anchor_localization_score: `0.775`
- candidate_window_chunk_ids: `['zh_doc_118.md::c0003', 'zh_doc_118.md::c0004', 'zh_doc_118.md::c0005']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh119 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 神秘博士clara是谁
- offline gold: `zh_doc_119.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_119.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_119.md::c0003`
- anchor_doc_id: `zh_doc_119.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.8`
- anchor_localization_score: `0.82`
- candidate_window_chunk_ids: `['zh_doc_119.md::c0002', 'zh_doc_119.md::c0003', 'zh_doc_119.md::c0004']`
- topk_same_doc_count: `5`
- topk_same_section_count: `2`
