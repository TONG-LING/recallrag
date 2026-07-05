# Reranker Notes

## Initial Retriever

A RAG pipeline often has two retrieval stages. The initial retriever quickly selects a candidate set from the vector database. This stage must be fast because it searches over many chunks. It usually returns top-k candidates according to embedding similarity, lexical score, or a hybrid score.

The initial retriever controls recall. If the correct evidence is not included in the candidate set, later components have no chance to use it. This is why Recall@k is an important diagnostic metric.

## Candidate Set

The candidate set is the limited group of chunks passed to later stages. A generator, reranker, or answer synthesizer only sees this subset. If the candidate set lacks the gold evidence, answer quality may drop even if the language model is strong.

A candidate set may be wrong for several reasons. The chunk might be too large and diluted. The evidence might be split across two chunks. The heading might be missing from the embedded text. Or the query may not match the document terminology at all.

## What a Reranker Does

A reranker takes the query and candidate chunks after the initial retrieval step and computes a more precise relevance order. Cross-encoder rerankers are often more accurate than simple vector similarity because they jointly inspect the query and each candidate.

A reranker can improve ranking quality inside the candidate set, but it cannot recover evidence that the initial retriever never returned. This sentence is central for diagnosing retrieval failures: reranking is a ranking-stage repair, not an indexing-stage repair.

## Missing Context

Missing context happens when a retrieved chunk contains a clue but not enough surrounding explanation to support the answer. The retriever may return a sentence such as “this improves the final ordering,” while the previous paragraph explained that “this” refers to a cross-encoder reranker applied after initial retrieval.

In this situation, the chunk is not completely irrelevant; it is incomplete. A local patch can include the neighboring paragraph or create a parent-style chunk that preserves the concept, mechanism, and limitation together.

## Diagnosis Boundary

If the correct evidence appears in top-20 but not top-5, a reranker might help. If the correct section is never retrieved because the chunk boundary damaged the evidence, a chunk patch might help. If the query uses different terminology from the document, query rewrite or hybrid retrieval might be more appropriate.

RecallRAG should record these cases separately. The goal is not to choose one universal fix, but to identify whether the failure is caused by indexing, ranking, or semantic mismatch.
