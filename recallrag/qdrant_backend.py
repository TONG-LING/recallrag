from __future__ import annotations
import hashlib, json, urllib.request, urllib.error, uuid
from pathlib import Path
from .embeddings import embed_lmstudio, require_equal_length, require_vector_dimensions
from .eval import (
    load_questions,
    coverage,
    relevance_score,
    is_relevant,
    build_ranked_result,
    first_relevant_rank,
    _top_row,
    _trace_row,
)
from .reranker import LocalCrossEncoderReranker

DEFAULT_URL = 'http://localhost:6333'
MAIN_COLLECTION = 'recallrag_main'
PATCH_COLLECTION = 'recallrag_patch'
PATCH_REPLACE_SCORE_MARGIN = 0.0

def _load_json(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))

def _write_json(p, obj):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')

def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def _artifact_hashes(root: Path, filenames: list[str]) -> dict[str, str]:
    hashes = {}
    for name in filenames:
        path = root / name
        if path.exists():
            hashes[name] = _sha256_file(path)
    return hashes

def _question_fingerprint(rows: list[dict]) -> str:
    compact = [
        {
            'qid': row['qid'],
            'question': row.get('question', ''),
            'gold_doc': row.get('gold_doc', ''),
            'gold_section': row.get('gold_section', ''),
        }
        for row in sorted(rows, key=lambda row: row['qid'])
    ]
    payload = json.dumps(compact, ensure_ascii=False, sort_keys=True).encode('utf-8')
    return hashlib.sha256(payload).hexdigest()

def _request(method: str, url: str, payload=None):
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method=method, headers={'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read().decode('utf-8')
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        detail = e.read().decode('utf-8', 'ignore')
        raise RuntimeError(f'{method} {url} -> HTTP {e.code}: {detail}') from e

def drop_collection(url: str, collection: str):
    try:
        _request('DELETE', f'{url}/collections/{collection}')
    except Exception:
        pass

def health(url: str = DEFAULT_URL):
    return _request('GET', f'{url}/collections')

def recreate_collection(url: str, collection: str, dim: int):
    drop_collection(url, collection)
    return _request('PUT', f'{url}/collections/{collection}', {
        'vectors': {'size': dim, 'distance': 'Cosine'}
    })

def _point_id(namespace: str, chunk_id: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, namespace + '::' + chunk_id))

def upsert_collection(url: str, collection: str, chunks: list[dict], vectors: list[list[float]], namespace: str):
    require_equal_length('chunks', chunks, 'vectors', vectors, f'upsert_collection({collection})')
    if not chunks:
        return {'upserted': 0, 'dim': 0}
    dim = require_vector_dimensions(vectors, f'upsert_collection({collection})')
    recreate_collection(url, collection, dim)
    points = []
    point_map = []
    for c, v in zip(chunks, vectors):
        pid = _point_id(namespace, c['chunk_id'])
        payload = {k: val for k, val in c.items() if k != 'text'}
        payload['text'] = c.get('text','')
        payload['text_preview'] = c.get('text','')[:240]
        points.append({'id': pid, 'vector': v, 'payload': payload})
        point_map.append({'point_id': pid, 'chunk_id': c['chunk_id'], 'collection': collection})
    for i in range(0, len(points), 64):
        _request('PUT', f'{url}/collections/{collection}/points?wait=true', {'points': points[i:i+64]})
    return {'upserted': len(points), 'dim': dim, 'point_map': point_map}

def _load_selected_patch_artifacts(patch_dir: Path):
    selected_chunks_path = patch_dir / 'selected_patch_chunks.json'
    selected_vectors_path = patch_dir / 'selected_patch_vectors.json'
    candidate_chunks_path = patch_dir / 'patch_chunks.json'
    candidate_vectors_path = patch_dir / 'patch_vectors.json'
    selected_ready = selected_chunks_path.exists() and selected_vectors_path.exists()
    selected_partial = selected_chunks_path.exists() ^ selected_vectors_path.exists()
    candidate_ready = candidate_chunks_path.exists() and candidate_vectors_path.exists()
    candidate_partial = candidate_chunks_path.exists() ^ candidate_vectors_path.exists()
    if selected_partial:
        raise RuntimeError('Selected patch artifacts are incomplete. Re-run eval-hybrid to rebuild selected_patch_chunks.json and selected_patch_vectors.json.')
    if selected_ready:
        return (
            _load_json(selected_chunks_path),
            _load_json(selected_vectors_path),
            'selected_patch_chunks.json',
        )
    if candidate_partial:
        raise RuntimeError('Candidate patch artifacts are incomplete. Re-run materialize-patches before building Qdrant.')
    if candidate_ready:
        raise RuntimeError('selected_patch_chunks.json is missing. Run eval-hybrid first; qdrant-build only loads selected patches into the online Patch Collection.')
    return [], [], 'no_patch_artifacts'

