from __future__ import annotations
import json, re
from pathlib import Path
from .embeddings import dot, embed_lmstudio, require_equal_length, require_vector_dimensions
from .reranker import LocalCrossEncoderReranker
from .text_utils import mixed_tokens

def load_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def load_questions(path: str | Path) -> list[dict]:
    return [json.loads(line) for line in Path(path).read_text(encoding='utf-8').splitlines() if line.strip()]

def words(s: str) -> list[str]:
    return mixed_tokens(s)

def coverage(gold_span: str, chunk_text: str) -> float:
    """计算标准答案片段被某个 chunk 覆盖了多少比例。
    0.65的阈值
    """
    gw = words(gold_span)  # text_utils.mixed_tokens
    if not gw:
        return 0.0
    chunk_tokens = set(words(chunk_text))
    hit = sum(1 for w in gw if w in chunk_tokens)  # gold 里有多少 token 出现在 chunk 中
    return hit / len(gw)  # chunk的hit长度/gold的长度

def question_eval_mode(q: dict) -> str:
    """决定这道题按什么标准判成功

    - 'span'：必须看 gold_span 被 chunk 覆盖多少（RecallRAG当前的口径）
    - 'doc' ：只要 doc_id 对上就算相关（用于没有 gold_span 的题）
    """
    return q.get('eval_mode') or ('span' if q.get('gold_span') else 'doc')

def relevance_score(q: dict, chunk: dict) -> float:
    """chuck的相关分数
    - relevance_score return 0.0 ~ 1.0
    - is_relevant return bool
    """
    if chunk.get('doc_id') != q.get('gold_doc'):
        return 0.0
    if question_eval_mode(q) == 'doc':
        return 1.0
    return coverage(q.get('gold_span', ''), chunk.get('text', ''))

def is_relevant(q: dict, chunk: dict, threshold: float) -> bool:
    """判断一个 chunk 是否算检索成功。
    span 模式，当前默认：
    1. chunk.doc_id == question.gold_doc
    2. coverage(gold_span, chunk.text) >= threshold
    """
    if chunk.get('doc_id') != q.get('gold_doc'):
        return False
    if question_eval_mode(q) == 'doc':
        return True
    return coverage(q.get('gold_span', ''), chunk.get('text', '')) >= threshold

def retrieve(query_vec: list[float], chunks: list[dict], vectors: list[list[float]], top_k: int) -> list[dict]:
    """向量检索：query和chunk点积，按分数降序取 Top-k。
    - query_vec: 问题的 embedding 向量
    - chunks: 候选 chunk 元数据列表（chunk_id, doc_id, text, ...）
    - vectors: 与 chunks 一一对应的 embedding 向量
    - top_k
      sorces和chuck的列表，还未经过coverage判断
    """
    require_equal_length('chunks', chunks, 'vectors', vectors, 'retrieve')  # 防止 chunk 和向量数量对不上
    if vectors:
        require_vector_dimensions(vectors, 'retrieve.candidate_vectors', expected_dim=len(query_vec))
    scored = []
    for c, v in zip(chunks, vectors):
        scored.append({**c, 'score': dot(query_vec, v)})  # cosine相似度的未归一化形式
    scored.sort(key=lambda x: x['score'], reverse=True)
    return scored[:top_k]  #top_k 条

def _round_score(value) -> float:
    return round(float(value), 6)

def _trace_row(row: dict, rank: int) -> dict:
    payload = {
        'rank': rank,
        'chunk_id': row.get('chunk_id'),
        'doc_id': row.get('doc_id'),
        'section_path': row.get('section_path',''),
        'score': _round_score(row.get('score', 0.0)),
        'text_preview': (row.get('text') or '')[:360].replace('\n',' '),
    }
    if row.get('source_index'):
        payload['source_index'] = row.get('source_index')
    if 'dense_rank_before_rerank' in row:
        payload['dense_rank_before_rerank'] = row.get('dense_rank_before_rerank')
    if 'dense_score' in row:
        payload['dense_score'] = _round_score(row.get('dense_score', 0.0))
    if 'rerank_score' in row:
        payload['rerank_score'] = _round_score(row.get('rerank_score', 0.0))
    return payload

