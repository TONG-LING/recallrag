#!/usr/bin/env python3
import json
from pathlib import Path


def load_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_result_map(path: str | Path):
    return {row["qid"]: row for row in load_json(path)}


def pct(num: int, den: int) -> float:
    return 100.0 * num / den if den else 0.0


def fmt_metric(value: float | None) -> str:
    return "n/a" if value is None else f"{value:.4f}"


def fmt_ratio(num: int, den: int) -> str:
    return f"{num}/{den} ({pct(num, den):.2f}%)" if den else f"{num}/0 (0.00%)"


def maybe_load_result_map(path: str | Path):
    path = Path(path)
    return load_result_map(path) if path.exists() else None


def maybe_load_json(path: str | Path):
    path = Path(path)
    return load_json(path) if path.exists() else None


DATASETS = [
    {
        "key": "controlled",
        "label": "Controlled chunk-failure case",
        "docs_glob": "case/docs/*.md",
        "chunks_path": "runs/base/chunks.json",
        "base_results": "runs/base/retrieval_results.json",
        "base_metrics": "runs/base/metrics.json",
        "bm25_hybrid_results": "runs/hybrid_bm25/hybrid_bm25_results.json",
        "bm25_hybrid_metrics": "runs/hybrid_bm25/hybrid_bm25_metrics.json",
        "patch_results": "runs/hybrid/retrieval_results.json",
        "patch_metrics": "runs/hybrid/metrics.json",
        "selected_patch_candidates": "runs/hybrid/selected_patch_candidates.json",
        "qdrant_main": "runs/qdrant_main/qdrant_retrieval_results.json",
        "qdrant_patch": "runs/qdrant/qdrant_retrieval_results.json",
        "qdrant_patch_metrics": "runs/qdrant/qdrant_metrics.json",
    },
    {
        "key": "scifact",
        "label": "BEIR SciFact scientific abstracts",
        "docs_glob": "case_beir/scifact/docs/*.md",
        "chunks_path": "runs/scifact_base/chunks.json",
        "base_results": "runs/scifact_base/retrieval_results.json",
        "base_metrics": "runs/scifact_base/metrics.json",
        "bm25_hybrid_results": "runs/scifact_hybrid_bm25/hybrid_bm25_results.json",
        "bm25_hybrid_metrics": "runs/scifact_hybrid_bm25/hybrid_bm25_metrics.json",
        "patch_results": "runs/scifact_hybrid/retrieval_results.json",
        "patch_metrics": "runs/scifact_hybrid/metrics.json",
        "selected_patch_candidates": "runs/scifact_hybrid/selected_patch_candidates.json",
        "qdrant_main": "runs/scifact_qdrant_main/qdrant_retrieval_results.json",
        "qdrant_patch": "runs/scifact_qdrant/qdrant_retrieval_results.json",
        "qdrant_patch_metrics": "runs/scifact_qdrant/qdrant_metrics.json",
    },
    {
        "key": "nfcorpus",
        "label": "BEIR NFCorpus medical/health texts",
        "docs_glob": "case_beir/nfcorpus/docs/*.md",
        "chunks_path": "runs/nfcorpus_base/chunks.json",
        "base_results": "runs/nfcorpus_base/retrieval_results.json",
        "base_metrics": "runs/nfcorpus_base/metrics.json",
        "bm25_hybrid_results": "runs/nfcorpus_hybrid_bm25/hybrid_bm25_results.json",
        "bm25_hybrid_metrics": "runs/nfcorpus_hybrid_bm25/hybrid_bm25_metrics.json",
        "patch_results": "runs/nfcorpus_hybrid/retrieval_results.json",
        "patch_metrics": "runs/nfcorpus_hybrid/metrics.json",
        "selected_patch_candidates": "runs/nfcorpus_hybrid/selected_patch_candidates.json",
        "qdrant_main": "runs/nfcorpus_qdrant_main/qdrant_retrieval_results.json",
        "qdrant_patch": "runs/nfcorpus_qdrant/qdrant_retrieval_results.json",
        "qdrant_patch_metrics": "runs/nfcorpus_qdrant/qdrant_metrics.json",
    },
]