def build_qdrant_from_runs(
    main_index_dir: str | Path = 'runs/base',
    patch_dir: str | Path = 'runs/patches',
    url: str = DEFAULT_URL,
    main_collection: str = MAIN_COLLECTION,
    patch_collection: str = PATCH_COLLECTION,
    out_dir: str | Path = 'runs/qdrant',
):
    main_index_dir = Path(main_index_dir)
    patch_dir = Path(patch_dir)
    out_dir = Path(out_dir)
    main_chunks = _load_json(main_index_dir / 'chunks.json')
    main_vectors = _load_json(main_index_dir / 'vectors.json')
    patch_chunks, patch_vectors, patch_artifact_source = _load_selected_patch_artifacts(patch_dir)
    main = upsert_collection(url, main_collection, main_chunks, main_vectors, 'main')
    if patch_chunks:
        patch = upsert_collection(url, patch_collection, patch_chunks, patch_vectors, 'patch')
    else:
        drop_collection(url, patch_collection)
        patch = {'upserted': 0, 'point_map': []}
    meta = {
        'url': url,
        'main_collection': main_collection,
        'patch_collection': patch_collection,
        'main_upserted': main['upserted'],
        'patch_upserted': patch['upserted'],
        'dim': main.get('dim'),
        'main_index_dir': str(main_index_dir.resolve()),
        'patch_dir': str(patch_dir.resolve()),
        'main_artifact_hashes': _artifact_hashes(main_index_dir, ['chunks.json', 'vectors.json']),
        'patch_artifact_hashes': _artifact_hashes(patch_dir, ['selected_patch_chunks.json', 'selected_patch_vectors.json']),
        'patch_artifact_source': patch_artifact_source,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / 'qdrant_meta.json', meta)
    _write_json(out_dir / 'point_map.json', main.get('point_map', []) + patch.get('point_map', []))
    return meta

def search_collection(url: str, collection: str, vector: list[float], limit: int):
    res = _request('POST', f'{url}/collections/{collection}/points/search', {
        'vector': vector,
        'limit': limit,
        'with_payload': True,
        'with_vector': False,
    })
    return res.get('result', [])

def _to_result(point, rank: int, source_index: str):
    p = point.get('payload') or {}
    return {
        **p,
        'rank': rank,
        'score': float(point.get('score', 0.0)),
        'source_index': p.get('source_index', source_index),
        'point_id': point.get('id'),
    }

def _patch_can_replace_main(patch_row: dict, main_row: dict | None, score_margin: float = PATCH_REPLACE_SCORE_MARGIN) -> bool:
    if patch_row.get('active') is False:
        return False
    if not main_row:
        return False
    patch_doc = patch_row.get('doc_id')
    main_doc = main_row.get('doc_id')
    if patch_doc and main_doc and patch_doc != main_doc:
        return False
    return float(patch_row.get('score', 0.0)) + score_margin >= float(main_row.get('score', 0.0))

def merge_qdrant_results(main_points, patch_points, final_k: int):
    main_results = [_to_result(p, i, 'main') for i, p in enumerate(main_points, 1)]
    patch_results = [_to_result(p, i, 'patch') for i, p in enumerate(patch_points, 1)]
    results = main_results + patch_results
    main_by_chunk_id = {r.get('chunk_id'): r for r in main_results if r.get('chunk_id')}
    patch_replaces = set()
    for patch_row in sorted(patch_results, key=lambda x: x['score'], reverse=True):
        for replaced_chunk_id in patch_row.get('replaces') or []:
            if _patch_can_replace_main(patch_row, main_by_chunk_id.get(replaced_chunk_id)):
                patch_replaces.add(replaced_chunk_id)
    filtered = []
    seen = set()
    for r in sorted(results, key=lambda x: x['score'], reverse=True):
        cid = r.get('chunk_id')
        if r.get('source_index') == 'main' and cid in patch_replaces:
            continue
        if cid in seen:
            continue
        seen.add(cid)
        filtered.append(r)
    final = filtered[:final_k]
    for i, r in enumerate(final, 1):
        r['rank'] = i
    return final

