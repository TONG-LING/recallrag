from __future__ import annotations
import json, re
from pathlib import Path
from .embeddings import (
    dot,
    embed_lmstudio,
    require_equal_length,
    require_vector_dimensions,
)
from .eval import load_questions, evaluate, write_report, relevance_score, is_relevant
from .text_utils import mixed_token_set, normalize_text, split_sentences

def _load_json(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))

def _write_json(p, obj):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')

def _tokens(s: str) -> set[str]:
    return mixed_token_set(s, drop_stopwords=True, min_ascii_len=2)

def _sentences(text: str) -> list[str]:
    return split_sentences(text, min_chars=18)

def _score_sentence(query: str, sent: str) -> float:
    q=_tokens(query)
    if not q: return 0.0
    st=_tokens(sent)
    return len(q & st)/len(q) + min(len(st), 40)/400.0

def _top_relevant_sentences(query: str, text: str, limit: int = 4) -> list[str]:
    sents=_sentences(text)
    if not sents:
        return [normalize_text(text)[:500]] if text else []
    ranked=sorted(enumerate(sents), key=lambda x: (_score_sentence(query,x[1]), -x[0]), reverse=True)
    selected=sorted([i for i,_ in ranked[:limit]])
    return [sents[i] for i in selected]

def _make_patch_text(candidate_type: str, qid: str, question: str, section_path: str, diagnosis: str, body: str) -> str:
    """Build the text that will be embedded for a patch candidate.

    Important anti-leakage rule:
    - The embedded text must NOT contain qid, the failed question, or diagnosis labels.
    - Those fields are stored only as metadata/logs.

    Otherwise the source query can match the patch because the patch literally
    contains the query text, which would make the experiment look like
    case-specific / question-leaking retrieval instead of evidence retrieval.
    """
    rel = _top_relevant_sentences(question, body, limit=4)
    # Keep only document-derived context in the embedded text.  Section paths
    # are allowed because they come from the source document and are a common
    # production chunking technique; qid/question/diagnosis are not allowed.
    header = f"Section: {section_path}\n\n" if section_path else ""
    if candidate_type == 'adjacent_merge':
        return header + body
    if candidate_type == 'contextual':
        return header + '\n'.join(rel)
    if candidate_type == 'local_proposition':
        bullets=[]
        for s in rel:
            clean=s.rstrip('. 。！？；;')
            bullets.append(f"- {clean}.")
        return header + '\n'.join(bullets)
    if candidate_type == 'local_summary':
        summary = ' '.join(rel[:3])
        return header + summary
    return header + body

