from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from recallrag.diagnose import diagnose_one
from recallrag.embeddings import embed_lmstudio
from recallrag.eval import coverage, evaluate, evaluate_with_reranker, retrieve
from recallrag.patch_index import _make_patch_text
from recallrag.patch_index import (
    _accepted_patch_ids,
    _filter_patch_pairs_by_ids,
    materialize_patches,
    _select_successful_patch_candidates,
)
from recallrag.qdrant_backend import (
    build_qdrant_from_runs,
    eval_qdrant_hybrid_rerank,
    merge_qdrant_results,
)
from recallrag.strong_baselines import HyDEGenerator, build_rrf_fused_rows, rrf_fuse_orders
from recallrag.triage import final_triage


def _write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _question_fingerprint(rows: list[dict]) -> str:
    compact = [
        {
            "qid": row["qid"],
            "question": row.get("question", ""),
            "gold_doc": row.get("gold_doc", ""),
            "gold_section": row.get("gold_section", ""),
        }
        for row in sorted(rows, key=lambda row: row["qid"])
    ]
    return hashlib.sha256(
        json.dumps(compact, ensure_ascii=False, sort_keys=True).encode("utf-8")
    ).hexdigest()


class _FakeHTTPResponse:
    def __init__(self, payload: dict):
        self._payload = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    def read(self):
        return self._payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class _FakeReranker:
    model_name_or_path = "fake-reranker"
    device = "cpu"
    batch_size = 2
    max_length = 256

    def __init__(self, score_by_chunk_id: dict[str, float]):
        self.score_by_chunk_id = score_by_chunk_id

    def rerank(self, query: str, candidates: list[dict], top_k: int | None = None) -> list[dict]:
        rows = []
        for dense_rank, candidate in enumerate(candidates, 1):
            row = dict(candidate)
            row["dense_rank_before_rerank"] = candidate.get(
                "dense_rank_before_rerank",
                candidate.get("rank", dense_rank),
            )
            row["dense_score"] = float(candidate.get("dense_score", candidate.get("score", 0.0)))
            row["rerank_score"] = float(self.score_by_chunk_id.get(candidate["chunk_id"], 0.0))
            row["score"] = row["rerank_score"]
            rows.append(row)
        rows.sort(key=lambda row: row["rerank_score"], reverse=True)
        for rank, row in enumerate(rows, 1):
            row["rank"] = rank
        if top_k is None:
            return rows
        return rows[:top_k]


def _write_qdrant_provenance(
    qdrant_dir: Path,
    base_dir: Path,
    base_results: list[dict],
    patch_source_dir: Path,
    patch_chunks: list[dict] | None = None,
    patch_vectors: list[list[float]] | None = None,
):
    qdrant_dir.mkdir(parents=True, exist_ok=True)
    patch_chunks = patch_chunks or []
    patch_vectors = patch_vectors or []
    patch_hashes = {}
    patch_source = "no_patch_artifacts"
    if patch_chunks or patch_vectors:
        _write_json(patch_source_dir / "selected_patch_chunks.json", patch_chunks)
        _write_json(patch_source_dir / "selected_patch_vectors.json", patch_vectors)
        patch_hashes = {
            "selected_patch_chunks.json": _sha256_file(patch_source_dir / "selected_patch_chunks.json"),
            "selected_patch_vectors.json": _sha256_file(patch_source_dir / "selected_patch_vectors.json"),
        }
        patch_source = "selected_patch_chunks.json"
    _write_json(
        qdrant_dir / "qdrant_meta.json",
        {
            "main_artifact_hashes": {
                "chunks.json": _sha256_file(base_dir / "chunks.json"),
                "vectors.json": _sha256_file(base_dir / "vectors.json"),
            },
            "patch_artifact_hashes": patch_hashes,
            "patch_artifact_source": patch_source,
            "patch_dir": str(patch_source_dir.resolve()),
        },
    )
    _write_json(
        qdrant_dir / "qdrant_eval_meta.json",
        {
            "question_count": len(base_results),
            "question_fingerprint": _question_fingerprint(base_results),
        },
    )


