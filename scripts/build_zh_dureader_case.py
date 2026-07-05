#!/usr/bin/env python3
from __future__ import annotations

import argparse
import gzip
import json
import random
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from recallrag.text_utils import mixed_token_set, normalize_text

SOURCE_URL = (
    "https://huggingface.co/datasets/zyznull/dureader-retrieval-ranking/resolve/main/dev.jsonl.gz"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a Chinese long-document RecallRAG case from DuReader Retrieval dev data."
    )
    parser.add_argument(
        "--source-gz",
        default="datasets/zh_dureader/dev.jsonl.gz",
        help="Local path to the downloaded DuReader Retrieval dev jsonl.gz",
    )
    parser.add_argument(
        "--out",
        default="case_zh_dureader",
        help="Output case directory",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=18,
        help="Number of query/doc pairs to build",
    )
    parser.add_argument(
        "--negatives-per-doc",
        type=int,
        default=4,
        help="How many negative passages to mix into each long document",
    )
    parser.add_argument(
        "--min-positive-len",
        type=int,
        default=380,
        help="Minimum positive passage length after cleanup",
    )
    parser.add_argument(
        "--max-positive-len",
        type=int,
        default=1400,
        help="Maximum positive passage length after cleanup",
    )
    parser.add_argument(
        "--min-negative-len",
        type=int,
        default=140,
        help="Minimum negative passage length after cleanup",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducible sampling",
    )
    return parser.parse_args()


def ensure_source(path: Path) -> None:
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    print(f"downloading {SOURCE_URL} -> {path}")
    with urllib.request.urlopen(SOURCE_URL, timeout=300) as response:
        path.write_bytes(response.read())


def clean_text(text: str) -> str:
    text = (text or "").replace("\r", "\n")
    text = re.sub(r"[\u0000-\u001f\u007f]", " ", text)
    text = re.sub(r"[\ue000-\uf8ff]", " ", text)
    text = normalize_text(text)
    return text.strip()


def query_overlap(query: str, passage: str) -> float:
    query_tokens = mixed_token_set(query, drop_stopwords=True, min_ascii_len=2)
    if not query_tokens:
        return 0.0
    passage_tokens = mixed_token_set(passage, drop_stopwords=True, min_ascii_len=2)
    return len(query_tokens & passage_tokens) / len(query_tokens)


def choose_negative_passages(
    query: str,
    passages: list[dict],
    negatives_per_doc: int,
    min_negative_len: int,
) -> list[dict]:
    ranked: list[tuple[float, int, dict]] = []
    seen_docids: set[str] = set()
    for row in passages:
        docid = row.get("docid", "")
        text = clean_text(row.get("text", ""))
        if not text or len(text) < min_negative_len or docid in seen_docids:
            continue
        seen_docids.add(docid)
        overlap = query_overlap(query, text)
        ranked.append((overlap, len(text), {"docid": docid, "text": text}))
    ranked.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return [row for _, _, row in ranked[:negatives_per_doc]]


def build_doc_text(negatives: list[dict], positive_text: str) -> str:
    before = negatives[:2]
    after = negatives[2:]
    sections = ["# 中文复杂检索文档", ""]
    for idx, row in enumerate(before, 1):
        sections += [f"## 背景材料{idx}", row["text"], ""]
    sections += ["## 关键材料", positive_text, ""]
    for idx, row in enumerate(after, 1):
        sections += [f"## 补充材料{idx}", row["text"], ""]
    return "\n".join(sections).strip() + "\n"


def build_question_row(qid: str, query: str, doc_name: str, gold_span: str, source_row: dict) -> dict:
    return {
        "qid": qid,
        "question": query,
        "gold_doc": doc_name,
        "gold_section": "关键材料",
        "gold_failure_type": "zh_long_span_boundary_candidate",
        "gold_span": gold_span,
        "source_dataset": "zyznull/dureader-retrieval-ranking",
        "source_query_id": str(source_row["query_id"]),
        "source_positive_docids": [row.get("docid", "") for row in source_row["positive_passages"]],
    }


