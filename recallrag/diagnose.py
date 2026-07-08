from __future__ import annotations
import json, re
from pathlib import Path
from .eval import load_questions
from .text_utils import mixed_token_set

def _load_json(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))

def _write_json(p, obj):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')

def _tokens(s: str) -> list[str]:
    # 算词面重叠时用，会去掉英文停用词
    return list(mixed_token_set(s, drop_stopwords=True, min_ascii_len=2))

def _token_set(s: str) -> set[str]:
    return mixed_token_set(s, drop_stopwords=True, min_ascii_len=2)

def _chunk_seq(chunk_id: str) -> int | None:
    m = re.search(r"::c(\d+)$", chunk_id or '')
    return int(m.group(1)) if m else None

def _query_overlap(query: str, text: str) -> float:
    q = _token_set(query)
    if not q:
        return 0.0
    t = _token_set(text)
    return len(q & t) / len(q)

def _lookup_trace_text(trace_row: dict, by_id: dict[str, dict]) -> str:
    c = by_id.get(trace_row.get('chunk_id'))
    return c.get('text', '') if c else trace_row.get('text_preview', '')

def _select_anchor_without_gold(q: dict, chunks: list[dict], result: dict) -> tuple[dict | None, list[dict], dict]:
    """只靠检索trace找有可能的定位点，不看gold_doc和gold_span

    模拟真实的场景：失败查询只有检索结果，要从近似命中里猜值得做patch的局部窗口

    定位器
    """
    by_id = {c['chunk_id']: c for c in chunks}
    trace = result.get('top_n_trace') or result.get('top_k') or []
    if not trace:
        return None, [], {'localization_signal': 'no_trace'}

    scored = []
    for row in trace:
        c = by_id.get(row.get('chunk_id'))
        if not c:
            continue
        rank = int(row.get('rank') or 999)
        #防异常rank值
        dense_rank_score = 1.0 / max(rank, 1)
        text = c.get('text', '')
        section = c.get('section_path', '')
        overlap = _query_overlap(q['question'], text + ' ' + section)
        # 看query-chunk词面重叠，排名只是之后的参考
        # chunk边界问题里证据经常在 top-n 靠后，rank-1 有可能是截断答案
        score = 0.10 * dense_rank_score + 0.90 * overlap
        scored.append((score, overlap, rank, c))
    if not scored:
        return None, [], {'localization_signal': 'trace_without_known_chunks'}
    # 按照综合得分、重叠度、原始rank排序
    # 为了防止平局
    scored.sort(key=lambda x: (x[0], x[1], -x[2]), reverse=True)
    best_score, best_overlap, best_rank, anchor = scored[0]
    # 找出和定位点同一篇文章的所有chunk
    doc_chunks = [c for c in chunks if c.get('doc_id') == anchor.get('doc_id')]
    doc_chunks.sort(key=lambda c: c.get('start_offset', 0))
    pos = next((i for i, c in enumerate(doc_chunks) if c['chunk_id'] == anchor['chunk_id']), None)
    if pos is None:
        window = [anchor]
    else:
        window = doc_chunks[max(0, pos-1): min(len(doc_chunks), pos+2)]

    # 看top-k是否聚集在同一文档，来判断：找对地方但局部上下文不够
    topk = result.get('top_k') or []
    topk_same_doc = sum(1 for r in topk if r.get('doc_id') == anchor.get('doc_id'))
    topk_same_section = sum(1 for r in topk if r.get('section_path') and r.get('section_path') == anchor.get('section_path'))
    evidence = {
        'localization_mode': 'production_near_miss_trace',
        'anchor_chunk_id': anchor['chunk_id'],
        'anchor_doc_id': anchor.get('doc_id'),
        'anchor_section_path': anchor.get('section_path',''),
        'anchor_rank_in_trace': best_rank,
        'anchor_query_overlap': round(best_overlap, 3),
        'anchor_localization_score': round(best_score, 3),
        'candidate_window_chunk_ids': [c['chunk_id'] for c in window],
        'topk_same_doc_count': topk_same_doc,
        'topk_same_section_count': topk_same_section,
    }
    return anchor, window, evidence

