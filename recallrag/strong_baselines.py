from __future__ import annotations

import json
import urllib.error
import urllib.request
from pathlib import Path

from .bm25 import BM25Index
from .embeddings import embed_lmstudio, dot, require_equal_length, require_vector_dimensions
from .eval import (
    _top_row,
    _trace_row,
    build_ranked_result,
    first_relevant_rank,
    load_questions,
    relevance_score,
)
from .reranker import LocalCrossEncoderReranker


def _load_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _write_json(path: str | Path, obj):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


class HyDEGenerator:
    def __init__(
        self,
        endpoint: str = "http://localhost:1234/v1/chat/completions",
        model: str = "hy-mt2-1.8b",
        protocol: str = "openai_chat",
        temperature: float = 0.0,
        max_tokens: int = 160,
        api_key: str | None = None,
        auth_mode: str = "auto",
        api_version: str = "2023-06-01",
        disable_thinking: bool = False,
    ):
        self.endpoint = endpoint
        self.model = model
        self.protocol = self._normalize_protocol(protocol)
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.api_key = api_key
        self.auth_mode = auth_mode
        self.api_version = api_version
        self.disable_thinking = disable_thinking

    @staticmethod
    def _normalize_protocol(protocol: str) -> str:
        if protocol in {"openai_chat", "messages", "anthropic_messages"}:
            return "messages" if protocol == "anthropic_messages" else protocol
        raise RuntimeError(
            f"Unsupported HyDE protocol `{protocol}`. Expected one of: "
            "`openai_chat`, `messages`, `anthropic_messages`."
        )

    def _headers(self) -> dict[str, str]:
        headers = {"Content-Type": "application/json"}
        auth_mode = self.auth_mode
        if auth_mode == "auto":
            auth_mode = "x-api-key" if self.protocol == "messages" else "authorization"
        if auth_mode not in {"none", "authorization", "x-api-key"}:
            raise RuntimeError(
                f"Unsupported HyDE auth mode `{self.auth_mode}`. Expected one of: "
                "`auto`, `none`, `authorization`, `x-api-key`."
            )
        if self.protocol == "messages":
            headers["anthropic-version"] = self.api_version
        if self.api_key:
            if auth_mode == "authorization":
                headers["Authorization"] = f"Bearer {self.api_key}"
            elif auth_mode == "x-api-key":
                headers["x-api-key"] = self.api_key
        return headers

    @staticmethod
    def _system_prompt() -> str:
        return (
            "你是检索增强助手。请根据问题写一小段可能出现在知识库里的中文材料，"
            "帮助向量检索更容易命中相关文档。只输出正文，不要解释任务。"
        )

    @staticmethod
    def _user_prompt(question: str) -> str:
        return (
            "请围绕下面的问题，写一段 80 到 160 字的中文材料。要求："
            "尽量像知识库正文，可以包含定义、原因、症状、步骤、结论等关键信息，"
            "不要写多余前后缀。"
            f"问题：{question}"
        )

    def _payload(self, question: str) -> dict:
        if self.protocol == "openai_chat":
            return {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": self._system_prompt()},
                    {"role": "user", "content": self._user_prompt(question)},
                ],
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
            }
        payload = {
            "model": self.model,
            "system": self._system_prompt(),
            "messages": [{"role": "user", "content": self._user_prompt(question)}],
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }
        if self.disable_thinking:
            payload["thinking"] = {"type": "disabled"}
        return payload

    @staticmethod
    def _extract_openai_chat_text(data: dict) -> str:
        choices = data.get("choices") or []
        if not choices:
            raise RuntimeError("HyDE request returned no choices.")
        message = choices[0].get("message") or {}
        content = message.get("content") or ""
        if isinstance(content, list):
            parts = []
            for item in content:
                if isinstance(item, dict) and item.get("type") == "text" and item.get("text"):
                    parts.append(str(item["text"]))
            content = "\n".join(parts)
        content = str(content).strip()
        if not content:
            raise RuntimeError("HyDE request returned empty content.")
        return content

    @staticmethod
    def _extract_messages_text(data: dict) -> str:
        content = data.get("content") or []
        if isinstance(content, str):
            content = [{"type": "text", "text": content}]
        if not isinstance(content, list):
            raise RuntimeError("HyDE request returned invalid `content` payload.")
        parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text" and item.get("text"):
                parts.append(str(item["text"]))
        text = "\n".join(parts).strip()
        if not text:
            raise RuntimeError("HyDE request returned empty text content.")
        return text

    def generate(self, question: str) -> str:
        payload = self._payload(question)
        req = urllib.request.Request(
            self.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers=self._headers(),
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=60) as response:
                data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "ignore")
            raise RuntimeError(f"HyDE request failed: HTTP {exc.code}: {detail}") from exc
        except Exception as exc:
            raise RuntimeError(f"HyDE request failed: {exc}") from exc
        if self.protocol == "openai_chat":
            return self._extract_openai_chat_text(data)
        return self._extract_messages_text(data)


