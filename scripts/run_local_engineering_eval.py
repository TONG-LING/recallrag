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

    delta = comparison.get("delta") or {}
    fixed_qids = comparison.get("fixed", []) if comparison else []
    regressed_qids = comparison.get("regressed", []) if comparison else []
    unchanged_failed_qids = comparison.get("unchanged_failure", []) if comparison else []
    service_base_metrics = qdrant_main_metrics or base_metrics
    service_patch_metrics = qdrant_patch_metrics or hybrid_metrics
    service_delta = (qdrant_cmp.get("delta") if qdrant_cmp else None) or delta
    service_fixed_qids = (qdrant_cmp.get("fixed") if qdrant_cmp else None) or fixed_qids
    service_regressed_qids = (qdrant_cmp.get("regressed") if qdrant_cmp else None) or regressed_qids
    service_metrics_source = "Qdrant 双集合检索" if qdrant_main_metrics and qdrant_patch_metrics else "离线向量产物评估"
    accepted_decisions = [d for d in patch_decisions if d.get("status") == "accepted"]
    review_decisions = [d for d in patch_decisions if d.get("status") == "needs_review"]
    rejected_decisions = [d for d in patch_decisions if d.get("status") == "rejected"]
    not_selected_decisions = [d for d in patch_decisions if d.get("status") == "candidate_not_selected"]

    generated_at = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    emb = config.get("embedding_check") or {}
    qdrant = config.get("qdrant_check") or {}
    qsel = config.get("question_selection") or {}
    qdrant_collections = config.get("qdrant_collections") or {}

    lines: list[str] = []
    lines += ["# RecallRAG 本地工程化评估报告", ""]
    lines += [
        f"- **生成时间**：`{generated_at}`",
        f"- **运行编号**：`{config.get('run_id')}`",
        f"- **报告目录**：`{out_dir}`",
        f"- **评估题目数**：`{qsel.get('selected')}` / `{qsel.get('total_available')}`",
        "",
    ]

    lines += ["## 1. 结论摘要", ""]
    lines += [
        "本次评估围绕 RAG 检索中的证据召回完整性问题展开：主索引保持不变，仅在失败样例触发后生成旁路 Patch Index，并通过验证门决定是否启用 patch。",
        "",
        "| 项目 | 结果 |",
        "|---|---:|",
        f"| 指标来源 | {service_metrics_source} |",
        f"| Main-only Hits | {service_base_metrics.get('hits')} / {service_base_metrics.get('total')} |",
        f"| Main+Patch Hits | {service_patch_metrics.get('hits')} / {service_patch_metrics.get('total')} |",
        f"| Hit 增量 | {service_delta.get('hits', 0):+} |",
        f"| Recall@{top_k} 增量 | {fmt_float(service_delta.get('recall'))} |",
        f"| MRR 增量 | {fmt_float(service_delta.get('mrr'))} |",
        f"| 已接受 Patch 数 | {len(accepted_decisions)} |",
        f"| 修复 query 数 | {len(service_fixed_qids)} |",
        f"| 回归 query 数 | {len(service_regressed_qids)} |",
        "",
    ]
    if service_regressed_qids:
        lines.append(f"> 风险提示：本次 main+patch 评估出现回归 query：`{list_or_dash(service_regressed_qids)}`，对应 patch 不应直接上线，需要进入复核。")
    else:
        lines.append("> 安全性结论：本次评估未观察到 main+patch 相比 main-only 的成功样例回归。")
    lines.append("")

    lines += ["## 2. 环境与依赖检查", ""]
    lines += [
        "| 检查项 | 状态 | 关键信息 |",
        "|---|---|---|",
        f"| Embedding 服务 | `{emb.get('status')}` | endpoint=`{emb.get('endpoint')}`, model=`{emb.get('model')}`, dim=`{emb.get('dim')}`, latency=`{emb.get('latency_sec')}s` |",
        f"| Qdrant 服务 | `{qdrant.get('status')}` | url=`{qdrant.get('url')}`, collections=`{qdrant.get('collection_count')}`, latency=`{qdrant.get('latency_sec')}s` |",
        "",
    ]
    if qdrant_collections:
        lines += [
            "本次运行使用临时 Qdrant collection：",
            "",
            f"- main collection：`{qdrant_collections.get('main_collection')}`",
            f"- patch collection：`{qdrant_collections.get('patch_collection')}`",
            "",
        ]

    lines += ["## 3. 评估配置", ""]
    lines += [
        "| 配置项 | 值 |",
        "|---|---|",
        f"| 文档目录 | `{config.get('docs')}` |",
        f"| 原始问题集 | `{config.get('questions')}` |",
        f"| 临时问题集 | `{qsel.get('output')}` |",
        f"| 题目选择方式 | `{qsel.get('mode')}` |",
        f"| chunk_size / overlap | `{config.get('chunk_size')}` / `{config.get('overlap')}` |",
        f"| keep_heading | `{config.get('keep_heading')}` |",
        f"| top_k | `{top_k}` |",
        f"| patch_k | `{config.get('patch_k')}` |",
        f"| coverage_threshold | `{config.get('coverage_threshold')}` |",
        f"| batch_size | `{config.get('batch_size')}` |",
        "",
    ]

    lines += ["## 4. 评估口径", ""]
    lines += [
        "本报告不使用普通文档级命中作为唯一标准，而采用证据级命中：Top-K 结果必须来自正确文档，并且 chunk 对 gold evidence span 的覆盖率达到阈值。",
        "",
        f"- **成功标准**：`doc_id` 匹配且 evidence coverage ≥ `{config.get('coverage_threshold')}`。",
        "- **Patch 触发条件**：仅对 main-only 失败且诊断为 near-miss / 局部上下文不足的样例生成 candidate。",
        "- **Patch 接受条件**：candidate 单独 probe 能修复源 query，合并后全量评估不引入 regression。",
        "- **BM25 countercheck**：如果 BM25 或 Dense+BM25 能修复该失败，说明失败可能是检索策略敏感，不应直接归因于 chunking。",
        "- **Qdrant 验证**：Main Index 与 Patch Index 使用独立 collection，验证旁路 patch 在向量库形态下的检索效果。",
        "",
    ]

    lines += ["## 5. Qdrant 主检索指标", ""]
    lines += [
        "本脚本默认要求 Qdrant 已启动，最终检索效果以 Qdrant 双集合验证为准。离线向量产物评估只用于诊断、patch candidate 筛选和一致性对照。",
        "",
        f"| Route | Recall@{top_k} | MRR | Hits | Failed |",
        "|---|---:|---:|---:|---:|",
        metric_row("main collection", service_base_metrics, top_k),
        metric_row("main + patch collections", service_patch_metrics, top_k),
        f"| delta | {fmt_float(service_delta.get('recall'))} | {fmt_float(service_delta.get('mrr'))} | {service_delta.get('hits')} | - |",
    ]
    lines += [
        "",
        "### 5.1 离线候选筛选指标",
        "",
        "以下指标来自本地 `chunks.json` / `vectors.json` 产物，用于 patch 生成、probe、回归检查和 Qdrant 写入前的候选筛选。该表不是第二套线上路由。",
        "",
        f"| Route | Recall@{top_k} | MRR | Hits | Failed |",
        "|---|---:|---:|---:|---:|",
        metric_row("offline main-only", base_metrics, top_k),
        metric_row("offline main + patch", hybrid_metrics, top_k),
        f"| offline delta | {fmt_float(delta.get('recall'))} | {fmt_float(delta.get('mrr'))} | {delta.get('hits')} | - |",
        "",
    ]

    if sig:
        lines += ["## 6. 配对检验", ""]
        lines += [
            "| 指标 | 值 |",
            "|---|---:|",
            f"| before_hits | {sig.get('before_hits')} |",
            f"| after_hits | {sig.get('after_hits')} |",
            f"| wins | {sig.get('wins')} |",
            f"| losses | {sig.get('losses')} |",
            f"| ties | {sig.get('ties')} |",
            f"| recall_delta | {fmt_float(sig.get('recall_delta'))} |",
            f"| recall_delta_bootstrap_ci95 | `{sig.get('recall_delta_bootstrap_ci95')}` |",
            f"| mrr_delta | {fmt_float(sig.get('mrr_delta'))} |",
            f"| mrr_delta_bootstrap_ci95 | `{sig.get('mrr_delta_bootstrap_ci95')}` |",
            f"| exact_mcnemar_pvalue | {sig.get('exact_mcnemar_pvalue')} |",
            "",
            f"逐 query 明细见：`{hybrid_dir / 'paired_significance.json'}`",
            "",
        ]

    lines += ["## 7. 失败诊断统计", ""]
    lines += [
        f"main-only 失败 query 数：`{len(diagnoses)}`。诊断阶段只基于 retrieval trace 定位 near-miss 窗口，不使用 gold span 来生成 patch。",
        "",
        "### 7.1 按 failure family 统计",
        "",
        "| failure_family | count |",
        "|---|---:|",
    ]
    if diagnosis_family:
        for k, v in diagnosis_family.most_common():
            lines.append(f"| `{k}` | {v} |")
    else:
        lines.append("| - | 0 |")
    lines += ["", "### 7.2 按 diagnosed_failure_type 统计", "", "| diagnosed_failure_type | count |", "|---|---:|"]
    if diagnosis_type:
        for k, v in diagnosis_type.most_common():
            lines.append(f"| `{k}` | {v} |")
    else:
        lines.append("| - | 0 |")
    lines.append("")

    lines += ["## 8. Patch 生成与筛选", ""]
    lines += [
        "Patch 采用旁路索引策略：主索引不被改写；candidate 先进入临时 patch 集，经过 probe 和全量回归检查后，才允许进入 selected patch 集。",
        "",
        "| 项目 | 数量 / 分布 |",
        "|---|---|",
        f"| materialized patch candidates | `{patch_meta.get('count')}` |",
        f"| candidate probe results | `{len(candidate_probe)}` |",
        f"| probe candidate type counts | `{dict(probe_type_counts)}` |",
        f"| selected patch candidates | `{len(selected)}` |",
        f"| selected patch type counts | `{dict(selected_type_counts)}` |",
        f"| patch decision counts | `{dict(decision_counts)}` |",
        "",
        "| movement | qids |",
        "|---|---|",
        f"| fixed | `{list_or_dash(fixed_qids)}` |",
        f"| regressed | `{list_or_dash(regressed_qids)}` |",
        f"| unchanged_failure | `{list_or_dash(unchanged_failed_qids)}` |",
        "",
    ]

    if bm25_metrics:
        lines += ["## 9. BM25 / Dense+BM25 反证检查", ""]
        lines += [
            "该部分用于判断失败是否只是 dense retrieval 策略问题。如果 BM25 或 Dense+BM25 能修复，则该样例不应简单归因于 chunk 边界问题。",
            "",
            f"| Route | Recall@{top_k} | MRR | Hits | Failed |",
            "|---|---:|---:|---:|---:|",
        ]
        for name in ["dense", "bm25", "dense_bm25"]:
            row = bm25_metrics.get(name) or {}
            if row:
                lines.append(metric_row(name, row, top_k))
        lines.append("")

    if triage:
        lines += ["## 10. Final Triage 汇总", ""]
        lines += [
            "Final triage 综合 dense 失败、patch 修复、BM25 countercheck 和 Qdrant 验证信号，输出最终工程动作。",
            "",
            "| 项目 | 数量 |",
            "|---|---:|",
            f"| total_dense_failures | {triage.get('total_dense_failures')} |",
            f"| accepted_patch_candidates | {triage.get('accepted_patch_candidates')} |",
            f"| retrieval_strategy_sensitive | {triage.get('retrieval_strategy_sensitive')} |",
            f"| manual_review | {triage.get('manual_review')} |",
            "",
        ]

    lines += ["## 11. 逐失败样例工程决策表", ""]
    if not diagnoses:
        lines += ["本次评估中 main-only 没有产生 dense retrieval 失败样例，因此没有触发 patch 诊断。", ""]
    else:
        lines += [
            "| qid | question | raw diagnosis | patch_allowed | final_decision | accepted_patch_type | base_cov | patch_cov | bm25_fixed | qdrant_patch_fixed | action |",
            "|---|---|---|---:|---|---|---:|---:|---:|---:|---|",
        ]
        for d in diagnoses:
            qid = d.get("qid")
            tr = triage_by_qid.get(qid, {})
            signals = tr.get("signals", {}) or {}
            q_decisions = decisions_by_qid.get(qid, [])
            accepted = [x for x in q_decisions if x.get("status") == "accepted"]
            accepted_types = sorted({x.get("candidate_type") for x in accepted if x.get("candidate_type")})
            lines.append(
                f"| {qid} | {short_text(d.get('question'), 42)} | `{d.get('diagnosed_failure_type')}` | "
                f"{d.get('patch_allowed')} | `{zh_status(tr.get('final_decision', '-'))}` | "
                f"`{','.join(accepted_types) if accepted_types else '-'}` | "
                f"{signals.get('base_best_coverage')} | {signals.get('patch_best_coverage')} | "
                f"{signals.get('bm25_fixed')} | {signals.get('qdrant_patch_fixed')} | "
                f"`{tr.get('recommended_action', '-')}` |"
            )
        lines.append("")

    lines += ["## 12. 逐失败样例详细说明", ""]
    if not diagnoses:
        lines.append("无失败样例详情。")
        lines.append("")
    else:
        for d in diagnoses:
            qid = d.get("qid")
            tr = triage_by_qid.get(qid, {})
            signals = tr.get("signals", {}) or {}
            q_decisions = decisions_by_qid.get(qid, [])
            accepted = [x for x in q_decisions if x.get("status") == "accepted"]
            reviewed = [x for x in q_decisions if x.get("status") == "needs_review"]
            rejected = [x for x in q_decisions if x.get("status") == "rejected"]
            not_selected = [x for x in q_decisions if x.get("status") == "candidate_not_selected"]
            lines += [
                f"### {qid} — {md_escape(d.get('question'))}",
                "",
                f"- gold：`{d.get('gold_doc')} > {d.get('gold_section', '')}`",
                f"- 原始诊断：`{d.get('failure_family')} / {d.get('diagnosed_failure_type')}`",
                f"- 诊断置信度：`{d.get('confidence')}`",
                f"- 诊断原因：{md_escape(d.get('reason'))}",
                f"- 是否允许生成 patch：`{d.get('patch_allowed')}`",
                f"- final_decision：`{zh_status(tr.get('final_decision', '-'))}`",
                f"- recommended_action：`{tr.get('recommended_action', '-')}`",
                "",
                "检索信号：",
                "",
                f"- dense_failed：`{signals.get('dense_failed')}`",
                f"- json_patch_fixed：`{signals.get('json_patch_fixed')}`",
                f"- qdrant_patch_fixed：`{signals.get('qdrant_patch_fixed')}`",
                f"- bm25_fixed：`{signals.get('bm25_fixed')}`",
                f"- dense_bm25_fixed：`{signals.get('dense_bm25_fixed')}`",
                f"- coverage：`{signals.get('base_best_coverage')}` -> `{signals.get('patch_best_coverage')}`",
                "",
                "Patch 决策：",
                "",
                f"- accepted：`{[x.get('patch_id') for x in accepted]}`",
                f"- needs_review：`{[x.get('patch_id') for x in reviewed]}`",
                f"- rejected：`{[x.get('patch_id') for x in rejected]}`",
                f"- candidate_not_selected：`{[x.get('patch_id') for x in not_selected]}`",
                "",
            ]
            rationale = tr.get("rationale") or []
            if rationale:
                lines += ["决策依据：", ""]
                for item in rationale:
                    lines.append(f"- {md_escape(item)}")
                lines.append("")

    lines += ["## 13. 已接受 Patch 详情", ""]
    if not accepted_decisions:
        lines += ["本次运行没有 accepted patch candidate。", ""]
    else:
        for d in accepted_decisions:
            probe = d.get("candidate_probe") or {}
            lines += [
                f"### {d.get('patch_id')}",
                "",
                "| 字段 | 值 |",
                "|---|---|",
                f"| qid | `{d.get('qid')}` |",
                f"| candidate_type | `{d.get('candidate_type')}` |",
                f"| failure_type | `{d.get('failure_type')}` |",
                f"| anchor_chunk_id | `{d.get('anchor_chunk_id')}` |",
                f"| affected_main_chunks | `{d.get('affected_main_chunks')}` |",
                f"| before_rank / after_rank | `{d.get('before_rank')}` -> `{d.get('after_rank')}` |",
                f"| before_coverage / after_coverage | `{d.get('before_best_coverage')}` -> `{d.get('after_best_coverage')}` |",
                f"| individual_probe_rank | `{probe.get('rank')}` |",
                f"| individual_probe_coverage | `{probe.get('best_topk_coverage')}` |",
                f"| decision_reason | {md_escape(d.get('decision_reason'))} |",
                "",
            ]

    if review_decisions or rejected_decisions or not_selected_decisions:
        lines += ["## 14. 未接受 Patch 统计", ""]
        lines += [
            "| 状态 | 数量 | 说明 |",
            "|---|---:|---|",
            f"| needs_review | {len(review_decisions)} | 可能存在回归或证据不足，需要人工复核 |",
            f"| rejected | {len(rejected_decisions)} | 源 query 未被修复 |",
            f"| candidate_not_selected | {len(not_selected_decisions)} | 同一 query 下存在更优候选，当前候选未被选中 |",
            "",
        ]

    if qdrant_cmp:
        lines += ["## 15. Qdrant 双集合验证", ""]
        lines += [
            "Qdrant 验证用于确认 Main Index 和 Patch Index 分离后的检索行为。Patch collection 仅加载通过验证的 selected patch。",
            "",
            f"- qdrant fixed qids：`{list_or_dash(qdrant_cmp.get('fixed'))}`",
            f"- qdrant regressed qids：`{list_or_dash(qdrant_cmp.get('regressed'))}`",
            f"- qdrant unchanged_failure：`{list_or_dash(qdrant_cmp.get('unchanged_failure'))}`",
            f"- qdrant comparison report：`{qdrant_patch_dir / 'qdrant_comparison_report.md'}`",
            "",
        ]

    lines += ["## 16. 工程化解释与上线边界", ""]
    lines += [
        "- 主索引在整个流程中不被直接改写，patch 作为旁路增量层存在。",
        "- patch 必须经过 source query probe 和全量 regression check，不能因为生成成功就直接进入检索系统。",
        "- BM25 / Dense+BM25 反证检查用于避免把检索策略问题误判为 chunking 问题。",
        "- Qdrant 侧采用 main collection 与 patch collection 分离，便于回滚、停用和重新验证。",
        "- 如果源文档或来源窗口发生变化，应重新计算来源窗口 hash，并将旧 patch 标记为 stale 后重新验证。",
        "- 本报告只评估检索证据召回，不评估最终 LLM 答案生成质量。",
        "",
    ]

    lines += ["## 17. 风险与局限", ""]
    lines += [
        "1. 本次评估依赖当前 embedding 模型和本地服务状态，替换 embedding 后指标可能变化。",
        "2. 评估集规模由 `--limit` 控制，小样本运行只适合作为流程检查，不应作为最终效果结论。",
        "3. Patch 主要修复局部上下文不足或 chunk 边界断裂，不覆盖文档缺失、语义表达差异过大或 embedding 模型能力不足等失败。",
        "4. Qdrant collection 为本次运行创建的临时集合；若需要长期保留，应另行制定 collection 命名、版本和清理策略。",
        "5. accepted patch 仍应结合人工 case review，尤其是业务知识库场景中的事实一致性和时效性。",
        "",
    ]

    lines += ["## 18. 输出产物索引", ""]
    artifact_paths = [
        out_dir / "run_config.json",
        base_dir / "eval_report.md",
        base_dir / "failure_diagnosis.md",
        base_dir / "failure_diagnosis.json",
        patch_dir / "patch_log.json",
        patch_dir / "patch_log_evaluated.json",
        hybrid_dir / "comparison_report.md",
        hybrid_dir / "comparison.json",
        hybrid_dir / "patch_decisions.json",
        hybrid_dir / "paired_significance.md",
        bm25_dir / "hybrid_bm25_report.md",
        triage_dir / "final_triage_report.md",
        triage_dir / "final_triage.json",
        qdrant_patch_dir / "qdrant_comparison_report.md",
        qdrant_patch_dir / "qdrant_comparison_report.json",
        out_dir / "logs",
    ]
    for p in artifact_paths:
        if p.exists():
            lines.append(f"- `{p}`")
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
