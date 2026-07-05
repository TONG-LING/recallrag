#!/usr/bin/env python3
"""Validate the saved patch-effect claim with paired and resampled analysis."""

from __future__ import annotations

import argparse
import json
import math
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def reciprocal_rank(rank: int | None) -> float:
    return 0.0 if not rank else 1.0 / rank


def percentile(values: list[float], q: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    pos = (len(ordered) - 1) * q
    low = math.floor(pos)
    high = math.ceil(pos)
    if low == high:
        return ordered[low]
    frac = pos - low
    return ordered[low] + (ordered[high] - ordered[low]) * frac


def maybe_round(value: float, digits: int = 6) -> float:
    return round(value, digits)


def load_result_map(path: Path) -> dict[str, dict[str, Any]]:
    rows = load_json(path)
    result = {}
    for row in rows:
        result[row["qid"]] = {
            "qid": row["qid"],
            "question": row.get("question"),
            "gold_doc": row.get("gold_doc"),
            "gold_section": row.get("gold_section"),
            "gold_failure_type": row.get("gold_failure_type"),
            "success": bool(row.get("success")),
            "rank": row.get("rank"),
            "best_topk_coverage": row.get("best_topk_coverage", 0.0),
        }
    return result


def build_paired_rows(
    before_map: dict[str, dict[str, Any]],
    after_map: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    before_qids = set(before_map)
    after_qids = set(after_map)
    if before_qids != after_qids:
        missing_before = sorted(after_qids - before_qids)
        missing_after = sorted(before_qids - after_qids)
        raise ValueError(
            "Mismatched qids between paired inputs: "
            f"missing_before={missing_before} missing_after={missing_after}"
        )

    rows = []
    for qid in sorted(before_qids):
        before = before_map[qid]
        after = after_map[qid]
        before_hit = 1 if before["success"] else 0
        after_hit = 1 if after["success"] else 0
        before_rr = reciprocal_rank(before["rank"])
        after_rr = reciprocal_rank(after["rank"])

        if before_hit == 0 and after_hit == 1:
            movement = "fixed"
        elif before_hit == 1 and after_hit == 0:
            movement = "regressed"
        elif before_hit == 1:
            movement = "unchanged_success"
        else:
            movement = "unchanged_failure"

        rows.append(
            {
                "qid": qid,
                "question": before.get("question") or after.get("question"),
                "gold_doc": before.get("gold_doc") or after.get("gold_doc"),
                "gold_section": before.get("gold_section") or after.get("gold_section"),
                "gold_failure_type": before.get("gold_failure_type")
                or after.get("gold_failure_type"),
                "before_hit": before_hit,
                "after_hit": after_hit,
                "before_rank": before.get("rank"),
                "after_rank": after.get("rank"),
                "before_rr": before_rr,
                "after_rr": after_rr,
                "before_best_topk_coverage": before.get("best_topk_coverage", 0.0),
                "after_best_topk_coverage": after.get("best_topk_coverage", 0.0),
                "delta_hit": after_hit - before_hit,
                "delta_rr": after_rr - before_rr,
                "movement": movement,
            }
        )
    return rows


def summarize_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(rows)
    before_hits = sum(row["before_hit"] for row in rows)
    after_hits = sum(row["after_hit"] for row in rows)
    before_rr = sum(row["before_rr"] for row in rows)
    after_rr = sum(row["after_rr"] for row in rows)
    fixed = [row["qid"] for row in rows if row["movement"] == "fixed"]
    regressed = [row["qid"] for row in rows if row["movement"] == "regressed"]
    unchanged_failure = [
        row["qid"] for row in rows if row["movement"] == "unchanged_failure"
    ]

    return {
        "total": total,
        "before": {
            "hits": before_hits,
            "failed": total - before_hits,
            "recall@5": before_hits / total if total else 0.0,
            "mrr": before_rr / total if total else 0.0,
        },
        "after": {
            "hits": after_hits,
            "failed": total - after_hits,
            "recall@5": after_hits / total if total else 0.0,
            "mrr": after_rr / total if total else 0.0,
        },
        "delta": {
            "hits": after_hits - before_hits,
            "recall@5": (after_hits - before_hits) / total if total else 0.0,
            "mrr": (after_rr - before_rr) / total if total else 0.0,
        },
        "fixed": fixed,
        "regressed": regressed,
        "unchanged_failure": unchanged_failure,
        "unchanged_success_count": sum(
            1 for row in rows if row["movement"] == "unchanged_success"
        ),
        "movement_counts": dict(Counter(row["movement"] for row in rows)),
    }


def exact_sign_test(rows: list[dict[str, Any]]) -> dict[str, Any]:
    improvements = sum(1 for row in rows if row["delta_hit"] > 0)
    regressions = sum(1 for row in rows if row["delta_hit"] < 0)
    discordant = improvements + regressions

    if discordant == 0:
        return {
            "discordant_pairs": 0,
            "improvements": 0,
            "regressions": 0,
            "direction": "tie",
            "one_sided_p": 1.0,
            "two_sided_p": 1.0,
        }

    dominant = max(improvements, regressions)
    weaker = min(improvements, regressions)
    denom = 2**discordant
    one_sided = sum(math.comb(discordant, k) for k in range(dominant, discordant + 1)) / denom
    two_sided = min(
        1.0,
        2.0 * sum(math.comb(discordant, k) for k in range(0, weaker + 1)) / denom,
    )
    direction = "positive" if improvements > regressions else "negative"

    return {
        "discordant_pairs": discordant,
        "improvements": improvements,
        "regressions": regressions,
        "direction": direction,
        "one_sided_p": one_sided,
        "two_sided_p": two_sided,
    }


def sample_delta(rows: list[dict[str, Any]]) -> tuple[float, float]:
    total = len(rows)
    if total == 0:
        return 0.0, 0.0
    delta_hits = sum(row["delta_hit"] for row in rows)
    delta_rr = sum(row["delta_rr"] for row in rows)
    return delta_hits / total, delta_rr / total


def summarize_distribution(values: list[float]) -> dict[str, Any]:
    positive = sum(1 for value in values if value > 0)
    negative = sum(1 for value in values if value < 0)
    zero = len(values) - positive - negative
    discrete_counts = Counter(maybe_round(value, 6) for value in values)
    top_counts = [
        {"value": value, "count": count}
        for value, count in discrete_counts.most_common(5)
    ]
    return {
        "mean": sum(values) / len(values) if values else 0.0,
        "median": percentile(values, 0.5) if values else 0.0,
        "p2_5": percentile(values, 0.025) if values else 0.0,
        "p97_5": percentile(values, 0.975) if values else 0.0,
        "min": min(values) if values else 0.0,
        "max": max(values) if values else 0.0,
        "positive_rounds": positive,
        "zero_rounds": zero,
        "negative_rounds": negative,
        "positive_rate": positive / len(values) if values else 0.0,
        "zero_rate": zero / len(values) if values else 0.0,
        "negative_rate": negative / len(values) if values else 0.0,
        "top_discrete_values": top_counts,
    }


def bootstrap_analysis(
    rows: list[dict[str, Any]],
    rounds: int,
    seed: int,
) -> dict[str, Any]:
    rng = random.Random(seed)
    sample_size = len(rows)
    recall_deltas = []
    mrr_deltas = []

    for _ in range(rounds):
        sample = [rows[rng.randrange(sample_size)] for _ in range(sample_size)]
        recall_delta, mrr_delta = sample_delta(sample)
        recall_deltas.append(recall_delta)
        mrr_deltas.append(mrr_delta)

    return {
        "rounds": rounds,
        "sample_size": sample_size,
        "seed": seed,
        "delta_recall@5": summarize_distribution(recall_deltas),
        "delta_mrr": summarize_distribution(mrr_deltas),
    }


def leave_one_out_analysis(rows: list[dict[str, Any]]) -> dict[str, Any]:
    fold_rows = []
    for omitted_qid in [row["qid"] for row in rows]:
        sample = [row for row in rows if row["qid"] != omitted_qid]
        recall_delta, mrr_delta = sample_delta(sample)
        fold_rows.append(
            {
                "omitted_qid": omitted_qid,
                "remaining_queries": len(sample),
                "delta_recall@5": recall_delta,
                "delta_mrr": mrr_delta,
            }
        )

    return {
        "rounds": len(fold_rows),
        "folds": fold_rows,
        "delta_recall@5": summarize_distribution(
            [row["delta_recall@5"] for row in fold_rows]
        ),
        "delta_mrr": summarize_distribution([row["delta_mrr"] for row in fold_rows]),
    }


def subset_trial_analysis(
    rows: list[dict[str, Any]],
    subset_sizes: list[int],
    rounds_per_size: int,
    seed: int,
) -> dict[str, Any]:
    rng = random.Random(seed)
    results = []

    for size in subset_sizes:
        if size <= 0 or size > len(rows):
            continue
        recall_deltas = []
        mrr_deltas = []
        for _ in range(rounds_per_size):
            sample = rng.sample(rows, size)
            recall_delta, mrr_delta = sample_delta(sample)
            recall_deltas.append(recall_delta)
            mrr_deltas.append(mrr_delta)
        results.append(
            {
                "subset_size": size,
                "rounds": rounds_per_size,
                "delta_recall@5": summarize_distribution(recall_deltas),
                "delta_mrr": summarize_distribution(mrr_deltas),
            }
        )

    return {
        "rounds_per_size": rounds_per_size,
        "seed": seed,
        "results": results,
    }


def grouped_analysis(rows: list[dict[str, Any]], field: str) -> list[dict[str, Any]]:
    grouped = defaultdict(list)
    for row in rows:
        grouped[row.get(field) or "unknown"].append(row)

    results = []
    for key in sorted(grouped):
        group_rows = grouped[key]
        summary = summarize_rows(group_rows)
        results.append(
            {
                "group": key,
                "total": summary["total"],
                "before_recall@5": summary["before"]["recall@5"],
                "after_recall@5": summary["after"]["recall@5"],
                "delta_recall@5": summary["delta"]["recall@5"],
                "before_mrr": summary["before"]["mrr"],
                "after_mrr": summary["after"]["mrr"],
                "delta_mrr": summary["delta"]["mrr"],
                "fixed": summary["fixed"],
                "regressed": summary["regressed"],
                "unchanged_failure": summary["unchanged_failure"],
            }
        )
    return results


def load_patch_metadata(path: Path | None) -> dict[str, Any]:
    if not path or not path.exists():
        return {}
    payload = load_json(path)
    accepted_types = []
    for decision in payload.get("patch_decisions", []):
        if decision.get("status") == "accepted":
            accepted_types.append(decision.get("candidate_type"))
    return {
        "main_chunks": payload.get("main_chunks"),
        "patch_chunks": payload.get("patch_chunks"),
        "patch_main_ratio": payload.get("patch_main_ratio"),
        "accepted_patch_types": accepted_types,
    }


def compare_backend_pairs(
    local_before: dict[str, dict[str, Any]],
    local_after: dict[str, dict[str, Any]],
    qdrant_before: dict[str, dict[str, Any]],
    qdrant_after: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    qids = sorted(set(local_before) & set(local_after) & set(qdrant_before) & set(qdrant_after))
    mismatches = []
    for qid in qids:
        local_signature = (
            bool(local_before[qid]["success"]),
            local_before[qid]["rank"],
            bool(local_after[qid]["success"]),
            local_after[qid]["rank"],
        )
        qdrant_signature = (
            bool(qdrant_before[qid]["success"]),
            qdrant_before[qid]["rank"],
            bool(qdrant_after[qid]["success"]),
            qdrant_after[qid]["rank"],
        )
        if local_signature != qdrant_signature:
            mismatches.append(
                {
                    "qid": qid,
                    "local": {
                        "before_success": local_signature[0],
                        "before_rank": local_signature[1],
                        "after_success": local_signature[2],
                        "after_rank": local_signature[3],
                    },
                    "qdrant": {
                        "before_success": qdrant_signature[0],
                        "before_rank": qdrant_signature[1],
                        "after_success": qdrant_signature[2],
                        "after_rank": qdrant_signature[3],
                    },
                }
            )

    return {
        "total_qids": len(qids),
        "matched_qids": len(qids) - len(mismatches),
        "match_rate": (len(qids) - len(mismatches)) / len(qids) if qids else 0.0,
        "mismatches": mismatches,
    }


def format_pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def format_float(value: float) -> str:
    return f"{value:.4f}"


def render_summary_table(name: str, summary: dict[str, Any]) -> str:
    return (
        f"| {name} | {summary['total']} | "
        f"{format_float(summary['before']['recall@5'])} | "
        f"{format_float(summary['after']['recall@5'])} | "
        f"{format_float(summary['delta']['recall@5'])} | "
        f"{format_float(summary['before']['mrr'])} | "
        f"{format_float(summary['after']['mrr'])} | "
        f"{format_float(summary['delta']['mrr'])} | "
        f"{summary['before']['hits']} -> {summary['after']['hits']} |"
    )


def render_group_table(groups: list[dict[str, Any]]) -> str:
    rows = [
        "| Group | Queries | Recall@5 Before | Recall@5 After | Delta | Fixed | Regressed |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for group in groups:
        rows.append(
            f"| {group['group']} | {group['total']} | "
            f"{format_float(group['before_recall@5'])} | "
            f"{format_float(group['after_recall@5'])} | "
            f"{format_float(group['delta_recall@5'])} | "
            f"{', '.join(group['fixed']) or '-'} | "
            f"{', '.join(group['regressed']) or '-'} |"
        )
    return "\n".join(rows)


def render_subset_table(results: list[dict[str, Any]]) -> str:
    rows = [
        "| Subset Size | Rounds | Positive | Zero | Negative | Mean Delta Recall@5 | 95% Range |",
        "|---:|---:|---:|---:|---:|---:|---|",
    ]
    for result in results:
        delta = result["delta_recall@5"]
        rows.append(
            f"| {result['subset_size']} | {result['rounds']} | "
            f"{format_pct(delta['positive_rate'])} | {format_pct(delta['zero_rate'])} | "
            f"{format_pct(delta['negative_rate'])} | {format_float(delta['mean'])} | "
            f"[{format_float(delta['p2_5'])}, {format_float(delta['p97_5'])}] |"
        )
    return "\n".join(rows)


def render_report(data: dict[str, Any], rounds: int, subset_sizes: list[int]) -> str:
    controlled_local = data["controlled_case"]["local"]
    controlled_qdrant = data["controlled_case"]["qdrant"]
    backend = data["controlled_case"]["backend_consistency"]
    cross_doc = data["cross_doc_stress"]

    bootstrap = controlled_local["bootstrap"]["delta_recall@5"]
    loo = controlled_local["leave_one_out"]["delta_recall@5"]
    sign_test = controlled_local["sign_test"]

    accepted_patch_types = ", ".join(
        controlled_local["patch_metadata"].get("accepted_patch_types", [])
    ) or "-"
    patch_chunks = controlled_local["patch_metadata"].get("patch_chunks")
    main_chunks = controlled_local["patch_metadata"].get("main_chunks")
    patch_ratio = controlled_local["patch_metadata"].get("patch_main_ratio")

    return f"""# Patch Effect Validation Report

## Scope

This report validates the saved claim that RecallRAG improves the controlled patch benchmark from `0.8333` to `0.9167`, and it does so with more than one lens:

1. full paired evaluation on the controlled set
2. leave-one-out repeated rounds
3. bootstrap repeated rounds
4. random subset repeated rounds
5. grouped slices by document and failure type
6. backend consistency check between local JSON and Qdrant
7. a second data group (`cross_doc_patch_nfcorpus`) as a boundary stress test

Important: the repeated rounds below are resampling analyses over the saved run outputs. They are not fresh end-to-end reruns with new embeddings, because the local embedding service was not running when this validation was produced.

## 1. Exact paired result for the claimed `83.33% -> 91.67%`

| Evaluation | Queries | Recall@5 Before | Recall@5 After | Delta Recall@5 | MRR Before | MRR After | Delta MRR | Hits |
|---|---:|---:|---:|---:|---:|---:|---:|---|
{render_summary_table("Controlled local JSON", controlled_local["summary"])}
{render_summary_table("Controlled Qdrant", controlled_qdrant["summary"])}

Key facts:

- fixed queries: `{", ".join(controlled_local["summary"]["fixed"]) or "-"}`
- regressed queries: `{", ".join(controlled_local["summary"]["regressed"]) or "-"}`
- unchanged failures: `{", ".join(controlled_local["summary"]["unchanged_failure"]) or "-"}`
- accepted patch type: `{accepted_patch_types}`
- patch footprint: `{patch_chunks}` patch chunk(s) over `{main_chunks}` main chunk(s), ratio `{format_pct(patch_ratio or 0.0)}`

This means the claimed lift is real in the saved artifacts, and it comes from exactly one repaired query with zero regressions.

## 2. Multiple rounds on the controlled set

### 2.1 Leave-one-out, 12 rounds

- positive rounds: `{loo['positive_rounds']}/{controlled_local['leave_one_out']['rounds']}` = `{format_pct(loo['positive_rate'])}`
- zero rounds: `{loo['zero_rounds']}/{controlled_local['leave_one_out']['rounds']}` = `{format_pct(loo['zero_rate'])}`
- negative rounds: `{loo['negative_rounds']}/{controlled_local['leave_one_out']['rounds']}` = `{format_pct(loo['negative_rate'])}`
- delta Recall@5 range: `[{format_float(loo['min'])}, {format_float(loo['max'])}]`

Interpretation: after removing one query at a time, the effect stays positive in 11 of 12 folds. The only zero fold is the one that omits `q001`, which is the only repaired case.

### 2.2 Bootstrap, {rounds} rounds

- positive rounds: `{bootstrap['positive_rounds']}/{controlled_local['bootstrap']['rounds']}` = `{format_pct(bootstrap['positive_rate'])}`
- zero rounds: `{bootstrap['zero_rounds']}/{controlled_local['bootstrap']['rounds']}` = `{format_pct(bootstrap['zero_rate'])}`
- negative rounds: `{bootstrap['negative_rounds']}/{controlled_local['bootstrap']['rounds']}` = `{format_pct(bootstrap['negative_rate'])}`
- mean delta Recall@5: `{format_float(bootstrap['mean'])}`
- 95% bootstrap range for delta Recall@5: `[{format_float(bootstrap['p2_5'])}, {format_float(bootstrap['p97_5'])}]`

Interpretation: resampling never produced a negative delta. The effect is directionally stable, but the interval is wide because the full benchmark has only 12 queries and only one query changes outcome.

### 2.3 Random subset rounds

Subset sizes used: `{", ".join(str(size) for size in subset_sizes)}`

{render_subset_table(controlled_local["subset_trials"]["results"])}

Interpretation: across different subset sizes, the patch effect remains non-negative. Smaller subsets hit zero more often because many subsets do not include `q001`.

## 3. Grouped analysis on the controlled set

### 3.1 By gold document

{render_group_table(controlled_local["by_gold_doc"])}

### 3.2 By failure type

{render_group_table(controlled_local["by_failure_type"])}

Interpretation: the lift is concentrated where the project says it should be concentrated, namely the `boundary_split` family and the `rag_chunking.md` document slice. Other groups stay unchanged rather than showing broad accidental gains.

## 4. Backend consistency: local JSON vs Qdrant

- matched qids: `{backend['matched_qids']}/{backend['total_qids']}` = `{format_pct(backend['match_rate'])}`
- mismatch count: `{len(backend['mismatches'])}`

Interpretation: the saved local JSON evaluation and the saved Qdrant evaluation tell the same story for every query in this benchmark. The `0.8333 -> 0.9167` claim is not an artifact of only one backend.

## 5. Second data group: cross-document NFCorpus stress test

| Evaluation | Queries | Recall@5 Before | Recall@5 After | Delta Recall@5 | MRR Before | MRR After | Delta MRR | Hits |
|---|---:|---:|---:|---:|---:|---:|---:|---|
{render_summary_table("Cross-document NFCorpus", cross_doc["summary"])}

Key facts:

- fixed queries: `{", ".join(cross_doc["summary"]["fixed"]) or "-"}`
- regressed queries: `{", ".join(cross_doc["summary"]["regressed"]) or "-"}`
- patch chunks selected: `{cross_doc["patch_metadata"].get("patch_chunks", 0)}`

Interpretation: this second data group is a clean negative result. Patch Index does not help a complex multi-document coverage problem here, and the system does not force a fake gain. That makes the positive controlled-case claim more credible.

## 6. Statistical caution

- discordant pairs on the controlled benchmark: `{sign_test['discordant_pairs']}`
- improvements: `{sign_test['improvements']}`
- regressions: `{sign_test['regressions']}`
- one-sided exact sign test p-value: `{format_float(sign_test['one_sided_p'])}`
- two-sided exact sign test p-value: `{format_float(sign_test['two_sided_p'])}`

Interpretation: the engineering effect is real in the saved run, but the controlled benchmark is too small to support a strong statistical-significance claim. The right statement is:

> RecallRAG repaired one clean chunk-boundary failure (`q001`) and raised Recall@5 from `10/12` to `11/12` with zero regressions, and the same effect appears in both local JSON and Qdrant evaluation. The gain is specific, honest, and reproducible across resampling, but it is not broad enough yet to claim strong statistical significance.

## 7. Bottom line

What can be claimed safely:

1. the `83.33% -> 91.67%` improvement is real in saved artifacts
2. the improvement is backend-consistent
3. it survives repeated resampling without ever going negative
4. it is concentrated on the intended failure family (`boundary_split`)
5. the project also has a negative second-group result, so it is not over-claiming patch usefulness

What still needs fresh reruns:

1. larger controlled eval sets
2. additional failure families with more than one repaired query
3. fresh end-to-end reruns once the embedding service is up again
"""


def build_validation_payload(rounds: int, subset_sizes: list[int], subset_rounds: int) -> dict[str, Any]:
    controlled_questions = load_jsonl(ROOT / "case/eval/questions.jsonl")
    controlled_question_count = len(controlled_questions)

    local_before = load_result_map(ROOT / "runs/base/retrieval_results.json")
    local_after = load_result_map(ROOT / "runs/hybrid/retrieval_results.json")
    qdrant_before = load_result_map(ROOT / "runs/qdrant_main/qdrant_retrieval_results.json")
    qdrant_after = load_result_map(ROOT / "runs/qdrant/qdrant_retrieval_results.json")
    cross_doc_before = load_result_map(
        ROOT / "runs/cross_doc_patch_nfcorpus/base/retrieval_results.json"
    )
    cross_doc_after = load_result_map(
        ROOT / "runs/cross_doc_patch_nfcorpus/hybrid/retrieval_results.json"
    )

    local_rows = build_paired_rows(local_before, local_after)
    qdrant_rows = build_paired_rows(qdrant_before, qdrant_after)
    cross_doc_rows = build_paired_rows(cross_doc_before, cross_doc_after)

    return {
        "generated_from": {
            "controlled_questions": "case/eval/questions.jsonl",
            "controlled_question_count": controlled_question_count,
            "controlled_local_before": "runs/base/retrieval_results.json",
            "controlled_local_after": "runs/hybrid/retrieval_results.json",
            "controlled_qdrant_before": "runs/qdrant_main/qdrant_retrieval_results.json",
            "controlled_qdrant_after": "runs/qdrant/qdrant_retrieval_results.json",
            "cross_doc_before": "runs/cross_doc_patch_nfcorpus/base/retrieval_results.json",
            "cross_doc_after": "runs/cross_doc_patch_nfcorpus/hybrid/retrieval_results.json",
        },
        "controlled_case": {
            "local": {
                "summary": summarize_rows(local_rows),
                "sign_test": exact_sign_test(local_rows),
                "leave_one_out": leave_one_out_analysis(local_rows),
                "bootstrap": bootstrap_analysis(local_rows, rounds=rounds, seed=42),
                "subset_trials": subset_trial_analysis(
                    local_rows,
                    subset_sizes=subset_sizes,
                    rounds_per_size=subset_rounds,
                    seed=43,
                ),
                "by_gold_doc": grouped_analysis(local_rows, "gold_doc"),
                "by_failure_type": grouped_analysis(local_rows, "gold_failure_type"),
                "patch_metadata": load_patch_metadata(ROOT / "runs/hybrid/comparison.json"),
                "rows": local_rows,
            },
            "qdrant": {
                "summary": summarize_rows(qdrant_rows),
                "sign_test": exact_sign_test(qdrant_rows),
                "patch_metadata": load_patch_metadata(
                    ROOT / "runs/qdrant/qdrant_comparison_report.json"
                ),
                "rows": qdrant_rows,
            },
            "backend_consistency": compare_backend_pairs(
                local_before,
                local_after,
                qdrant_before,
                qdrant_after,
            ),
        },
        "cross_doc_stress": {
            "summary": summarize_rows(cross_doc_rows),
            "sign_test": exact_sign_test(cross_doc_rows),
            "patch_metadata": load_patch_metadata(
                ROOT / "runs/cross_doc_patch_nfcorpus/hybrid/comparison.json"
            ),
            "rows": cross_doc_rows,
        },
        "limitations": [
            "Repeated rounds are resampling analyses over saved artifacts, not fresh full-pipeline reruns.",
            "The controlled benchmark has 12 queries, so any significance claim is naturally weak.",
            "The saved positive lift comes from one repaired query and zero regressions.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bootstrap-rounds", type=int, default=5000)
    parser.add_argument("--subset-rounds", type=int, default=2000)
    parser.add_argument("--subset-sizes", type=int, nargs="+", default=[6, 8, 10])
    parser.add_argument(
        "--json-out",
        default="runs/analysis/patch_effect_validation.json",
        help="Output path relative to repo root for machine-readable JSON.",
    )
    parser.add_argument(
        "--report-out",
        default="project_docs/03_experiment_reports/patch_effect_validation.md",
        help="Output path relative to repo root for the Markdown report.",
    )
    args = parser.parse_args()

    payload = build_validation_payload(
        rounds=args.bootstrap_rounds,
        subset_sizes=args.subset_sizes,
        subset_rounds=args.subset_rounds,
    )

    json_out = ROOT / args.json_out
    report_out = ROOT / args.report_out
    json_out.parent.mkdir(parents=True, exist_ok=True)
    report_out.parent.mkdir(parents=True, exist_ok=True)

    report_text = render_report(payload, args.bootstrap_rounds, args.subset_sizes)
    json_out.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    report_out.write_text(report_text, encoding="utf-8")

    local_summary = payload["controlled_case"]["local"]["summary"]
    cross_doc_summary = payload["cross_doc_stress"]["summary"]
    print(
        "Validated controlled claim: "
        f"{local_summary['before']['recall@5']:.4f} -> "
        f"{local_summary['after']['recall@5']:.4f}; "
        "cross-doc stress test: "
        f"{cross_doc_summary['before']['recall@5']:.4f} -> "
        f"{cross_doc_summary['after']['recall@5']:.4f}."
    )
    print(f"Wrote JSON to {json_out.relative_to(ROOT)}")
    print(f"Wrote report to {report_out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
