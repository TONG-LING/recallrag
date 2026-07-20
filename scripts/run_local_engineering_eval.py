#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import random
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]


def read_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: str | Path, obj: Any) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with Path(path).open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def write_jsonl(path: str | Path, rows: list[dict[str, Any]]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def now_id() -> str:
    return dt.datetime.now().strftime("%Y%m%d_%H%M%S")


def post_json(url: str, payload: dict[str, Any], timeout: int = 30) -> dict[str, Any]:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_json(url: str, timeout: int = 10) -> dict[str, Any]:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def check_embedding(endpoint: str, model: str) -> dict[str, Any]:
    started = time.time()
    payload = {"model": model, "input": ["RecallRAG embedding health check"]}
    obj = post_json(endpoint, payload, timeout=60)
    data = obj.get("data")
    if not isinstance(data, list) or len(data) != 1:
        raise RuntimeError("embedding response missing data[0]")
    embedding = data[0].get("embedding")
    if not isinstance(embedding, list) or not embedding:
        raise RuntimeError("embedding response missing non-empty embedding vector")
    return {
        "status": "ok",
        "endpoint": endpoint,
        "model": model,
        "dim": len(embedding),
        "latency_sec": round(time.time() - started, 3),
    }


def check_qdrant(url: str) -> dict[str, Any]:
    started = time.time()
    obj = get_json(url.rstrip("/") + "/collections", timeout=10)
    result = obj.get("result") or {}
    collections = result.get("collections") or []
    return {
        "status": "ok",
        "url": url,
        "collection_count": len(collections),
        "collections_preview": [c.get("name") for c in collections[:10]],
        "latency_sec": round(time.time() - started, 3),
    }


def run_cmd(cmd: list[str], cwd: Path, log_file: Path) -> None:
    log_file.parent.mkdir(parents=True, exist_ok=True)
    printable = " ".join(cmd)
    print(f"\n$ {printable}")
    with log_file.open("w", encoding="utf-8") as log:
        log.write(f"$ {printable}\n\n")
        proc = subprocess.Popen(
            cmd,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert proc.stdout is not None
        for line in proc.stdout:
            print(line, end="")
            log.write(line)
        rc = proc.wait()
        log.write(f"\n[exit_code] {rc}\n")
    if rc != 0:
        raise RuntimeError(f"command failed with exit code {rc}: {printable}. See log: {log_file}")


def prepare_questions(src: Path, out: Path, limit: int | None, sample: bool, seed: int) -> dict[str, Any]:
    rows = read_jsonl(src)
    total = len(rows)
    if limit is None or limit <= 0 or limit >= total:
        selected = rows
        mode = "all"
    elif sample:
        rng = random.Random(seed)
        selected = rng.sample(rows, limit)
        selected.sort(key=lambda r: r.get("qid", ""))
        mode = f"sample(seed={seed})"
    else:
        selected = rows[:limit]
        mode = "first_n"
    write_jsonl(out, selected)
    return {
        "source": str(src),
        "output": str(out),
        "total_available": total,
        "selected": len(selected),
        "mode": mode,
        "qids": [r.get("qid") for r in selected],
    }


def metric(path: Path) -> dict[str, Any]:
    return read_json(path) if path.exists() else {}


def fmt_float(v: Any) -> str:
    if isinstance(v, float):
        return f"{v:.4f}"
    return str(v)


def summarize_decisions(decisions: list[dict[str, Any]]) -> Counter:
    return Counter(d.get("status", "unknown") for d in decisions)


def generate_engineering_report(out_dir: Path, config: dict[str, Any]) -> Path:
    runs = out_dir / "runs"
    base_dir = runs / "base"
    patch_dir = runs / "patches"
    hybrid_dir = runs / "hybrid"
    bm25_dir = runs / "bm25"
    qdrant_main_dir = runs / "qdrant_main"
    qdrant_patch_dir = runs / "qdrant_patch"
    triage_dir = runs / "triage"

    base_metrics = metric(base_dir / "metrics.json")
    hybrid_metrics = metric(hybrid_dir / "metrics.json")
    comparison = metric(hybrid_dir / "comparison.json")
    patch_meta = metric(patch_dir / "patch_index_meta.json")
    patch_decisions = read_json(hybrid_dir / "patch_decisions.json") if (hybrid_dir / "patch_decisions.json").exists() else []
    candidate_probe = read_json(hybrid_dir / "candidate_probe_results.json") if (hybrid_dir / "candidate_probe_results.json").exists() else []
    diagnoses = read_json(base_dir / "failure_diagnosis.json") if (base_dir / "failure_diagnosis.json").exists() else []
    triage = metric(triage_dir / "final_triage.json")
    bm25_metrics = metric(bm25_dir / "hybrid_bm25_metrics.json")
    qdrant_cmp = metric(qdrant_patch_dir / "qdrant_comparison_report.json")
    qdrant_main_metrics = metric(qdrant_main_dir / "qdrant_metrics.json")
    qdrant_patch_metrics = metric(qdrant_patch_dir / "qdrant_metrics.json")
    sig = metric(hybrid_dir / "paired_significance.json")

    diagnosis_family = Counter(d.get("failure_family", "unknown") for d in diagnoses)
    diagnosis_type = Counter(d.get("diagnosed_failure_type", "unknown") for d in diagnoses)
    decision_counts = summarize_decisions(patch_decisions)
    probe_type_counts = Counter(r.get("candidate_type", "unknown") for r in candidate_probe)
    selected = comparison.get("selected_patch_candidates") or []
    selected_type_counts = Counter(r.get("candidate_type", "unknown") for r in selected)

    triage_rows = triage.get("rows") or []
    triage_by_qid = {r.get("qid"): r for r in triage_rows}
    decisions_by_qid: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for d in patch_decisions:
        decisions_by_qid[d.get("qid")].append(d)

    lines: list[str] = []
    lines += ["# RecallRAG Local Engineering Evaluation Report", ""]
    lines += ["## Run Configuration", ""]
    for key, value in config.items():
        if key in {"embedding_check", "qdrant_check", "question_selection"}:
            continue
        lines.append(f"- **{key}**: `{value}`")
    lines += [""]

    lines += ["## Environment Checks", ""]
    emb = config.get("embedding_check") or {}
    qdrant = config.get("qdrant_check") or {}
    lines += [
        f"- embedding: `{emb.get('status')}` endpoint=`{emb.get('endpoint')}` model=`{emb.get('model')}` dim=`{emb.get('dim')}` latency=`{emb.get('latency_sec')}s`",
        f"- qdrant: `{qdrant.get('status')}` url=`{qdrant.get('url')}` collections=`{qdrant.get('collection_count')}`",
        "",
    ]

    qsel = config.get("question_selection") or {}
    lines += ["## Question Set", ""]
    lines += [
        f"- source: `{qsel.get('source')}`",
        f"- selected: `{qsel.get('selected')}` / `{qsel.get('total_available')}`",
        f"- mode: `{qsel.get('mode')}`",
        f"- temp questions: `{qsel.get('output')}`",
        "",
    ]

    lines += ["## Retrieval Metrics", ""]
    lines += [
        "| Route | Recall@K | MRR | Hits | Failed |",
        "|---|---:|---:|---:|---:|",
        f"| main-only | {fmt_float(base_metrics.get('recall@5'))} | {fmt_float(base_metrics.get('mrr'))} | {base_metrics.get('hits')} / {base_metrics.get('total')} | {base_metrics.get('failed')} |",
        f"| main + patch | {fmt_float(hybrid_metrics.get('recall@5'))} | {fmt_float(hybrid_metrics.get('mrr'))} | {hybrid_metrics.get('hits')} / {hybrid_metrics.get('total')} | {hybrid_metrics.get('failed')} |",
    ]
    if comparison:
        delta = comparison.get("delta") or {}
        lines.append(f"| delta | {fmt_float(delta.get('recall'))} | {fmt_float(delta.get('mrr'))} | {delta.get('hits')} | - |")
    if qdrant_main_metrics and qdrant_patch_metrics:
        lines.append(f"| qdrant main-only | {fmt_float(qdrant_main_metrics.get('recall@5'))} | {fmt_float(qdrant_main_metrics.get('mrr'))} | {qdrant_main_metrics.get('hits')} / {qdrant_main_metrics.get('total')} | {qdrant_main_metrics.get('failed')} |")
        lines.append(f"| qdrant main + patch | {fmt_float(qdrant_patch_metrics.get('recall@5'))} | {fmt_float(qdrant_patch_metrics.get('mrr'))} | {qdrant_patch_metrics.get('hits')} / {qdrant_patch_metrics.get('total')} | {qdrant_patch_metrics.get('failed')} |")
    lines.append("")

    if sig:
        lines += ["## Paired Significance", ""]
        for k, v in sig.items():
            if k == "per_query":
                continue
            lines.append(f"- **{k}**: `{v}`")
        if "per_query" in sig:
            lines.append(f"- **per_query**: see `{hybrid_dir / 'paired_significance.json'}`")
        lines.append("")

    lines += ["## Patch Summary", ""]
    lines += [
        f"- materialized patch candidates: `{patch_meta.get('count')}`",
        f"- candidate probe results: `{len(candidate_probe)}`",
        f"- selected patch candidates: `{len(selected)}`",
        f"- selected patch type counts: `{dict(selected_type_counts)}`",
        f"- decision counts: `{dict(decision_counts)}`",
        f"- fixed qids: `{comparison.get('fixed', [])}`",
        f"- regressed qids: `{comparison.get('regressed', [])}`",
        f"- unchanged failed qids: `{comparison.get('unchanged_failure', [])}`",
        "",
    ]

    lines += ["## Failure Diagnosis Summary", ""]
    lines += ["### By family", ""]
    for k, v in diagnosis_family.most_common():
        lines.append(f"- `{k}`: {v}")
    lines += ["", "### By type", ""]
    for k, v in diagnosis_type.most_common():
        lines.append(f"- `{k}`: {v}")
    lines.append("")

    if bm25_metrics:
        lines += ["## BM25 / Dense+BM25 Countercheck", ""]
        lines += ["| Route | Recall@K | MRR | Hits |", "|---|---:|---:|---:|"]
        for name in ["dense", "bm25", "dense_bm25"]:
            row = bm25_metrics.get(name) or {}
            if row:
                lines.append(f"| {name} | {fmt_float(row.get('recall@5'))} | {fmt_float(row.get('mrr'))} | {row.get('hits')} / {row.get('total')} |")
        lines.append("")

    if triage:
        lines += ["## Final Triage Summary", ""]
        for k in ["total_dense_failures", "accepted_patch_candidates", "retrieval_strategy_sensitive", "manual_review"]:
            lines.append(f"- **{k}**: `{triage.get(k)}`")
        lines.append("")

    lines += ["## Per-failure Engineering Decisions", ""]
    if not diagnoses:
        lines.append("No dense retrieval failures were diagnosed.")
        lines.append("")
    else:
        lines += [
            "| qid | question | raw diagnosis | need patch | accepted patch type | before cov | after cov | final decision | action |",
            "|---|---|---|---:|---|---:|---:|---|---|",
        ]
        for d in diagnoses:
            qid = d.get("qid")
            tr = triage_by_qid.get(qid, {})
            q_decisions = decisions_by_qid.get(qid, [])
            accepted = [x for x in q_decisions if x.get("status") == "accepted"]
            accepted_types = sorted({x.get("candidate_type") for x in accepted if x.get("candidate_type")})
            before_cov = tr.get("signals", {}).get("base_best_coverage")
            after_cov = tr.get("signals", {}).get("patch_best_coverage")
            need_patch = bool(tr.get("patch_allowed_final")) or bool(accepted)
            question = (d.get("question") or "").replace("|", "\\|")
            if len(question) > 42:
                question = question[:39] + "..."
            lines.append(
                f"| {qid} | {question} | `{d.get('diagnosed_failure_type')}` | {need_patch} | "
                f"`{','.join(accepted_types) if accepted_types else '-'}` | {before_cov} | {after_cov} | "
                f"`{tr.get('final_decision', '-')}` | `{tr.get('recommended_action', '-')}` |"
            )
        lines.append("")

    lines += ["## Accepted Patch Details", ""]
    accepted_decisions = [d for d in patch_decisions if d.get("status") == "accepted"]
    if not accepted_decisions:
        lines.append("No accepted patch candidate.")
    else:
        for d in accepted_decisions:
            probe = d.get("candidate_probe") or {}
            lines += [
                f"### {d.get('patch_id')}",
                "",
                f"- qid: `{d.get('qid')}`",
                f"- candidate_type: `{d.get('candidate_type')}`",
                f"- failure_type: `{d.get('failure_type')}`",
                f"- anchor_chunk_id: `{d.get('anchor_chunk_id')}`",
                f"- affected_main_chunks: `{d.get('affected_main_chunks')}`",
                f"- before_rank / after_rank: `{d.get('before_rank')}` -> `{d.get('after_rank')}`",
                f"- before_coverage / after_coverage: `{d.get('before_best_coverage')}` -> `{d.get('after_best_coverage')}`",
                f"- individual_probe_rank: `{probe.get('rank')}`",
                f"- individual_probe_coverage: `{probe.get('best_topk_coverage')}`",
                f"- decision_reason: {d.get('decision_reason')}",
                "",
            ]

    if qdrant_cmp:
        lines += ["## Qdrant Main/Patch Validation", ""]
        lines += [
            f"- qdrant fixed qids: `{qdrant_cmp.get('fixed')}`",
            f"- qdrant regressed qids: `{qdrant_cmp.get('regressed')}`",
            f"- qdrant report: `{qdrant_patch_dir / 'qdrant_comparison_report.md'}`",
            "",
        ]

    lines += ["## Output Artifacts", ""]
    artifact_paths = [
        base_dir / "eval_report.md",
        base_dir / "failure_diagnosis.md",
        hybrid_dir / "comparison_report.md",
        hybrid_dir / "patch_decisions.json",
        bm25_dir / "hybrid_bm25_report.md",
        triage_dir / "final_triage_report.md",
        qdrant_patch_dir / "qdrant_comparison_report.md",
        out_dir / "logs",
    ]
    for p in artifact_paths:
        if p.exists():
            lines.append(f"- `{p}`")
    lines.append("")

    report_path = out_dir / "engineering_report.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a local RecallRAG engineering evaluation into an external temp directory.")
    parser.add_argument("--docs", default="case_zh_dureader_120/docs")
    parser.add_argument("--questions", default="case_zh_dureader_120/eval/questions_patch_source.jsonl")
    parser.add_argument("--limit", type=int, default=120, help="Number of questions to evaluate. <=0 means all.")
    parser.add_argument("--sample", action="store_true", help="Randomly sample --limit questions instead of taking the first N.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", default=None, help="Output directory. Default: ../RecallRAG_temp/engineering_eval_<timestamp>_n<limit>.")
    parser.add_argument("--endpoint", default="http://localhost:1234/v1/embeddings")
    parser.add_argument("--model", default="text-embedding-bge-large-zh-v1.5")
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--qdrant-url", default="http://localhost:6333")
    parser.add_argument("--chunk-size", type=int, default=600)
    parser.add_argument("--overlap", type=int, default=0)
    parser.add_argument("--no-keep-heading", action="store_true")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--patch-k", type=int, default=3)
    parser.add_argument("--coverage-threshold", type=float, default=0.65)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    run_id = now_id()
    limit_label = "all" if args.limit <= 0 else str(args.limit)
    out_dir = Path(args.out) if args.out else ROOT.parent / "RecallRAG_temp" / f"engineering_eval_{run_id}_n{limit_label}_c{args.chunk_size}_o{args.overlap}"
    out_dir = out_dir.resolve()
    runs = out_dir / "runs"
    logs = out_dir / "logs"
    out_dir.mkdir(parents=True, exist_ok=True)
    logs.mkdir(parents=True, exist_ok=True)

    print(f"RecallRAG local engineering eval")
    print(f"Output dir: {out_dir}")

    config: dict[str, Any] = {
        "run_id": run_id,
        "out_dir": str(out_dir),
        "docs": str((ROOT / args.docs).resolve() if not Path(args.docs).is_absolute() else Path(args.docs)),
        "questions": str((ROOT / args.questions).resolve() if not Path(args.questions).is_absolute() else Path(args.questions)),
        "limit": args.limit,
        "sample": args.sample,
        "seed": args.seed,
        "endpoint": args.endpoint,
        "model": args.model,
        "batch_size": args.batch_size,
        "qdrant_url": args.qdrant_url,
        "chunk_size": args.chunk_size,
        "overlap": args.overlap,
        "keep_heading": not args.no_keep_heading,
        "top_k": args.top_k,
        "patch_k": args.patch_k,
        "coverage_threshold": args.coverage_threshold,
    }

    try:
        print("\n[check] embedding endpoint")
        config["embedding_check"] = check_embedding(args.endpoint, args.model)
        print(json.dumps(config["embedding_check"], ensure_ascii=False, indent=2))

        print("\n[check] qdrant")
        config["qdrant_check"] = check_qdrant(args.qdrant_url)
        print(json.dumps(config["qdrant_check"], ensure_ascii=False, indent=2))

        question_src = Path(config["questions"])
        temp_questions = out_dir / "questions.jsonl"
        config["question_selection"] = prepare_questions(question_src, temp_questions, args.limit, args.sample, args.seed)
        write_json(out_dir / "run_config.json", config)

        py = sys.executable
        base = runs / "base"
        patches = runs / "patches"
        hybrid = runs / "hybrid"
        bm25 = runs / "bm25"
        qdrant_main = runs / "qdrant_main"
        qdrant_patch = runs / "qdrant_patch"
        triage = runs / "triage"

        base_cmd = [
            py, "-m", "recallrag.cli", "run-baseline",
            "--docs", config["docs"],
            "--questions", str(temp_questions),
            "--out", str(base),
            "--chunk-size", str(args.chunk_size),
            "--overlap", str(args.overlap),
            "--endpoint", args.endpoint,
            "--model", args.model,
            "--batch-size", str(args.batch_size),
            "--top-k", str(args.top_k),
            "--coverage-threshold", str(args.coverage_threshold),
        ]
        if not args.no_keep_heading:
            base_cmd.append("--keep-heading")
        run_cmd(base_cmd, ROOT, logs / "01_run_baseline.log")

        run_cmd([
            py, "-m", "recallrag.cli", "diagnose",
            "--index", str(base),
            "--questions", str(temp_questions),
            "--out", str(base),
            "--coverage-threshold", str(args.coverage_threshold),
        ], ROOT, logs / "02_diagnose.log")

        run_cmd([
            py, "-m", "recallrag.cli", "materialize-patches",
            "--index", str(base),
            "--out", str(patches),
            "--endpoint", args.endpoint,
            "--model", args.model,
            "--batch-size", str(args.batch_size),
        ], ROOT, logs / "03_materialize_patches.log")

        run_cmd([
            py, "-m", "recallrag.cli", "eval-hybrid",
            "--index", str(base),
            "--patch-index", str(patches),
            "--questions", str(temp_questions),
            "--out", str(hybrid),
            "--endpoint", args.endpoint,
            "--model", args.model,
            "--top-k", str(args.top_k),
            "--coverage-threshold", str(args.coverage_threshold),
        ], ROOT, logs / "04_eval_hybrid.log")

        run_cmd([
            py, "scripts/paired_significance.py",
            "--before", str(base / "retrieval_results.json"),
            "--after", str(hybrid / "retrieval_results.json"),
            "--out-json", str(hybrid / "paired_significance.json"),
            "--out-md", str(hybrid / "paired_significance.md"),
        ], ROOT, logs / "05_paired_significance.log")

        run_cmd([
            py, "-m", "recallrag.cli", "eval-bm25-hybrid",
            "--index", str(base),
            "--questions", str(temp_questions),
            "--out", str(bm25),
            "--endpoint", args.endpoint,
            "--model", args.model,
            "--top-k", str(args.top_k),
            "--coverage-threshold", str(args.coverage_threshold),
            "--alpha-dense", "0.65",
        ], ROOT, logs / "06_eval_bm25_hybrid.log")

        qdrant_dir_for_triage = None
        prefix = f"recallrag_tmp_{run_id}"
        main_collection = f"{prefix}_main"
        patch_collection = f"{prefix}_patch"
        config["qdrant_collections"] = {
            "main_collection": main_collection,
            "patch_collection": patch_collection,
        }
        write_json(out_dir / "run_config.json", config)

        run_cmd([
                py, "-m", "recallrag.cli", "qdrant-build",
                "--index", str(base),
                "--patch-index", str(patches),
                "--out", str(qdrant_patch),
                "--url", args.qdrant_url,
                "--main-collection", main_collection,
                "--patch-collection", patch_collection,
        ], ROOT, logs / "07_qdrant_build.log")

        run_cmd([
                py, "-m", "recallrag.cli", "qdrant-eval",
                "--questions", str(temp_questions),
                "--out", str(qdrant_main),
                "--url", args.qdrant_url,
                "--main-collection", main_collection,
                "--patch-collection", patch_collection,
                "--endpoint", args.endpoint,
                "--model", args.model,
                "--main-k", str(args.top_k),
                "--patch-k", "0",
                "--final-k", str(args.top_k),
                "--coverage-threshold", str(args.coverage_threshold),
        ], ROOT, logs / "08_qdrant_eval_main.log")

        run_cmd([
                py, "-m", "recallrag.cli", "qdrant-eval",
                "--questions", str(temp_questions),
                "--out", str(qdrant_patch),
                "--url", args.qdrant_url,
                "--main-collection", main_collection,
                "--patch-collection", patch_collection,
                "--endpoint", args.endpoint,
                "--model", args.model,
                "--main-k", str(args.top_k),
                "--patch-k", str(args.patch_k),
                "--final-k", str(args.top_k),
                "--coverage-threshold", str(args.coverage_threshold),
        ], ROOT, logs / "09_qdrant_eval_patch.log")

        run_cmd([
                py, "-m", "recallrag.cli", "qdrant-compare",
                "--main-only-dir", str(qdrant_main),
                "--main-patch-dir", str(qdrant_patch),
                "--out", str(qdrant_patch / "qdrant_comparison_report.md"),
        ], ROOT, logs / "10_qdrant_compare.log")
        qdrant_dir_for_triage = qdrant_patch

        triage_cmd = [
            py, "-m", "recallrag.cli", "final-triage",
            "--base-dir", str(base),
            "--patch-eval-dir", str(hybrid),
            "--bm25-dir", str(bm25),
            "--out", str(triage),
        ]
        if qdrant_dir_for_triage is not None:
            triage_cmd.extend(["--qdrant-dir", str(qdrant_dir_for_triage)])
        run_cmd(triage_cmd, ROOT, logs / "11_final_triage.log")

        write_json(out_dir / "run_config.json", config)
        report_path = generate_engineering_report(out_dir, config)
        print("\nDONE")
        print(f"Engineering report: {report_path}")
        print(f"All temporary artifacts: {out_dir}")
        return 0
    except (RuntimeError, urllib.error.URLError, urllib.error.HTTPError) as exc:
        config["failed_at"] = str(exc)
        write_json(out_dir / "run_config.json", config)
        print(f"\nERROR: {exc}", file=sys.stderr)
        print(f"Partial artifacts: {out_dir}", file=sys.stderr)
        print("Start Qdrant first, for example: ./scripts/start_qdrant.sh", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
