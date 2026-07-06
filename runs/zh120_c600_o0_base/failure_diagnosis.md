# Production-style Failure Diagnosis Report

## Summary

- failed queries diagnosed: 14
- chunking/local-context candidates: 14
- uncertain/non-chunk: 0
- patch_allowed: 14

> Localization does not use `gold_doc` or `gold_span`; gold fields are only retained for offline evaluation readability.

## zh002 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 空气净化器哪种净化方式好
- offline gold: `zh_doc_002.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_002.md::c0002` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_002.md::c0002`
- anchor_doc_id: `zh_doc_002.md`
- anchor_section_path: `中文复杂检索文档 > 关`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.7`
- anchor_localization_score: `0.73`
- candidate_window_chunk_ids: `['zh_doc_002.md::c0001', 'zh_doc_002.md::c0002', 'zh_doc_002.md::c0003']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh003 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 黄山风景古诗赞
- offline gold: `zh_doc_003.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_003.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_003.md::c0003`
- anchor_doc_id: `zh_doc_003.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.5`
- anchor_localization_score: `0.55`
- candidate_window_chunk_ids: `['zh_doc_003.md::c0002', 'zh_doc_003.md::c0003', 'zh_doc_003.md::c0004']`
- topk_same_doc_count: `4`
- topk_same_section_count: `3`

## zh004 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 一天放很多屁
- offline gold: `zh_doc_004.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_004.md::c0007` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_004.md::c0007`
- anchor_doc_id: `zh_doc_004.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `5`
- anchor_query_overlap: `0.6`
- anchor_localization_score: `0.56`
- candidate_window_chunk_ids: `['zh_doc_004.md::c0006', 'zh_doc_004.md::c0007', 'zh_doc_004.md::c0008']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

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
- anchor_rank_in_trace: `3`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.933`
- candidate_window_chunk_ids: `['zh_doc_006.md::c0000', 'zh_doc_006.md::c0001']`
- topk_same_doc_count: `4`
- topk_same_section_count: `0`

## zh007 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 经常用肥皂洗脸好吗
- offline gold: `zh_doc_007.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_007.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_007.md::c0001`
- anchor_doc_id: `zh_doc_007.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.95`
- candidate_window_chunk_ids: `['zh_doc_007.md::c0000', 'zh_doc_007.md::c0001', 'zh_doc_007.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh008 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 冬天怎样养鹦鹉
- offline gold: `zh_doc_008.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_008.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_008.md::c0001`
- anchor_doc_id: `zh_doc_008.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.5`
- anchor_localization_score: `0.55`
- candidate_window_chunk_ids: `['zh_doc_008.md::c0000', 'zh_doc_008.md::c0001', 'zh_doc_008.md::c0002']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

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
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.857`
- anchor_localization_score: `0.821`
- candidate_window_chunk_ids: `['zh_doc_010.md::c0000', 'zh_doc_010.md::c0001']`
- topk_same_doc_count: `3`
- topk_same_section_count: `0`

## zh011 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 比较好看的电视剧
- offline gold: `zh_doc_011.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_011.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_011.md::c0003`
- anchor_doc_id: `zh_doc_011.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.714`
- anchor_localization_score: `0.743`
- candidate_window_chunk_ids: `['zh_doc_011.md::c0002', 'zh_doc_011.md::c0003']`
- topk_same_doc_count: `4`
- topk_same_section_count: `1`

## zh017 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 阴部变白
- offline gold: `zh_doc_017.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_017.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_017.md::c0003`
- anchor_doc_id: `zh_doc_017.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `3`
- anchor_query_overlap: `1.0`
- anchor_localization_score: `0.933`
- candidate_window_chunk_ids: `['zh_doc_017.md::c0002', 'zh_doc_017.md::c0003']`
- topk_same_doc_count: `4`
- topk_same_section_count: `1`

## zh027 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 小米平板钢化膜怎么贴
- offline gold: `zh_doc_027.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_027.md::c0003` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_027.md::c0003`
- anchor_doc_id: `zh_doc_027.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.889`
- anchor_localization_score: `0.9`
- candidate_window_chunk_ids: `['zh_doc_027.md::c0002', 'zh_doc_027.md::c0003', 'zh_doc_027.md::c0004']`
- topk_same_doc_count: `3`
- topk_same_section_count: `1`

## zh033 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 电暖桌哪个牌子好
- offline gold: `zh_doc_033.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_033.md::c0000` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_033.md::c0000`
- anchor_doc_id: `zh_doc_033.md`
- anchor_section_path: ``
- anchor_rank_in_trace: `4`
- anchor_query_overlap: `0.857`
- anchor_localization_score: `0.796`
- candidate_window_chunk_ids: `['zh_doc_033.md::c0000', 'zh_doc_033.md::c0001']`
- topk_same_doc_count: `5`
- topk_same_section_count: `0`

## zh057 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: word怎么不能修改
- offline gold: `zh_doc_057.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_057.md::c0007` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_057.md::c0007`
- anchor_doc_id: `zh_doc_057.md`
- anchor_section_path: `中文复杂检索文档 > 补充材料1`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.833`
- anchor_localization_score: `0.8`
- candidate_window_chunk_ids: `['zh_doc_057.md::c0006', 'zh_doc_057.md::c0007']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`

## zh067 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 武松属什么
- offline gold: `zh_doc_067.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_067.md::c0001` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_067.md::c0001`
- anchor_doc_id: `zh_doc_067.md`
- anchor_section_path: `中文复杂检索文档 > 背景材料2`
- anchor_rank_in_trace: `1`
- anchor_query_overlap: `0.75`
- anchor_localization_score: `0.775`
- candidate_window_chunk_ids: `['zh_doc_067.md::c0000', 'zh_doc_067.md::c0001', 'zh_doc_067.md::c0002']`
- topk_same_doc_count: `4`
- topk_same_section_count: `1`

## zh101 — missing_local_context_candidate

- expected label: `zh_long_span_boundary_candidate`
- family: `chunking_failure_candidate`
- patch_allowed: `True`
- confidence: `0.82`
- question: 小米的平板好用吗
- offline gold: `zh_doc_101.md > 关键材料`
- reason: failed query has near-miss retrieval evidence; localized a candidate window around `zh_doc_101.md::c0004` without using gold labels
- recommendation: `generate_local_proposition_patch_candidates_and_validate`

Localization evidence:

- localization_mode: `production_near_miss_trace`
- anchor_chunk_id: `zh_doc_101.md::c0004`
- anchor_doc_id: `zh_doc_101.md`
- anchor_section_path: `中文复杂检索文档 > 关键材料`
- anchor_rank_in_trace: `2`
- anchor_query_overlap: `0.571`
- anchor_localization_score: `0.564`
- candidate_window_chunk_ids: `['zh_doc_101.md::c0003', 'zh_doc_101.md::c0004', 'zh_doc_101.md::c0005']`
- topk_same_doc_count: `5`
- topk_same_section_count: `1`
