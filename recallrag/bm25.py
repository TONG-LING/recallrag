from __future__ import annotations
import json, math, re
from collections import Counter, defaultdict
from pathlib import Path
from .embeddings import embed_lmstudio, dot, require_equal_length, require_vector_dimensions
from .eval import load_questions, coverage, relevance_score, is_relevant
from .text_utils import mixed_tokens

def _load_json(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))

def _write_json(p, obj):
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    Path(p).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')

def tokenize(text: str) -> list[str]:
    return mixed_tokens(text)

class BM25Index:
    def __init__(self, texts: list[str], k1: float = 1.5, b: float = 0.75):
        self.texts = texts
        self.k1 = k1
        self.b = b
        self.doc_tokens = [tokenize(t) for t in texts]
        self.doc_len = [len(toks) for toks in self.doc_tokens]
        self.avgdl = sum(self.doc_len) / len(self.doc_len) if self.doc_len else 0.0
        self.tf = [Counter(toks) for toks in self.doc_tokens]
        df = defaultdict(int)
        for toks in self.doc_tokens:
            for tok in set(toks):
                df[tok] += 1
        n = len(texts)
        self.idf = {tok: math.log(1 + (n - freq + 0.5) / (freq + 0.5)) for tok, freq in df.items()}

    def score(self, query: str, idx: int) -> float:
        q_tokens = tokenize(query)
        score = 0.0
        dl = self.doc_len[idx] or 1
        tf = self.tf[idx]
        for tok in q_tokens:
            if tok not in self.idf:
                continue
            f = tf.get(tok, 0)
            if f == 0:
                continue
            denom = f + self.k1 * (1 - self.b + self.b * dl / (self.avgdl or 1))
            score += self.idf[tok] * f * (self.k1 + 1) / denom
        return score

    def search(self, query: str, top_k: int) -> list[tuple[int,float]]:
        scored = [(i, self.score(query, i)) for i in range(len(self.texts))]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

def minmax(scores: list[float]) -> list[float]:
    if not scores:
        return []
    lo, hi = min(scores), max(scores)
    if abs(hi - lo) < 1e-12:
        return [0.0 for _ in scores]
    return [(s - lo) / (hi - lo) for s in scores]

