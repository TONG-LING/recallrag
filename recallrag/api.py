from __future__ import annotations

import argparse
from pathlib import Path

from . import __version__
from .demo import collect_artifact_summary, collect_triage_rows
from .triage import final_triage


def _import_fastapi():
    try:
        from fastapi import FastAPI
        from pydantic import BaseModel
    except ImportError as exc:
        raise RuntimeError(
            "Demo API dependencies are not installed. Run `pip install -e .[serve]` first."
        ) from exc
    return FastAPI, BaseModel


def create_app(project_root: str | Path = "."):
    FastAPI, BaseModel = _import_fastapi()
    root = Path(project_root).resolve()

    class TriageRequest(BaseModel):
        base_dir: str = "runs/base"
        patch_eval_dir: str = "runs/hybrid"
        bm25_dir: str = "runs/hybrid_bm25"
        qdrant_dir: str | None = None
        out_dir: str = "runs/triage"

    app = FastAPI(
        title="RecallRAG Demo API",
        version=__version__,
        description="Thin interview/demo API over saved RecallRAG artifacts.",
    )

    def _resolve(path_str: str) -> Path:
        path = Path(path_str)
        return path if path.is_absolute() else root / path

    @app.get("/health")
    def health():
        summary = collect_artifact_summary(root)
        return {
            "status": "ok",
            "project_root": str(root),
            "available_artifacts": summary["available_artifacts"],
        }

    @app.get("/summary")
    def summary():
        return collect_artifact_summary(root)

    @app.get("/failures")
    def failures(limit: int = 20):
        rows = collect_triage_rows(root)
        return {
            "total": len(rows),
            "rows": rows[: max(limit, 0)],
        }

    @app.post("/triage")
    def run_triage(request: TriageRequest):
        summary = final_triage(
            _resolve(request.base_dir),
            _resolve(request.patch_eval_dir),
            _resolve(request.bm25_dir),
            _resolve(request.qdrant_dir) if request.qdrant_dir else None,
            _resolve(request.out_dir),
        )
        return {
            "out_dir": str(_resolve(request.out_dir)),
            "summary": {k: v for k, v in summary.items() if k != "rows"},
            "rows": summary["rows"],
        }

    return app


def run(argv: list[str] | None = None):
    parser = argparse.ArgumentParser(prog="recallrag-api")
    parser.add_argument("--project-root", default=".")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args(argv)
    try:
        import uvicorn
    except ImportError as exc:
        raise RuntimeError(
            "Demo API dependencies are not installed. Run `pip install -e .[serve]` first."
        ) from exc
    uvicorn.run(create_app(args.project_root), host=args.host, port=args.port)


if __name__ == "__main__":
    run()
