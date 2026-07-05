# Vector Database and Patch Index Notes

## Embeddings and Metadata

A vector database stores embedded chunks and metadata. The text vector supports similarity search, while metadata supports filtering, tracing, and evaluation. Useful metadata includes document id, section id, start offset, end offset, chunking strategy, and chunk version.

Without metadata, it is hard to debug retrieval failures. A result might look wrong, but the system cannot tell whether it came from the correct document, the wrong section, or an obsolete chunking strategy.

## Main Index

The main index contains the baseline chunks used by the production retrieval path or by the current experiment. It should be stable because many evaluation results, cached answers, and trace records depend on it. Directly deleting and replacing chunks after every failed query is risky.

A full re-chunk and full re-index can be expensive. It creates many new embeddings, changes many chunk identifiers, and may introduce regressions for queries that were already working.

## Chunk Patch Index

A chunk patch index is a small side index that stores only local repair chunks created from diagnosed chunking failures. It does not duplicate the entire corpus. It is used as a shadow validation layer before touching the main index.

The patch index stores new chunks produced from a limited span window or section. Each patch chunk records which main chunks it may replace, which failure case created it, and which strategy generated it. This makes the repair auditable and reversible.

## Hybrid Main Plus Patch Retrieval

During validation, the retriever searches the main index and the patch index separately. The two result lists are merged, deduplicated, and truncated to the final top-k. Patch results should not blindly dominate main results. A replacement-aware merge can prefer a patch chunk only when it covers the same affected region and receives a strong score.

The report should compare main-only retrieval with main-plus-patch retrieval. Important fields include fixed queries, regressed queries, Recall@k, MRR, number of patch chunks, and patch-to-main ratio.

## Accept or Reject

A patch proposal should move through states such as proposed, materialized, evaluated, accepted, rejected, and needs_review. The system should accept a patch only if it improves retrieval for relevant failures without causing unacceptable regression.

This design turns chunk optimization into a controlled engineering loop. Instead of rebuilding the whole index, the system performs a small, measurable, and reversible experiment.