class DiagnoseTests(unittest.TestCase):
    def test_near_miss_trace_produces_patch_candidate_without_gold_localization(self):
        question = {
            "qid": "q1",
            "question": "Why can fixed-size chunking cause a boundary split failure?",
            "gold_doc": "gold.md",
            "gold_section": "Secret > Gold",
            "gold_failure_type": "chunk_failure",
        }
        chunks = [
            {
                "chunk_id": "doc.md::c0000",
                "doc_id": "doc.md",
                "text": "Fixed-size chunking can split a definition across neighboring chunks and hide the causal explanation.",
                "section_path": "RAG Notes > Boundary Split",
                "start_offset": 0,
                "end_offset": 110,
            },
            {
                "chunk_id": "doc.md::c0001",
                "doc_id": "doc.md",
                "text": "The second chunk may carry the missing cause or conclusion that makes the first chunk meaningful.",
                "section_path": "RAG Notes > Boundary Split",
                "start_offset": 111,
                "end_offset": 220,
            },
        ]
        result = {
            "success": False,
            "top_n_trace": [
                {"rank": 1, "chunk_id": "doc.md::c0000"},
                {"rank": 2, "chunk_id": "doc.md::c0001"},
            ],
            "top_k": [
                {"rank": 1, "chunk_id": "doc.md::c0000", "doc_id": "doc.md", "section_path": "RAG Notes > Boundary Split"},
                {"rank": 2, "chunk_id": "doc.md::c0001", "doc_id": "doc.md", "section_path": "RAG Notes > Boundary Split"},
            ],
        }

        diagnosis = diagnose_one(question, chunks, result)

        self.assertTrue(diagnosis["patch_allowed"])
        self.assertEqual("chunking_failure_candidate", diagnosis["failure_family"])
        self.assertEqual("production_near_miss_trace", diagnosis["evidence"]["localization_mode"])
        self.assertEqual("doc.md::c0000", diagnosis["evidence"]["anchor_chunk_id"])

    def test_same_doc_cluster_without_query_overlap_is_not_auto_patched(self):
        question = {
            "qid": "q2",
            "question": "Why does chunk boundary splitting hurt answer recall?",
            "gold_doc": "gold.md",
            "gold_section": "Secret > Gold",
            "gold_failure_type": "chunk_failure",
        }
        chunks = [
            {
                "chunk_id": "wrong.md::c0000",
                "doc_id": "wrong.md",
                "text": "Vitamin intake and diet planning for adults.",
                "section_path": "Nutrition > Overview",
                "start_offset": 0,
                "end_offset": 60,
            },
            {
                "chunk_id": "wrong.md::c0001",
                "doc_id": "wrong.md",
                "text": "Dietary supplements and meal frequency suggestions.",
                "section_path": "Nutrition > Overview",
                "start_offset": 61,
                "end_offset": 120,
            },
        ]
        result = {
            "success": False,
            "top_n_trace": [
                {"rank": 1, "chunk_id": "wrong.md::c0000"},
                {"rank": 2, "chunk_id": "wrong.md::c0001"},
            ],
            "top_k": [
                {"rank": 1, "chunk_id": "wrong.md::c0000", "doc_id": "wrong.md", "section_path": "Nutrition > Overview"},
                {"rank": 2, "chunk_id": "wrong.md::c0001", "doc_id": "wrong.md", "section_path": "Nutrition > Overview"},
            ],
        }

        diagnosis = diagnose_one(question, chunks, result)

        self.assertFalse(diagnosis["patch_allowed"])
        self.assertEqual("non_chunk_or_uncertain_failure", diagnosis["failure_family"])

    def test_strong_single_anchor_overlap_can_still_patch(self):
        question = {
            "qid": "q3",
            "question": "How does local context loss reduce retrieval quality?",
            "gold_doc": "gold.md",
            "gold_section": "Secret > Gold",
            "gold_failure_type": "chunk_failure",
        }
        chunks = [
            {
                "chunk_id": "doc.md::c0002",
                "doc_id": "doc.md",
                "text": "Local context loss reduces retrieval quality because the explanation is split and only half the evidence is returned.",
                "section_path": "RAG Notes > Local Context",
                "start_offset": 0,
                "end_offset": 120,
            }
        ]
        result = {
            "success": False,
            "top_n_trace": [{"rank": 4, "chunk_id": "doc.md::c0002"}],
            "top_k": [{"rank": 4, "chunk_id": "doc.md::c0002", "doc_id": "doc.md", "section_path": "RAG Notes > Local Context"}],
        }

        diagnosis = diagnose_one(question, chunks, result)

        self.assertTrue(diagnosis["patch_allowed"])
        self.assertEqual("chunking_failure_candidate", diagnosis["failure_family"])


