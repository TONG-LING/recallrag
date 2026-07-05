from __future__ import annotations
import argparse, json
from pathlib import Path
from .ingest import load_markdown_docs
from .chunkers import fixed_char_chunk
from .embeddings import embed_lmstudio
from .eval import load_questions, evaluate, evaluate_with_reranker, write_report, write_rerank_report
from .diagnose import diagnose_run
from .patch_index import materialize_patches, evaluate_hybrid
from .qdrant_backend import (
    build_qdrant_from_runs,
    eval_qdrant_hybrid,
    eval_qdrant_hybrid_rerank,
    compare_qdrant_runs,
    health as qdrant_health,
)
from .bm25 import eval_bm25_and_hybrid
from .strong_baselines import evaluate_rrf_rerank
from .triage import final_triage

def write_json(path: str | Path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding='utf-8')

def read_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def cmd_chunk(args):
    docs = load_markdown_docs(args.docs)
    chunks = fixed_char_chunk(docs, chunk_size=args.chunk_size, overlap=args.overlap, keep_heading=args.keep_heading)
    write_json(Path(args.out) / 'chunks.json', [c.to_dict() for c in chunks])
    print(f'wrote {len(chunks)} chunks -> {Path(args.out)/"chunks.json"}')

def cmd_embed(args):
    chunks = read_json(Path(args.index) / 'chunks.json')
    texts = [c['text'] for c in chunks]
    vectors = embed_lmstudio(texts, endpoint=args.endpoint, model=args.model, batch_size=args.batch_size)
    write_json(Path(args.index) / 'vectors.json', vectors)
    meta = {'endpoint': args.endpoint, 'model': args.model, 'count': len(vectors), 'dim': len(vectors[0]) if vectors else 0}
    write_json(Path(args.index) / 'index_meta.json', meta)
    print(f'wrote vectors -> {Path(args.index)/"vectors.json"}')


def cmd_eval(args):
    base = Path(args.index)
    chunks = read_json(base / 'chunks.json')
    vectors = read_json(base / 'vectors.json')
    questions = load_questions(args.questions)
    results, metrics = evaluate(chunks, vectors, questions, endpoint=args.endpoint, model=args.model, top_k=args.top_k, coverage_threshold=args.coverage_threshold)
    out = Path(args.out or args.index)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / 'retrieval_results.json', results)
    write_json(out / 'metrics.json', metrics)
    config = {'index': args.index, 'questions': args.questions, 'top_k': args.top_k, 'coverage_threshold': args.coverage_threshold, 'endpoint': args.endpoint, 'model': args.model}
    write_report(out / 'eval_report.md', metrics, results, config)
    print(json.dumps(metrics, indent=2))
    print(f'wrote report -> {out/"eval_report.md"}')

def cmd_eval_rerank(args):
    base = Path(args.index)
    chunks = read_json(base / 'chunks.json')
    vectors = read_json(base / 'vectors.json')
    questions = load_questions(args.questions)
    results, metrics = evaluate_with_reranker(
        chunks,
        vectors,
        questions,
        endpoint=args.endpoint,
        model=args.model,
        top_k=args.top_k,
        candidate_k=args.candidate_k,
        coverage_threshold=args.coverage_threshold,
        reranker_model_path=args.reranker_model_path,
        reranker_device=args.reranker_device,
        reranker_batch_size=args.reranker_batch_size,
        reranker_max_length=args.reranker_max_length,
        reranker_use_fp16=not args.reranker_no_fp16,
    )
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / 'retrieval_results.json', results)
    write_json(out / 'metrics.json', metrics)
    config = {
        'index': args.index,
        'questions': args.questions,
        'top_k': args.top_k,
        'candidate_k': args.candidate_k,
        'coverage_threshold': args.coverage_threshold,
        'endpoint': args.endpoint,
        'model': args.model,
        'reranker_model_path': args.reranker_model_path,
        'reranker_device': args.reranker_device,
        'reranker_batch_size': args.reranker_batch_size,
        'reranker_max_length': args.reranker_max_length,
        'reranker_use_fp16': not args.reranker_no_fp16,
    }
    write_rerank_report(out / 'eval_report.md', metrics, results, config)
    print(json.dumps(metrics, indent=2))
    print(f'wrote rerank report -> {out/"eval_report.md"}')

