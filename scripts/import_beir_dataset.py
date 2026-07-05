#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, csv, random, re
from pathlib import Path

def load_jsonl(p):
    return [json.loads(line) for line in p.read_text(encoding='utf-8').splitlines() if line.strip()]

def safe_name(dataset: str, raw: str) -> str:
    x = re.sub(r'[^A-Za-z0-9]+', '_', raw).strip('_')
    return f'{dataset}_{x}.md'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--name', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--max-queries', type=int, default=80)
    ap.add_argument('--distractors', type=int, default=700)
    ap.add_argument('--seed', type=int, default=42)
    ap.add_argument('--qrels-split', default='test')
    args=ap.parse_args()
    random.seed(args.seed)
    src=Path(args.src)
    out=Path(args.out)
    out_docs=out/'docs'; out_eval=out/'eval'
    out_docs.mkdir(parents=True, exist_ok=True); out_eval.mkdir(parents=True, exist_ok=True)
    corpus_raw=load_jsonl(src/'corpus.jsonl')
    queries_raw=load_jsonl(src/'queries.jsonl')
    corpus={x['_id']:x for x in corpus_raw}
    queries={x['_id']:x for x in queries_raw}
    qrels=[]
    with (src/'qrels'/f'{args.qrels_split}.tsv').open(encoding='utf-8') as f:
        reader=csv.DictReader(f, delimiter='\t')
        for row in reader:
            if int(row['score'])>0 and row['query-id'] in queries and row['corpus-id'] in corpus:
                qrels.append(row)
    seen=set(); selected=[]
    for row in qrels:
        if row['query-id'] in seen:
            continue
        seen.add(row['query-id']); selected.append(row)
        if len(selected)>=args.max_queries: break
    positive_ids={r['corpus-id'] for r in selected}
    distractor_ids=[x for x in corpus if x not in positive_ids]
    random.shuffle(distractor_ids)
    keep_ids=set(positive_ids)|set(distractor_ids[:args.distractors])
    for old in out_docs.glob('*.md'): old.unlink()
    for cid in sorted(keep_ids):
        doc=corpus[cid]
        title=(doc.get('title') or '').strip() or cid
        text=(doc.get('text') or '').strip()
        meta=doc.get('metadata') or {}
        url=meta.get('url','')
        md=f"# {title}\n\n{text}\n\n---\n\nsource_dataset: BEIR {args.name}\nsource_corpus_id: {cid}\nsource_url: {url}\n"
        (out_docs/safe_name(args.name.lower(), cid)).write_text(md, encoding='utf-8')
    with (out_eval/'questions.jsonl').open('w', encoding='utf-8') as f:
        for row in selected:
            qid=row['query-id']; cid=row['corpus-id']; doc=corpus[cid]
            q={
                'qid': f'{args.name.lower()}_q{re.sub(r"[^A-Za-z0-9]+", "_", qid).strip("_")}',
                'question': queries[qid]['text'],
                'gold_doc': safe_name(args.name.lower(), cid),
                'gold_section': doc.get('title',''),
                'gold_failure_type': 'beir_doc_retrieval',
                'eval_mode': 'doc',
                'source_dataset': f'BEIR {args.name}',
                'source_query_id': qid,
                'source_corpus_id': cid,
                'gold_span': '',
            }
            f.write(json.dumps(q, ensure_ascii=False)+'\n')
    meta={
        'dataset': f'BEIR {args.name}', 'src': str(src), 'docs_written': len(keep_ids),
        'eval_questions': len(selected), 'positive_docs': len(positive_ids),
        'distractors': len(keep_ids)-len(positive_ids), 'eval_mode':'doc'
    }
    (out/'README.md').write_text('# Imported BEIR dataset\n\n```json\n'+json.dumps(meta, indent=2, ensure_ascii=False)+'\n```\n', encoding='utf-8')
    print(json.dumps(meta, indent=2, ensure_ascii=False))
if __name__=='__main__': main()