def eval_qdrant_hybrid(
    questions_path: str | Path = 'case/eval/questions.jsonl',
    url: str = DEFAULT_URL,
    main_collection: str = MAIN_COLLECTION,
    patch_collection: str = PATCH_COLLECTION,
    endpoint: str = 'http://localhost:1234/v1/embeddings',
    model: str = 'bge-small-en-v1.5',
    main_k: int = 5,
    patch_k: int = 3,
    final_k: int = 5,
    coverage_threshold: float = 0.65,
    out_dir: str | Path = 'runs/qdrant',
):
    out_dir = Path(out_dir)
    questions = load_questions(questions_path)
    qvecs = embed_lmstudio([q['question'] for q in questions], endpoint=endpoint, model=model)
    require_equal_length('questions', questions, 'query_vectors', qvecs, 'eval_qdrant_hybrid')
    require_vector_dimensions(qvecs, 'eval_qdrant_hybrid.query_vectors') if qvecs else None
    results=[]; hits=0; mrr=0.0
    for q, qv in zip(questions, qvecs):
        main_points = search_collection(url, main_collection, qv, main_k)
        if patch_k > 0:
            try:
                patch_points = search_collection(url, patch_collection, qv, patch_k)
            except Exception:
                patch_points = []
        else:
            patch_points = []
        top = merge_qdrant_results(main_points, patch_points, final_k)
        result = build_ranked_result(q, top, top_k=final_k, coverage_threshold=coverage_threshold)
        success = result['success']
        hits += int(success)
        mrr += 1.0 / result['rank'] if result['rank'] else 0.0
        results.append(result)
    metrics = {
        'total': len(questions),
        f'recall@{final_k}': hits / len(questions) if questions else 0.0,
        'mrr': mrr / len(questions) if questions else 0.0,
        'hits': hits,
        'failed': len(questions)-hits,
        'main_k': main_k,
        'patch_k': patch_k,
        'final_k': final_k,
        'coverage_threshold': coverage_threshold,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / 'qdrant_retrieval_results.json', results)
    _write_json(out_dir / 'qdrant_metrics.json', metrics)
    _write_json(out_dir / 'qdrant_eval_meta.json', {
        'questions_path': str(Path(questions_path).resolve()),
        'question_count': len(questions),
        'question_fingerprint': _question_fingerprint(questions),
        'endpoint': endpoint,
        'model': model,
        'main_k': main_k,
        'patch_k': patch_k,
        'final_k': final_k,
        'coverage_threshold': coverage_threshold,
    })
    write_qdrant_report(out_dir / 'qdrant_eval_report.md', metrics, results, main_collection, patch_collection)
    return results, metrics