def materialize_patches(
    index_dir: str | Path,
    out_dir: str | Path = 'runs/patches',
    endpoint: str = 'http://localhost:1234/v1/embeddings',
    model: str = 'bge-small-en-v1.5',
    batch_size: int = 16,
):
    """Create candidate Patch Index chunks from production-style diagnoses.

    Main index is never mutated.  For each localized failure, we create multiple
    evidence-representation candidates around the same near-miss window:
    adjacent_merge, contextual, local_proposition, local_summary.
    """
    index_dir = Path(index_dir)
    out_dir = Path(out_dir)
    chunks = _load_json(index_dir / 'chunks.json')
    by_id = {c['chunk_id']: c for c in chunks}
    diagnoses = _load_json(index_dir / 'failure_diagnosis.json')
    patch_chunks = []
    patch_log = []
    candidate_types = ['adjacent_merge', 'contextual', 'local_proposition', 'local_summary']
    for n, d in enumerate(diagnoses, 1):
        if not d.get('patch_allowed'):
            continue
        ids = d.get('evidence', {}).get('candidate_window_chunk_ids') or d.get('evidence', {}).get('adjacent_chunk_ids') or []
        selected = [by_id[i] for i in ids if i in by_id]
        if not selected:
            continue
        selected.sort(key=lambda c: (c['doc_id'], c['start_offset']))
        doc_id = selected[0]['doc_id']
        anchor_id = d.get('evidence', {}).get('anchor_chunk_id') or selected[len(selected)//2]['chunk_id']
        anchor = by_id.get(anchor_id, selected[len(selected)//2])
        # Section labels in patch text must come from source chunks only.
        # Offline gold annotations are allowed in evaluation/reporting, but
        # must not leak into the embedded patch text.
        section_path = anchor.get('section_path') or selected[0].get('section_path') or ''
        start = min(c['start_offset'] for c in selected)
        end = max(c['end_offset'] for c in selected)
        body = '\n'.join(c['text'] for c in selected)
        created=[]
        for cand_i, cand_type in enumerate(candidate_types, 1):
            patch_id = f"patch_{d['qid']}_{n:03d}_{cand_type}"
            text = _make_patch_text(cand_type, d['qid'], d['question'], section_path, d['diagnosed_failure_type'], body)
            pc = {
                'chunk_id': f'{patch_id}_c001',
                'patch_id': patch_id,
                'candidate_type': cand_type,
                'source_index': 'patch',
                'doc_id': doc_id,
                'section_id': section_path.split(' > ')[-1] if section_path else '',
                'section_path': section_path,
                'start_offset': start,
                'end_offset': end,
                'text': text,
                'strategy': 'failure_driven_local_proposition_patch_search',
                'replaces': ids,
                'anchor_chunk_id': anchor_id,
                'active': True,
                'created_from_qid': d['qid'],
                'failure_type': d['diagnosed_failure_type'],
                'localization_mode': d.get('evidence', {}).get('localization_mode'),
                'requires_validation': True,
            }
            patch_chunks.append(pc)
            created.append(pc['chunk_id'])
            patch_log.append({
                'patch_id': patch_id,
                'status': 'candidate_materialized',
                'qid': d['qid'],
                'candidate_type': cand_type,
                'failure_type': d['diagnosed_failure_type'],
                'diagnosis_confidence': d['confidence'],
                'reason': d['reason'],
                'strategy': pc['strategy'],
                'anchor_chunk_id': anchor_id,
                'affected_main_chunks': ids,
                'created_patch_chunks': [pc['chunk_id']],
                'notes': 'Main index is untouched. Candidate patch is stored in the side Patch Index for shadow validation.'
            })
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / 'patch_chunks.json', patch_chunks)
    _write_json(out_dir / 'patch_log.json', patch_log)
    if patch_chunks:
        vectors = embed_lmstudio([c['text'] for c in patch_chunks], endpoint=endpoint, model=model, batch_size=batch_size)
    else:
        vectors = []
    _write_json(out_dir / 'patch_vectors.json', vectors)
    _write_json(out_dir / 'patch_index_meta.json', {
        'endpoint': endpoint,
        'model': model,
        'count': len(vectors),
        'dim': len(vectors[0]) if vectors else 0,
        'main_index': str(index_dir),
        'candidate_search': candidate_types,
    })
    return patch_chunks, patch_log

def evaluate_hybrid(
    main_index_dir: str | Path,
    patch_dir: str | Path,
    questions_path: str | Path,
    out_dir: str | Path = 'runs/hybrid',
    endpoint: str = 'http://localhost:1234/v1/embeddings',
    model: str = 'bge-small-en-v1.5',
    top_k: int = 5,
    coverage_threshold: float = 0.65,
):
    """Evaluate main-only vs main+patch retrieval and write decision reports."""
    main_index_dir = Path(main_index_dir)
    patch_dir = Path(patch_dir)
    out_dir = Path(out_dir)
    main_chunks = _load_json(main_index_dir / 'chunks.json')
    main_vectors = _load_json(main_index_dir / 'vectors.json')
    patch_chunks = _load_json(patch_dir / 'patch_chunks.json') if (patch_dir / 'patch_chunks.json').exists() else []
    patch_vectors = _load_json(patch_dir / 'patch_vectors.json') if (patch_dir / 'patch_vectors.json').exists() else []
    require_equal_length('main_chunks', main_chunks, 'main_vectors', main_vectors, 'evaluate_hybrid.main_index')
    main_dim = require_vector_dimensions(main_vectors, 'evaluate_hybrid.main_vectors') if main_vectors else None
    require_equal_length('patch_chunks', patch_chunks, 'patch_vectors', patch_vectors, 'evaluate_hybrid.patch_index')
    if patch_vectors:
        require_vector_dimensions(patch_vectors, 'evaluate_hybrid.patch_vectors', expected_dim=main_dim)
    questions = load_questions(questions_path)
    candidate_probe = probe_patch_candidates(
        main_chunks, main_vectors, patch_chunks, patch_vectors, questions,
        endpoint=endpoint, model=model, top_k=top_k, coverage_threshold=coverage_threshold,
    )
    selected_by_qid = _select_successful_patch_candidates(candidate_probe)
    selected_ids = {r['patch_id'] for r in selected_by_qid.values()}
    selected_pairs = [(c, v) for c, v in zip(patch_chunks, patch_vectors) if c.get('patch_id') in selected_ids]
    selected_patch_chunks = [c for c, _ in selected_pairs]
    selected_patch_vectors = [v for _, v in selected_pairs]
    chunks = main_chunks + selected_patch_chunks
    vectors = main_vectors + selected_patch_vectors
    results, metrics = evaluate(
        chunks,
        vectors,
        questions,
        endpoint=endpoint,
        model=model,
        top_k=top_k,
        coverage_threshold=coverage_threshold,
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / 'retrieval_results.json', results)
    _write_json(out_dir / 'metrics.json', metrics)
    _write_json(out_dir / 'candidate_probe_results.json', candidate_probe)
    _write_json(out_dir / 'selected_patch_candidates.json', list(selected_by_qid.values()))
    _write_json(out_dir / 'selected_patch_chunks.json', selected_patch_chunks)
    _write_json(out_dir / 'selected_patch_vectors.json', selected_patch_vectors)
    config = {
        'main_index': str(main_index_dir),
        'patch_index': str(patch_dir),
        'questions': str(questions_path),
        'top_k': top_k,
        'coverage_threshold': coverage_threshold,
        'endpoint': endpoint,
        'model': model,
        'main_chunks': len(main_chunks),
        'patch_chunks': len(selected_patch_chunks),
        'candidate_patch_chunks': len(patch_chunks),
    }
    write_report(out_dir / 'eval_report.md', metrics, results, config)
    comparison = write_comparison(main_index_dir, patch_dir, out_dir, len(main_chunks), len(selected_patch_chunks), candidate_probe)
    accepted_ids = _accepted_patch_ids(comparison.get('patch_decisions', []))
    accepted_patch_chunks, accepted_patch_vectors = _filter_patch_pairs_by_ids(patch_chunks, patch_vectors, accepted_ids)
    _write_json(patch_dir / 'selected_patch_chunks.json', accepted_patch_chunks)
    _write_json(patch_dir / 'selected_patch_vectors.json', accepted_patch_vectors)
    return results, metrics, comparison

def _rank_with_vectors(q: dict, qv: list[float], chunks: list[dict], vectors: list[list[float]], top_k: int, threshold: float):
    require_equal_length('chunks', chunks, 'vectors', vectors, 'patch_index._rank_with_vectors')
    if vectors:
        require_vector_dimensions(vectors, 'patch_index._rank_with_vectors.candidate_vectors', expected_dim=len(qv))
    scored = [{**c, 'score': dot(qv, v)} for c, v in zip(chunks, vectors)]
    scored.sort(key=lambda x: x['score'], reverse=True)
    rank = None
    best_cov = 0.0
    for i, r in enumerate(scored[:top_k], 1):
        cov = relevance_score(q, r)
        best_cov = max(best_cov, cov)
        if is_relevant(q, r, threshold) and rank is None:
            rank = i
    return {
        'success': rank is not None,
        'rank': rank,
        'best_topk_coverage': round(best_cov, 3),
        'top_patch_hits': [
            {
                'rank': i,
                'chunk_id': r['chunk_id'],
                'candidate_type': r.get('candidate_type'),
                'score': round(r['score'], 6),
                'coverage': round(relevance_score(q, r), 3),
            }
            for i, r in enumerate(scored[:top_k], 1)
            if r.get('source_index') == 'patch'
        ],
    }

def probe_patch_candidates(
    main_chunks: list[dict],
    main_vectors: list[list[float]],
    patch_chunks: list[dict],
    patch_vectors: list[list[float]],
    questions: list[dict],
    endpoint: str,
    model: str,
    top_k: int,
    coverage_threshold: float,
):
    """Evaluate each patch candidate alone for its source query."""
    if not patch_chunks:
        return []
    require_equal_length('main_chunks', main_chunks, 'main_vectors', main_vectors, 'probe_patch_candidates.main_index')
    main_dim = require_vector_dimensions(main_vectors, 'probe_patch_candidates.main_vectors') if main_vectors else None
    require_equal_length('patch_chunks', patch_chunks, 'patch_vectors', patch_vectors, 'probe_patch_candidates.patch_index')
    if patch_vectors:
        require_vector_dimensions(patch_vectors, 'probe_patch_candidates.patch_vectors', expected_dim=main_dim)
    q_by_id = {q['qid']: q for q in questions}
    needed, seen = [], set()
    for p in patch_chunks:
        qid = p.get('created_from_qid')
        if qid in q_by_id and qid not in seen:
            needed.append(q_by_id[qid])
            seen.add(qid)
    qvecs = embed_lmstudio([q['question'] for q in needed], endpoint=endpoint, model=model) if needed else []
    require_equal_length('needed_questions', needed, 'query_vectors', qvecs, 'probe_patch_candidates')
    if qvecs:
        require_vector_dimensions(qvecs, 'probe_patch_candidates.query_vectors', expected_dim=main_dim)
    qv_by_id = {q['qid']: v for q, v in zip(needed, qvecs)}
    rows = []
    for p, pv in zip(patch_chunks, patch_vectors):
        qid = p.get('created_from_qid')
        q = q_by_id.get(qid)
        qv = qv_by_id.get(qid)
        if q is None or qv is None:
            continue
        res = _rank_with_vectors(q, qv, main_chunks + [p], main_vectors + [pv], top_k, coverage_threshold)
        rows.append({
            'qid': qid,
            'patch_id': p['patch_id'],
            'chunk_id': p['chunk_id'],
            'candidate_type': p.get('candidate_type'),
            'text_len': len(p.get('text','')),
            **res,
        })
    return rows

def _fmt_delta(after: float, before: float) -> str:
    delta = after - before
    sign = '+' if delta >= 0 else ''
    return f'{after:.4f} ({sign}{delta:.4f})'

def _accepted_patch_ids(patch_decisions: list[dict]) -> set[str]:
    return {row.get('patch_id') for row in patch_decisions if row.get('status') == 'accepted'}

def _patch_selection_key(row: dict):
    priority = {'local_proposition': 0, 'contextual': 1, 'local_summary': 2, 'adjacent_merge': 3}
    # Prefer candidates with stronger evidence coverage before using text length
    # as a tie-breaker. This avoids selecting a shorter patch that only barely
    # clears the threshold while a slightly longer patch captures the evidence
    # much more completely.
    return (
        -(row.get('best_topk_coverage') or 0.0),
        row.get('rank') or 999,
        row.get('text_len') or 0,
        priority.get(row.get('candidate_type'), 9),
    )

def _select_successful_patch_candidates(candidate_probe: list[dict]) -> dict[str, dict]:
    selected_by_qid: dict[str, dict] = {}
    for row in candidate_probe:
        if not row.get('success'):
            continue
        old = selected_by_qid.get(row['qid'])
        if old is None or _patch_selection_key(row) < _patch_selection_key(old):
            selected_by_qid[row['qid']] = row
    return selected_by_qid

def _filter_patch_pairs_by_ids(
    patch_chunks: list[dict],
    patch_vectors: list[list[float]],
    patch_ids: set[str],
):
    require_equal_length('patch_chunks', patch_chunks, 'patch_vectors', patch_vectors, 'patch_index._filter_patch_pairs_by_ids')
    pairs = [(c, v) for c, v in zip(patch_chunks, patch_vectors) if c.get('patch_id') in patch_ids]
    return [c for c, _ in pairs], [v for _, v in pairs]

def write_comparison(main_dir: Path, patch_dir: Path, hybrid_dir: Path, main_chunks: int, patch_chunks: int, candidate_probe: list[dict] | None = None):
    base_metrics = _load_json(main_dir / 'metrics.json')
    hybrid_metrics = _load_json(hybrid_dir / 'metrics.json')
    base_results = {r['qid']: r for r in _load_json(main_dir / 'retrieval_results.json')}
    hy_results = {r['qid']: r for r in _load_json(hybrid_dir / 'retrieval_results.json')}
    patch_log = _load_json(patch_dir / 'patch_log.json') if (patch_dir / 'patch_log.json').exists() else []
    candidate_probe = candidate_probe or []
    probe_by_patch = {r['patch_id']: r for r in candidate_probe}

    fixed=[]; regressed=[]; unchanged_failure=[]; unchanged_success=[]
    movements = []
    for qid,b in base_results.items():
        h=hy_results[qid]
        if (not b['success']) and h['success']:
            bucket = 'fixed'
            fixed.append(qid)
        elif b['success'] and (not h['success']):
            bucket = 'regressed'
            regressed.append(qid)
        elif (not b['success']) and (not h['success']):
            bucket = 'unchanged_failure'
            unchanged_failure.append(qid)
        else:
            bucket = 'unchanged_success'
            unchanged_success.append(qid)
        movements.append({
            'qid': qid,
            'movement': bucket,
            'before_success': b['success'],
            'after_success': h['success'],
            'before_rank': b['rank'],
            'after_rank': h['rank'],
            'before_best_coverage': b['best_topk_coverage'],
            'after_best_coverage': h['best_topk_coverage'],
        })

    selected_patch_ids = set()
    selected_path = hybrid_dir / 'selected_patch_candidates.json'
    if selected_path.exists():
        try:
            selected_patch_ids = {r.get('patch_id') for r in _load_json(selected_path)}
        except Exception:
            selected_patch_ids = set()

    # Patch-level decision: only the selected patch candidate can be accepted.
    # Non-selected candidates stay auditable but should not be described as
    # accepted, even if the qid was fixed by another selected candidate.
    decisions = []
    for p in patch_log:
        qid = p['qid']
        before = base_results.get(qid)
        after = hy_results.get(qid)
        if regressed:
            status = 'needs_review'
            reason = f'global regression detected: {regressed}'
        elif p.get('patch_id') not in selected_patch_ids:
            status = 'candidate_not_selected'
            reason = 'candidate was materialized/probed but not selected under the stronger-coverage-then-shorter rule'
        elif before and after and (not before['success']) and after['success']:
            status = 'accepted'
            reason = 'source query fixed and no regression detected'
        elif after and not after['success']:
            status = 'rejected'
            reason = 'source query still fails after main+patch retrieval'
        else:
            status = 'needs_review'
            reason = 'no clear query-level improvement'
        d = {
            **p,
            'status': status,
            'decision_reason': reason,
            'candidate_probe': probe_by_patch.get(p['patch_id']),
            'before_rank': before['rank'] if before else None,
            'after_rank': after['rank'] if after else None,
            'before_best_coverage': before['best_topk_coverage'] if before else None,
            'after_best_coverage': after['best_topk_coverage'] if after else None,
        }
        decisions.append(d)

    selected = list(_select_successful_patch_candidates(candidate_probe).values())

    ratio = patch_chunks / main_chunks if main_chunks else 0
    comparison = {
        'main_only': base_metrics,
        'main_plus_patch': hybrid_metrics,
        'delta': {
            'recall': hybrid_metrics.get('recall@5', 0) - base_metrics.get('recall@5', 0),
            'mrr': hybrid_metrics.get('mrr', 0) - base_metrics.get('mrr', 0),
            'hits': hybrid_metrics.get('hits', 0) - base_metrics.get('hits', 0),
        },
        'main_chunks': main_chunks,
        'patch_chunks': patch_chunks,
        'patch_main_ratio': ratio,
        'fixed': fixed,
        'regressed': regressed,
        'unchanged_failure': unchanged_failure,
        'unchanged_success_count': len(unchanged_success),
        'movements': movements,
        'patch_decisions': decisions,
        'candidate_probe_results': candidate_probe,
        'selected_patch_candidates': selected,
    }
    _write_json(hybrid_dir / 'comparison.json', comparison)
    _write_json(hybrid_dir / 'patch_decisions.json', decisions)
    # Also update patch log with decision statuses for easier inspection.
    if decisions:
        _write_json(patch_dir / 'patch_log_evaluated.json', decisions)

    lines = ['# Main-only vs Main+Patch Comparison', '']
    lines += ['## Metrics', '']
    lines += [
        '| Metric | Main-only | Main+Patch | Delta |',
        '|---|---:|---:|---:|',
        f"| Recall@5 | {base_metrics.get('recall@5', 0):.4f} | {hybrid_metrics.get('recall@5', 0):.4f} | {comparison['delta']['recall']:+.4f} |",
        f"| MRR | {base_metrics.get('mrr', 0):.4f} | {hybrid_metrics.get('mrr', 0):.4f} | {comparison['delta']['mrr']:+.4f} |",
        f"| Hits | {base_metrics.get('hits', 0)} / {base_metrics.get('total', 0)} | {hybrid_metrics.get('hits', 0)} / {hybrid_metrics.get('total', 0)} | {comparison['delta']['hits']:+d} |",
        '',
        f'- main_chunks: {main_chunks}',
        f'- patch_chunks: {patch_chunks}',
        f'- patch/main ratio: {ratio:.2%}',
        '',
    ]
    lines += ['## Query Movement', '']
    lines += [
        f'- fixed: {fixed}',
        f'- regressed: {regressed}',
        f'- unchanged_failure: {unchanged_failure}',
        f'- unchanged_success_count: {len(unchanged_success)}',
        '',
        '| qid | movement | before rank | after rank | before coverage | after coverage |',
        '|---|---|---:|---:|---:|---:|',
    ]
    for m in movements:
        lines.append(f"| {m['qid']} | {m['movement']} | {m['before_rank']} | {m['after_rank']} | {m['before_best_coverage']} | {m['after_best_coverage']} |")
    lines += ['', '## Candidate Probe / Selected Patch', '']
    if selected:
        lines += ['| qid | selected patch | type | individual rank | text_len |', '|---|---|---|---:|---:|']
        for r in selected:
            lines.append(f"| {r['qid']} | `{r['patch_id']}` | `{r.get('candidate_type')}` | {r.get('rank')} | {r.get('text_len')} |")
    else:
        lines.append('No individually successful candidate patch found.')
    lines += ['', '## Patch Decisions', '']
    if not decisions:
        lines.append('No patch decisions generated.')
    else:
        lines += ['| patch_id | source qid | status | before rank | after rank | reason |', '|---|---|---|---:|---:|---|']
        for d in decisions:
            lines.append(f"| {d['patch_id']} | {d['qid']} | {d['status']} | {d['before_rank']} | {d['after_rank']} | {d['decision_reason']} |")
    lines += ['', '## Safety Interpretation', '']
    lines += [
        '- The main index was not modified.',
        '- Patch chunks were stored in a small side Patch Index.',
        '- A patch is accepted only when it fixes its source failure and no regression appears in the eval set.',
        '- Rejected patches remain auditable but should not be merged into the main index.',
    ]
    Path(hybrid_dir / 'comparison_report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return comparison
