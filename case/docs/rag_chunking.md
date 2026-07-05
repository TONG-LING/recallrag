# RAG Chunking Failure Notes

## Overview

A retrieval augmented generation system usually converts long documents into smaller chunks before embedding them into a vector index. The chunking stage looks simple, but it decides what evidence can be retrieved later. If a chunk does not preserve a complete semantic unit, the retriever may miss the evidence even when the original document contains the answer. In practice, chunking is not just a preprocessing detail; it is part of the retrieval design.

The simplest baseline is fixed-size chunking. It walks through the document by a fixed number of characters or tokens and optionally keeps a small overlap. This is easy to implement and cheap to run, but it ignores headings, paragraphs, tables, code blocks, and definitions. A fixed-size splitter can cut a definition into two halves or separate an explanation from the concept name that gives it meaning.

## Boundary Split

Boundary split happens when a complete evidence span is separated across two adjacent chunks. The first chunk may contain the concept name and the beginning of the explanation, while the second chunk contains the causal reason or final conclusion. Each chunk alone is only partially relevant, so neither one receives a high enough retrieval score.

Fixed-size chunking can split a complete evidence span across two adjacent chunks, causing each individual chunk to contain only partial support for the answer. Increasing overlap or merging the neighboring chunks can restore the complete evidence unit without rebuilding the whole corpus.

This failure is common in technical writing because the first sentence often introduces a method and the next sentence explains why it works. If these two sentences are separated, the retriever sees a weaker representation. A patch can be generated around the affected span: keep the main index unchanged, create a local overlapping chunk that covers both sentences, and test it in a small patch index.

## Chunk Too Large

The opposite problem is also common. A large chunk can contain the correct sentence, but it may also contain several unrelated topics. The embedding of that chunk becomes an average of many signals, so a specific query may not match it strongly.

For example, one chunk may discuss retriever choice, prompt construction, evaluation metrics, and document cleaning at the same time. A query about chunk boundary errors will match only a small part of the chunk. The answer is technically present, but the chunk vector is semantically diluted.

A local patch does not need to reprocess the whole document. The system can identify the section where the gold evidence lives, cut only that section into smaller heading-aware chunks, and store those new chunks in the patch index. The main index remains untouched until the patch is evaluated.

## Heading-aware Chunking

Headings often carry the key entity name. If the heading is separated from the body, the body chunk may lose the phrase that users search for. A section titled `Boundary Split` followed by a paragraph saying “this failure happens when...” is clear to a human, but the body chunk alone may be ambiguous.

A heading-aware strategy prepends the nearest heading path to each chunk. The text that is embedded can include `RAG Chunking Failure Notes > Boundary Split` before the paragraph body. This small metadata change can improve retrieval without increasing the chunk length very much.

## Patch Index Evaluation

The safe repair workflow is not to delete old chunks immediately. Instead, a failure case produces a patch proposal with a reason, an affected span, and a new local chunking strategy. The patch chunks are embedded into a small patch index. During evaluation, retrieval queries both the main index and patch index, merges the results, and compares main-only with main-plus-patch performance.

A patch should be accepted only if it fixes some failed queries and does not create too many regressions. This makes chunk optimization measurable rather than a manual tuning exercise.