LMStudioHyDEGenerator = HyDEGenerator


def rrf_fuse_orders(dense_order: list[int], bm25_order: list[int], rrf_k: int = 60) -> dict[int, float]:
    scores: dict[int, float] = {}
    for rank, idx in enumerate(dense_order, 1):
        scores[idx] = scores.get(idx, 0.0) + 1.0 / (rrf_k + rank)
    for rank, idx in enumerate(bm25_order, 1):
        scores[idx] = scores.get(idx, 0.0) + 1.0 / (rrf_k + rank)
    return scores


def build_rrf_fused_rows(
    chunks: list[dict],
    dense_scores: list[float],
    bm25_scores: list[float],
    dense_order: list[int],
    bm25_order: list[int],
    rrf_k: int = 60,
) -> list[dict]:
    dense_rank_by_idx = {idx: rank for rank, idx in enumerate(dense_order, 1)}
    bm25_rank_by_idx = {idx: rank for rank, idx in enumerate(bm25_order, 1)}
    fused_scores = rrf_fuse_orders(dense_order, bm25_order, rrf_k=rrf_k)

    def sort_key(idx: int):
        best_rank = min(dense_rank_by_idx.get(idx, 10**9), bm25_rank_by_idx.get(idx, 10**9))
        return (
            -fused_scores[idx],
            best_rank,
            -dense_scores[idx],
            -bm25_scores[idx],
            idx,
        )

    fused_order = sorted(fused_scores, key=sort_key)
    rows = []
    for rank, idx in enumerate(fused_order, 1):
        rows.append(
            {
                **chunks[idx],
                "rank": rank,
                "score": float(fused_scores[idx]),
                "rrf_score": float(fused_scores[idx]),
                "dense_score": float(dense_scores[idx]),
                "bm25_score": float(bm25_scores[idx]),
                "dense_rank_before_fusion": dense_rank_by_idx.get(idx),
                "bm25_rank_before_fusion": bm25_rank_by_idx.get(idx),
            }
        )
    return rows