def cmd_run_baseline(args):
    out = Path(args.out)
    docs = load_markdown_docs(args.docs)
    chunks = fixed_char_chunk(docs, chunk_size=args.chunk_size, overlap=args.overlap, keep_heading=args.keep_heading)
    out.mkdir(parents=True, exist_ok=True)
    write_json(out / 'chunks.json', [c.to_dict() for c in chunks])
    vectors = embed_lmstudio([c.text for c in chunks], endpoint=args.endpoint, model=args.model, batch_size=args.batch_size)
    write_json(out / 'vectors.json', vectors)
    write_json(out / 'index_meta.json', {'endpoint': args.endpoint, 'model': args.model, 'count': len(vectors), 'dim': len(vectors[0]) if vectors else 0, 'chunk_size': args.chunk_size, 'overlap': args.overlap, 'keep_heading': args.keep_heading})
    questions = load_questions(args.questions)
    results, metrics = evaluate([c.to_dict() for c in chunks], vectors, questions, endpoint=args.endpoint, model=args.model, top_k=args.top_k, coverage_threshold=args.coverage_threshold)
    write_json(out / 'retrieval_results.json', results)
    write_json(out / 'metrics.json', metrics)
    config = {'docs': args.docs, 'questions': args.questions, 'chunk_size': args.chunk_size, 'overlap': args.overlap, 'keep_heading': args.keep_heading, 'top_k': args.top_k, 'coverage_threshold': args.coverage_threshold, 'endpoint': args.endpoint, 'model': args.model}
    write_report(out / 'eval_report.md', metrics, results, config)
    print(json.dumps(metrics, indent=2))
    print(f'wrote baseline run -> {out}')

def cmd_diagnose(args):
    diagnoses = diagnose_run(args.index, args.questions, out_dir=args.out, threshold=args.coverage_threshold)
    print(f'wrote {len(diagnoses)} diagnoses -> {Path(args.out or args.index)/"failure_diagnosis.md"}')

def cmd_materialize_patches(args):
    chunks, log = materialize_patches(args.index, args.out, endpoint=args.endpoint, model=args.model, batch_size=args.batch_size)
    print(f'wrote {len(chunks)} patch chunks -> {Path(args.out)/"patch_chunks.json"}')

def cmd_eval_hybrid(args):
    results, metrics, comparison = evaluate_hybrid(args.index, args.patch_index, args.questions, out_dir=args.out, endpoint=args.endpoint, model=args.model, top_k=args.top_k, coverage_threshold=args.coverage_threshold)
    print(json.dumps(metrics, indent=2))
    print(f'wrote hybrid report -> {Path(args.out)/"comparison_report.md"}')

def cmd_qdrant_health(args):
    print(json.dumps(qdrant_health(args.url), indent=2))

def cmd_qdrant_build(args):
    meta = build_qdrant_from_runs(args.index, args.patch_index, url=args.url, main_collection=args.main_collection, patch_collection=args.patch_collection, out_dir=args.out)
    print(json.dumps(meta, indent=2))

def cmd_qdrant_eval(args):
    results, metrics = eval_qdrant_hybrid(args.questions, url=args.url, main_collection=args.main_collection, patch_collection=args.patch_collection, endpoint=args.endpoint, model=args.model, main_k=args.main_k, patch_k=args.patch_k, final_k=args.final_k, coverage_threshold=args.coverage_threshold, out_dir=args.out)
    print(json.dumps(metrics, indent=2))
    print(f'wrote qdrant report -> {Path(args.out)/"qdrant_eval_report.md"}')

def cmd_qdrant_eval_rerank(args):
    results, metrics = eval_qdrant_hybrid_rerank(
        args.questions,
        url=args.url,
        main_collection=args.main_collection,
        patch_collection=args.patch_collection,
        endpoint=args.endpoint,
        model=args.model,
        main_k=args.main_k,
        patch_k=args.patch_k,
        final_k=args.final_k,
        coverage_threshold=args.coverage_threshold,
        reranker_model_path=args.reranker_model_path,
        reranker_device=args.reranker_device,
        reranker_batch_size=args.reranker_batch_size,
        reranker_max_length=args.reranker_max_length,
        reranker_use_fp16=not args.reranker_no_fp16,
        out_dir=args.out,
    )
    print(json.dumps(metrics, indent=2))
    print(f'wrote qdrant rerank report -> {Path(args.out)/"qdrant_eval_report.md"}')

def cmd_qdrant_compare(args):
    comparison = compare_qdrant_runs(args.main_only_dir, args.main_patch_dir, args.out)
    print(json.dumps(comparison['delta'], indent=2))
    print(f'wrote qdrant comparison -> {args.out}')