def eval_qdrant_hybrid_rerank(
    questions_path: str | Path = 'case/eval/questions.jsonl',
    url: str = DEFAULT_URL,
    main_collection: str = MAIN_COLLECTION,
    patch_collection: str = PATCH_COLLECTION,
    endpoint: str = 'http://localhost:1234/v1/embeddings',
    model: str = 'bge-small-en-v1.5',
    main_k: int = 10,
    patch_k: int = 5,
    final_k: int = 5,
    coverage_threshold: float = 0.65,
    reranker: LocalCrossEncoderReranker | None = None,
    reranker_model_path: str | None = None,
    reranker_device: str | None = None,
    reranker_batch_size: int = 8,
    reranker_max_length: int = 512,
    reranker_use_fp16: bool = True,
    out_dir: str | Path = 'runs/qdrant_rerank',
):
    if final_k > main_k + patch_k:
        raise RuntimeError(
            f'eval_qdrant_hybrid_rerank: final_k {final_k} must be <= main_k + patch_k {main_k + patch_k}.'
        )
    out_dir = Path(out_dir)
    questions = load_questions(questions_path)
    qvecs = embed_lmstudio([q['question'] for q in questions], endpoint=endpoint, model=model)
    require_equal_length('questions', questions, 'query_vectors', qvecs, 'eval_qdrant_hybrid_rerank')
    require_vector_dimensions(qvecs, 'eval_qdrant_hybrid_rerank.query_vectors') if qvecs else None
    reranker = reranker or LocalCrossEncoderReranker(
        model_name_or_path=reranker_model_path,
        device=reranker_device,
        batch_size=reranker_batch_size,
        max_length=reranker_max_length,
        use_fp16=reranker_use_fp16,
    )
    results = []
    dense_rr = 0.0
    rerank_rr = 0.0
    dense_hits = 0
    rerank_hits = 0
    rerank_fixed = 0
    rerank_improved = 0
    merged_limit = max(final_k, main_k + patch_k)
    for q, qv in zip(questions, qvecs):
        main_points = search_collection(url, main_collection, qv, main_k)
        if patch_k > 0:
            try:
                patch_points = search_collection(url, patch_collection, qv, patch_k)
            except Exception:
                patch_points = []
        else:
            patch_points = []
        merged_candidates = merge_qdrant_results(main_points, patch_points, merged_limit)
        dense_success_rank = first_relevant_rank(q, merged_candidates[:final_k], coverage_threshold)
        dense_candidate_rank = first_relevant_rank(q, merged_candidates, coverage_threshold)
        reranker_candidates = []
        for dense_rank, row in enumerate(merged_candidates, 1):
            reranker_candidates.append({
                **row,
                'dense_rank_before_rerank': dense_rank,
                'dense_score': float(row.get('score', 0.0)),
            })
        reranked_rows = reranker.rerank(q['question'], reranker_candidates)
        result = build_ranked_result(q, reranked_rows, top_k=final_k, coverage_threshold=coverage_threshold)
        dense_best_topk_coverage = 0.0
        for row in merged_candidates[:final_k]:
            dense_best_topk_coverage = max(dense_best_topk_coverage, relevance_score(q, row))
        success_before = dense_success_rank is not None
        success_after = result['success']
        fixed = (not success_before) and success_after
        improved = fixed or (
            dense_candidate_rank is not None
            and result['rank'] is not None
            and result['rank'] < dense_candidate_rank
        )
        dense_hits += int(success_before)
        rerank_hits += int(success_after)
        dense_rr += 1.0 / dense_success_rank if dense_success_rank else 0.0
        rerank_rr += 1.0 / result['rank'] if result['rank'] else 0.0
        rerank_fixed += int(fixed)
        rerank_improved += int(improved)
        result.update({
            'success_before_rerank': success_before,
            'rank_before_rerank': dense_success_rank,
            'first_relevant_candidate_rank_before_rerank': dense_candidate_rank,
            'best_topk_coverage_before_rerank': round(dense_best_topk_coverage, 3),
            'rerank_candidate_k': len(merged_candidates),
            'rerank_fixed': fixed,
            'rerank_improved': improved,
            'top_k_before_rerank': [_top_row(q, row, i) for i, row in enumerate(merged_candidates[:final_k], 1)],
            'top_n_trace': [_trace_row(row, i) for i, row in enumerate(merged_candidates[:30], 1)],
            'top_n_trace_after_rerank': [_trace_row(row, i) for i, row in enumerate(reranked_rows[:30], 1)],
        })
        results.append(result)
    metrics = {
        'total': len(questions),
        f'dense_recall@{final_k}': dense_hits / len(questions) if questions else 0.0,
        f'recall@{final_k}': rerank_hits / len(questions) if questions else 0.0,
        'dense_mrr': dense_rr / len(questions) if questions else 0.0,
        'mrr': rerank_rr / len(questions) if questions else 0.0,
        'dense_hits_before_rerank': dense_hits,
        'hits': rerank_hits,
        'failed': len(questions) - rerank_hits,
        'rerank_fixed': rerank_fixed,
        'rerank_improved': rerank_improved,
        'main_k': main_k,
        'patch_k': patch_k,
        'final_k': final_k,
        'coverage_threshold': coverage_threshold,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / 'qdrant_retrieval_results.json', results)
    _write_json(out_dir / 'qdrant_metrics.json', metrics)
    _write_json(out_dir / 'qdrant_eval_meta.json', {
        'questions_path': str(Path(questions_path).resolve()),
        'question_count': len(questions),
        'question_fingerprint': _question_fingerprint(questions),
        'endpoint': endpoint,
        'model': model,
        'main_k': main_k,
        'patch_k': patch_k,
        'final_k': final_k,
        'coverage_threshold': coverage_threshold,
        'reranker_model_path': reranker.model_name_or_path,
        'reranker_device': reranker.device,
        'reranker_batch_size': reranker.batch_size,
        'reranker_max_length': reranker.max_length,
    })
    write_qdrant_rerank_report(out_dir / 'qdrant_eval_report.md', metrics, results, main_collection, patch_collection)
    return results, metrics