def summarize_dataset(cfg: dict) -> dict:
    base_metrics = load_json(cfg["base_metrics"])
    bm25_hybrid_results = load_json(cfg["bm25_hybrid_results"])
    bm25_hybrid_metrics = load_json(cfg["bm25_hybrid_metrics"])
    patch_metrics = maybe_load_json(cfg["patch_metrics"])
    qdrant_patch_metrics = maybe_load_json(cfg["qdrant_patch_metrics"])

    base = load_result_map(cfg["base_results"])
    bm25 = {row["qid"]: row for row in bm25_hybrid_results["bm25"]}
    dense_bm25 = {row["qid"]: row for row in bm25_hybrid_results["dense_bm25"]}
    patch = maybe_load_result_map(cfg["patch_results"])
    qdrant_main = maybe_load_result_map(cfg["qdrant_main"])
    qdrant_patch = maybe_load_result_map(cfg["qdrant_patch"])

    qids = sorted(base)
    dense_failures = [qid for qid in qids if not base[qid]["success"]]
    fixed_by_bm25 = [qid for qid in qids if (not base[qid]["success"]) and bm25[qid]["success"]]
    fixed_by_dense_bm25 = [qid for qid in qids if (not base[qid]["success"]) and dense_bm25[qid]["success"]]
    fixed_by_patch = []
    patch_only = []
    patch_but_strategy_sensitive = []
    qdrant_fixed_by_patch = []

    if patch:
        for qid in qids:
            if (not base[qid]["success"]) and patch[qid]["success"]:
                fixed_by_patch.append(qid)
                if (not bm25[qid]["success"]) and (not dense_bm25[qid]["success"]):
                    patch_only.append(qid)
                else:
                    patch_but_strategy_sensitive.append(qid)

    if qdrant_main and qdrant_patch:
        for qid in qids:
            if (not qdrant_main[qid]["success"]) and qdrant_patch[qid]["success"]:
                qdrant_fixed_by_patch.append(qid)

    selected_patch_candidates = maybe_load_json(cfg["selected_patch_candidates"]) or []

    return {
        "key": cfg["key"],
        "label": cfg["label"],
        "docs": len(list(Path().glob(cfg["docs_glob"]))),
        "chunks": len(load_json(cfg["chunks_path"])),
        "queries": base_metrics["total"],
        "dense_recall": base_metrics["recall@5"],
        "bm25_recall": bm25_hybrid_metrics["bm25"]["recall@5"],
        "dense_bm25_recall": bm25_hybrid_metrics["dense_bm25"]["recall@5"],
        "patch_recall": patch_metrics["recall@5"] if patch_metrics else None,
        "qdrant_patch_recall": qdrant_patch_metrics["recall@5"] if qdrant_patch_metrics else None,
        "dense_failures": len(dense_failures),
        "selected_patches": len(selected_patch_candidates),
        "fixed_by_bm25": fixed_by_bm25,
        "fixed_by_dense_bm25": fixed_by_dense_bm25,
        "fixed_by_patch": fixed_by_patch,
        "patch_only": patch_only,
        "patch_but_strategy_sensitive": patch_but_strategy_sensitive,
        "qdrant_fixed_by_patch": qdrant_fixed_by_patch,
    }


