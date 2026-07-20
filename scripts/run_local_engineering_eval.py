#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import random
import shutil
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


def zh_status(status: Any) -> str:
    mapping = {
        "accepted": "已接受",
        "rejected": "已拒绝",
        "candidate_not_selected": "候选未选中",
        "needs_review": "需人工复核",
        "manual_review": "人工复核",
        "accepted_patch_candidate": "接受 Patch",
        "retrieval_strategy_sensitive": "检索策略敏感",
    }
    return mapping.get(str(status), str(status))


def md_escape(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def short_text(value: Any, limit: int = 56) -> str:
    text = md_escape(value)
    return text if len(text) <= limit else text[: limit - 3] + "..."


def metric_recall(metrics: dict[str, Any], top_k: int = 5) -> Any:
    return metrics.get(f"recall@{top_k}", metrics.get("recall@5"))


def metric_row(name: str, metrics: dict[str, Any], top_k: int = 5) -> str:
    return (
        f"| {name} | {fmt_float(metric_recall(metrics, top_k))} | "
        f"{fmt_float(metrics.get('mrr'))} | {metrics.get('hits')} / {metrics.get('total')} | "
        f"{metrics.get('failed')} |"
    )


def list_or_dash(value: Any) -> str:
    if not value:
        return "-"
    if isinstance(value, list):
        return ", ".join(str(x) for x in value) if value else "-"
    return str(value)


def display_path(value: Any) -> str:
    if value is None:
        return "-"
    path = Path(str(value))
    try:
        resolved = path.resolve()
    except Exception:
        return str(value)
    try:
        return str(resolved.relative_to(ROOT))
    except ValueError:
        pass
    try:
        return str(resolved.relative_to(ROOT.parent))
    except ValueError:
        return resolved.name


def cn_bool(value: Any) -> str:
    if value is True:
        return "是"
    if value is False:
        return "否"
    if value is None:
        return "-"
    return str(value)


def cn_patch_type(value: Any) -> str:
    mapping = {
        "adjacent_merge": "相邻块合并",
        "contextual": "相关句抽取",
        "local_proposition": "要点句改写",
        "local_summary": "局部摘要",
    }
    return mapping.get(str(value), str(value) if value else "-")


def cn_action(value: Any) -> str:
    mapping = {
        "accept_patch_for_shadow_index; optional later merge": "接受补丁，进入旁路索引；后续可考虑合入主索引",
        "accept_patch_candidate_in_qdrant_shadow_validation": "接受补丁，Qdrant 旁路验证通过",
        "manual_review_or_new_strategy": "人工复核，当前补丁未解决",
        "prefer_hybrid_retrieval_or_mark_patch_needs_review": "优先考虑混合检索，该问题不直接归因于切块",
        "needs_review_before_shadow_index_activation": "补丁进入旁路前需要复核",
    }
    return mapping.get(str(value), str(value) if value else "-")


def cn_decision(value: Any) -> str:
    mapping = {
        "accepted_patch_candidate": "接受补丁",
        "manual_review": "人工复核",
        "needs_review": "需要复核",
        "accepted": "已接受",
        "rejected": "已拒绝",
        "candidate_not_selected": "未选中",
        "retrieval_strategy_sensitive": "检索策略敏感",
    }
    return mapping.get(str(value), str(value) if value else "-")


def generate_engineering_report(out_dir: Path, config: dict[str, Any]) -> Path:
    runs = out_dir / "runs"
    base_dir = runs / "base"
    patch_dir = runs / "patches"
    hybrid_dir = runs / "hybrid"
    bm25_dir = runs / "bm25"
    qdrant_main_dir = runs / "qdrant_main"
    qdrant_patch_dir = runs / "qdrant_patch"
    triage_dir = runs / "triage"

    top_k = int(config.get("top_k", 5) or 5)
    base_metrics = metric(base_dir / "metrics.json")
    hybrid_metrics = metric(hybrid_dir / "metrics.json")
    comparison = metric(hybrid_dir / "comparison.json")
    patch_meta = metric(patch_dir / "patch_index_meta.json")
    patch_decisions = read_json(hybrid_dir / "patch_decisions.json") if (hybrid_dir / "patch_decisions.json").exists() else []
    diagnoses = read_json(base_dir / "failure_diagnosis.json") if (base_dir / "failure_diagnosis.json").exists() else []
    triage = metric(triage_dir / "final_triage.json")
    bm25_metrics = metric(bm25_dir / "hybrid_bm25_metrics.json")
    qdrant_cmp = metric(qdrant_patch_dir / "qdrant_comparison_report.json")
    qdrant_main_metrics = metric(qdrant_main_dir / "qdrant_metrics.json")
    qdrant_patch_metrics = metric(qdrant_patch_dir / "qdrant_metrics.json")
    sig = metric(hybrid_dir / "paired_significance.json")

    selected = comparison.get("selected_patch_candidates") or []
    selected_type_counts = Counter(cn_patch_type(r.get("candidate_type")) for r in selected)
    decision_counts = summarize_decisions(patch_decisions)
    triage_rows = triage.get("rows") or []
    triage_by_qid = {r.get("qid"): r for r in triage_rows}
    decisions_by_qid: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in patch_decisions:
        decisions_by_qid[row.get("qid")].append(row)

    delta = comparison.get("delta") or {}
    fixed_qids = comparison.get("fixed", []) if comparison else []
    unchanged_failed_qids = comparison.get("unchanged_failure", []) if comparison else []
    service_base_metrics = qdrant_main_metrics or base_metrics
    service_patch_metrics = qdrant_patch_metrics or hybrid_metrics
    service_delta = (qdrant_cmp.get("delta") if qdrant_cmp else None) or delta
    service_fixed_qids = (qdrant_cmp.get("fixed") if qdrant_cmp else None) or fixed_qids
    service_regressed_qids = (qdrant_cmp.get("regressed") if qdrant_cmp else None) or (comparison.get("regressed", []) if comparison else [])
    accepted_decisions = [d for d in patch_decisions if d.get("status") == "accepted"]

    generated_at = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    emb = config.get("embedding_check") or {}
    qdrant = config.get("qdrant_check") or {}
    qsel = config.get("question_selection") or {}
    qdrant_collections = config.get("qdrant_collections") or {}

    lines: list[str] = []
    lines += ["# RecallRAG 本地评估报告", ""]
    lines += [
        f"- 生成时间：`{generated_at}`",
        f"- 运行编号：`{config.get('run_id')}`",
        f"- 评估题目：`{qsel.get('selected')}` / `{qsel.get('total_available')}`",
        f"- 报告目录：`{display_path(out_dir)}`",
        "",
    ]

    lines += ["## 1. 总体结论", ""]
    lines += [
        "本次评估检查的是：在主知识库不重建的情况下，旁路补丁索引能否修复一部分证据召回不完整的问题。最终效果以 Qdrant 向量库中的主集合和补丁集合验证结果为准。",
        "",
        "| 指标 | 结果 |",
        "|---|---:|",
        f"| 主集合命中数 | {service_base_metrics.get('hits')} / {service_base_metrics.get('total')} |",
        f"| 主集合 + 补丁集合命中数 | {service_patch_metrics.get('hits')} / {service_patch_metrics.get('total')} |",
        f"| 新增修复数 | {service_delta.get('hits', 0):+} |",
        f"| 召回率提升 | {fmt_float(service_delta.get('recall'))} |",
        f"| 排名指标提升 | {fmt_float(service_delta.get('mrr'))} |",
        f"| 通过验证的补丁数 | {len(accepted_decisions)} |",
        f"| 发生回退的问题数 | {len(service_regressed_qids)} |",
        "",
    ]
    if service_regressed_qids:
        lines.append(f"> 结论：存在回退问题（{list_or_dash(service_regressed_qids)}），相关补丁需要复核后再使用。")
    else:
        lines.append("> 结论：本次没有发现补丁导致原本成功的问题失败。")
    lines.append("")

    lines += ["## 2. 运行环境", ""]
    lines += [
        "| 项目 | 状态 | 说明 |",
        "|---|---|---|",
        f"| 向量模型服务 | `{emb.get('status')}` | 地址 `{emb.get('endpoint')}`，模型 `{emb.get('model')}`，维度 `{emb.get('dim')}` |",
        f"| Qdrant 向量库 | `{qdrant.get('status')}` | 地址 `{qdrant.get('url')}`，已有集合数 `{qdrant.get('collection_count')}` |",
        "",
    ]
    if qdrant_collections:
        lines += [
            "本次运行创建了两个临时集合：",
            "",
            f"- 主集合：`{qdrant_collections.get('main_collection')}`",
            f"- 补丁集合：`{qdrant_collections.get('patch_collection')}`",
            "",
        ]

    lines += ["## 3. 评估设置", ""]
    lines += [
        "| 项目 | 值 |",
        "|---|---|",
        f"| 文档目录 | `{display_path(config.get('docs'))}` |",
        f"| 问题集 | `{display_path(config.get('questions'))}` |",
        f"| 本次使用的问题集 | `{display_path(qsel.get('output'))}` |",
        f"| 题目选择 | `{qsel.get('mode')}` |",
        f"| 切块长度 | `{config.get('chunk_size')}` |",
        f"| 重叠长度 | `{config.get('overlap')}` |",
        f"| 返回条数 | `{top_k}` |",
        f"| 证据覆盖阈值 | `{config.get('coverage_threshold')}` |",
        "",
        "命中标准：检索结果必须来自正确文档，并且覆盖足够多的标准答案证据。只找到正确文档但证据不完整，不算命中。",
        "",
    ]

    lines += ["## 4. 向量库检索结果", ""]
    lines += [
        "| 路线 | 召回率 | 排名指标 | 命中数 | 失败数 |",
        "|---|---:|---:|---:|---:|",
        metric_row("主集合", service_base_metrics, top_k),
        metric_row("主集合 + 补丁集合", service_patch_metrics, top_k),
        f"| 提升 | {fmt_float(service_delta.get('recall'))} | {fmt_float(service_delta.get('mrr'))} | {service_delta.get('hits')} | - |",
        "",
        "说明：补丁不是直接写回主集合，而是单独放在补丁集合中。这样可以单独验证、停用或回滚。",
        "",
    ]

    if sig:
        lines += ["## 5. 修复是否稳定", ""]
        lines += [
            "| 项目 | 结果 |",
            "|---|---:|",
            f"| 修复的问题数 | {sig.get('wins')} |",
            f"| 变差的问题数 | {sig.get('losses')} |",
            f"| 不变的问题数 | {sig.get('ties')} |",
            f"| 召回率变化 | {fmt_float(sig.get('recall_delta'))} |",
            f"| 排名指标变化 | {fmt_float(sig.get('mrr_delta'))} |",
            f"| McNemar 检验 p 值 | {sig.get('exact_mcnemar_pvalue')} |",
            "",
        ]

    lines += ["## 6. 失败问题和补丁决策", ""]
    if triage:
        lines += [
            "| 项目 | 数量 |",
            "|---|---:|",
            f"| 主集合失败问题 | {triage.get('total_dense_failures')} |",
            f"| 接受补丁 | {triage.get('accepted_patch_candidates')} |",
            f"| 更适合改检索策略 | {triage.get('retrieval_strategy_sensitive')} |",
            f"| 需要人工复核 | {triage.get('manual_review')} |",
            "",
        ]
    lines += [
        "| 问题编号 | 问题 | 是否补丁修复 | 补丁类型 | 修复前覆盖率 | 修复后覆盖率 | 最终处理 |",
        "|---|---|---:|---|---:|---:|---|",
    ]
    if not diagnoses:
        lines.append("| - | 本次没有失败问题 | - | - | - | - | - |")
    else:
        for d in diagnoses:
            qid = d.get("qid")
            tr = triage_by_qid.get(qid, {})
            signals = tr.get("signals", {}) or {}
            accepted = [x for x in decisions_by_qid.get(qid, []) if x.get("status") == "accepted"]
            patch_types = sorted({cn_patch_type(x.get("candidate_type")) for x in accepted})
            lines.append(
                f"| {qid} | {short_text(d.get('question'), 34)} | "
                f"{cn_bool(bool(accepted))} | {', '.join(patch_types) if patch_types else '-'} | "
                f"{signals.get('base_best_coverage')} | {signals.get('patch_best_coverage')} | "
                f"{cn_action(tr.get('recommended_action'))} |"
            )
    lines.append("")

    lines += ["## 7. 已接受补丁明细", ""]
    if not accepted_decisions:
        lines += ["本次没有补丁通过验证。", ""]
    else:
        lines += [
            "| 补丁编号 | 来源问题 | 补丁类型 | 影响的主索引块 | 覆盖率变化 | 选择原因 |",
            "|---|---|---|---|---:|---|",
        ]
        for d in accepted_decisions:
            lines.append(
                f"| `{d.get('patch_id')}` | {d.get('qid')} | {cn_patch_type(d.get('candidate_type'))} | "
                f"`{d.get('affected_main_chunks')}` | {d.get('before_best_coverage')} -> {d.get('after_best_coverage')} | "
                f"补丁修复了来源问题，且没有发现回退 |"
            )
        lines.append("")

    if bm25_metrics:
        lines += ["## 8. 检索策略对照", ""]
        lines += [
            "这里检查失败是否只是因为单一向量检索不够好。如果关键词检索或混合检索能修复，则该问题不应简单归因于切块。",
            "",
            "| 路线 | 召回率 | 排名指标 | 命中数 | 失败数 |",
            "|---|---:|---:|---:|---:|",
        ]
        labels = {"dense": "向量检索", "bm25": "关键词检索", "dense_bm25": "向量 + 关键词"}
        for name in ["dense", "bm25", "dense_bm25"]:
            row = bm25_metrics.get(name) or {}
            if row:
                lines.append(metric_row(labels[name], row, top_k))
        lines.append("")

    lines += ["## 9. 结论和边界", ""]
    lines += [
        "- 主集合没有被直接改写，补丁作为旁路集合存在。",
        "- 补丁只有在修复来源问题、且没有造成其他问题回退时，才会被接受。",
        "- 如果源文档变化，补丁需要重新验证。",
        "- 本报告只评估检索阶段是否找到了完整证据，不评估最终大模型回答质量。",
        "- 小样本运行只适合检查流程，正式结论应以完整题目数运行结果为准。",
        "",
    ]

    lines += ["## 10. 文件位置", ""]
    artifact_paths = [
        out_dir / "run_config.json",
        out_dir / "report.md",
        base_dir / "failure_diagnosis.md",
        hybrid_dir / "comparison_report.md",
        hybrid_dir / "patch_decisions.json",
        bm25_dir / "hybrid_bm25_report.md",
        triage_dir / "final_triage_report.md",
        qdrant_patch_dir / "qdrant_comparison_report.md",
        out_dir / "logs",
    ]
    for path in artifact_paths:
        if path.exists() or path == out_dir / "report.md":
            lines.append(f"- `{display_path(path)}`")
    lines.append("")

    report_path = out_dir / "report.md"
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path

def copy_report_to_project(report_path: Path, config: dict[str, Any]) -> dict[str, str]:
    report_dir = ROOT / "report"
    report_dir.mkdir(parents=True, exist_ok=True)
    limit_label = "all" if int(config.get("limit", 0) or 0) <= 0 else str(config.get("limit"))
    chunk_size = config.get("chunk_size")
    overlap = config.get("overlap")
    run_id = config.get("run_id")
    final_name = f"report_{run_id}_n{limit_label}_c{chunk_size}_o{overlap}.md"
    final_path = report_dir / final_name
    latest_path = report_dir / "latest_report.md"
    shutil.copy2(report_path, final_path)
    shutil.copy2(report_path, latest_path)
    return {"report_dir": str(report_dir), "final_report": str(final_path), "latest_report": str(latest_path)}

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a local RecallRAG engineering evaluation into project temp/.")
    parser.add_argument("--docs", default="case_zh_dureader_120/docs")
    parser.add_argument("--questions", default="case_zh_dureader_120/eval/questions_patch_source.jsonl")
    parser.add_argument("--limit", type=int, default=120, help="Number of questions to evaluate. <=0 means all.")
    parser.add_argument("--sample", action="store_true", help="Randomly sample --limit questions instead of taking the first N.")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", default=None, help="Output directory. Default: temp/engineering_eval_<timestamp>_n<limit>.")
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
    out_dir = Path(args.out) if args.out else ROOT / "temp" / f"engineering_eval_{run_id}_n{limit_label}_c{args.chunk_size}_o{args.overlap}"
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
        report_copy = copy_report_to_project(report_path, config)
        config["project_report"] = report_copy
        write_json(out_dir / "run_config.json", config)
        print("\nDONE")
        print(f"Engineering report: {report_path}")
        print(f"Project report: {report_copy['final_report']}")
        print(f"Latest project report: {report_copy['latest_report']}")
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
