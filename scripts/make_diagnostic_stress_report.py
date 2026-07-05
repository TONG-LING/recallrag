#!/usr/bin/env python3
"""Legacy helper for the old chunk/overlap sweep report.

This script only works with archived `runs/sweeps/c*_o*` outputs. The current
repo no longer keeps those sweep runs by default, and the current
interview/demo flow does not depend on this report.
"""

from __future__ import annotations
import json, glob, re
from pathlib import Path

def load(p):
    return json.loads(Path(p).read_text(encoding='utf-8'))

def cfg_name(d: str):
    m = re.search(r'c(\d+)_o(\d+)$', d)
    return (int(m.group(1)), int(m.group(2))) if m else (9999,9999)

def main():
    sweep_dirs = sorted(glob.glob('runs/sweeps/c*_o*'), key=cfg_name)
    if not sweep_dirs:
        raise SystemExit(
            'No runs/sweeps/c*_o* directories found. '
            'This is a legacy helper for archived sweep outputs only.'
        )
    rows=[]
    for d in sweep_dirs:
        p=Path(d)
        if not (p/'metrics.json').exists() or not (p/'triage/final_triage.json').exists():
            continue
        m=load(p/'metrics.json')
        hm=load(p/'hybrid/metrics.json')
        bm=load(p/'bm25/hybrid_bm25_metrics.json')
        tri=load(p/'triage/final_triage.json')
        rows.append({
            'run': p.name,
            'chunk_size': cfg_name(d)[0],
            'overlap': cfg_name(d)[1],
            'base_recall': m['recall@5'],
            'patch_recall': hm['recall@5'],
            'bm25_recall': bm['bm25']['recall@5'],
            'hybrid_recall': bm['dense_bm25']['recall@5'],
            'base_mrr': m['mrr'],
            'patch_mrr': hm['mrr'],
            'failures': tri['total_dense_failures'],
            'accepted_patch': tri['accepted_patch_candidates'],
            'retrieval_strategy': tri['retrieval_strategy_sensitive'],
            'manual_review': tri['manual_review'],
            'decisions': [(r['qid'], r['final_family'], r['final_decision']) for r in tri['rows']],
        })
    if not rows:
        raise SystemExit(
            'Sweep directories were found, but no complete sweep outputs were available. '
            'Legacy stress report was not generated.'
        )
    out=Path('project_docs/03_experiment_reports/diagnostic_stress_test.md')
    out.parent.mkdir(parents=True, exist_ok=True)
    lines=['# Legacy Diagnostic Stress Test: Can RecallRAG avoid blaming every failure on chunking?', '']
    lines += [
        '> Historical report. This is not part of the current interview/demo primary readout.', '',
        '## Purpose', '',
        '这个实验专门回答两个问题：', '',
        '1. **提升是不是太小？** 在不同 chunk size / overlap 下，Patch Index 的上限和收益是否稳定。',
        '2. **诊断是否可靠？** 如果 BM25 / dense+BM25 能修复失败，系统必须把它降级为 `retrieval_strategy_sensitive`，而不是硬说成 chunk 问题。', '',
        '诊断逻辑采用“两阶段”：raw diagnosis 只给候选原因；final triage 必须结合 patch validation 与 BM25/hybrid 对照实验，才允许接受 chunk patch。', '',
        '## Sweep Results', '',
        '| run | base R@5 | main+patch R@5 | BM25 R@5 | dense+BM25 R@5 | accepted patch | retrieval-strategy | manual |',
        '|---|---:|---:|---:|---:|---:|---:|---:|'
    ]
    for r in rows:
        lines.append(f"| {r['run']} | {r['base_recall']:.4f} | {r['patch_recall']:.4f} | {r['bm25_recall']:.4f} | {r['hybrid_recall']:.4f} | {r['accepted_patch']} | {r['retrieval_strategy']} | {r['manual_review']} |")
    if rows:
        avg_base=sum(r['base_recall'] for r in rows)/len(rows)
        avg_patch=sum(r['patch_recall'] for r in rows)/len(rows)
        avg_hybrid=sum(r['hybrid_recall'] for r in rows)/len(rows)
        max_gain=max(r['patch_recall']-r['base_recall'] for r in rows)
        total_fail=sum(r['failures'] for r in rows)
        total_patch=sum(r['accepted_patch'] for r in rows)
        total_retr=sum(r['retrieval_strategy'] for r in rows)
        lines += ['', '## Aggregate Findings', '']
        lines += [
            f'- runs: `{len(rows)}`',
            f'- average base Recall@5: `{avg_base:.4f}`',
            f'- average main+patch Recall@5: `{avg_patch:.4f}` (`+{avg_patch-avg_base:.4f}`)',
            f'- average dense+BM25 Recall@5: `{avg_hybrid:.4f}` (`+{avg_hybrid-avg_base:.4f}`)',
            f'- max patch gain in one setting: `+{max_gain:.4f}`',
            f'- total dense failures inspected: `{total_fail}`',
            f'- accepted patch candidates after final triage: `{total_patch}`',
            f'- downgraded to retrieval_strategy_sensitive: `{total_retr}`',
            '',
            '结论：Patch 不是万能优化器；它主要解决“局部上下文/切片导致证据没有被有效表达”的失败。只要 BM25 或 dense+BM25 能解释失败，final triage 会降级，避免胡乱 re-chunk。',
        ]
    lines += ['', '## Per-run Final Decisions', '']
    for r in rows:
        lines += [f"### {r['run']}", '']
        for qid, fam, dec in r['decisions']:
            lines.append(f'- `{qid}` -> `{fam}` / `{dec}`')
        lines.append('')
    lines += [
        '## What was optimized after the first version?', '',
        '- 增加 `first_gold_rank`、`best_evidence_rank`、`best_evidence_chunk_id`，避免只看“是否命中同一文档”的粗糙信号。',
        '- raw diagnosis 不再直接把所有同文档错块都叫 `boundary_split`，而是标成更保守的 `local_context_missing` / `chunking_failure_candidate`。',
        '- Patch materialization 现在用 best-evidence chunk 作为 section lineage anchor，避免 adjacent window 起点落在上一节导致 patch 元数据错误。',
        '- final triage 引入 BM25 / dense+BM25 对照：能被检索策略修复的样本，不接受为 clean chunk patch。', '',
        '## Interview-safe claim', '',
        '> 我不是说所有 recall failure 都是 chunk 问题。RecallRAG 先产生 chunk patch 候选，再用 Patch Index 和 BM25/hybrid 做反事实验证。只有 patch 能修、且 BM25/hybrid 不能解释的样本，才会被接受为 chunking failure；否则标记为 retrieval_strategy_sensitive 或 manual_review。',
    ]
    out.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'wrote legacy report to {out}')

if __name__ == '__main__':
    main()
