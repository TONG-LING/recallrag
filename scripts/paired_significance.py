#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import random
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Paired significance analysis for before/after retrieval results."
    )
    parser.add_argument("--before", required=True, help="Before retrieval_results.json")
    parser.add_argument("--after", required=True, help="After retrieval_results.json")
    parser.add_argument(
        "--out-json",
        default=None,
        help="Optional JSON output path. Defaults to <after>.paired_significance.json",
    )
    parser.add_argument(
        "--out-md",
        default=None,
        help="Optional Markdown output path. Defaults to <after>.paired_significance.md",
    )
    parser.add_argument(
        "--bootstrap-samples",
        type=int,
        default=10000,
        help="Bootstrap sample count for delta confidence intervals",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed",
    )
    return parser.parse_args()


def _load_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _write_json(path: str | Path, obj) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def _reciprocal_rank(row: dict) -> float:
    rank = row.get("rank")
    return 1.0 / rank if rank else 0.0


def _success(row: dict) -> int:
    return int(bool(row.get("success")))


def _exact_mcnemar_pvalue(wins: int, losses: int) -> float:
    discordant = wins + losses
    if discordant == 0:
        return 1.0
    tail = sum(math.comb(discordant, i) for i in range(0, min(wins, losses) + 1)) / (2 ** discordant)
    return min(1.0, 2.0 * tail)


def _bootstrap_ci(values: list[float], samples: int, seed: int) -> tuple[float, float]:
    if not values:
        return 0.0, 0.0
    rng = random.Random(seed)
    means = []
    n = len(values)
    for _ in range(samples):
        sample = [values[rng.randrange(n)] for _ in range(n)]
        means.append(sum(sample) / n)
    means.sort()
    low_idx = max(0, int(0.025 * samples) - 1)
    high_idx = min(samples - 1, int(0.975 * samples) - 1)
    return means[low_idx], means[high_idx]


def main() -> None:
    args = parse_args()
    before_rows = {row["qid"]: row for row in _load_json(args.before)}
    after_rows = {row["qid"]: row for row in _load_json(args.after)}
    qids = sorted(set(before_rows) & set(after_rows))
    if not qids:
        raise RuntimeError("No overlapping qids between before and after results.")

    per_query = []
    recall_deltas = []
    mrr_deltas = []
    wins = 0
    losses = 0
    before_hits = 0
    after_hits = 0

    for qid in qids:
        before = before_rows[qid]
        after = after_rows[qid]
        before_success = _success(before)
        after_success = _success(after)
        before_rr = _reciprocal_rank(before)
        after_rr = _reciprocal_rank(after)
        before_hits += before_success
        after_hits += after_success
        if (not before_success) and after_success:
            wins += 1
        elif before_success and (not after_success):
            losses += 1
        recall_delta = after_success - before_success
        mrr_delta = after_rr - before_rr
        recall_deltas.append(float(recall_delta))
        mrr_deltas.append(float(mrr_delta))
        per_query.append(
            {
                "qid": qid,
                "before_success": bool(before_success),
                "after_success": bool(after_success),
                "before_rank": before.get("rank"),
                "after_rank": after.get("rank"),
                "before_rr": round(before_rr, 6),
                "after_rr": round(after_rr, 6),
                "recall_delta": recall_delta,
                "mrr_delta": round(mrr_delta, 6),
            }
        )

    n = len(qids)
    recall_delta_mean = sum(recall_deltas) / n
    mrr_delta_mean = sum(mrr_deltas) / n
    recall_ci = _bootstrap_ci(recall_deltas, args.bootstrap_samples, args.seed)
    mrr_ci = _bootstrap_ci(mrr_deltas, args.bootstrap_samples, args.seed + 1)

    payload = {
        "n": n,
        "before_hits": before_hits,
        "after_hits": after_hits,
        "wins": wins,
        "losses": losses,
        "ties": n - wins - losses,
        "before_recall": before_hits / n,
        "after_recall": after_hits / n,
        "recall_delta": recall_delta_mean,
        "recall_delta_bootstrap_ci95": [recall_ci[0], recall_ci[1]],
        "mrr_delta": mrr_delta_mean,
        "mrr_delta_bootstrap_ci95": [mrr_ci[0], mrr_ci[1]],
        "exact_mcnemar_pvalue": _exact_mcnemar_pvalue(wins, losses),
        "per_query": per_query,
    }

    out_json = Path(args.out_json) if args.out_json else Path(args.after).with_suffix(".paired_significance.json")
    out_md = Path(args.out_md) if args.out_md else Path(args.after).with_suffix(".paired_significance.md")
    _write_json(out_json, payload)

    lines = [
        "# Paired Significance Report",
        "",
        "## Summary",
        "",
        f"- n: `{payload['n']}`",
        f"- before hits: `{before_hits}`",
        f"- after hits: `{after_hits}`",
        f"- wins (0->1): `{wins}`",
        f"- losses (1->0): `{losses}`",
        f"- ties: `{payload['ties']}`",
        f"- recall delta: `{payload['recall_delta']:.4f}`",
        f"- recall 95% bootstrap CI: `[{payload['recall_delta_bootstrap_ci95'][0]:.4f}, {payload['recall_delta_bootstrap_ci95'][1]:.4f}]`",
        f"- MRR delta: `{payload['mrr_delta']:.4f}`",
        f"- MRR 95% bootstrap CI: `[{payload['mrr_delta_bootstrap_ci95'][0]:.4f}, {payload['mrr_delta_bootstrap_ci95'][1]:.4f}]`",
        f"- exact McNemar p-value: `{payload['exact_mcnemar_pvalue']:.6f}`",
        "",
        "## Interpretation",
        "",
        "- `wins` 看的是原来失败、后来成功的 query 数。",
        "- `losses` 看的是原来成功、后来失败的 query 数。",
        "- McNemar 只针对 paired 二分类成功/失败，不是看小数漂不漂亮。",
        "- bootstrap CI 更适合解释增益区间，不代表严格因果证明。",
        "",
        "## Per Query",
        "",
        "| qid | before_success | after_success | before_rank | after_rank | mrr_delta |",
        "|---|---|---|---:|---:|---:|",
    ]
    for row in per_query:
        lines.append(
            f"| {row['qid']} | {row['before_success']} | {row['after_success']} | {row['before_rank']} | {row['after_rank']} | {row['mrr_delta']:.6f} |"
        )
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    print(f"wrote paired significance -> {out_md}")


if __name__ == "__main__":
    main()
