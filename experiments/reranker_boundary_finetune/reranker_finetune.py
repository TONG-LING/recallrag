#!/usr/bin/env python3
from __future__ import annotations

import argparse
import random
from pathlib import Path

from reranker_common import (
    configure_hf_endpoint,
    export_cross_encoder,
    is_loadable_dir,
    load_json,
    load_jsonl,
    make_cross_encoder,
    resolve_cross_encoder_path,
    resolve_device,
    write_json,
)

SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_MODEL = "BAAI/bge-reranker-base"
DEFAULT_PAIRS = str(SCRIPT_DIR / "data" / "pairs.jsonl")


def cmd_train(args: argparse.Namespace) -> None:
    from sentence_transformers import InputExample
    from torch.utils.data import DataLoader

    random.seed(args.seed)
    rows = load_jsonl(args.pairs)
    train_examples = [
        InputExample(texts=[row["query"], row["text"]], label=float(row["label"]))
        for row in rows
        if row.get("split") == "train"
    ]
    if not train_examples:
        raise RuntimeError("No train examples found in pairs file.")

    device = resolve_device(args.device)
    dev_count = sum(1 for row in rows if row.get("split") == "dev")
    model = make_cross_encoder(
        args.model_name_or_path,
        args.max_length,
        args.trust_remote_code,
        num_labels=1,
        device=device,
    )
    train_loader = DataLoader(train_examples, shuffle=True, batch_size=args.batch_size)
    warmup_steps = int(len(train_loader) * args.epochs * args.warmup_ratio)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    write_json(
        out_dir / "train_config.json",
        {
            "pairs": str(Path(args.pairs).resolve()),
            "model_name_or_path": args.model_name_or_path,
            "device": device,
            "epochs": args.epochs,
            "batch_size": args.batch_size,
            "lr": args.lr,
            "max_length": args.max_length,
            "warmup_steps": warmup_steps,
            "train_examples": len(train_examples),
            "dev_examples": dev_count,
        },
    )

    model.fit(
        train_dataloader=train_loader,
        epochs=args.epochs,
        warmup_steps=warmup_steps,
        optimizer_params={"lr": args.lr},
        output_path=args.output_dir,
        show_progress_bar=True,
        use_amp=args.fp16,
    )

    export_dir = export_cross_encoder(model, out_dir)
    if not is_loadable_dir(export_dir):
        raise RuntimeError(f"Training finished but export is not loadable: {export_dir}")
    print(f"saved fine-tuned reranker -> {export_dir}")


def fmt(value) -> str:
    return f"{value:.6f}" if isinstance(value, float) else str(value)


def cmd_compare(args: argparse.Namespace) -> None:
    before = load_json(args.before)
    after = load_json(args.after)
    keys = [
        "total",
        "dense_recall@5",
        "recall@5",
        "dense_mrr",
        "mrr",
        "mrr_delta",
        "rerank_fixed",
        "rerank_regressed",
        "rerank_improved",
        "candidate_missing_positive",
    ]
    lines = ["# Reranker Fine-tune Comparison", "", "| metric | before | after | delta |", "|---|---:|---:|---:|"]
    for key in keys:
        b, a = before.get(key), after.get(key)
        delta = a - b if isinstance(a, (int, float)) and isinstance(b, (int, float)) else ""
        lines.append(f"| {key} | {fmt(b)} | {fmt(a)} | {fmt(delta)} |")
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote compare report -> {out}")


def cmd_export(args: argparse.Namespace) -> None:
    source = resolve_cross_encoder_path(args.source)
    model = make_cross_encoder(source, args.max_length, args.trust_remote_code, num_labels=1, device=args.device)
    export_dir = export_cross_encoder(model, args.out)
    print(f"exported loadable reranker -> {export_dir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(required=True)

    train = sub.add_parser("train")
    train.add_argument("--pairs", default=DEFAULT_PAIRS)
    train.add_argument("--model-name-or-path", default=DEFAULT_MODEL)
    train.add_argument("--output-dir", default=str(SCRIPT_DIR / "outputs" / "bge_reranker_evidence"))
    train.add_argument("--device", default=None)
    train.add_argument("--epochs", type=int, default=2)
    train.add_argument("--batch-size", type=int, default=8)
    train.add_argument("--lr", type=float, default=2e-5)
    train.add_argument("--max-length", type=int, default=512)
    train.add_argument("--warmup-ratio", type=float, default=0.1)
    train.add_argument("--fp16", action="store_true")
    train.add_argument("--trust-remote-code", action="store_true")
    train.add_argument("--hf-endpoint", default=None)
    train.add_argument("--no-hf-mirror", action="store_true")
    train.add_argument("--seed", type=int, default=42)
    train.set_defaults(func=cmd_train)

    cmp_parser = sub.add_parser("compare")
    cmp_parser.add_argument("--before", default=str(SCRIPT_DIR / "outputs" / "eval_base_test" / "metrics.json"))
    cmp_parser.add_argument("--after", default=str(SCRIPT_DIR / "outputs" / "eval_finetuned_test" / "metrics.json"))
    cmp_parser.add_argument("--out", default=str(SCRIPT_DIR / "outputs" / "compare_report.md"))
    cmp_parser.set_defaults(func=cmd_compare)

    export_parser = sub.add_parser("export")
    export_parser.add_argument("--source", default=str(SCRIPT_DIR / "outputs" / "bge_reranker_evidence"))
    export_parser.add_argument("--out", default=str(SCRIPT_DIR / "outputs" / "bge_reranker_evidence"))
    export_parser.add_argument("--device", default=None)
    export_parser.add_argument("--max-length", type=int, default=512)
    export_parser.add_argument("--trust-remote-code", action="store_true")
    export_parser.set_defaults(func=cmd_export)

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    endpoint = configure_hf_endpoint(
        getattr(args, "hf_endpoint", None),
        use_mirror=not getattr(args, "no_hf_mirror", False),
    )
    if getattr(args, "hf_endpoint", None) is not None or getattr(args, "no_hf_mirror", False):
        print(f"==> HF_ENDPOINT={endpoint}")
    args.func(args)


if __name__ == "__main__":
    main()