def _top_row(q: dict, row: dict, rank: int) -> dict:
    payload = {
        'rank': rank,
        'chunk_id': row.get('chunk_id'),
        'doc_id': row.get('doc_id'),
        'section_path': row.get('section_path',''),
        'score': _round_score(row.get('score', 0.0)),
        'coverage': round(relevance_score(q, row), 3),
        'text_preview': (row.get('text') or '')[:220].replace('\n',' '),
    }
    if row.get('source_index'):
        payload['source_index'] = row.get('source_index')
    if 'candidate_type' in row:
        payload['candidate_type'] = row.get('candidate_type')
    if 'dense_rank_before_rerank' in row:
        payload['dense_rank_before_rerank'] = row.get('dense_rank_before_rerank')
    if 'dense_score' in row:
        payload['dense_score'] = _round_score(row.get('dense_score', 0.0))
    if 'rerank_score' in row:
        payload['rerank_score'] = _round_score(row.get('rerank_score', 0.0))
    return payload

def first_relevant_rank(q: dict, ranked_rows: list[dict], threshold: float) -> int | None:
    for i, row in enumerate(ranked_rows, 1):
        if is_relevant(q, row, threshold):
            return i
    return None

def build_ranked_result(
    q: dict,
    ranked_rows: list[dict],
    top_k: int,
    coverage_threshold: float,
    trace_rows: list[dict] | None = None,
    trace_limit: int = 30,
) -> dict:
    """排序列表->单道题的评测结果
    输入 ranked_rows 应该已经排好序（dense 或 rerank 之后都行）
    - rank / success：
         Top-5 第一个 is_relevant=True 的块排第几,recall@5 和 MRR 的主口径。
    - first_gold_rank：
        不限于 Top-5，但上限取决于传入列表长度,第一个 doc_id==gold_doc,不要求 coverage够
        文档找到了，但证据不完整
    - best_evidence_rank：
        同上，gold_doc 中 coverage 最高的那块排第几，完整块在候选池，但是未在top-k
    - top_n_trace：
         diagnose.py 读取 top_n_trace 扩大top范围来形成 trace
        保存前top-30，用于后续重排和分析（非完整数据，截断的）
    """
    trace_rows = trace_rows or ranked_rows  # 默认 trace 和 ranked_rows 相同；rerank 时可分开传
    rank = None  # Top-k 内第一个够完整证据的排名
    best_cov = 0.0  # Top-k 内出现过的最高 coverage
    first_gold_rank = None  # 全排序里第一次出现 gold_doc 的排名
    best_evidence_rank = None  # 全排序里 gold_doc 中 coverage 最高的排名
    best_evidence_coverage = 0.0
    best_evidence_chunk_id = None
    # --- 第一遍：只扫 Top-k，算主评测指标 rank / success ---
    for i, row in enumerate(ranked_rows[:top_k], 1):
        cov = relevance_score(q, row)
        best_cov = max(best_cov, cov)
        if is_relevant(q, row, coverage_threshold) and rank is None:
            rank = i  # 只取第一个成功的位置用于MRR
    # --- 第二遍：扫全排序，算诊断指标（文档命中 / 最佳证据在哪） ---
    for i, row in enumerate(ranked_rows, 1):
        if row.get('doc_id') == q.get('gold_doc'):
            cov = relevance_score(q, row)
            if first_gold_rank is None:
                first_gold_rank = i  # 第一次碰到正确文档的位置
            if cov > best_evidence_coverage:
                best_evidence_coverage = cov
                best_evidence_rank = i  # coverage 最高的那块在哪（可能是完整块，也可能只是半截）
                best_evidence_chunk_id = row.get('chunk_id')
    return {
        'qid': q['qid'],
        'question': q['question'],
        'gold_doc': q['gold_doc'],
        'gold_section': q.get('gold_section',''),
        'gold_failure_type': q.get('gold_failure_type',''),
        'success': rank is not None,
        'rank': rank,
        'best_topk_coverage': round(best_cov, 3),
        'best_gold_rank_hint': first_gold_rank,
        'first_gold_rank': first_gold_rank,
        'best_evidence_rank': best_evidence_rank,
        'best_evidence_coverage': round(best_evidence_coverage, 3),
        'best_evidence_chunk_id': best_evidence_chunk_id,
        'top_n_trace': [_trace_row(row, i) for i, row in enumerate(trace_rows[:trace_limit], 1)],
        'top_k': [_top_row(q, row, i) for i, row in enumerate(ranked_rows[:top_k], 1)],
    }