def eval_bm25_and_hybrid(
    index_dir: str | Path = 'runs/base',
    questions_path: str | Path = 'case/eval/questions.jsonl',
    out_dir: str | Path = 'runs/hybrid_bm25',
    endpoint: str = 'http://localhost:1234/v1/embeddings',
    model: str = 'bge-small-en-v1.5',
    top_k: int = 5,
    coverage_threshold: float = 0.65,
    alpha_dense: float = 0.65,
):
    index_dir = Path(index_dir)
    out_dir = Path(out_dir)
    chunks = _load_json(index_dir / 'chunks.json')
    vectors = _load_json(index_dir / 'vectors.json')
    require_equal_length('chunks', chunks, 'vectors', vectors, 'eval_bm25_and_hybrid')
    vector_dim = require_vector_dimensions(vectors, 'eval_bm25_and_hybrid.chunk_vectors') if vectors else None
    questions = load_questions(questions_path)
    bm25 = BM25Index([c['text'] for c in chunks])
    qvecs = embed_lmstudio([q['question'] for q in questions], endpoint=endpoint, model=model)
    require_equal_length('questions', questions, 'query_vectors', qvecs, 'eval_bm25_and_hybrid')
    if qvecs:
        require_vector_dimensions(qvecs, 'eval_bm25_and_hybrid.query_vectors', expected_dim=vector_dim)
    modes = ['dense', 'bm25', 'dense_bm25']
    all_results = {m: [] for m in modes}
    all_metrics = {}
    for mode in modes:
        hits=0; mrr=0.0
        for q, qv in zip(questions, qvecs):
            dense_scores = [dot(qv, v) for v in vectors]
            bm25_scores = [bm25.score(q['question'], i) for i in range(len(chunks))]
            if mode == 'dense':
                scores = dense_scores
            elif mode == 'bm25':
                scores = bm25_scores
            else:
                nd = minmax(dense_scores)
                nb = minmax(bm25_scores)
                scores = [alpha_dense*d + (1-alpha_dense)*b for d,b in zip(nd,nb)]
            order = sorted(range(len(chunks)), key=lambda i: scores[i], reverse=True)[:top_k]
            rank=None; best_cov=0.0; top_rows=[]
            for pos, idx in enumerate(order,1):
                c = chunks[idx]
                cov = relevance_score(q, c)
                best_cov = max(best_cov, cov)
                if is_relevant(q, c, coverage_threshold) and rank is None:
                    rank = pos
                top_rows.append({
                    'rank': pos,
                    'chunk_id': c['chunk_id'],
                    'doc_id': c['doc_id'],
                    'section_path': c.get('section_path',''),
                    'score': round(scores[idx], 6),
                    'dense_score': round(dense_scores[idx], 6),
                    'bm25_score': round(bm25_scores[idx], 6),
                    'coverage': round(cov, 3),
                    'text_preview': c['text'][:220].replace('\n',' '),
                })
            success = rank is not None
            hits += int(success)
            mrr += 1/rank if rank else 0.0
            all_results[mode].append({
                'qid': q['qid'],
                'question': q['question'],
                'gold_doc': q['gold_doc'],
                'gold_section': q.get('gold_section',''),
                'gold_failure_type': q.get('gold_failure_type',''),
                'success': success,
                'rank': rank,
                'best_topk_coverage': round(best_cov,3),
                'top_k': top_rows,
            })
        all_metrics[mode] = {
            'total': len(questions),
            f'recall@{top_k}': hits/len(questions) if questions else 0.0,
            'mrr': mrr/len(questions) if questions else 0.0,
            'hits': hits,
            'failed': len(questions)-hits,
            'top_k': top_k,
            'coverage_threshold': coverage_threshold,
        }
    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / 'hybrid_bm25_results.json', all_results)
    _write_json(out_dir / 'hybrid_bm25_metrics.json', all_metrics)
    write_report(out_dir / 'hybrid_bm25_report.md', all_metrics, all_results, alpha_dense)
    return all_results, all_metrics

def write_report(path: Path, metrics: dict, results: dict, alpha_dense: float):
    lines = ['# Dense / BM25 / Hybrid Retrieval Report', '', f'- dense weight in hybrid: `{alpha_dense}`', '']
    lines += ['## Metrics', '', '| mode | Recall@5 | MRR | hits | failed |', '|---|---:|---:|---:|---:|']
    for mode, m in metrics.items():
        lines.append(f"| {mode} | {m.get('recall@5',0):.4f} | {m['mrr']:.4f} | {m['hits']} | {m['failed']} |")
    lines += ['', '## Query Movement vs Dense', '']
    dense = {r['qid']: r for r in results['dense']}
    for mode in ['bm25','dense_bm25']:
        fixed=[]; regressed=[]
        for r in results[mode]:
            d=dense[r['qid']]
            if not d['success'] and r['success']:
                fixed.append(r['qid'])
            elif d['success'] and not r['success']:
                regressed.append(r['qid'])
        lines += [f'### {mode}', '', f'- fixed_vs_dense: {fixed}', f'- regressed_vs_dense: {regressed}', '']
    lines += ['## Interpretation', '', '- BM25 is useful for exact terms, identifiers, acronyms and lexical matches.', '- Dense retrieval is useful for semantic paraphrases.', '- Dense+BM25 hybrid is a production-like multi-retrieval baseline.', '- If BM25/hybrid fixes a failed query, the failure may be retrieval-strategy related rather than chunking-related.']
    path.write_text('\n'.join(lines)+'\n', encoding='utf-8')
