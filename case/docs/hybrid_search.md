# Hybrid Search Notes

## Dense Retrieval

Dense retrieval embeds a query and document chunks into a vector space. It is useful when the query and document use different words but express similar meaning. A user may ask for “make answers more factual,” while the document may discuss “grounding generation in retrieved evidence.” Dense retrieval can connect these expressions if the embedding model understands the domain.

However, dense retrieval is not perfect. It may miss exact identifiers, function names, rare acronyms, error codes, or product-specific terms. If the embedding model has not learned the domain language, semantically correct evidence may receive a low score.

## Sparse Retrieval

Sparse retrieval methods such as BM25 rely on lexical matching. They are strong when the query contains exact terms from the document. A query with an API name, a parameter such as `top_k`, or an acronym such as `DQN` may benefit from sparse retrieval because the exact token matters.

Sparse retrieval can fail when the user paraphrases the concept. If a document says “lexical matching” and the user asks about “keyword based search,” sparse matching may not connect them well unless the same words appear.

## Why Combine Them

Hybrid search combines dense retrieval with sparse lexical retrieval so that semantic similarity and exact term matching can compensate for each other. Dense retrieval helps with paraphrases, while sparse retrieval protects rare terms, acronyms, IDs, and exact keywords.

This is important for failure diagnosis. If a query fails because the user expression and the document expression are different, re-chunking may not fix the problem. The right recommendation may be query rewrite, multi-query retrieval, or dense-plus-sparse hybrid search.

## Semantic Mismatch Is Not a Chunk Bug

A retrieval failure is not always caused by chunking. Semantic mismatch happens when the evidence is located inside a reasonable chunk, but the query and the chunk still receive a low similarity score because they use different terminology or because the embedding model does not fit the domain.

When semantic mismatch is the likely cause, the system should mark the sample as non_chunk_failure and avoid creating a chunk patch. Generating new chunks for this case would add noise to the patch index without addressing the real retrieval problem.

## Example Failure Pattern

Suppose a document says that “hybrid retrieval fuses dense semantic vectors with sparse lexical scores.” A user asks, “How can we handle exact product codes and paraphrased questions at the same time?” This query may need both semantic and lexical signals. If the current dense-only retriever fails, the diagnosis should suggest hybrid retrieval rather than local re-chunking.

The project should report this boundary clearly. A robust RAG optimization system is valuable not because it patches every failure, but because it knows when not to patch.