def evaluate(
    chunks: list[dict],
    vectors: list[list[float]],
    questions: list[dict],
    endpoint: str,
    model: str,
    top_k: int = 5,
    coverage_threshold: float = 0.65,
) -> tuple[list[dict], dict]:
    """向量检索评测
    整体流程（每道题）：
    1. 把 question 编成向量 qvec
    2. retrieve 对全库 chunk 打分排序
    3. build_ranked_result 看 Top-k 里有没有够完整的证据
    4. 汇总 recall@k 和 MRR
    返回：
    - results: 每道题一条 dict（含 top_k、top_n_trace、rank、success 等）
    - metrics: 全局指标
    """
    require_equal_length('chunks', chunks, 'vectors', vectors, 'evaluate')
    vector_dim = require_vector_dimensions(vectors, 'evaluate.candidate_vectors') if vectors else None
    qvecs = embed_lmstudio([q['question'] for q in questions], endpoint=endpoint, model=model)  # 批量 embed 所有问题
    require_equal_length('questions', questions, 'query_vectors', qvecs, 'evaluate')
    if qvecs:
        require_vector_dimensions(qvecs, 'evaluate.query_vectors', expected_dim=vector_dim)
    results = []
    reciprocal_ranks = []  # 存每题的 1/rank，最后求平均就是 MRR
    hits = 0  # 成功的题数（Top-k 内有完整证据）
    for q, qv in zip(questions, qvecs):
        all_scored = retrieve(qv, chunks, vectors, top_k=len(chunks))  # 先全库排序，后面 build_ranked_result 自己截 Top-k
        result = build_ranked_result(q, all_scored, top_k=top_k, coverage_threshold=coverage_threshold)
        success = result['success']
        hits += int(success)
        reciprocal_ranks.append(1.0 / result['rank'] if result['rank'] else 0.0)  # 没成功时 rank=None，贡献 0
        results.append(result)
    metrics = {
        'total': len(questions),
        f'recall@{top_k}': hits / len(questions) if questions else 0.0,
        'mrr': sum(reciprocal_ranks) / len(questions) if questions else 0.0,
        'hits': hits,
        'failed': len(questions) - hits,
        'coverage_threshold': coverage_threshold,
    }
    return results, metrics