def evaluate_rrf_rerank(
    index_dir: str | Path,
    questions_path: str | Path,
    out_dir: str | Path,
    endpoint: str,
    model: str,
    top_k: int = 5,
    dense_k: int = 20,
    bm25_k: int = 20,
    candidate_k: int = 20,
    coverage_threshold: float = 0.65,
    rrf_k: int = 60,
    reranker: LocalCrossEncoderReranker | None = None,
    reranker_model_path: str | None = None,
    reranker_device: str | None = None,
    reranker_batch_size: int = 8,
    reranker_max_length: int = 512,
    reranker_use_fp16: bool = True,
    hyde_model: str | None = None,
    hyde_endpoint: str = "http://localhost:1234/v1/chat/completions",
    hyde_protocol: str = "openai_chat",
    hyde_temperature: float = 0.0,
    hyde_max_tokens: int = 160,
    hyde_api_key: str | None = None,
    hyde_auth_mode: str = "auto",
    hyde_api_version: str = "2023-06-01",
    hyde_disable_thinking: bool = False,
):
    if candidate_k < top_k:
        raise RuntimeError(f"evaluate_rrf_rerank: candidate_k {candidate_k} must be >= top_k {top_k}.")
    if dense_k <= 0 or bm25_k <= 0:
        raise RuntimeError("evaluate_rrf_rerank: dense_k and bm25_k must both be positive.")

    index_dir = Path(index_dir)
    out_dir = Path(out_dir)
    chunks = _load_json(index_dir / "chunks.json")
    vectors = _load_json(index_dir / "vectors.json")
    require_equal_length("chunks", chunks, "vectors", vectors, "evaluate_rrf_rerank")
    vector_dim = require_vector_dimensions(vectors, "evaluate_rrf_rerank.chunk_vectors") if vectors else None
    questions = load_questions(questions_path)

    hyde_rows = []
    dense_query_texts = [q["question"] for q in questions]
    if hyde_model:
        generator = HyDEGenerator(
            endpoint=hyde_endpoint,
            model=hyde_model,
            protocol=hyde_protocol,
            temperature=hyde_temperature,
            max_tokens=hyde_max_tokens,
            api_key=hyde_api_key,
            auth_mode=hyde_auth_mode,
            api_version=hyde_api_version,
            disable_thinking=hyde_disable_thinking,
        )
        dense_query_texts = []
        for q in questions:
            hypothesis = generator.generate(q["question"])
            dense_query_texts.append(hypothesis)
            hyde_rows.append({"qid": q["qid"], "question": q["question"], "hyde_hypothesis": hypothesis})

    qvecs = embed_lmstudio(dense_query_texts, endpoint=endpoint, model=model)
    require_equal_length("questions", questions, "query_vectors", qvecs, "evaluate_rrf_rerank")
    if qvecs:
        require_vector_dimensions(qvecs, "evaluate_rrf_rerank.query_vectors", expected_dim=vector_dim)

    reranker = reranker or LocalCrossEncoderReranker(
        model_name_or_path=reranker_model_path,
        device=reranker_device,
        batch_size=reranker_batch_size,
        max_length=reranker_max_length,
        use_fp16=reranker_use_fp16,
    )
    bm25 = BM25Index([c["text"] for c in chunks])

    results = []
    fusion_rr = 0.0
    rerank_rr = 0.0
    fusion_hits = 0
    rerank_hits = 0
    rerank_fixed = 0
    rerank_improved = 0

    for q, qv, dense_query_text in zip(questions, qvecs, dense_query_texts):
        dense_scores = [dot(qv, v) for v in vectors]
        bm25_scores = [bm25.score(q["question"], i) for i in range(len(chunks))]
        dense_order = sorted(range(len(chunks)), key=lambda idx: dense_scores[idx], reverse=True)[:dense_k]
        bm25_order = sorted(range(len(chunks)), key=lambda idx: bm25_scores[idx], reverse=True)[:bm25_k]
        fused_rows = build_rrf_fused_rows(
            chunks,
            dense_scores,
            bm25_scores,
            dense_order,
            bm25_order,
            rrf_k=rrf_k,
        )
        fusion_success_rank = first_relevant_rank(q, fused_rows[:top_k], coverage_threshold)
        fusion_candidate_rank = first_relevant_rank(q, fused_rows, coverage_threshold)
        fusion_candidate_count = min(candidate_k, len(fused_rows))
        reranker_candidates = []
        for fusion_rank, row in enumerate(fused_rows[:fusion_candidate_count], 1):
            reranker_candidates.append(
                {
                    **row,
                    "dense_rank_before_rerank": fusion_rank,
                    "dense_score": float(row.get("rrf_score", row.get("score", 0.0))),
                }
            )
        reranked_rows = reranker.rerank(q["question"], reranker_candidates)
        result = build_ranked_result(q, reranked_rows, top_k=top_k, coverage_threshold=coverage_threshold)

        fusion_best_topk_coverage = 0.0
        for row in fused_rows[:top_k]:
            fusion_best_topk_coverage = max(fusion_best_topk_coverage, relevance_score(q, row))

        success_before = fusion_success_rank is not None
        success_after = result["success"]
        fixed = (not success_before) and success_after
        improved = fixed or (
            fusion_candidate_rank is not None
            and result["rank"] is not None
            and result["rank"] < fusion_candidate_rank
        )

        fusion_hits += int(success_before)
        rerank_hits += int(success_after)
        fusion_rr += 1.0 / fusion_success_rank if fusion_success_rank else 0.0
        rerank_rr += 1.0 / result["rank"] if result["rank"] else 0.0
        rerank_fixed += int(fixed)
        rerank_improved += int(improved)

        result.update(
            {
                "success_before_rerank": success_before,
                "rank_before_rerank": fusion_success_rank,
                "first_relevant_candidate_rank_before_rerank": fusion_candidate_rank,
                "best_topk_coverage_before_rerank": round(fusion_best_topk_coverage, 3),
                "rerank_candidate_k": fusion_candidate_count,
                "rerank_fixed": fixed,
                "rerank_improved": improved,
                "top_k_before_rerank": [_top_row(q, row, i) for i, row in enumerate(fused_rows[:top_k], 1)],
                "top_n_trace": [_trace_row(row, i) for i, row in enumerate(fused_rows[:30], 1)],
                "top_n_trace_after_rerank": [_trace_row(row, i) for i, row in enumerate(reranked_rows[:30], 1)],
                "dense_query_mode": "hyde" if hyde_model else "raw_query",
            }
        )
        if hyde_model:
            result["hyde_hypothesis"] = dense_query_text
        results.append(result)

    metrics = {
        "total": len(questions),
        f"fusion_recall@{top_k}": fusion_hits / len(questions) if questions else 0.0,
        f"recall@{top_k}": rerank_hits / len(questions) if questions else 0.0,
        "fusion_mrr": fusion_rr / len(questions) if questions else 0.0,
        "mrr": rerank_rr / len(questions) if questions else 0.0,
        "fusion_hits_before_rerank": fusion_hits,
        "hits": rerank_hits,
        "failed": len(questions) - rerank_hits,
        "rerank_fixed": rerank_fixed,
        "rerank_improved": rerank_improved,
        "dense_k": dense_k,
        "bm25_k": bm25_k,
        "candidate_k": candidate_k,
        "rrf_k": rrf_k,
        "coverage_threshold": coverage_threshold,
        "hyde_enabled": bool(hyde_model),
    }
    if hyde_model:
        metrics["hyde_model"] = hyde_model

    out_dir.mkdir(parents=True, exist_ok=True)
    _write_json(out_dir / "retrieval_results.json", results)
    _write_json(out_dir / "metrics.json", metrics)
    if hyde_rows:
        _write_json(out_dir / "hyde_generations.json", hyde_rows)
    config = {
        "index": str(index_dir),
        "questions": str(questions_path),
        "endpoint": endpoint,
        "model": model,
        "top_k": top_k,
        "dense_k": dense_k,
        "bm25_k": bm25_k,
        "candidate_k": candidate_k,
        "rrf_k": rrf_k,
        "coverage_threshold": coverage_threshold,
        "reranker_model_path": reranker.model_name_or_path,
        "reranker_device": reranker.device,
        "reranker_batch_size": reranker.batch_size,
        "reranker_max_length": reranker.max_length,
        "hyde_enabled": bool(hyde_model),
        "hyde_model": hyde_model or "",
        "hyde_endpoint": hyde_endpoint if hyde_model else "",
        "hyde_protocol": hyde_protocol if hyde_model else "",
        "hyde_auth_mode": hyde_auth_mode if hyde_model else "",
        "hyde_disable_thinking": hyde_disable_thinking if hyde_model else False,
    }
    write_rrf_rerank_report(out_dir / "eval_report.md", metrics, results, config)
    return results, metrics


