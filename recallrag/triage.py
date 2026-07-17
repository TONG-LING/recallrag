from __future__ import annotations
import json
from pathlib import Path
from .qdrant_backend import _artifact_hashes, _question_fingerprint

def _load_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def _write_json(path: str | Path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')

def _load_validated_qdrant_results(
    base_dir: Path,
    base_results: dict[str, dict],
    qdrant_dir: str | Path | None,
):
    if not qdrant_dir:
        return {}
    qdrant_dir = Path(qdrant_dir)
    results_path = qdrant_dir / 'qdrant_retrieval_results.json'
    if not results_path.exists():
        return {}
    meta_path = qdrant_dir / 'qdrant_meta.json'
    eval_meta_path = qdrant_dir / 'qdrant_eval_meta.json'
    if not meta_path.exists() or not eval_meta_path.exists():
        raise RuntimeError(
            'Explicit qdrant_dir contains qdrant_retrieval_results.json but no provenance metadata. '
            'Re-run qdrant-build and qdrant-eval, or omit --qdrant-dir.'
        )
    meta = _load_json(meta_path)
    eval_meta = _load_json(eval_meta_path)
    current_main_hashes = _artifact_hashes(base_dir, ['chunks.json', 'vectors.json'])
    if meta.get('main_artifact_hashes') != current_main_hashes:
        raise RuntimeError(
            'Qdrant results were not built from the current runs/base chunks.json and vectors.json. '
            'Re-run qdrant-build and qdrant-eval, or omit --qdrant-dir.'
        )
    patch_source = meta.get('patch_artifact_source')
    recorded_patch_hashes = meta.get('patch_artifact_hashes') or {}
    if patch_source and patch_source != 'no_patch_artifacts':
        patch_dir_value = meta.get('patch_dir')
        if not patch_dir_value:
            raise RuntimeError('Qdrant metadata is missing patch_dir provenance.')
        patch_dir = Path(patch_dir_value)
        current_patch_hashes = _artifact_hashes(patch_dir, ['selected_patch_chunks.json', 'selected_patch_vectors.json'])
        if recorded_patch_hashes != current_patch_hashes:
            raise RuntimeError(
                'Qdrant results were not built from the current selected patch artifacts. '
                'Re-run qdrant-build and qdrant-eval, or omit --qdrant-dir.'
            )
    elif recorded_patch_hashes:
        raise RuntimeError('Qdrant metadata is inconsistent: no patch artifacts expected, but patch hashes were recorded.')

    base_rows = list(base_results.values())
    expected_fingerprint = _question_fingerprint(base_rows)
    if eval_meta.get('question_fingerprint') != expected_fingerprint:
        raise RuntimeError(
            'Qdrant eval metadata does not match the current query set in runs/base. '
            'Re-run qdrant-eval on the current benchmark, or omit --qdrant-dir.'
        )

    qdrant_results = {r['qid']: r for r in _load_json(results_path)}
    if set(qdrant_results) != set(base_results):
        raise RuntimeError(
            'Qdrant retrieval results qid set does not match the current runs/base retrieval results.'
        )
    for qid, qdrant_row in qdrant_results.items():
        base_row = base_results[qid]
        for field in ('question', 'gold_doc', 'gold_section'):
            if qdrant_row.get(field, '') != base_row.get(field, ''):
                raise RuntimeError(
                    f'Qdrant retrieval results mismatch current runs/base on {qid} field `{field}`.'
                )
    return qdrant_results

def final_triage(
    base_dir: str | Path = 'runs/base',
    patch_eval_dir: str | Path = 'runs/hybrid',
    bm25_dir: str | Path = 'runs/hybrid_bm25',
    qdrant_dir: str | Path | None = None,
    out_dir: str | Path = 'runs/triage',
):
    base_dir = Path(base_dir)
    patch_eval_dir = Path(patch_eval_dir)
    bm25_dir = Path(bm25_dir)
    out_dir = Path(out_dir)

    diagnoses = {d['qid']: d for d in _load_json(base_dir / 'failure_diagnosis.json')}
    base_results = {r['qid']: r for r in _load_json(base_dir / 'retrieval_results.json')}
    patch_results = {r['qid']: r for r in _load_json(patch_eval_dir / 'retrieval_results.json')} if (patch_eval_dir / 'retrieval_results.json').exists() else {}
    patch_decision_rows = _load_json(patch_eval_dir / 'patch_decisions.json') if (patch_eval_dir / 'patch_decisions.json').exists() else []
    patch_decisions_by_qid: dict[str, list[dict]] = {}
    for row in patch_decision_rows:
        patch_decisions_by_qid.setdefault(row.get('qid'), []).append(row)
    bm25_results = _load_json(bm25_dir / 'hybrid_bm25_results.json') if (bm25_dir / 'hybrid_bm25_results.json').exists() else {}
    qdrant_results = _load_validated_qdrant_results(base_dir, base_results, qdrant_dir)

    rows = []
    for qid, d in diagnoses.items():
        base = base_results.get(qid, {})
        patch = patch_results.get(qid, {})
        qdrant = qdrant_results.get(qid, {})
        bm25 = (bm25_results.get('bm25') or [])
        hybrid = (bm25_results.get('dense_bm25') or [])
        bm25_by_id = {r['qid']: r for r in bm25}
        hybrid_by_id = {r['qid']: r for r in hybrid}
        bm25_fixed = (not base.get('success')) and bm25_by_id.get(qid, {}).get('success', False)
        dense_bm25_fixed = (not base.get('success')) and hybrid_by_id.get(qid, {}).get('success', False)
        patch_fixed = (not base.get('success')) and patch.get('success', False)
        qdrant_patch_fixed = (not base.get('success')) and qdrant.get('success', False)
        qid_patch_decisions = patch_decisions_by_qid.get(qid, [])
        accepted_patch_ids = [p.get('patch_id') for p in qid_patch_decisions if p.get('status') == 'accepted']
        accepted_candidate_types = [p.get('candidate_type') for p in qid_patch_decisions if p.get('status') == 'accepted']
        patch_approved = bool(accepted_patch_ids)

        final_family = d['failure_family']
        final_type = d['diagnosed_failure_type']
        final_action = d['recommendation']
        patch_allowed = d['patch_allowed']
        decision = 'needs_review'
        rationale = []

        if bm25_fixed or dense_bm25_fixed:
            final_family = 'retrieval_strategy_sensitive'
            final_type = 'dense_retrieval_miss_fixed_by_bm25_or_hybrid'
            final_action = 'prefer_hybrid_retrieval_or_mark_patch_needs_review'
            patch_allowed = False
            decision = 'needs_review'
            rationale.append('BM25/dense+BM25 fixes this dense failure, so do not claim it is purely chunking-related.')
        elif (patch_fixed or qdrant_patch_fixed) and not patch_approved:
            final_family = 'patch_validation_inconclusive'
            final_type = 'patch_improved_retrieval_but_not_approved_for_shadow_index'
            final_action = 'needs_review_before_shadow_index_activation'
            patch_allowed = False
            decision = 'needs_review'
            rationale.append('Patch retrieval improved the source query, but patch_decisions did not approve any candidate for the shadow index.')
        elif patch_fixed and patch_approved and not (bm25_fixed or dense_bm25_fixed):
            final_family = 'chunking_failure'
            final_type = d['diagnosed_failure_type']
            final_action = 'accept_patch_for_shadow_index; optional later merge'
            patch_allowed = True
            decision = 'accepted_patch_candidate'
            rationale.append('Patch retrieval fixes the source query and BM25/hybrid does not explain it away.')
        elif qdrant_patch_fixed and patch_approved and not (bm25_fixed or dense_bm25_fixed):
            final_family = 'chunking_failure'
            final_action = 'accept_patch_candidate_in_qdrant_shadow_validation'
            patch_allowed = True
            decision = 'accepted_patch_candidate'
            rationale.append('Qdrant main+patch fixes the source query without BM25/hybrid being the primary explanation.')
        elif not patch_fixed and not qdrant_patch_fixed and not (bm25_fixed or dense_bm25_fixed):
            final_family = 'unresolved_failure'
            final_type = 'unresolved_after_patch_and_hybrid'
            final_action = 'manual_review_or_new_strategy'
            patch_allowed = False
            decision = 'manual_review'
            rationale.append('Neither patch nor BM25/hybrid fixed the failure.')

        if qid_patch_decisions:
            rationale.append(f"JSON patch decisions: {len(qid_patch_decisions)} candidates; accepted patch ids={accepted_patch_ids}; accepted candidate types={accepted_candidate_types}.")
        if qdrant_patch_fixed:
            rationale.append('Qdrant main+patch retrieval fixes the query.')
        if bm25_fixed:
            rationale.append('BM25 fixes the dense failure.')
        if dense_bm25_fixed:
            rationale.append('Dense+BM25 hybrid fixes the dense failure.')

        rows.append({
            'qid': qid,
            'question': d['question'],
            'gold_doc': d['gold_doc'],
            'gold_section': d.get('gold_section',''),
            'raw_diagnosis': d['diagnosed_failure_type'],
            'raw_family': d['failure_family'],
            'final_family': final_family,
            'final_type': final_type,
            'final_decision': decision,
            'patch_allowed_final': patch_allowed,
            'recommended_action': final_action,
            'signals': {
                'dense_failed': not base.get('success', True),
                'json_patch_fixed': patch_fixed,
                'qdrant_patch_fixed': qdrant_patch_fixed,
                'bm25_fixed': bm25_fixed,
                'dense_bm25_fixed': dense_bm25_fixed,
                'base_best_coverage': base.get('best_topk_coverage'),
                'patch_best_coverage': patch.get('best_topk_coverage'),
                'qdrant_best_coverage': qdrant.get('best_topk_coverage'),
            },
            'rationale': rationale,
        })

    summary = {
        'total_dense_failures': len(rows),
        'accepted_patch_candidates': sum(1 for r in rows if r['final_decision'] == 'accepted_patch_candidate'),
        'retrieval_strategy_sensitive': sum(1 for r in rows if r['final_family'] == 'retrieval_strategy_sensitive'),
        'manual_review': sum(1 for r in rows if r['final_decision'] == 'manual_review'),
        'rows': rows,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / 'final_triage.json', summary)
    write_triage_report(out_dir / 'final_triage_report.md', summary)
    return summary

def write_triage_report(path: str | Path, summary: dict):
    lines = ['# Final Failure Triage Report', '']
    lines += ['## Summary', '']
    for k in ['total_dense_failures','accepted_patch_candidates','retrieval_strategy_sensitive','manual_review']:
        lines.append(f'- **{k}**: {summary[k]}')
    lines += ['', '## Decision Table', '', '| qid | raw diagnosis | final family | final decision | recommended action |', '|---|---|---|---|---|']
    for r in summary['rows']:
        lines.append(f"| {r['qid']} | {r['raw_diagnosis']} | {r['final_family']} | {r['final_decision']} | `{r['recommended_action']}` |")
    lines += ['', '## Detailed Cases', '']
    for r in summary['rows']:
        lines += [f"### {r['qid']} — {r['final_family']}", '', f"- question: {r['question']}", f"- gold: `{r['gold_doc']} > {r['gold_section']}`", f"- raw diagnosis: `{r['raw_family']} / {r['raw_diagnosis']}`", f"- final decision: `{r['final_decision']}`", f"- patch_allowed_final: `{r['patch_allowed_final']}`", f"- recommended_action: `{r['recommended_action']}`", '', 'Signals:', '']
        for k,v in r['signals'].items():
            lines.append(f'- {k}: `{v}`')
        lines += ['', 'Rationale:', '']
        for item in r['rationale']:
            lines.append(f'- {item}')
        lines.append('')
    lines += ['## Production Rule', '', '> A dense retrieval failure is not automatically a chunking failure. If BM25 or dense+BM25 fixes it, mark it as retrieval-strategy-sensitive / needs_review. Only clean chunking failures should become accepted patch candidates.']
    Path(path).write_text('\n'.join(lines)+'\n', encoding='utf-8')