def evaluate_with_reranker(
    chunks: list[dict],
    vectors: list[list[float]],
    questions: list[dict],
    endpoint: str,
    model: str,
    top_k: int = 5,
    candidate_k: int = 20,
    coverage_threshold: float = 0.65,
    reranker: LocalCrossEncoderReranker | None = None,
    reranker_model_path: str | None = None,
    reranker_device: str | None = None,
    reranker_batch_size: int = 8,
    reranker_max_length: int = 512,
    reranker_use_fp16: bool = True,
) -> tuple[list[dict], dict]:
    """向量检索 + cross-encoder重排的评测，（非主线基线对比）
    """
    if candidate_k < top_k:
        raise RuntimeError(f'evaluate_with_reranker: candidate_k {candidate_k} must be >= top_k {top_k}.')
    require_equal_length('chunks', chunks, 'vectors', vectors, 'evaluate_with_reranker')
    vector_dim = require_vector_dimensions(vectors, 'evaluate_with_reranker.candidate_vectors') if vectors else None
    qvecs = embed_lmstudio([q['question'] for q in questions], endpoint=endpoint, model=model)
    require_equal_length('questions', questions, 'query_vectors', qvecs, 'evaluate_with_reranker')
    if qvecs:
        require_vector_dimensions(qvecs, 'evaluate_with_reranker.query_vectors', expected_dim=vector_dim)
    reranker = reranker or LocalCrossEncoderReranker(  # 允许外部传入已加载的 reranker，避免重复加载
        model_name_or_path=reranker_model_path,
        device=reranker_device,
        batch_size=reranker_batch_size,
        max_length=reranker_max_length,
        use_fp16=reranker_use_fp16,
    )
    results = []
    dense_rr = 0.0  # 重排前 MRR 累加器
    rerank_rr = 0.0  # 重排后 MRR 累加器
    dense_hits = 0
    rerank_hits = 0
    rerank_fixed = 0
    rerank_improved = 0
    for q, qv in zip(questions, qvecs):
        dense_all = retrieve(qv, chunks, vectors, top_k=len(chunks))  # 第一步：dense 全库检索
        dense_success_rank = first_relevant_rank(q, dense_all[:top_k], coverage_threshold)  # 重排前：Top-5 里成功块排第几
        dense_candidate_count = min(candidate_k, len(dense_all))  # 候选不够 20 个时取实际数量
        dense_candidates = []
        for dense_rank, row in enumerate(dense_all[:dense_candidate_count], 1):
            dense_candidates.append({
                **row,
                'dense_rank_before_rerank': dense_rank,  # 记下重排前的名次，方便后面对比
                'dense_score': float(row.get('score', 0.0)),
            })
        reranked_rows = reranker.rerank(q['question'], dense_candidates)  # 第二步：只重排前 candidate_k 个
        result = build_ranked_result(q, reranked_rows, top_k=top_k, coverage_threshold=coverage_threshold)  # 在重排结果上算最终指标
        dense_best_topk_coverage = 0.0
        for row in dense_all[:top_k]:
            dense_best_topk_coverage = max(dense_best_topk_coverage, relevance_score(q, row))
        dense_candidate_rank = first_relevant_rank(q, dense_candidates, coverage_threshold)  # 候选池（Top-20）里完整块原本排第几
        success_before = dense_success_rank is not None  # 重排前 Top-5 是否已成功
        success_after = result['success']  # 重排后 Top-5 是否成功
        fixed = (not success_before) and success_after  # 从失败变成功（召回修复）
        improved = fixed or (
            dense_candidate_rank is not None
            and result['rank'] is not None
            and result['rank'] < dense_candidate_rank  # 候选池里本来有完整块，重排后名次更靠前
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
            'rerank_candidate_k': dense_candidate_count,
            'rerank_fixed': fixed,
            'rerank_improved': improved,
            'top_k_before_rerank': [_top_row(q, row, i) for i, row in enumerate(dense_all[:top_k], 1)],
            'top_n_trace': [_trace_row(row, i) for i, row in enumerate(dense_all[:30], 1)],
            'top_n_trace_after_rerank': [_trace_row(row, i) for i, row in enumerate(reranked_rows[:30], 1)],
        })
        results.append(result)
    metrics = {
        'total': len(questions),
        f'dense_recall@{top_k}': dense_hits / len(questions) if questions else 0.0,
        f'recall@{top_k}': rerank_hits / len(questions) if questions else 0.0,
        'dense_mrr': dense_rr / len(questions) if questions else 0.0,
        'mrr': rerank_rr / len(questions) if questions else 0.0,
        'dense_hits_before_rerank': dense_hits,
        'hits': rerank_hits,
        'failed': len(questions) - rerank_hits,
        'rerank_fixed': rerank_fixed,
        'rerank_improved': rerank_improved,
        'rerank_candidate_k': candidate_k,
        'coverage_threshold': coverage_threshold,
    }
    return results, metrics

