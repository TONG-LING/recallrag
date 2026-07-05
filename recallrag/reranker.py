from __future__ import annotations

import os
from pathlib import Path


DEFAULT_HF_RERANKER = "BAAI/bge-reranker-v2-m3"
DEFAULT_LOCAL_MODEL_PATHS = [
    Path("/mnt/d/projects/hf_models/BAAI__bge-reranker-v2-m3"),
]


def default_reranker_model() -> str:
    env_value = os.environ.get("RECALLRAG_RERANKER_MODEL")
    if env_value:
        return env_value
    for path in DEFAULT_LOCAL_MODEL_PATHS:
        if path.exists():
            return str(path)
    return DEFAULT_HF_RERANKER


def detect_reranker_device(device: str | None = None) -> str:
    if device:
        return device
    try:
        import torch
    except Exception:
        return "cpu"
    if torch.cuda.is_available():
        return "cuda:0"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


class LocalCrossEncoderReranker:
    """Minimal local cross-encoder reranker wrapper for BGE reranker models."""

    def __init__(
        self,
        model_name_or_path: str | None = None,
        device: str | None = None,
        batch_size: int = 8,
        max_length: int = 512,
        use_fp16: bool = True,
        trust_remote_code: bool = False,
    ):
        self.model_name_or_path = model_name_or_path or default_reranker_model()
        self.device = detect_reranker_device(device)
        self.batch_size = batch_size
        self.max_length = max_length
        self.use_fp16 = use_fp16 and self.device.startswith("cuda")

        try:
            import torch
            from transformers import AutoModelForSequenceClassification, AutoTokenizer
        except Exception as exc:
            raise RuntimeError(
                "Reranker dependencies are missing. Activate the dedicated reranker venv "
                "or install `torch` and `transformers` first."
            ) from exc

        self._torch = torch
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name_or_path,
            trust_remote_code=trust_remote_code,
        )
        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.model_name_or_path,
            trust_remote_code=trust_remote_code,
        )
        if self.use_fp16:
            self.model.half()
        self.model.to(self.device)
        self.model.eval()

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        if not pairs:
            return []
        scores: list[float] = []
        with self._torch.inference_mode():
            for start in range(0, len(pairs), self.batch_size):
                batch = pairs[start:start + self.batch_size]
                queries = [query for query, _ in batch]
                passages = [passage for _, passage in batch]
                inputs = self.tokenizer(
                    queries,
                    passages,
                    padding=True,
                    truncation="only_second",
                    max_length=self.max_length,
                    return_tensors="pt",
                ).to(self.device)
                logits = self.model(**inputs, return_dict=True).logits.view(-1).float()
                scores.extend(float(score) for score in logits.cpu().tolist())
        return scores

    def rerank(
        self,
        query: str,
        candidates: list[dict],
        top_k: int | None = None,
    ) -> list[dict]:
        pairs = [(query, candidate.get("text", "")) for candidate in candidates]
        scores = self.score_pairs(pairs)
        rows = []
        for dense_rank, (candidate, score) in enumerate(zip(candidates, scores), 1):
            row = dict(candidate)
            row["dense_rank_before_rerank"] = candidate.get(
                "dense_rank_before_rerank",
                candidate.get("rank", dense_rank),
            )
            row["dense_score"] = float(candidate.get("dense_score", candidate.get("score", 0.0)))
            row["rerank_score"] = float(score)
            row["score"] = float(score)
            rows.append(row)
        rows.sort(
            key=lambda row: (
                row.get("rerank_score", float("-inf")),
                row.get("dense_score", float("-inf")),
            ),
            reverse=True,
        )
        for rank, row in enumerate(rows, 1):
            row["rank"] = rank
        if top_k is None:
            return rows
        return rows[:top_k]

    def unload(self):
        try:
            self.model.to("cpu")
            if self._torch.cuda.is_available():
                self._torch.cuda.empty_cache()
        except Exception:
            pass
