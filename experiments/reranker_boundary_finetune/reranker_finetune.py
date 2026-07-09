#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
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


class LossHistoryCallback:
    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)
        self.records: list[dict] = []
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text("", encoding="utf-8")

    def on_log(self, args, state, control, logs=None, **kwargs) -> None:
        if not logs or "loss" not in logs:
            return
        record = {
            "step": int(state.global_step),
            "epoch": None if state.epoch is None else float(state.epoch),
            "loss": float(logs["loss"]),
        }
        if logs.get("learning_rate") is not None:
            record["learning_rate"] = float(logs["learning_rate"])
        self.records.append(record)
        with self.path.open("a", encoding="utf-8") as fout:
            fout.write(json.dumps(record, ensure_ascii=False) + "\n")


def write_loss_curve(records: list[dict], path: str | Path) -> None:
    if not records:
        raise RuntimeError("No training loss records were captured; loss curve cannot be generated.")

    import matplotlib

    matplotlib.use("Agg")
    from matplotlib import pyplot as plt

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    steps = [row["step"] for row in records]
    losses = [row["loss"] for row in records]

    plt.figure(figsize=(7, 4))
    plt.plot(steps, losses, linewidth=1.5, marker="o", markersize=2.5)
    plt.title("Training Loss Curve")
    plt.xlabel("Global step")
    plt.ylabel("Loss")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(path, dpi=200)
    plt.close()


def build_train_dataset(rows: list[dict]):
    from datasets import Dataset

    train_rows = [
        {
            "sentence_0": row["query"],
            "sentence_1": row["text"],
            "label": float(row["label"]),
        }
        for row in rows
        if row.get("split") == "train"
    ]
    if not train_rows:
        raise RuntimeError("No train examples found in pairs file.")
    return Dataset.from_list(train_rows)


def cmd_train(args: argparse.Namespace) -> None:
    import torch
    import transformers
    from packaging import version
    from sentence_transformers.cross_encoder.losses.binary_cross_entropy import BinaryCrossEntropyLoss
    from sentence_transformers.cross_encoder.losses.cross_entropy import CrossEntropyLoss
    from sentence_transformers.cross_encoder.trainer import CrossEncoderTrainer
    from sentence_transformers.cross_encoder.training_args import CrossEncoderTrainingArguments
    from sentence_transformers.sentence_transformer.model import SentenceTransformer
    from transformers import TrainerCallback

    class _LossHistoryCallback(TrainerCallback, LossHistoryCallback):
        def __init__(self, path: str | Path) -> None:
            LossHistoryCallback.__init__(self, path)

    random.seed(args.seed)
    rows = load_jsonl(args.pairs)
    train_dataset = build_train_dataset(rows)

    device = resolve_device(args.device)
    dev_count = sum(1 for row in rows if row.get("split") == "dev")
    model = make_cross_encoder(
        args.model_name_or_path,
        args.max_length,
        args.trust_remote_code,
        num_labels=1,
        device=device,
    )
    steps_per_epoch = max(1, (len(train_dataset) + args.batch_size - 1) // args.batch_size)
    scheduler_steps_per_epoch = max(1, len(train_dataset) // args.batch_size)
    warmup_steps = int(steps_per_epoch * args.epochs * args.warmup_ratio)
    num_train_steps = int(scheduler_steps_per_epoch * args.epochs)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    loss_history_path = out_dir / "loss_history.jsonl"
    loss_curve_path = out_dir / "loss_curve.png"
    write_json(
        out_dir / "train_config.json",
        {
            "pairs": str(Path(args.pairs).resolve()),
            "model_name_or_path": args.model_name_or_path,
            "device": device,
            "epochs": args.epochs,
            "batch_size": args.batch_size,
            "lr": args.lr,
            "weight_decay": args.weight_decay,
            "max_length": args.max_length,
            "warmup_steps": warmup_steps,
            "logging_steps": args.logging_steps,
            "train_examples": len(train_dataset),
            "dev_examples": dev_count,
            "loss_history": str(loss_history_path.resolve()),
            "loss_curve": str(loss_curve_path.resolve()),
        },
    )

    args_kwargs = {
        "output_dir": str(out_dir),
        "overwrite_output_dir": True,
        "num_train_epochs": args.epochs,
        "per_device_train_batch_size": args.batch_size,
        "learning_rate": args.lr,
        "warmup_steps": warmup_steps,
        "fp16": args.fp16,
        "weight_decay": args.weight_decay,
        "lr_scheduler_type": "linear",
        "max_grad_norm": 1.0,
        "logging_strategy": "steps",
        "logging_steps": args.logging_steps,
        "save_strategy": "no",
        "report_to": [],
        "disable_tqdm": False,
        "seed": args.seed,
    }
    eval_strategy_key = (
        "eval_strategy" if version.parse(transformers.__version__) >= version.parse("4.41.0") else "evaluation_strategy"
    )
    args_kwargs[eval_strategy_key] = "no"

    param_optimizer = list(model.named_parameters())
    no_decay = ["bias", "LayerNorm.bias", "LayerNorm.weight"]
    optimizer_grouped_parameters = [
        {
            "params": [p for n, p in param_optimizer if not any(nd in n for nd in no_decay)],
            "weight_decay": args.weight_decay,
        },
        {
            "params": [p for n, p in param_optimizer if any(nd in n for nd in no_decay)],
            "weight_decay": 0.0,
        },
    ]
    optimizer = torch.optim.AdamW(optimizer_grouped_parameters, lr=args.lr)
    scheduler = SentenceTransformer._get_scheduler(
        optimizer,
        scheduler="WarmupLinear",
        warmup_steps=warmup_steps,
        t_total=num_train_steps,
    )
    loss_fct = BinaryCrossEntropyLoss(model) if model.config.num_labels == 1 else CrossEntropyLoss(model)

    loss_callback = _LossHistoryCallback(loss_history_path)
    trainer = CrossEncoderTrainer(
        model=model,
        args=CrossEncoderTrainingArguments(**args_kwargs),
        train_dataset=train_dataset,
        loss=loss_fct,
        optimizers=(optimizer, scheduler),
        callbacks=[loss_callback],
    )
    trainer.train()

    export_dir = export_cross_encoder(model, out_dir)
    if not is_loadable_dir(export_dir):
        raise RuntimeError(f"Training finished but export is not loadable: {export_dir}")
    write_loss_curve(loss_callback.records, loss_curve_path)
    print(f"saved fine-tuned reranker -> {export_dir}")
    print(f"saved loss history -> {loss_history_path}")
    print(f"saved loss curve -> {loss_curve_path}")


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
    train.add_argument("--weight-decay", type=float, default=0.01)
    train.add_argument("--max-length", type=int, default=512)
    train.add_argument("--warmup-ratio", type=float, default=0.1)
    train.add_argument("--logging-steps", type=int, default=1)
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