def write_report(path: str | Path, metrics: dict, results: list[dict], config: dict):
    failed = [r for r in results if not r['success']]
    lines = []
    lines.append('# Baseline Retrieval Report')
    lines.append('')
    lines.append('## Config')
    lines.append('')
    for k,v in config.items():
        lines.append(f'- **{k}**: `{v}`')
    lines.append('')
    lines.append('## Metrics')
    lines.append('')
    for k,v in metrics.items():
        lines.append(f'- **{k}**: {v:.4f}' if isinstance(v, float) else f'- **{k}**: {v}')
    lines.append('')
    lines.append('## Failed Queries')
    lines.append('')
    if not failed:
        lines.append('No failed queries under current threshold.')
    for r in failed:
        lines.append(f"### {r['qid']} — {r['gold_failure_type']}")
        lines.append(f"- question: {r['question']}")
        lines.append(f"- gold: `{r['gold_doc']} > {r['gold_section']}`")
        lines.append(f"- best_topk_coverage: {r['best_topk_coverage']}")
        lines.append(f"- best_gold_rank_hint: {r['best_gold_rank_hint']}")
        lines.append('- top results:')
        for t in r['top_k']:
            lines.append(f"  - rank {t['rank']}: `{t['chunk_id']}` score={t['score']} cov={t['coverage']} section={t['section_path']}")
        lines.append('')
    lines.append('## All Query Summary')
    lines.append('')
    lines.append('| qid | expected type | success | rank | best cov | gold rank hint |')
    lines.append('|---|---|---:|---:|---:|---:|')
    for r in results:
        lines.append(f"| {r['qid']} | {r['gold_failure_type']} | {r['success']} | {r['rank']} | {r['best_topk_coverage']} | {r['best_gold_rank_hint']} |")
    Path(path).write_text('\n'.join(lines) + '\n', encoding='utf-8')

def write_rerank_report(path: str | Path, metrics: dict, results: list[dict], config: dict):
    fixed = [r for r in results if r.get('rerank_fixed')]
    failed = [r for r in results if not r['success']]
    lines = []
    lines.append('# Dense -> Rerank Report')
    lines.append('')
    lines.append('## Config')
    lines.append('')
    for k, v in config.items():
        lines.append(f'- **{k}**: `{v}`')
    lines.append('')
    lines.append('## Metrics')
    lines.append('')
    for k, v in metrics.items():
        lines.append(f'- **{k}**: {v:.4f}' if isinstance(v, float) else f'- **{k}**: {v}')
    lines.append('')
    lines.append('## Fixed By Rerank')
    lines.append('')
    if not fixed:
        lines.append('No query was fixed by reranking under current candidate_k.')
    for row in fixed:
        lines.append(f"### {row['qid']} — {row['gold_failure_type']}")
        lines.append(f"- question: {row['question']}")
        lines.append(f"- before rank: {row.get('rank_before_rerank')}")
        lines.append(f"- after rank: {row.get('rank')}")
        lines.append(f"- before best_topk_coverage: {row.get('best_topk_coverage_before_rerank')}")
        lines.append(f"- after best_topk_coverage: {row.get('best_topk_coverage')}")
        lines.append('- top results after rerank:')
        for top in row['top_k']:
            lines.append(
                f"  - rank {top['rank']}: `{top['chunk_id']}` rerank_score={top.get('rerank_score', top['score'])} "
                f"dense_rank={top.get('dense_rank_before_rerank')} cov={top['coverage']}"
            )
        lines.append('')
    lines.append('## Still Failed After Rerank')
    lines.append('')
    if not failed:
        lines.append('No failed queries after reranking.')
    for row in failed:
        lines.append(f"### {row['qid']} — {row['gold_failure_type']}")
        lines.append(f"- question: {row['question']}")
        lines.append(f"- before rank: {row.get('rank_before_rerank')}")
        lines.append(f"- after rank: {row.get('rank')}")
        lines.append(f"- before best_topk_coverage: {row.get('best_topk_coverage_before_rerank')}")
        lines.append(f"- after best_topk_coverage: {row.get('best_topk_coverage')}")
        lines.append('')
    lines.append('## All Query Summary')
    lines.append('')
    lines.append('| qid | success before | success after | rank before | rank after | rerank fixed | rerank improved |')
    lines.append('|---|---:|---:|---:|---:|---:|---:|')
    for row in results:
        lines.append(
            f"| {row['qid']} | {row.get('success_before_rerank')} | {row['success']} | "
            f"{row.get('rank_before_rerank')} | {row['rank']} | {row.get('rerank_fixed')} | {row.get('rerank_improved')} |"
        )
    Path(path).write_text('\n'.join(lines) + '\n', encoding='utf-8')