def render_table(rows: list[dict]) -> str:
    header = [
        "| dataset | docs | chunks | queries | dense R@5 | BM25 R@5 | dense+BM25 R@5 | main+patch R@5 | Qdrant main+patch R@5 | dense failures | selected patches | patch fixed | patch-only vs BM25+dense+BM25 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    body = []
    for row in rows:
        body.append(
            "| {label} | {docs} | {chunks} | {queries} | {dense} | {bm25} | {dense_bm25} | {patch} | {qdrant_patch} | {dense_failures} | {selected_patches} | {fixed_by_patch} | {patch_only} |".format(
                label=row["label"],
                docs=row["docs"],
                chunks=row["chunks"],
                queries=row["queries"],
                dense=fmt_metric(row["dense_recall"]),
                bm25=fmt_metric(row["bm25_recall"]),
                dense_bm25=fmt_metric(row["dense_bm25_recall"]),
                patch=fmt_metric(row["patch_recall"]),
                qdrant_patch=fmt_metric(row["qdrant_patch_recall"]),
                dense_failures=row["dense_failures"],
                selected_patches=row["selected_patches"],
                fixed_by_patch=len(row["fixed_by_patch"]),
                patch_only=fmt_ratio(len(row["patch_only"]), row["queries"]),
            )
        )
    return "\n".join(header + body)


def render_detail(row: dict) -> str:
    return "\n".join(
        [
            f"### {row['label']}",
            "",
            f"- dense failures: {row['dense_failures']}",
            f"- selected patches: {row['selected_patches']}",
            f"- fixed by patch: {len(row['fixed_by_patch'])} -> {row['fixed_by_patch'] or '[]'}",
            f"- fixed by BM25: {len(row['fixed_by_bm25'])} -> {row['fixed_by_bm25'] or '[]'}",
            f"- fixed by dense+BM25: {len(row['fixed_by_dense_bm25'])} -> {row['fixed_by_dense_bm25'] or '[]'}",
            f"- patch fixed but BM25/dense+BM25 already fixed too: {len(row['patch_but_strategy_sensitive'])} -> {row['patch_but_strategy_sensitive'] or '[]'}",
            f"- patch-only vs BM25+dense+BM25: {fmt_ratio(len(row['patch_only']), row['queries'])}",
            f"- patch-only inside dense failures: {fmt_ratio(len(row['patch_only']), row['dense_failures'])}",
            f"- Qdrant fixed by patch: {len(row['qdrant_fixed_by_patch'])} -> {row['qdrant_fixed_by_patch'] or '[]'}",
            "",
        ]
    )


rows = [summarize_dataset(cfg) for cfg in DATASETS]
beir_rows = [row for row in rows if row["key"] in {"scifact", "nfcorpus"}]
beir_queries = sum(row["queries"] for row in beir_rows)
beir_dense_failures = sum(row["dense_failures"] for row in beir_rows)
beir_patch_only = sum(len(row["patch_only"]) for row in beir_rows)
beir_patch_fixed = sum(len(row["fixed_by_patch"]) for row in beir_rows)

text = f"""# Generalization Report: Controlled Case + BEIR Datasets

This report re-audits RecallRAG on the controlled chunk-failure case and on two additional BEIR-style datasets with the current exact-token evaluation logic.

## Aggregate table

{render_table(rows)}

## Key readout

- Controlled case still shows the mechanism works on a clean chunk-boundary failure:
  - patch-only vs BM25+dense+BM25 = {fmt_ratio(len(rows[0]['patch_only']), rows[0]['queries'])}
  - patch-only inside dense failures = {fmt_ratio(len(rows[0]['patch_only']), rows[0]['dense_failures'])}
- Across the two extra BEIR reruns ({beir_queries} queries total):
  - fixed by patch = {beir_patch_fixed}
  - patch-only vs BM25+dense+BM25 = {fmt_ratio(beir_patch_only, beir_queries)}
  - patch-only inside dense failures = {fmt_ratio(beir_patch_only, beir_dense_failures)}

This means the current Patch Index is not a general recall booster. Its unique gain remains concentrated in the controlled near-miss chunk-failure case. On broader BEIR-style data, BM25/hybrid explains more of the recoverable failures.

## Per-dataset detail

{render_detail(rows[0])}
{render_detail(rows[1])}
{render_detail(rows[2])}

## Interview-safe conclusion

1. The controlled benchmark still supports the core claim: when top-N already contains the right local area but fixed chunking split the evidence, a failure-driven side Patch Index can repair that case without rebuilding the whole main index.
2. The extra BEIR reruns make the boundary clearer:
   - SciFact: patch improved recall a little, but the repaired query was also fixed by BM25 and dense+BM25, so it is retrieval-strategy-sensitive rather than patch-unique.
   - NFCorpus: patch selected nothing and recall stayed flat, which is consistent with domain mismatch / ranking difficulty rather than local chunk-boundary repair.
3. The honest summary is therefore:
   - controlled mechanism proof: yes
   - broader unique patch gain on these BEIR reruns: limited to none
   - hybrid retrieval remains a required baseline before claiming chunk repair helped
"""

out = Path("project_docs/03_experiment_reports/generalization_report.md")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(text, encoding="utf-8")
print(text)