def write_rrf_rerank_report(path: str | Path, metrics: dict, results: list[dict], config: dict):
    fixed = [r for r in results if r.get("rerank_fixed")]
    failed = [r for r in results if not r["success"]]
    lines = ["# Dense + BM25 -> RRF -> Rerank Report", ""]
    lines += ["## Config", ""]
    for k, v in config.items():
        lines.append(f"- **{k}**: `{v}`")
    lines += ["", "## Metrics", ""]
    for k, v in metrics.items():
        lines.append(f"- **{k}**: {v:.4f}" if isinstance(v, float) else f"- **{k}**: {v}")
    lines += ["", "## Fixed By Rerank", ""]
    if not fixed:
        lines.append("No query was fixed by reranking under current fused candidate set.")
    for row in fixed:
        lines += [
            f"### {row['qid']} — {row['gold_failure_type']}",
            f"- question: {row['question']}",
            f"- before rank: {row.get('rank_before_rerank')}",
            f"- after rank: {row.get('rank')}",
            f"- before best_topk_coverage: {row.get('best_topk_coverage_before_rerank')}",
            f"- after best_topk_coverage: {row.get('best_topk_coverage')}",
            "- top results after rerank:",
        ]
        for top in row["top_k"]:
            lines.append(
                f"  - rank {top['rank']}: `{top['chunk_id']}` rerank_score={top.get('rerank_score', top['score'])} "
                f"pre_rerank_rank={top.get('dense_rank_before_rerank')} cov={top['coverage']}"
            )
        lines.append("")
    lines += ["## Still Failed After Rerank", ""]
    if not failed:
        lines.append("No failed queries after reranking.")
    for row in failed:
        lines += [
            f"### {row['qid']} — {row['gold_failure_type']}",
            f"- question: {row['question']}",
            f"- before rank: {row.get('rank_before_rerank')}",
            f"- after rank: {row.get('rank')}",
            f"- before best_topk_coverage: {row.get('best_topk_coverage_before_rerank')}",
            f"- after best_topk_coverage: {row.get('best_topk_coverage')}",
            "",
        ]
    lines += ["## All Query Summary", ""]
    lines.append("| qid | success before | success after | rank before | rank after | rerank fixed | rerank improved |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for row in results:
        lines.append(
            f"| {row['qid']} | {row.get('success_before_rerank')} | {row['success']} | "
            f"{row.get('rank_before_rerank')} | {row['rank']} | {row.get('rerank_fixed')} | {row.get('rerank_improved')} |"
        )
    Path(path).write_text("\n".join(lines) + "\n", encoding="utf-8")