def diagnose_one(q: dict, chunks: list[dict], result: dict, threshold: float = 0.65) -> dict:
    """根据重叠度和同文档数量，判断是否可以打补丁(决断器)"""
    anchor, window, evidence = _select_anchor_without_gold(q, chunks, result)
    patch_allowed = False
    #失败类型：找不到定位点
    failure_type = 'evidence_not_localized'
    family = 'needs_review'
    recommendation = 'expand_retrieval_or_manual_review'
    confidence = 0.35
    reason = 'could not localize a candidate evidence window from production retrieval traces'

    if anchor and window:
        overlap = evidence.get('anchor_query_overlap', 0.0)
        same_doc = evidence.get('topk_same_doc_count', 0)
        # 同文档聚集只是辅助，还得有问题对齐才行
        # 不然错文档在 top-k 时会被误判成 chunk 边界问题
        strong_overlap = overlap >= 0.25
        clustered_window = same_doc >= 2
        weak_but_supported_overlap = overlap >= 0.10 and clustered_window
        if strong_overlap or weak_but_supported_overlap:
            patch_allowed = True
            #定位器找到了，局部答案上下文缺失
            failure_type = 'missing_local_context_candidate'
            family = 'chunking_failure_candidate'
            #自动生成候选patch并送去验证
            recommendation = 'generate_local_proposition_patch_candidates_and_validate'
            #置信度公式：confidence = min (0.82,0.45 + overlap + 0.05 × min (same_doc,3))
            #0.45基础分，同一文档只能是3个（总共0.15），因为是无监督的，防止算法过于自信导致误判
            #0.3 好像有点小，改成了0.45，0.8->0.82
            confidence = min(0.82, 0.45 + float(overlap) + 0.05 * min(same_doc, 3))
            reason = (
                'failed query has near-miss retrieval evidence; localized a candidate '
                f'window around `{anchor["chunk_id"]}` without using gold labels'
            )
        else:
            #定位器找到了，但是证据不够强，无发生成补丁
            failure_type = 'weak_localization_signal'
            family = 'non_chunk_or_uncertain_failure'
            #给出建议：建议人工查看或换混合检索
            recommendation = 'try_query_rewrite_bm25_hybrid_or_manual_review'
            confidence = 0.45
            #给出原因：词匹配强度较弱
            reason = 'retrieval trace exists but query-window alignment is weak; do not patch automatically'

    return {
        'qid': q['qid'],
        'question': q['question'],
        # gold字段方便报告对照，不参与定位器逻辑
        'gold_doc': q.get('gold_doc',''),
        'gold_section': q.get('gold_section',''),
        'expected_failure_type': q.get('gold_failure_type',''),
        'diagnosed_failure_type': failure_type,
        'failure_family': family,
        'patch_allowed': patch_allowed,
        'confidence': round(confidence, 3),
        'reason': reason,
        'recommendation': recommendation,
        'evidence': evidence,
    }

def diagnose_run(index_dir: str | Path, questions_path: str | Path, out_dir: str | Path | None = None, threshold: float = 0.65):
    """批量找出所有检索失败的查询"""
    index_dir = Path(index_dir)
    out_dir = Path(out_dir or index_dir)
    chunks = _load_json(index_dir / 'chunks.json')
    results = _load_json(index_dir / 'retrieval_results.json')
    questions = {q['qid']: q for q in load_questions(questions_path)}
    failed = [r for r in results if not r['success']]
    diagnoses = [diagnose_one(questions[r['qid']], chunks, r, threshold=threshold) for r in failed]
    _write_json(out_dir / 'failure_diagnosis.json', diagnoses)
    write_diagnosis_report(out_dir / 'failure_diagnosis.md', diagnoses)
    return diagnoses

def write_diagnosis_report(path: str | Path, diagnoses: list[dict]):
    total = len(diagnoses)
    chunking = sum(1 for d in diagnoses if 'chunking' in d['failure_family'])
    uncertain = sum(1 for d in diagnoses if d['failure_family'] != 'chunking_failure_candidate')
    lines = ['# Production-style Failure Diagnosis Report', '']
    lines += ['## Summary', '']
    lines += [
        f'- failed queries diagnosed: {total}',
        f'- chunking/local-context candidates: {chunking}',
        f'- uncertain/non-chunk: {uncertain}',
        f'- patch_allowed: {sum(1 for d in diagnoses if d["patch_allowed"])}',
        '',
        '> Localization does not use `gold_doc` or `gold_span`; gold fields are only retained for offline evaluation readability.',
        '',
    ]
    for d in diagnoses:
        lines += [
            f"## {d['qid']} — {d['diagnosed_failure_type']}", '',
            f"- expected label: `{d['expected_failure_type']}`",
            f"- family: `{d['failure_family']}`",
            f"- patch_allowed: `{d['patch_allowed']}`",
            f"- confidence: `{d['confidence']}`",
            f"- question: {d['question']}",
            f"- offline gold: `{d.get('gold_doc','')} > {d.get('gold_section','')}`",
            f"- reason: {d['reason']}",
            f"- recommendation: `{d['recommendation']}`",
            '', 'Localization evidence:', ''
        ]
        for k, v in d['evidence'].items():
            lines.append(f'- {k}: `{v}`')
        lines.append('')
    Path(path).write_text('\n'.join(lines), encoding='utf-8')