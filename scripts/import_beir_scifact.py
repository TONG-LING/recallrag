#!/usr/bin/env python3
from __future__ import annotations
import json, csv, random
from pathlib import Path

SRC = Path('datasets/beir/scifact/scifact')
OUT_DOCS = Path('case_beir/scifact/docs')
OUT_EVAL = Path('case_beir/scifact/eval')
OUT_META = Path('case_beir/scifact')
MAX_QUERIES = 80
DISTRACTORS = 700
SEED = 42

def load_jsonl(p):
    return [json.loads(line) for line in p.read_text(encoding='utf-8').splitlines() if line.strip()]

def safe_doc_id(raw: str) -> str:
    return f'scifact_{raw}.md'

def main():
    random.seed(SEED)
    corpus_raw = load_jsonl(SRC / 'corpus.jsonl')
    queries_raw = load_jsonl(SRC / 'queries.jsonl')
    corpus = {x['_id']: x for x in corpus_raw}
    queries = {x['_id']: x for x in queries_raw}
    qrels=[]
    with (SRC / 'qrels/test.tsv').open(encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            if int(row['score']) > 0 and row['query-id'] in queries and row['corpus-id'] in corpus:
                qrels.append(row)
    # one positive per query, deterministic
    seen=set(); selected=[]
    for row in qrels:
        if row['query-id'] in seen:
            continue
        seen.add(row['query-id'])
        selected.append(row)
        if len(selected) >= MAX_QUERIES:
            break
    positive_ids = {r['corpus-id'] for r in selected}
    all_ids = list(corpus.keys())
    distractor_ids = [x for x in all_ids if x not in positive_ids]
    random.shuffle(distractor_ids)
    keep_ids = set(positive_ids) | set(distractor_ids[:DISTRACTORS])

    OUT_DOCS.mkdir(parents=True, exist_ok=True)
    OUT_EVAL.mkdir(parents=True, exist_ok=True)
    for old in OUT_DOCS.glob('*.md'):
        old.unlink()

    for cid in sorted(keep_ids, key=lambda x: int(x) if x.isdigit() else x):
        doc = corpus[cid]
        title = (doc.get('title') or '').strip()
        text = (doc.get('text') or '').strip()
        md = f"# {title}\n\n{text}\n\n---\n\nsource_dataset: BEIR SciFact\nsource_corpus_id: {cid}\n"
        (OUT_DOCS / safe_doc_id(cid)).write_text(md, encoding='utf-8')

    questions=[]
    for i,row in enumerate(selected,1):
        qid = row['query-id']
        cid = row['corpus-id']
        doc = corpus[cid]
        questions.append({
            'qid': f'scifact_q{qid}',
            'question': queries[qid]['text'],
            'gold_doc': safe_doc_id(cid),
            'gold_section': doc.get('title',''),
            'gold_failure_type': 'beir_doc_retrieval',
            'eval_mode': 'doc',
            'source_dataset': 'BEIR SciFact',
            'source_query_id': qid,
            'source_corpus_id': cid,
            'gold_span': '',
        })
    with (OUT_EVAL / 'questions.jsonl').open('w', encoding='utf-8') as f:
        for q in questions:
            f.write(json.dumps(q, ensure_ascii=False) + '\n')
    meta = {
        'dataset': 'BEIR SciFact',
        'source': str(SRC),
        'docs_written': len(keep_ids),
        'eval_questions': len(questions),
        'positive_docs': len(positive_ids),
        'distractors': len(keep_ids)-len(positive_ids),
        'eval_mode': 'doc',
        'notes': 'Doc-level qrels imported from BEIR SciFact test split. Documents are scientific abstracts converted to markdown.'
    }
    (OUT_META / 'README.md').write_text('# BEIR SciFact imported case set\n\n```json\n'+json.dumps(meta, indent=2, ensure_ascii=False)+'\n```\n', encoding='utf-8')
    print(json.dumps(meta, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
