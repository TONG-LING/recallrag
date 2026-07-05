from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _load_json_if_exists(path: Path) -> Any | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def collect_artifact_summary(project_root: str | Path = ".") -> dict[str, Any]:
    root = Path(project_root).resolve()
    artifact_paths = {
        "baseline": root / "runs/base/metrics.json",
        "main_plus_patch": root / "runs/hybrid/metrics.json",
        "hybrid_bm25": root / "runs/hybrid_bm25/hybrid_bm25_metrics.json",
        "qdrant": root / "runs/qdrant/qdrant_metrics.json",
        "triage": root / "runs/triage/final_triage.json",
    }
    artifacts = {name: _load_json_if_exists(path) for name, path in artifact_paths.items()}
    baseline = artifacts["baseline"] or {}
    main_plus_patch = artifacts["main_plus_patch"] or {}
    triage = artifacts["triage"] or {}
    highlights = {
        "baseline_recall_at_5": baseline.get("recall@5"),
        "main_plus_patch_recall_at_5": main_plus_patch.get("recall@5"),
        "accepted_patch_candidates": triage.get("accepted_patch_candidates"),
        "retrieval_strategy_sensitive": triage.get("retrieval_strategy_sensitive"),
        "manual_review": triage.get("manual_review"),
    }
    available_artifacts = {
        name: str(path.relative_to(root))
        for name, path in artifact_paths.items()
        if artifacts[name] is not None
    }
    return {
        "project_root": str(root),
        "available_artifacts": available_artifacts,
        "highlights": highlights,
        "artifacts": artifacts,
    }


def collect_triage_rows(project_root: str | Path = ".", limit: int | None = None) -> list[dict[str, Any]]:
    root = Path(project_root).resolve()
    triage = _load_json_if_exists(root / "runs/triage/final_triage.json") or {}
    rows = list(triage.get("rows") or [])
    if limit is not None and limit >= 0:
        rows = rows[:limit]
    return rows
