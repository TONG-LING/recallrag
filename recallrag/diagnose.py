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
    """Locate a candidate evidence window from retrieval traces only.

    This intentionally does NOT look at gold_doc/gold_span.  It simulates the
    production setting: a failed query provides near-miss retrieval traces, and
    the system must infer a local window worth patching.
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
        dense_rank_score = 1.0 / max(rank, 1)
        text = c.get('text', '')
        section = c.get('section_path', '')
        overlap = _query_overlap(q['question'], text + ' ' + section)
        # Prefer query-aligned chunks over generic rank-1 overviews.  Rank is
        # only a weak prior; in production chunk failures the evidence often
        # appears deeper in top-N because the top-k contains only partial clues.
        score = 0.10 * dense_rank_score + 0.90 * overlap
        scored.append((score, overlap, rank, c))
    if not scored:
        return None, [], {'localization_signal': 'trace_without_known_chunks'}
    scored.sort(key=lambda x: (x[0], x[1], -x[2]), reverse=True)
    best_score, best_overlap, best_rank, anchor = scored[0]

    doc_chunks = [c for c in chunks if c.get('doc_id') == anchor.get('doc_id')]
    doc_chunks.sort(key=lambda c: c.get('start_offset', 0))
    pos = next((i for i, c in enumerate(doc_chunks) if c['chunk_id'] == anchor['chunk_id']), None)
    if pos is None:
        window = [anchor]
    else:
        window = doc_chunks[max(0, pos-1): min(len(doc_chunks), pos+2)]

    # Check whether top-k already clusters around the same document.  This is a
    # common production signal for "right area but incomplete local context".
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
    anchor, window, evidence = _select_anchor_without_gold(q, chunks, result)
    patch_allowed = False
    failure_type = 'evidence_not_localized'
    family = 'needs_review'
    recommendation = 'expand_retrieval_or_manual_review'
    confidence = 0.35
    reason = 'could not localize a candidate evidence window from production retrieval traces'

    if anchor and window:
        overlap = evidence.get('anchor_query_overlap', 0.0)
        same_doc = evidence.get('topk_same_doc_count', 0)
        # Production rule: same-document clustering is only supporting
        # evidence.  We still require some direct query-window alignment;
        # otherwise a wrong document that happens to dominate top-k can be
        # misdiagnosed as a chunk-boundary/local-context failure.
        strong_overlap = overlap >= 0.25
        clustered_window = same_doc >= 2
        weak_but_supported_overlap = overlap >= 0.10 and clustered_window
        if strong_overlap or weak_but_supported_overlap:
            patch_allowed = True
            failure_type = 'missing_local_context_candidate'
            family = 'chunking_failure_candidate'
            recommendation = 'generate_local_proposition_patch_candidates_and_validate'
            confidence = min(0.82, 0.45 + float(overlap) + 0.05 * min(same_doc, 3))
            reason = (
                'failed query has near-miss retrieval evidence; localized a candidate '
                f'window around `{anchor["chunk_id"]}` without using gold labels'
            )
        else:
            failure_type = 'weak_localization_signal'
            family = 'non_chunk_or_uncertain_failure'
            recommendation = 'try_query_rewrite_bm25_hybrid_or_manual_review'
            confidence = 0.45
            reason = 'retrieval trace exists but query-window alignment is weak; do not patch automatically'

    return {
        'qid': q['qid'],
        'question': q['question'],
        # Gold fields are copied only for offline report readability. They are
        # not used by localization/diagnosis above.
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