def cmd_eval_bm25_hybrid(args):
    results, metrics = eval_bm25_and_hybrid(args.index, args.questions, out_dir=args.out, endpoint=args.endpoint, model=args.model, top_k=args.top_k, coverage_threshold=args.coverage_threshold, alpha_dense=args.alpha_dense)
    print(json.dumps(metrics, indent=2))
    print(f'wrote BM25/hybrid report -> {Path(args.out)/"hybrid_bm25_report.md"}')

def cmd_eval_rrf_rerank(args):
    results, metrics = evaluate_rrf_rerank(
        args.index,
        args.questions,
        out_dir=args.out,
        endpoint=args.endpoint,
        model=args.model,
        top_k=args.top_k,
        dense_k=args.dense_k,
        bm25_k=args.bm25_k,
        candidate_k=args.candidate_k,
        coverage_threshold=args.coverage_threshold,
        rrf_k=args.rrf_k,
        reranker_model_path=args.reranker_model_path,
        reranker_device=args.reranker_device,
        reranker_batch_size=args.reranker_batch_size,
        reranker_max_length=args.reranker_max_length,
        reranker_use_fp16=not args.reranker_no_fp16,
        hyde_model=args.hyde_model,
        hyde_endpoint=args.hyde_endpoint,
        hyde_protocol=args.hyde_protocol,
        hyde_temperature=args.hyde_temperature,
        hyde_max_tokens=args.hyde_max_tokens,
        hyde_api_key=args.hyde_api_key,
        hyde_auth_mode=args.hyde_auth_mode,
        hyde_api_version=args.hyde_api_version,
        hyde_disable_thinking=args.hyde_disable_thinking,
    )
    print(json.dumps(metrics, indent=2, ensure_ascii=False))
    print(f'wrote RRF/rerank report -> {Path(args.out)/"eval_report.md"}')

def cmd_final_triage(args):
    summary = final_triage(args.base_dir, args.patch_eval_dir, args.bm25_dir, args.qdrant_dir, args.out)
    print(json.dumps({k: v for k, v in summary.items() if k != 'rows'}, indent=2))
    print(f'wrote final triage -> {Path(args.out)/"final_triage_report.md"}')

def cmd_serve_demo(args):
    from .api import run as run_api
    run_api([
        '--project-root', args.project_root,
        '--host', args.host,
        '--port', str(args.port),
    ])

