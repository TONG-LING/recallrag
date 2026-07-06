# Dense / BM25 / Hybrid Retrieval Report

- dense weight in hybrid: `0.65`

## Metrics

| mode | Recall@5 | MRR | hits | failed |
|---|---:|---:|---:|---:|
| dense | 0.1417 | 0.0651 | 17 | 103 |
| bm25 | 0.0667 | 0.0244 | 8 | 112 |
| dense_bm25 | 0.0917 | 0.0318 | 11 | 109 |

## Query Movement vs Dense

### bm25

- fixed_vs_dense: []
- regressed_vs_dense: ['zh043', 'zh059', 'zh086', 'zh092', 'zh104', 'zh107', 'zh108', 'zh114', 'zh115']

### dense_bm25

- fixed_vs_dense: []
- regressed_vs_dense: ['zh086', 'zh092', 'zh104', 'zh107', 'zh108', 'zh114']

## Interpretation

- BM25 is useful for exact terms, identifiers, acronyms and lexical matches.
- Dense retrieval is useful for semantic paraphrases.
- Dense+BM25 hybrid is a production-like multi-retrieval baseline.
- If BM25/hybrid fixes a failed query, the failure may be retrieval-strategy related rather than chunking-related.