def collect_candidates(args: argparse.Namespace, source_path: Path) -> list[dict]:
    candidates: list[dict] = []
    with gzip.open(source_path, "rt", encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            query = clean_text(row.get("query", ""))
            positives = []
            for passage in row.get("positive_passages", []):
                text = clean_text(passage.get("text", ""))
                if not text:
                    continue
                positives.append({"docid": passage.get("docid", ""), "text": text})
            if not query or not positives:
                continue
            positive = max(positives, key=lambda item: len(item["text"]))
            positive_len = len(positive["text"])
            if positive_len < args.min_positive_len or positive_len > args.max_positive_len:
                continue
            negatives = choose_negative_passages(
                query,
                row.get("negative_passages", []),
                args.negatives_per_doc,
                args.min_negative_len,
            )
            if len(negatives) < args.negatives_per_doc:
                continue
            candidates.append(
                {
                    "query_id": str(row["query_id"]),
                    "query": query,
                    "positive_docid": positive["docid"],
                    "positive_text": positive["text"],
                    "positive_len": positive_len,
                    "negatives": negatives,
                    "source_row": row,
                }
            )
    return candidates


def build_case(args: argparse.Namespace) -> None:
    source_path = Path(args.source_gz)
    out_dir = Path(args.out)
    docs_dir = out_dir / "docs"
    eval_dir = out_dir / "eval"
    ensure_source(source_path)

    candidates = collect_candidates(args, source_path)
    if len(candidates) < args.sample_size:
        raise RuntimeError(
            f"Only found {len(candidates)} eligible candidates, less than requested sample_size={args.sample_size}"
        )

    rng = random.Random(args.seed)
    rng.shuffle(candidates)
    selected = sorted(
        candidates[: args.sample_size],
        key=lambda item: (item["positive_len"], item["query_id"]),
        reverse=True,
    )

    docs_dir.mkdir(parents=True, exist_ok=True)
    eval_dir.mkdir(parents=True, exist_ok=True)
    questions_path = eval_dir / "questions.jsonl"
    metadata_path = out_dir / "source_metadata.json"
    readme_path = out_dir / "README.md"

    question_rows: list[dict] = []
    metadata_rows: list[dict] = []
    for idx, item in enumerate(selected, 1):
        doc_name = f"zh_doc_{idx:03d}.md"
        qid = f"zh{idx:03d}"
        doc_text = build_doc_text(item["negatives"], item["positive_text"])
        (docs_dir / doc_name).write_text(doc_text, encoding="utf-8")
        question_rows.append(
            build_question_row(
                qid=qid,
                query=item["query"],
                doc_name=doc_name,
                gold_span=item["positive_text"],
                source_row=item["source_row"],
            )
        )
        metadata_rows.append(
            {
                "qid": qid,
                "doc_name": doc_name,
                "source_query_id": item["query_id"],
                "query": item["query"],
                "positive_docid": item["positive_docid"],
                "positive_len": item["positive_len"],
                "negative_docids": [row["docid"] for row in item["negatives"]],
                "negative_lens": [len(row["text"]) for row in item["negatives"]],
            }
        )

    questions_path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in question_rows) + "\n",
        encoding="utf-8",
    )
    metadata_path.write_text(
        json.dumps(
            {
                "source_url": SOURCE_URL,
                "sample_size": args.sample_size,
                "negatives_per_doc": args.negatives_per_doc,
                "min_positive_len": args.min_positive_len,
                "max_positive_len": args.max_positive_len,
                "min_negative_len": args.min_negative_len,
                "seed": args.seed,
                "rows": metadata_rows,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    readme_path.write_text(
        "\n".join(
            [
                "# 中文 DuReader 长文档评测集",
                "",
                "这套 case 不是原始 DuReader 评测格式，而是从公开的 `DuReader Retrieval` dev 数据派生出来的长文档版本，专门用于测试 RecallRAG 的 chunk / patch 逻辑。",
                "",
                "构造方式：",
                f"- 来源：`{SOURCE_URL}`",
                f"- 样本数：`{args.sample_size}`",
                f"- 每个文档混入的负样本段数：`{args.negatives_per_doc}`",
                f"- 正样本长度范围：`[{args.min_positive_len}, {args.max_positive_len}]`",
                "",
                "目录：",
                "- `docs/`：长文档 markdown",
                "- `eval/questions.jsonl`：中文查询与 gold span",
                "- `source_metadata.json`：来源映射，方便审计",
                "",
                "说明：",
                "- `gold_span` 对应原始正样本文段。",
                "- 文档中加入了同 query 的负样本文段，目的是构造更接近 RAG 长文档检索的干扰环境。",
                "- 这是一套面向 RecallRAG 的中文复杂文档测试集，不等同于原始 benchmark leaderboard 用法。",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"built {len(question_rows)} questions -> {questions_path}")
    print(f"wrote docs -> {docs_dir}")
    print(f"wrote metadata -> {metadata_path}")


def main() -> None:
    args = parse_args()
    build_case(args)


if __name__ == "__main__":
    main()