def main():
    p = argparse.ArgumentParser(prog='recallrag')
    sub = p.add_subparsers(required=True)
    c = sub.add_parser('chunk')
    c.add_argument('--docs', default='case/docs')
    c.add_argument('--out', default='runs/base')
    c.add_argument('--chunk-size', type=int, default=380)
    c.add_argument('--overlap', type=int, default=0)
    c.add_argument('--keep-heading', action='store_true')
    c.set_defaults(func=cmd_chunk)

    e = sub.add_parser('embed')
    e.add_argument('--index', default='runs/base')
    e.add_argument('--endpoint', default='http://localhost:1234/v1/embeddings')
    e.add_argument('--model', default='bge-small-en-v1.5')
    e.add_argument('--batch-size', type=int, default=16)
    e.set_defaults(func=cmd_embed)

    ev = sub.add_parser('eval')
    ev.add_argument('--index', default='runs/base')
    ev.add_argument('--questions', default='case/eval/questions.jsonl')
    ev.add_argument('--out', default=None)
    ev.add_argument('--endpoint', default='http://localhost:1234/v1/embeddings')
    ev.add_argument('--model', default='bge-small-en-v1.5')
    ev.add_argument('--top-k', type=int, default=5)
    ev.add_argument('--coverage-threshold', type=float, default=0.65)
    ev.set_defaults(func=cmd_eval)

    evr = sub.add_parser('eval-rerank')
    evr.add_argument('--index', default='runs/base')
    evr.add_argument('--questions', default='case/eval/questions.jsonl')
    evr.add_argument('--out', default='runs/rerank')
    evr.add_argument('--endpoint', default='http://localhost:1234/v1/embeddings')
    evr.add_argument('--model', default='bge-small-en-v1.5')
    evr.add_argument('--top-k', type=int, default=5)
    evr.add_argument('--candidate-k', type=int, default=20)
    evr.add_argument('--coverage-threshold', type=float, default=0.65)
    evr.add_argument('--reranker-model-path', default=None)
    evr.add_argument('--reranker-device', default=None)
    evr.add_argument('--reranker-batch-size', type=int, default=8)
    evr.add_argument('--reranker-max-length', type=int, default=512)
    evr.add_argument('--reranker-no-fp16', action='store_true')
    evr.set_defaults(func=cmd_eval_rerank)

    dg = sub.add_parser('diagnose')
    dg.add_argument('--index', default='runs/base')
    dg.add_argument('--questions', default='case/eval/questions.jsonl')
    dg.add_argument('--out', default=None)
    dg.add_argument('--coverage-threshold', type=float, default=0.65)
    dg.set_defaults(func=cmd_diagnose)

    mp = sub.add_parser('materialize-patches')
    mp.add_argument('--index', default='runs/base')
    mp.add_argument('--out', default='runs/patches')
    mp.add_argument('--endpoint', default='http://localhost:1234/v1/embeddings')
    mp.add_argument('--model', default='bge-small-en-v1.5')
    mp.add_argument('--batch-size', type=int, default=16)
    mp.set_defaults(func=cmd_materialize_patches)

    eh = sub.add_parser('eval-hybrid')
    eh.add_argument('--index', default='runs/base')
    eh.add_argument('--patch-index', default='runs/patches')
    eh.add_argument('--questions', default='case/eval/questions.jsonl')
    eh.add_argument('--out', default='runs/hybrid')
    eh.add_argument('--endpoint', default='http://localhost:1234/v1/embeddings')
    eh.add_argument('--model', default='bge-small-en-v1.5')
    eh.add_argument('--top-k', type=int, default=5)
    eh.add_argument('--coverage-threshold', type=float, default=0.65)
    eh.set_defaults(func=cmd_eval_hybrid)

    qh = sub.add_parser('qdrant-health')
    qh.add_argument('--url', default='http://localhost:6333')
    qh.set_defaults(func=cmd_qdrant_health)

    qb = sub.add_parser('qdrant-build')
    qb.add_argument('--index', default='runs/base')
    qb.add_argument('--patch-index', default='runs/patches')
    qb.add_argument('--out', default='runs/qdrant')
    qb.add_argument('--url', default='http://localhost:6333')
    qb.add_argument('--main-collection', default='recallrag_main')
    qb.add_argument('--patch-collection', default='recallrag_patch')
    qb.set_defaults(func=cmd_qdrant_build)

    qe = sub.add_parser('qdrant-eval')
    qe.add_argument('--questions', default='case/eval/questions.jsonl')
    qe.add_argument('--out', default='runs/qdrant')
    qe.add_argument('--url', default='http://localhost:6333')
    qe.add_argument('--main-collection', default='recallrag_main')
    qe.add_argument('--patch-collection', default='recallrag_patch')
    qe.add_argument('--endpoint', default='http://localhost:1234/v1/embeddings')
    qe.add_argument('--model', default='bge-small-en-v1.5')
    qe.add_argument('--main-k', type=int, default=5)
    qe.add_argument('--patch-k', type=int, default=3)
    qe.add_argument('--final-k', type=int, default=5)
    qe.add_argument('--coverage-threshold', type=float, default=0.65)
    qe.set_defaults(func=cmd_qdrant_eval)

    qer = sub.add_parser('qdrant-eval-rerank')
    qer.add_argument('--questions', default='case/eval/questions.jsonl')
    qer.add_argument('--out', default='runs/qdrant_rerank')
    qer.add_argument('--url', default='http://localhost:6333')
    qer.add_argument('--main-collection', default='recallrag_main')
    qer.add_argument('--patch-collection', default='recallrag_patch')
    qer.add_argument('--endpoint', default='http://localhost:1234/v1/embeddings')
    qer.add_argument('--model', default='bge-small-en-v1.5')
    qer.add_argument('--main-k', type=int, default=10)
    qer.add_argument('--patch-k', type=int, default=5)
    qer.add_argument('--final-k', type=int, default=5)
    qer.add_argument('--coverage-threshold', type=float, default=0.65)
    qer.add_argument('--reranker-model-path', default=None)
    qer.add_argument('--reranker-device', default=None)
    qer.add_argument('--reranker-batch-size', type=int, default=8)
    qer.add_argument('--reranker-max-length', type=int, default=512)
    qer.add_argument('--reranker-no-fp16', action='store_true')
    qer.set_defaults(func=cmd_qdrant_eval_rerank)

    qc = sub.add_parser('qdrant-compare')
    qc.add_argument('--main-only-dir', default='runs/qdrant_main')
    qc.add_argument('--main-patch-dir', default='runs/qdrant')
    qc.add_argument('--out', default='runs/qdrant/qdrant_comparison_report.md')
    qc.set_defaults(func=cmd_qdrant_compare)

    hb = sub.add_parser('eval-bm25-hybrid')
    hb.add_argument('--index', default='runs/base')
    hb.add_argument('--questions', default='case/eval/questions.jsonl')
    hb.add_argument('--out', default='runs/hybrid_bm25')
    hb.add_argument('--endpoint', default='http://localhost:1234/v1/embeddings')
    hb.add_argument('--model', default='bge-small-en-v1.5')
    hb.add_argument('--top-k', type=int, default=5)
    hb.add_argument('--coverage-threshold', type=float, default=0.65)
    hb.add_argument('--alpha-dense', type=float, default=0.65)
    hb.set_defaults(func=cmd_eval_bm25_hybrid)

    hrr = sub.add_parser('eval-rrf-rerank')
    hrr.add_argument('--index', default='runs/base')
    hrr.add_argument('--questions', default='case/eval/questions.jsonl')
    hrr.add_argument('--out', default='runs/rrf_rerank')
    hrr.add_argument('--endpoint', default='http://localhost:1234/v1/embeddings')
    hrr.add_argument('--model', default='bge-small-en-v1.5')
    hrr.add_argument('--top-k', type=int, default=5)
    hrr.add_argument('--dense-k', type=int, default=20)
    hrr.add_argument('--bm25-k', type=int, default=20)
    hrr.add_argument('--candidate-k', type=int, default=20)
    hrr.add_argument('--coverage-threshold', type=float, default=0.65)
    hrr.add_argument('--rrf-k', type=int, default=60)
    hrr.add_argument('--reranker-model-path', default=None)
    hrr.add_argument('--reranker-device', default=None)
    hrr.add_argument('--reranker-batch-size', type=int, default=8)
    hrr.add_argument('--reranker-max-length', type=int, default=512)
    hrr.add_argument('--reranker-no-fp16', action='store_true')
    hrr.add_argument('--hyde-model', default=None)
    hrr.add_argument('--hyde-endpoint', default='http://localhost:1234/v1/chat/completions')
    hrr.add_argument('--hyde-protocol', choices=['openai_chat', 'messages', 'anthropic_messages'], default='openai_chat')
    hrr.add_argument('--hyde-temperature', type=float, default=0.0)
    hrr.add_argument('--hyde-max-tokens', type=int, default=160)
    hrr.add_argument('--hyde-api-key', default=None, help='Optional HyDE API key. If omitted, uses RECALLRAG_HYDE_API_KEY.')
    hrr.add_argument('--hyde-auth-mode', choices=['auto', 'none', 'authorization', 'x-api-key'], default='auto')
    hrr.add_argument('--hyde-api-version', default='2023-06-01')
    hrr.add_argument('--hyde-disable-thinking', action='store_true')
    hrr.set_defaults(func=cmd_eval_rrf_rerank)

    ft = sub.add_parser('final-triage')
    ft.add_argument('--base-dir', default='runs/base')
    ft.add_argument('--patch-eval-dir', default='runs/hybrid')
    ft.add_argument('--bm25-dir', default='runs/hybrid_bm25')
    ft.add_argument('--qdrant-dir', default=None)
    ft.add_argument('--out', default='runs/triage')
    ft.set_defaults(func=cmd_final_triage)

    sd = sub.add_parser('serve-demo')
    sd.add_argument('--project-root', default='.')
    sd.add_argument('--host', default='127.0.0.1')
    sd.add_argument('--port', type=int, default=8000)
    sd.set_defaults(func=cmd_serve_demo)

    rb = sub.add_parser('run-baseline')
    rb.add_argument('--docs', default='case/docs')
    rb.add_argument('--questions', default='case/eval/questions.jsonl')
    rb.add_argument('--out', default='runs/base')
    rb.add_argument('--chunk-size', type=int, default=380)
    rb.add_argument('--overlap', type=int, default=0)
    rb.add_argument('--keep-heading', action='store_true')
    rb.add_argument('--endpoint', default='http://localhost:1234/v1/embeddings')
    rb.add_argument('--model', default='bge-small-en-v1.5')
    rb.add_argument('--batch-size', type=int, default=16)
    rb.add_argument('--top-k', type=int, default=5)
    rb.add_argument('--coverage-threshold', type=float, default=0.65)
    rb.set_defaults(func=cmd_run_baseline)

    args = p.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