def write_qdrant_report(path: str | Path, metrics: dict, results: list[dict], main_collection: str, patch_collection: str):
    lines = ['# Qdrant Main+Patch Retrieval Report', '']
    lines += [f'- main_collection: `{main_collection}`', f'- patch_collection: `{patch_collection}`', '']
    lines += ['## Metrics', '']
    for k,v in metrics.items():
        lines.append(f'- **{k}**: {v:.4f}' if isinstance(v,float) else f'- **{k}**: {v}')
    lines += ['', '## Query Summary', '', '| qid | success | rank | best coverage | top sources |', '|---|---:|---:|---:|---|']
    for r in results:
        sources = ','.join(t['source_index'] for t in r['top_k'][:5])
        lines.append(f"| {r['qid']} | {r['success']} | {r['rank']} | {r['best_topk_coverage']} | {sources} |")
    lines += ['', '## Failed Queries', '']
    failed = [r for r in results if not r['success']]
    if not failed:
        lines.append('No failed queries.')
    for r in failed:
        lines += [f"### {r['qid']} — {r['gold_failure_type']}", '', f"- question: {r['question']}", f"- gold: `{r['gold_doc']} > {r['gold_section']}`", '- top results:']
        for t in r['top_k']:
            lines.append(f"  - rank {t['rank']}: `{t['chunk_id']}` source={t['source_index']} score={t['score']} cov={t['coverage']}")
        lines.append('')
    Path(path).write_text('\n'.join(lines)+'\n', encoding='utf-8')

def write_qdrant_rerank_report(path: str | Path, metrics: dict, results: list[dict], main_collection: str, patch_collection: str):
    lines = ['# Qdrant Main+Patch -> Rerank Report', '']
    lines += [
        f'- main_collection: `{main_collection}`',
        f'- patch_collection: `{patch_collection}`',
        '',
        '## Metrics',
        '',
    ]
    for k, v in metrics.items():
        lines.append(f'- **{k}**: {v:.4f}' if isinstance(v, float) else f'- **{k}**: {v}')
    lines += ['', '## Fixed By Rerank', '']
    fixed = [row for row in results if row.get('rerank_fixed')]
    if not fixed:
        lines.append('No query was fixed by reranking.')
    for row in fixed:
        lines += [
            f"### {row['qid']} — {row['gold_failure_type']}",
            '',
            f"- question: {row['question']}",
            f"- before rank: {row.get('rank_before_rerank')}",
            f"- after rank: {row.get('rank')}",
            f"- before best_topk_coverage: {row.get('best_topk_coverage_before_rerank')}",
            f"- after best_topk_coverage: {row.get('best_topk_coverage')}",
            '- top results after rerank:',
        ]
        for top in row['top_k']:
            lines.append(
                f"  - rank {top['rank']}: `{top['chunk_id']}` source={top.get('source_index')} "
                f"rerank_score={top.get('rerank_score', top['score'])} dense_rank={top.get('dense_rank_before_rerank')} "
                f"cov={top['coverage']}"
            )
        lines.append('')
    lines += ['', '## All Query Summary', '', '| qid | success before | success after | rank before | rank after | rerank fixed |', '|---|---:|---:|---:|---:|---:|']
    for row in results:
        lines.append(
            f"| {row['qid']} | {row.get('success_before_rerank')} | {row['success']} | "
            f"{row.get('rank_before_rerank')} | {row['rank']} | {row.get('rerank_fixed')} |"
        )
    Path(path).write_text('\n'.join(lines) + '\n', encoding='utf-8')