class PatchTextTests(unittest.TestCase):
    def test_patch_text_excludes_query_id_and_diagnosis_metadata(self):
        question = "Why does query leakage make retrieval experiments invalid?"
        text = _make_patch_text(
            "contextual",
            "q001",
            question,
            "Audit > Leakage",
            "missing_local_context_candidate",
            (
                "Query leakage makes retrieval experiments invalid because the patch text "
                "can match the failed query through copied metadata instead of real evidence."
            ),
        )

        self.assertNotIn("q001", text)
        self.assertNotIn("missing_local_context_candidate", text)
        self.assertNotIn(question, text)
        self.assertIn("Section: Audit > Leakage", text)

    def test_materialize_patches_does_not_fallback_to_gold_section(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            index_dir = root / "runs/base"
            out_dir = root / "runs/patches"

            _write_json(
                index_dir / "chunks.json",
                [
                    {
                        "chunk_id": "doc.md::c0000",
                        "doc_id": "doc.md",
                        "text": "Chunk boundary splitting can hide the missing explanation across neighbors.",
                        "section_path": "",
                        "start_offset": 0,
                        "end_offset": 80,
                    },
                    {
                        "chunk_id": "doc.md::c0001",
                        "doc_id": "doc.md",
                        "text": "The second chunk contains the evidence that completes the first one.",
                        "section_path": "",
                        "start_offset": 81,
                        "end_offset": 160,
                    },
                ],
            )
            _write_json(
                index_dir / "failure_diagnosis.json",
                [
                    {
                        "qid": "q_leak",
                        "question": "Why does boundary splitting hurt recall?",
                        "gold_doc": "doc.md",
                        "gold_section": "Secret > Gold Label",
                        "diagnosed_failure_type": "missing_local_context_candidate",
                        "patch_allowed": True,
                        "confidence": 0.8,
                        "reason": "localized near miss",
                        "evidence": {
                            "candidate_window_chunk_ids": ["doc.md::c0000", "doc.md::c0001"],
                            "anchor_chunk_id": "doc.md::c0000",
                            "localization_mode": "production_near_miss_trace",
                        },
                    }
                ],
            )

            with patch("recallrag.patch_index.embed_lmstudio", return_value=[[0.1, 0.2, 0.3]] * 4):
                patch_chunks, _ = materialize_patches(index_dir=index_dir, out_dir=out_dir)

            self.assertEqual(4, len(patch_chunks))
            for chunk in patch_chunks:
                self.assertEqual("", chunk["section_path"])
                self.assertNotIn("Secret > Gold Label", chunk["text"])
                self.assertFalse(chunk["text"].startswith("Section:"))

    def test_coverage_requires_exact_token_matches(self):
        self.assertEqual(0.0, coverage("is", "this"))
        self.assertEqual(0.0, coverage("rank search", "reranker"))
        self.assertEqual(1.0, coverage("bm25 dense", "bm25 dense retrieval"))

    def test_coverage_supports_chinese_span_overlap(self):
        score = coverage("国家法定节假日全年一共有11天", "目前国家法定节假日全年一共有11天，法定休息日每年52个周末总共104天。")
        self.assertGreaterEqual(score, 0.8)


class StrongBaselineTests(unittest.TestCase):
    def test_rrf_prefers_consensus_candidate(self):
        fused = rrf_fuse_orders([0, 2, 3], [1, 2, 4], rrf_k=60)
        self.assertGreater(fused[2], fused[0])
        self.assertGreater(fused[2], fused[1])

    def test_build_rrf_rows_keeps_rank_metadata(self):
        chunks = [
            {"chunk_id": "c0", "doc_id": "d0", "text": "a"},
            {"chunk_id": "c1", "doc_id": "d1", "text": "b"},
            {"chunk_id": "c2", "doc_id": "d2", "text": "c"},
        ]
        dense_scores = [0.9, 0.2, 0.8]
        bm25_scores = [0.1, 0.95, 0.7]
        rows = build_rrf_fused_rows(chunks, dense_scores, bm25_scores, [0, 2], [1, 2], rrf_k=60)

        self.assertEqual("c2", rows[0]["chunk_id"])
        self.assertEqual(2, rows[0]["dense_rank_before_fusion"])
        self.assertEqual(2, rows[0]["bm25_rank_before_fusion"])
        self.assertIn("rrf_score", rows[0])

    def test_hyde_messages_protocol_extracts_text_and_disables_thinking(self):
        captured = {}
        response = _FakeHTTPResponse(
            {
                "content": [
                    {"type": "thinking", "thinking": "skip me"},
                    {"type": "text", "text": "这是生成出来的假设文档。"},
                ]
            }
        )

        def _fake_urlopen(req, timeout=60):
            captured["headers"] = {k.lower(): v for k, v in req.header_items()}
            captured["payload"] = json.loads(req.data.decode("utf-8"))
            return response

        with patch("recallrag.strong_baselines.urllib.request.urlopen", side_effect=_fake_urlopen):
            text = HyDEGenerator(
                endpoint="https://fake.example/v1/messages",
                model="deepseek-v4-flash",
                protocol="messages",
                api_key="test-key",
                auth_mode="x-api-key",
                disable_thinking=True,
            ).generate("为什么 chunk 会断裂")

        self.assertEqual("这是生成出来的假设文档。", text)
        self.assertEqual("test-key", captured["headers"]["x-api-key"])
        self.assertEqual("2023-06-01", captured["headers"]["anthropic-version"])
        self.assertEqual({"type": "disabled"}, captured["payload"]["thinking"])


class EmbeddingValidationTests(unittest.TestCase):
    def test_embed_lmstudio_accepts_complete_out_of_order_indexes(self):
        response = _FakeHTTPResponse(
            {
                "data": [
                    {"index": 1, "embedding": [0.0, 3.0]},
                    {"index": 0, "embedding": [4.0, 0.0]},
                ]
            }
        )

        with patch("recallrag.embeddings.urllib.request.urlopen", return_value=response):
            with patch("recallrag.embeddings.time.sleep", return_value=None):
                vectors = embed_lmstudio(
                    ["first text", "second text"],
                    endpoint="http://fake",
                    model="fake",
                    batch_size=2,
                    normalize=False,
                )

        self.assertEqual([[4.0, 0.0], [0.0, 3.0]], vectors)

    def test_embed_lmstudio_rejects_missing_embedding_rows(self):
        response = _FakeHTTPResponse(
            {
                "data": [
                    {"index": 0, "embedding": [0.1, 0.2, 0.3]},
                ]
            }
        )

        with patch("recallrag.embeddings.urllib.request.urlopen", return_value=response):
            with patch("recallrag.embeddings.time.sleep", return_value=None):
                with self.assertRaisesRegex(RuntimeError, "returned 1 vectors for 2 texts"):
                    embed_lmstudio(
                        ["first text", "second text"],
                        endpoint="http://fake",
                        model="fake",
                        batch_size=2,
                    )

    def test_embed_lmstudio_rejects_inconsistent_dimensions_across_batches(self):
        responses = [
            _FakeHTTPResponse(
                {
                    "data": [
                        {"index": 0, "embedding": [0.1, 0.2]},
                        {"index": 1, "embedding": [0.3, 0.4]},
                    ]
                }
            ),
            _FakeHTTPResponse(
                {
                    "data": [
                        {"index": 0, "embedding": [0.5, 0.6, 0.7]},
                    ]
                }
            ),
        ]

        with patch("recallrag.embeddings.urllib.request.urlopen", side_effect=responses):
            with patch("recallrag.embeddings.time.sleep", return_value=None):
                with self.assertRaisesRegex(RuntimeError, "embedding dim 3 != expected dim 2"):
                    embed_lmstudio(
                        ["first text", "second text", "third text"],
                        endpoint="http://fake",
                        model="fake",
                        batch_size=2,
                    )

    def test_retrieve_rejects_chunk_vector_count_mismatch(self):
        with self.assertRaises(RuntimeError):
            retrieve(
                [0.1, 0.2],
                [
                    {"chunk_id": "doc::c1", "doc_id": "doc.md", "text": "one"},
                    {"chunk_id": "doc::c2", "doc_id": "doc.md", "text": "two"},
                ],
                [[0.1, 0.2]],
                top_k=1,
            )

    def test_evaluate_rejects_missing_query_vectors(self):
        chunks = [{"chunk_id": "doc::c1", "doc_id": "doc.md", "text": "boundary split explanation"}]
        vectors = [[0.1, 0.2, 0.3]]
        questions = [
            {"qid": "q1", "question": "What is a boundary split failure?", "gold_doc": "doc.md", "gold_span": "boundary split"},
            {"qid": "q2", "question": "Why does local context matter?", "gold_doc": "doc.md", "gold_span": "local context"},
        ]

        with patch("recallrag.eval.embed_lmstudio", return_value=[[0.1, 0.2, 0.3]]):
            with self.assertRaises(RuntimeError):
                evaluate(chunks, vectors, questions, endpoint="http://fake", model="fake")

    def test_evaluate_with_reranker_can_fix_candidate_set_ranking(self):
        chunks = [
            {"chunk_id": "doc::c_bad", "doc_id": "doc.md", "text": "无关解释", "section_path": "Wrong"},
            {"chunk_id": "doc::c_gold", "doc_id": "doc.md", "text": "这里包含 关键 答案 和完整解释", "section_path": "Gold"},
            {"chunk_id": "doc::c_other", "doc_id": "other.md", "text": "其他内容", "section_path": "Other"},
        ]
        vectors = [
            [0.95, 0.0],
            [0.90, 0.0],
            [0.80, 0.0],
        ]
        questions = [
            {
                "qid": "q1",
                "question": "什么是关键答案",
                "gold_doc": "doc.md",
                "gold_section": "Gold",
                "gold_span": "关键 答案",
            }
        ]
        reranker = _FakeReranker(
            {
                "doc::c_bad": 0.1,
                "doc::c_gold": 0.9,
                "doc::c_other": 0.2,
            }
        )

        with patch("recallrag.eval.embed_lmstudio", return_value=[[1.0, 0.0]]):
            results, metrics = evaluate_with_reranker(
                chunks,
                vectors,
                questions,
                endpoint="http://fake",
                model="fake",
                top_k=2,
                candidate_k=3,
                coverage_threshold=0.65,
                reranker=reranker,
            )

        self.assertEqual(1.0, metrics["dense_recall@2"])
        self.assertEqual(1.0, metrics["recall@2"])
        self.assertEqual("doc::c_gold", results[0]["top_k"][0]["chunk_id"])
        self.assertTrue(results[0]["rerank_improved"])
        self.assertFalse(results[0]["rerank_fixed"])
        self.assertEqual(2, results[0]["first_relevant_candidate_rank_before_rerank"])

    def test_evaluate_with_reranker_marks_fixed_when_gold_was_below_topk(self):
        chunks = [
            {"chunk_id": "doc::c_bad", "doc_id": "doc.md", "text": "无关解释", "section_path": "Wrong"},
            {"chunk_id": "doc::c_gold", "doc_id": "doc.md", "text": "这里包含 关键 答案 和完整解释", "section_path": "Gold"},
        ]
        vectors = [
            [0.95, 0.0],
            [0.90, 0.0],
        ]
        questions = [
            {
                "qid": "q1",
                "question": "什么是关键答案",
                "gold_doc": "doc.md",
                "gold_section": "Gold",
                "gold_span": "关键 答案",
            }
        ]
        reranker = _FakeReranker(
            {
                "doc::c_bad": 0.1,
                "doc::c_gold": 0.9,
            }
        )

        with patch("recallrag.eval.embed_lmstudio", return_value=[[1.0, 0.0]]):
            results, metrics = evaluate_with_reranker(
                chunks,
                vectors,
                questions,
                endpoint="http://fake",
                model="fake",
                top_k=1,
                candidate_k=2,
                coverage_threshold=0.65,
                reranker=reranker,
            )

        self.assertEqual(0.0, metrics["dense_recall@1"])
        self.assertEqual(1.0, metrics["recall@1"])
        self.assertTrue(results[0]["rerank_fixed"])
        self.assertFalse(results[0]["success_before_rerank"])
        self.assertEqual("doc::c_bad", results[0]["top_k_before_rerank"][0]["chunk_id"])
        self.assertEqual("doc::c_gold", results[0]["top_k"][0]["chunk_id"])


class TriageTests(unittest.TestCase):
    def test_final_triage_accepts_patch_and_downgrades_bm25_sensitive_failures(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            base_dir = root / "runs/base"
            patch_dir = root / "runs/hybrid"
            bm25_dir = root / "runs/hybrid_bm25"
            qdrant_dir = root / "runs/qdrant"
            out_dir = root / "runs/triage"

            _write_json(
                base_dir / "failure_diagnosis.json",
                [
                    {
                        "qid": "q_patch",
                        "question": "What causes a boundary split failure?",
                        "gold_doc": "doc.md",
                        "gold_section": "Notes > Boundary Split",
                        "diagnosed_failure_type": "missing_local_context_candidate",
                        "failure_family": "chunking_failure_candidate",
                        "patch_allowed": True,
                        "confidence": 0.81,
                        "reason": "near miss localized",
                        "recommendation": "generate_local_proposition_patch_candidates_and_validate",
                    },
                    {
                        "qid": "q_bm25",
                        "question": "What is BM25 good at?",
                        "gold_doc": "lexical.md",
                        "gold_section": "Notes > BM25",
                        "diagnosed_failure_type": "missing_local_context_candidate",
                        "failure_family": "chunking_failure_candidate",
                        "patch_allowed": True,
                        "confidence": 0.77,
                        "reason": "near miss localized",
                        "recommendation": "generate_local_proposition_patch_candidates_and_validate",
                    },
                ],
            )
            _write_json(
                base_dir / "retrieval_results.json",
                [
                    {
                        "qid": "q_patch",
                        "question": "What causes a boundary split failure?",
                        "gold_doc": "doc.md",
                        "gold_section": "Notes > Boundary Split",
                        "success": False,
                        "best_topk_coverage": 0.41,
                    },
                    {
                        "qid": "q_bm25",
                        "question": "What is BM25 good at?",
                        "gold_doc": "lexical.md",
                        "gold_section": "Notes > BM25",
                        "success": False,
                        "best_topk_coverage": 0.32,
                    },
                ],
            )
            _write_json(
                patch_dir / "retrieval_results.json",
                [
                    {"qid": "q_patch", "success": True, "best_topk_coverage": 1.0},
                    {"qid": "q_bm25", "success": False, "best_topk_coverage": 0.42},
                ],
            )
            _write_json(
                patch_dir / "patch_decisions.json",
                [
                    {"qid": "q_patch", "status": "accepted", "candidate_type": "contextual"},
                    {"qid": "q_bm25", "status": "candidate_not_selected", "candidate_type": "contextual"},
                ],
            )
            _write_json(
                bm25_dir / "hybrid_bm25_results.json",
                {
                    "bm25": [
                        {"qid": "q_patch", "success": False},
                        {"qid": "q_bm25", "success": True},
                    ],
                    "dense_bm25": [
                        {"qid": "q_patch", "success": False},
                        {"qid": "q_bm25", "success": True},
                    ],
                },
            )

            summary = final_triage(base_dir, patch_dir, bm25_dir, qdrant_dir, out_dir)
            rows = {row["qid"]: row for row in summary["rows"]}

            self.assertEqual(1, summary["accepted_patch_candidates"])
            self.assertEqual(1, summary["retrieval_strategy_sensitive"])
            self.assertEqual("accepted_patch_candidate", rows["q_patch"]["final_decision"])
            self.assertEqual("chunking_failure", rows["q_patch"]["final_family"])
            self.assertEqual("retrieval_strategy_sensitive", rows["q_bm25"]["final_family"])
            self.assertEqual("needs_review", rows["q_bm25"]["final_decision"])
            self.assertTrue((out_dir / "final_triage_report.md").exists())

    def test_final_triage_does_not_accept_unapproved_patch(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            base_dir = root / "runs/base"
            patch_dir = root / "runs/hybrid"
            bm25_dir = root / "runs/hybrid_bm25"
            qdrant_dir = root / "runs/qdrant"
            patch_source_dir = root / "runs/patches"
            out_dir = root / "runs/triage"

            _write_json(
                base_dir / "failure_diagnosis.json",
                [
                    {
                        "qid": "q_patch",
                        "question": "What causes a boundary split failure?",
                        "gold_doc": "doc.md",
                        "gold_section": "Notes > Boundary Split",
                        "diagnosed_failure_type": "missing_local_context_candidate",
                        "failure_family": "chunking_failure_candidate",
                        "patch_allowed": True,
                        "confidence": 0.81,
                        "reason": "near miss localized",
                        "recommendation": "generate_local_proposition_patch_candidates_and_validate",
                    }
                ],
            )
            _write_json(
                base_dir / "retrieval_results.json",
                [
                    {
                        "qid": "q_patch",
                        "question": "What causes a boundary split failure?",
                        "gold_doc": "doc.md",
                        "gold_section": "Notes > Boundary Split",
                        "success": False,
                        "best_topk_coverage": 0.41,
                    }
                ],
            )
            _write_json(
                base_dir / "chunks.json",
                [{"chunk_id": "doc::c1", "doc_id": "doc.md", "text": "boundary split explanation"}],
            )
            _write_json(base_dir / "vectors.json", [[0.1, 0.2, 0.3]])
            _write_json(
                patch_dir / "retrieval_results.json",
                [{"qid": "q_patch", "success": True, "best_topk_coverage": 0.7}],
            )
            _write_json(
                patch_dir / "patch_decisions.json",
                [{"qid": "q_patch", "patch_id": "patch1", "status": "needs_review", "candidate_type": "contextual"}],
            )
            _write_json(
                bm25_dir / "hybrid_bm25_results.json",
                {
                    "bm25": [{"qid": "q_patch", "success": False}],
                    "dense_bm25": [{"qid": "q_patch", "success": False}],
                },
            )
            _write_json(
                qdrant_dir / "qdrant_retrieval_results.json",
                [
                    {
                        "qid": "q_patch",
                        "question": "What causes a boundary split failure?",
                        "gold_doc": "doc.md",
                        "gold_section": "Notes > Boundary Split",
                        "success": True,
                        "best_topk_coverage": 0.7,
                    }
                ],
            )
            _write_qdrant_provenance(
                qdrant_dir,
                base_dir,
                _load_json(base_dir / "retrieval_results.json"),
                patch_source_dir,
                patch_chunks=[{"patch_id": "patch1", "chunk_id": "patch1::c1"}],
                patch_vectors=[[0.1, 0.2, 0.3]],
            )

            summary = final_triage(base_dir, patch_dir, bm25_dir, qdrant_dir, out_dir)
            row = summary["rows"][0]

            self.assertEqual("needs_review", row["final_decision"])
            self.assertEqual("patch_validation_inconclusive", row["final_family"])

    def test_final_triage_does_not_read_qdrant_unless_explicit(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            base_dir = root / "runs/base"
            patch_dir = root / "runs/hybrid"
            bm25_dir = root / "runs/hybrid_bm25"
            qdrant_dir = root / "runs/qdrant"
            out_dir = root / "runs/triage"

            _write_json(
                base_dir / "failure_diagnosis.json",
                [
                    {
                        "qid": "q_patch",
                        "question": "What causes a boundary split failure?",
                        "gold_doc": "doc.md",
                        "gold_section": "Notes > Boundary Split",
                        "diagnosed_failure_type": "missing_local_context_candidate",
                        "failure_family": "chunking_failure_candidate",
                        "patch_allowed": True,
                        "confidence": 0.81,
                        "reason": "near miss localized",
                        "recommendation": "generate_local_proposition_patch_candidates_and_validate",
                    }
                ],
            )
            _write_json(
                base_dir / "retrieval_results.json",
                [
                    {
                        "qid": "q_patch",
                        "question": "What causes a boundary split failure?",
                        "gold_doc": "doc.md",
                        "gold_section": "Notes > Boundary Split",
                        "success": False,
                        "best_topk_coverage": 0.41,
                    }
                ],
            )
            _write_json(
                patch_dir / "retrieval_results.json",
                [{"qid": "q_patch", "success": False, "best_topk_coverage": 0.42}],
            )
            _write_json(
                patch_dir / "patch_decisions.json",
                [{"qid": "q_patch", "patch_id": "patch1", "status": "needs_review", "candidate_type": "contextual"}],
            )
            _write_json(
                bm25_dir / "hybrid_bm25_results.json",
                {
                    "bm25": [{"qid": "q_patch", "success": False}],
                    "dense_bm25": [{"qid": "q_patch", "success": False}],
                },
            )
            _write_json(
                qdrant_dir / "qdrant_retrieval_results.json",
                [
                    {
                        "qid": "q_patch",
                        "question": "What causes a boundary split failure?",
                        "gold_doc": "doc.md",
                        "gold_section": "Notes > Boundary Split",
                        "success": True,
                        "best_topk_coverage": 1.0,
                    }
                ],
            )

            summary = final_triage(base_dir, patch_dir, bm25_dir, None, out_dir)

            self.assertEqual("manual_review", summary["rows"][0]["final_decision"])

    def test_final_triage_rejects_stale_qdrant_artifacts(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            base_dir = root / "runs/base"
            patch_dir = root / "runs/hybrid"
            bm25_dir = root / "runs/hybrid_bm25"
            qdrant_dir = root / "runs/qdrant"
            patch_source_dir = root / "runs/patches"
            out_dir = root / "runs/triage"

            _write_json(
                base_dir / "failure_diagnosis.json",
                [
                    {
                        "qid": "q_patch",
                        "question": "What causes a boundary split failure?",
                        "gold_doc": "doc.md",
                        "gold_section": "Notes > Boundary Split",
                        "diagnosed_failure_type": "missing_local_context_candidate",
                        "failure_family": "chunking_failure_candidate",
                        "patch_allowed": True,
                        "confidence": 0.81,
                        "reason": "near miss localized",
                        "recommendation": "generate_local_proposition_patch_candidates_and_validate",
                    }
                ],
            )
            _write_json(
                base_dir / "retrieval_results.json",
                [
                    {
                        "qid": "q_patch",
                        "question": "What causes a boundary split failure?",
                        "gold_doc": "doc.md",
                        "gold_section": "Notes > Boundary Split",
                        "success": False,
                        "best_topk_coverage": 0.41,
                    }
                ],
            )
            _write_json(
                base_dir / "chunks.json",
                [{"chunk_id": "doc::c1", "doc_id": "doc.md", "text": "boundary split explanation"}],
            )
            _write_json(base_dir / "vectors.json", [[0.1, 0.2, 0.3]])
            _write_json(
                patch_dir / "retrieval_results.json",
                [{"qid": "q_patch", "success": False, "best_topk_coverage": 0.42}],
            )
            _write_json(patch_dir / "patch_decisions.json", [])
            _write_json(
                bm25_dir / "hybrid_bm25_results.json",
                {
                    "bm25": [{"qid": "q_patch", "success": False}],
                    "dense_bm25": [{"qid": "q_patch", "success": False}],
                },
            )
            _write_json(
                qdrant_dir / "qdrant_retrieval_results.json",
                [
                    {
                        "qid": "q_patch",
                        "question": "What causes a boundary split failure?",
                        "gold_doc": "doc.md",
                        "gold_section": "Notes > Boundary Split",
                        "success": True,
                        "best_topk_coverage": 0.7,
                    }
                ],
            )
            _write_qdrant_provenance(
                qdrant_dir,
                base_dir,
                _load_json(base_dir / "retrieval_results.json"),
                patch_source_dir,
            )
            _write_json(base_dir / "vectors.json", [[0.9, 0.8, 0.7]])

            with self.assertRaises(RuntimeError):
                final_triage(base_dir, patch_dir, bm25_dir, qdrant_dir, out_dir)


class QdrantMergeTests(unittest.TestCase):
    def test_lower_scoring_patch_cannot_evict_main_chunk(self):
        main_points = [
            {"id": "m1", "score": 0.82, "payload": {"chunk_id": "doc::c1", "doc_id": "doc.md"}},
            {"id": "m2", "score": 0.76, "payload": {"chunk_id": "doc::c4", "doc_id": "doc.md"}},
            {"id": "m3", "score": 0.75, "payload": {"chunk_id": "doc::c5", "doc_id": "doc.md"}},
        ]
        patch_points = [
            {
                "id": "p1",
                "score": 0.64,
                "payload": {
                    "chunk_id": "patch::c1",
                    "doc_id": "doc.md",
                    "source_index": "patch",
                    "replaces": ["doc::c4"],
                    "active": True,
                },
            }
        ]

        merged = merge_qdrant_results(main_points, patch_points, final_k=3)

        self.assertEqual(["doc::c1", "doc::c4", "doc::c5"], [row["chunk_id"] for row in merged])

    def test_higher_scoring_patch_can_replace_main_chunk(self):
        main_points = [
            {"id": "m1", "score": 0.82, "payload": {"chunk_id": "doc::c1", "doc_id": "doc.md"}},
            {"id": "m2", "score": 0.71, "payload": {"chunk_id": "doc::c4", "doc_id": "doc.md"}},
            {"id": "m3", "score": 0.70, "payload": {"chunk_id": "doc::c5", "doc_id": "doc.md"}},
        ]
        patch_points = [
            {
                "id": "p1",
                "score": 0.79,
                "payload": {
                    "chunk_id": "patch::c1",
                    "doc_id": "doc.md",
                    "source_index": "patch",
                    "replaces": ["doc::c4"],
                    "active": True,
                },
            }
        ]

        merged = merge_qdrant_results(main_points, patch_points, final_k=3)

        self.assertEqual(["doc::c1", "patch::c1", "doc::c5"], [row["chunk_id"] for row in merged])

    def test_qdrant_build_requires_selected_patch_artifacts(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            base_dir = root / "runs/base"
            patch_dir = root / "runs/patches"
            _write_json(base_dir / "chunks.json", [])
            _write_json(base_dir / "vectors.json", [])
            _write_json(patch_dir / "patch_chunks.json", [{"chunk_id": "patch::c1"}])
            _write_json(patch_dir / "patch_vectors.json", [[0.1, 0.2]])

            with self.assertRaises(RuntimeError):
                build_qdrant_from_runs(base_dir, patch_dir, out_dir=root / "runs/qdrant")

    def test_qdrant_rerank_can_fix_main_patch_candidate_order(self):
        reranker = _FakeReranker(
            {
                "main::c1": 0.1,
                "main::c2": 0.2,
                "patch::c1": 0.9,
            }
        )
        main_points = [
            {"id": "m1", "score": 0.92, "payload": {"chunk_id": "main::c1", "doc_id": "doc.md", "text": "无关材料", "source_index": "main"}},
            {"id": "m2", "score": 0.88, "payload": {"chunk_id": "main::c2", "doc_id": "doc.md", "text": "还是无关材料", "source_index": "main"}},
        ]
        patch_points = [
            {
                "id": "p1",
                "score": 0.83,
                "payload": {
                    "chunk_id": "patch::c1",
                    "doc_id": "doc.md",
                    "text": "这里包含 关键 答案 和完整解释",
                    "source_index": "patch",
                    "active": True,
                    "replaces": [],
                },
            }
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            questions_path = Path(tmpdir) / "questions.jsonl"
            questions_path.write_text(
                json.dumps(
                    {
                        "qid": "q1",
                        "question": "什么是关键答案",
                        "gold_doc": "doc.md",
                        "gold_section": "Gold",
                        "gold_span": "关键 答案",
                    },
                    ensure_ascii=False,
                ) + "\n",
                encoding="utf-8",
            )
            out_dir = Path(tmpdir) / "runs/qdrant_rerank"
            with patch("recallrag.qdrant_backend.embed_lmstudio", return_value=[[1.0, 0.0]]):
                with patch("recallrag.qdrant_backend.search_collection", side_effect=[main_points, patch_points]):
                    results, metrics = eval_qdrant_hybrid_rerank(
                        questions_path=questions_path,
                        url="http://fake",
                        main_collection="main",
                        patch_collection="patch",
                        endpoint="http://fake",
                        model="fake",
                        main_k=2,
                        patch_k=1,
                        final_k=2,
                        coverage_threshold=0.65,
                        reranker=reranker,
                        out_dir=out_dir,
                    )

        self.assertEqual(0.0, metrics["dense_recall@2"])
        self.assertEqual(1.0, metrics["recall@2"])
        self.assertTrue(results[0]["rerank_fixed"])
        self.assertEqual("patch::c1", results[0]["top_k"][0]["chunk_id"])
        self.assertEqual("main::c1", results[0]["top_k_before_rerank"][0]["chunk_id"])


class PatchArtifactTests(unittest.TestCase):
    def test_only_accepted_patch_ids_are_kept_for_online_shadow_index(self):
        patch_chunks = [
            {"patch_id": "p1", "chunk_id": "p1::c1"},
            {"patch_id": "p2", "chunk_id": "p2::c1"},
        ]
        patch_vectors = [[0.1, 0.2], [0.3, 0.4]]
        decisions = [
            {"patch_id": "p1", "status": "accepted"},
            {"patch_id": "p2", "status": "needs_review"},
        ]

        accepted_ids = _accepted_patch_ids(decisions)
        kept_chunks, kept_vectors = _filter_patch_pairs_by_ids(patch_chunks, patch_vectors, accepted_ids)

        self.assertEqual({"p1"}, accepted_ids)
        self.assertEqual(["p1"], [row["patch_id"] for row in kept_chunks])
        self.assertEqual([[0.1, 0.2]], kept_vectors)

    def test_patch_selection_prefers_stronger_coverage_before_shorter_length(self):
        candidate_probe = [
            {
                "qid": "q1",
                "patch_id": "p_short",
                "candidate_type": "contextual",
                "success": True,
                "rank": 3,
                "text_len": 520,
                "best_topk_coverage": 0.68,
            },
            {
                "qid": "q1",
                "patch_id": "p_strong",
                "candidate_type": "adjacent_merge",
                "success": True,
                "rank": 1,
                "text_len": 830,
                "best_topk_coverage": 0.76,
            },
        ]

        selected = _select_successful_patch_candidates(candidate_probe)

        self.assertEqual("p_strong", selected["q1"]["patch_id"])


if __name__ == "__main__":
    unittest.main()
