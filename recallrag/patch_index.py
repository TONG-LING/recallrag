"""patch侧索引：生成候选 → probe验证 → 拼进主索引 → 对比fixed/regressed

主索引chunks.json始终不改，patch是旁路一层
"""

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
    #定位器查询到的局部窗口进行句子打分
    q=_tokens(query)
    if not q: return 0.0
    st=_tokens(sent)
    #召回率+长句偏向奖励值
    return len(q & st)/len(q) + min(len(st), 40)/400.0

def _top_relevant_sentences(query: str, text: str, limit: int = 4) -> list[str]:
    """从局部窗口里挑出和问题最相关的几句
    适配：contextual/local_proposition/local_summary三类patch
    切不出句子时退化成截断原文前500字符
    """
    sents=_sentences(text)
    if not sents:
        return [normalize_text(text)[:500]] if text else []
    ranked=sorted(enumerate(sents), key=lambda x: (_score_sentence(query,x[1]), -x[0]), reverse=True)
    #原文顺序返回，避免patch的文本顺序乱了
    selected=sorted([i for i,_ in ranked[:limit]])
    return [sents[i] for i in selected]

def _make_patch_text(candidate_type: str, qid: str, question: str, section_path: str, diagnosis: str, body: str) -> str:
    """拼patch最终要写进embedding的文本。

    防泄漏：qid/原question/diagnosis不能进patch text，只能放 metadata
    question只用来挑相关句，不会原文写进patch中去，防止"问题对问题"
    section_path来自源chunk可以留

    四种candidate_type：
    - adjacent_merge：邻居chunk原文直接合并,噪声很大
    - contextual：挑出的相关句原样拼接
    - local_proposition：相关句改成项目符号列表,embedded模型原因
    - local_summary：前几句压成一段摘要,高度压缩的zhaiyao
    """
    rel = _top_relevant_sentences(question, body, limit=4)
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
    """从 failure_diagnosis.json (patch_allowed)生成 patch 索引

    读diagnose输出的局部窗口，对每个patch_allowed的失败query固定生成
    4种表示，embed后写到patch_chunks.json/patch_vectors.json。
    主索引chunks.json始终不动。
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
        #过滤：如果诊断结果是不允许打补丁 (patch_allowed=False)，直接跳过
        if not d.get('patch_allowed'):
            continue
        # 提取出诊断定位到的“问题上下文窗口”所包含的所有 chunk ID
        ids = d.get('evidence', {}).get('candidate_window_chunk_ids') or d.get('evidence', {}).get('adjacent_chunk_ids') or []
        selected = [by_id[i] for i in ids if i in by_id]
        if not selected:
            continue
        # 排序：确保这些块按照文档物理顺序（从前到后）排列，防止拼出来的文本顺序错乱
        selected.sort(key=lambda c: (c['doc_id'], c['start_offset']))

        # 提取窗口的边界和元数据
        doc_id = selected[0]['doc_id']
        anchor_id = d.get('evidence', {}).get('anchor_chunk_id') or selected[len(selected)//2]['chunk_id']
        anchor = by_id.get(anchor_id, selected[len(selected)//2])
        section_path = anchor.get('section_path') or selected[0].get('section_path') or ''

        # 计算当前窗口在原文档里的物理跨度（起始偏移和结束偏移）
        start = min(c['start_offset'] for c in selected)
        end = max(c['end_offset'] for c in selected)
        # 合并窗口：用换行符连接这个窗口里所有的 chunks 文本，形成“大原材料段落”
        body = '\n'.join(c['text'] for c in selected)
        #开始生成四种patch的元数据
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
                # *** 记录这个补丁可以“替换/覆盖”主索引中的哪些原始 chunk ID
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
            #添加patch审计日志
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
    # 将生成的补丁数据和审计日志落盘保存
    _write_json(out_dir / 'patch_chunks.json', patch_chunks)
    _write_json(out_dir / 'patch_log.json', patch_log)
    #调用本地嵌入模型接口，把这些补丁文本全部转化为向量
    if patch_chunks:
        vectors = embed_lmstudio([c['text'] for c in patch_chunks], endpoint=endpoint, model=model, batch_size=batch_size)
    else:
        vectors = []
    # 保存独立的补丁向量文件和元数据文件  Qdrant
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
    """patch验证与混合检索的主流程。

    1.先 probe：每个patch单独加到主索引后，用源query测能不能修好（4选1）：
    再筛选：每题只留 probe成功且 coverage最高的一个候选
    2.再评估：选中patch拼到主索引后跑全量检索
    最后对比main-only baseline，统计fixed/regressed，给patch打 accepted/rejected
    （第二个评估主要是怕这个patch把除了自己query对应以外其他的query搞坏）
    """
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
    # 会遍历每一个失败 Query，对于它生成的 4 种补丁变体（直接合并、上下文、命题化、摘要），
    # 每次只将其中一个补丁加入主索引进行单点测试
    # 如果4选x的话，向量空间中距离极近，从而互相抢夺 Top-K 位置，也方便以后统计具体是哪种patch较多
    candidate_probe = probe_patch_candidates(
        main_chunks, main_vectors, patch_chunks, patch_vectors, questions,
        endpoint=endpoint, model=model, top_k=top_k, coverage_threshold=coverage_threshold,
    )
    selected_by_qid = _select_successful_patch_candidates(candidate_probe)
    selected_ids = {r['patch_id'] for r in selected_by_qid.values()}
    selected_pairs = [(c, v) for c, v in zip(patch_chunks, patch_vectors) if c.get('patch_id') in selected_ids]
    selected_patch_chunks = [c for c, _ in selected_pairs]
    selected_patch_vectors = [v for _, v in selected_pairs]

    # 第二次评估：检查某个patch上线后，会不会干扰其他query（除了自己对应的query）
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
    # 最终只有被接受的（accepted）补丁才会写入正式的 selected_* ,为了保证 query的"零回退"
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
    """逐个patch做shadow验证。

    每次只在主索引后面加一个patch，用源query检索，看Top-K coverage能不能
    修好这道题。不把同题多个候选一次性塞进去，避免互相抢排名。
    同题多个probe成功的候选，后续按coverage → rank → 文本长度 → 类型优先级择优。
    """
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
    return (
        -(row.get('best_topk_coverage') or 0.0),
        row.get('rank') or 999,
        row.get('text_len') or 0,
        priority.get(row.get('candidate_type'), 9),
    )

def _select_successful_patch_candidates(candidate_probe: list[dict]) -> dict[str, dict]:
    #
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
    """对比main-only和main+patch，输出fixed/regressed与patch决策。

    逐题比较检索成败变化（fixed/regressed/unchanged）。
    对每个patch打标签：
    - accepted：被选为最优候选，源query从失败变成功，且全局无regression
    - rejected：加了patch源query还是失败
    - candidate_not_selected：probe过但没被选上
    - needs_review：出现regression或改进不明确
    """
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