def compare_qdrant_runs(main_only_dir: str | Path, main_patch_dir: str | Path, out_path: str | Path = 'runs/qdrant/qdrant_comparison_report.md'):
    main_only_dir = Path(main_only_dir)
    main_patch_dir = Path(main_patch_dir)
    base_metrics = _load_json(main_only_dir / 'qdrant_metrics.json')
    patch_metrics = _load_json(main_patch_dir / 'qdrant_metrics.json')
    base_results = {r['qid']: r for r in _load_json(main_only_dir / 'qdrant_retrieval_results.json')}
    patch_results = {r['qid']: r for r in _load_json(main_patch_dir / 'qdrant_retrieval_results.json')}
    fixed=[]; regressed=[]; unchanged_failure=[]; unchanged_success=[]; rows=[]
    for qid,b in base_results.items():
        h=patch_results[qid]
        if (not b['success']) and h['success']:
            movement='fixed'; fixed.append(qid)
        elif b['success'] and not h['success']:
            movement='regressed'; regressed.append(qid)
        elif not b['success'] and not h['success']:
            movement='unchanged_failure'; unchanged_failure.append(qid)
        else:
            movement='unchanged_success'; unchanged_success.append(qid)
        rows.append({
            'qid': qid, 'movement': movement,
            'before_rank': b['rank'], 'after_rank': h['rank'],
            'before_cov': b['best_topk_coverage'], 'after_cov': h['best_topk_coverage'],
            'after_sources': ','.join(t['source_index'] for t in h['top_k'][:5]),
        })
    comparison = {
        'main_only': base_metrics,
        'main_plus_patch': patch_metrics,
        'delta': {
            'recall': patch_metrics.get('recall@5', 0) - base_metrics.get('recall@5', 0),
            'mrr': patch_metrics.get('mrr', 0) - base_metrics.get('mrr', 0),
            'hits': patch_metrics.get('hits', 0) - base_metrics.get('hits', 0),
        },
        'fixed': fixed,
        'regressed': regressed,
        'unchanged_failure': unchanged_failure,
        'unchanged_success_count': len(unchanged_success),
        'rows': rows,
    }
    out_path = Path(out_path)
    _write_json(out_path.with_suffix('.json'), comparison)
    lines = ['# Qdrant Main-only vs Main+Patch Comparison', '']
    lines += ['## Metrics', '', '| Metric | Qdrant Main-only | Qdrant Main+Patch | Delta |', '|---|---:|---:|---:|']
    lines.append(f"| Recall@5 | {base_metrics.get('recall@5',0):.4f} | {patch_metrics.get('recall@5',0):.4f} | {comparison['delta']['recall']:+.4f} |")
    lines.append(f"| MRR | {base_metrics.get('mrr',0):.4f} | {patch_metrics.get('mrr',0):.4f} | {comparison['delta']['mrr']:+.4f} |")
    lines.append(f"| Hits | {base_metrics.get('hits',0)} / {base_metrics.get('total',0)} | {patch_metrics.get('hits',0)} / {patch_metrics.get('total',0)} | {comparison['delta']['hits']:+d} |")
    lines += ['', '## Query Movement', '', f'- fixed: {fixed}', f'- regressed: {regressed}', f'- unchanged_failure: {unchanged_failure}', f'- unchanged_success_count: {len(unchanged_success)}', '']
    lines += ['| qid | movement | before rank | after rank | before cov | after cov | after sources |', '|---|---|---:|---:|---:|---:|---|']
    for r in rows:
        lines.append(f"| {r['qid']} | {r['movement']} | {r['before_rank']} | {r['after_rank']} | {r['before_cov']} | {r['after_cov']} | {r['after_sources']} |")
    lines += ['', '## Production-like interpretation', '', '- `recallrag_main` is the stable main collection.', '- `recallrag_patch` is a small side collection for shadow validation.', '- Main+patch improves retrieval without deleting or overwriting main points.', '- Regressions are explicitly reported before any patch is considered for merge.']
    out_path.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    return comparison
