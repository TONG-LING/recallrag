#!/usr/bin/env python3
from __future__ import annotations

import inspect
import json
import os
from pathlib import Path

DEFAULT_HF_MIRROR = "https://hf-mirror.com"


def load_json(path: str | Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_jsonl(path: str | Path) -> list[dict]:
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: str | Path, obj) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def configure_hf_endpoint(endpoint: str | None = None, *, use_mirror: bool = True) -> str:
    if endpoint:
        os.environ["HF_ENDPOINT"] = endpoint.rstrip("/")
    elif use_mirror and not os.environ.get("HF_ENDPOINT"):
        os.environ["HF_ENDPOINT"] = DEFAULT_HF_MIRROR
    return os.environ.get("HF_ENDPOINT", "https://huggingface.co")


def resolve_device(device: str | None) -> str:
    import torch

    if device:
        return device
    return "cuda:0" if torch.cuda.is_available() else "cpu"


def _has_model_type(config_path: Path) -> bool:
    if not config_path.exists():
        return False
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    return bool(data.get("model_type"))


def _is_cross_encoder_export(path: Path) -> bool:
    return (path / "modules.json").exists()


def is_loadable_dir(path: Path) -> bool:
    return _is_cross_encoder_export(path) or _has_model_type(path / "config.json")


def _checkpoint_sort_key(path: Path) -> int:
    try:
        return int(path.name.split("-", 1)[1])
    except (IndexError, ValueError):
        return -1


def resolve_cross_encoder_path(model_name_or_path: str) -> str:
    path = Path(model_name_or_path)
    if not path.is_dir():
        return model_name_or_path

    marker = path / "exported_model.json"
    if marker.exists():
        export_path = Path(load_json(marker)["path"])
        if export_path.exists():
            return str(export_path.resolve())

    for candidate in (path / "final", path):
        if candidate.exists() and is_loadable_dir(candidate):
            return str(candidate.resolve())

    checkpoints = sorted(
        (child for child in path.glob("checkpoint-*") if child.is_dir()),
        key=_checkpoint_sort_key,
        reverse=True,
    )
    for candidate in checkpoints:
        if is_loadable_dir(candidate):
            return str(candidate.resolve())

    raise FileNotFoundError(f"No loadable CrossEncoder export found under `{path}`.")


def export_cross_encoder(model, out_dir: str | Path) -> Path:
    out_dir = Path(out_dir)
    export_dir = out_dir / "final"
    export_dir.mkdir(parents=True, exist_ok=True)
    if hasattr(model, "save_pretrained"):
        model.save_pretrained(str(export_dir))
    elif hasattr(model, "save"):
        model.save(str(export_dir))
    else:
        raise RuntimeError("CrossEncoder model has neither save_pretrained() nor save().")
    write_json(out_dir / "exported_model.json", {"path": str(export_dir.resolve())})
    return export_dir


def make_cross_encoder(
    model_name_or_path: str,
    max_length: int,
    trust_remote_code: bool,
    num_labels: int | None = None,
    device: str | None = None,
):
    from sentence_transformers.cross_encoder import CrossEncoder

    resolved_path = resolve_cross_encoder_path(model_name_or_path)
    if resolved_path != model_name_or_path:
        print(f"==> resolved model path: {resolved_path}")

    kwargs = {"max_length": max_length}
    if num_labels is not None:
        kwargs["num_labels"] = num_labels

    params = inspect.signature(CrossEncoder.__init__).parameters
    if "device" in params:
        kwargs["device"] = resolve_device(device)
    if "trust_remote_code" in params:
        kwargs["trust_remote_code"] = trust_remote_code
    elif trust_remote_code:
        remote_args = {"trust_remote_code": True}
        for key in ("automodel_args", "tokenizer_args", "config_args"):
            if key in params:
                kwargs[key] = remote_args
    return CrossEncoder(resolved_path, **kwargs)
