#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

if [[ -n "${PYTHON:-}" ]]; then
  :
elif [[ -x "$SCRIPT_DIR/.venv/bin/python" ]]; then
  PYTHON="$SCRIPT_DIR/.venv/bin/python"
elif [[ -x "$SCRIPT_DIR/../.venv/bin/python" ]]; then
  PYTHON="$SCRIPT_DIR/../.venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
  PYTHON="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON="python"
else
  echo "error: python3/python not found. Install Python or set PYTHON=/path/to/python." >&2
  exit 1
fi

echo "==> using python: $PYTHON"

# sentence-transformers 的 CrossEncoder.fit 在多卡 DataParallel 下会报错，默认只用第一张 GPU
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
echo "==> CUDA_VISIBLE_DEVICES: $CUDA_VISIBLE_DEVICES"

"$PYTHON" -c "import torch, sentence_transformers, datasets, matplotlib" 2>/dev/null || {
  echo "error: missing dependencies. Run:" >&2
  echo "  $PYTHON -m pip install -r requirements.txt" >&2
  exit 1
}

is_local_model_dir() {
  local p="$1"
  [[ -d "$p" ]] && { [[ -f "$p/config.json" ]] || [[ -f "$p/modules.json" ]]; }
}

resolve_model() {
  if [[ -n "${MODEL_NAME_OR_PATH:-}" ]]; then
    printf '%s' "$MODEL_NAME_OR_PATH"
    return
  fi
  local candidate
  for candidate in \
    "$SCRIPT_DIR/models/bge-reranker-base" \
    "$SCRIPT_DIR/model/bge-reranker-base" \
    "$SCRIPT_DIR/bge-reranker-base"; do
    if is_local_model_dir "$candidate"; then
      printf '%s' "$candidate"
      return
    fi
  done
  printf '%s' "BAAI/bge-reranker-base"
}

MODEL_NAME_OR_PATH="$(resolve_model)"

# HuggingFace 国内镜像：通过环境变量生效，不依赖 reranker_finetune.py 是否支持 --hf-endpoint
# 关闭镜像: USE_HF_MIRROR=0 bash run_example.sh
if is_local_model_dir "$MODEL_NAME_OR_PATH"; then
  export HF_HUB_OFFLINE=1
  export TRANSFORMERS_OFFLINE=1
  unset HF_ENDPOINT
  echo "==> model (local offline): $MODEL_NAME_OR_PATH"
elif [[ "${USE_HF_MIRROR:-1}" == "1" && -z "${HF_ENDPOINT:-}" ]]; then
  export HF_ENDPOINT="https://hf-mirror.com"
  echo "==> model (remote via mirror): $MODEL_NAME_OR_PATH"
  echo "==> HF_ENDPOINT: $HF_ENDPOINT"
else
  echo "==> model (remote): $MODEL_NAME_OR_PATH"
  echo "==> HF_ENDPOINT: ${HF_ENDPOINT:-https://huggingface.co}"
fi

echo "==> workdir: $SCRIPT_DIR"

DATA_DIR="data"
MODEL_OUTPUT_DIR="${MODEL_OUTPUT_DIR:-outputs/bge_reranker_boundary_topk}"
BASE_EVAL_DIR="${BASE_EVAL_DIR:-outputs/eval_base_test}"
FINETUNED_EVAL_DIR="${FINETUNED_EVAL_DIR:-outputs/eval_finetuned_test}"
COMPARE_REPORT="${COMPARE_REPORT:-outputs/compare_report.md}"
RUN_BOUNDARY_EVAL="${RUN_BOUNDARY_EVAL:-0}"

if [[ "${SKIP_REBUILD_DATA:-0}" != "1" ]]; then
  echo
  echo "[0/5] rebuild boundary-focused Top-k data"
  "$PYTHON" -u build_topk_boundary_dataset.py \
    --out-dir "$DATA_DIR"
fi

echo
echo "[1/5] eval base reranker (test split)"
"$PYTHON" -u reranker_eval.py \
  --model-name-or-path "$MODEL_NAME_OR_PATH" \
  --split-filter test \
  --out "$BASE_EVAL_DIR"

echo
echo "[2/5] train reranker"
"$PYTHON" -u reranker_finetune.py train \
  --pairs "$DATA_DIR/pairs.jsonl" \
  --model-name-or-path "$MODEL_NAME_OR_PATH" \
  --output-dir "$MODEL_OUTPUT_DIR" \
  --epochs 2 \
  --batch-size 8 \
  --lr 2e-5 \
  --max-length 512 \
  --fp16

echo
echo "[3/5] eval fine-tuned reranker (test split)"
"$PYTHON" -u reranker_eval.py \
  --model-name-or-path "$MODEL_OUTPUT_DIR" \
  --split-filter test \
  --out "$FINETUNED_EVAL_DIR"

if [[ "$RUN_BOUNDARY_EVAL" == "1" ]]; then
  echo
  echo "[3.5/5] eval fine-tuned reranker (boundary-sensitive test subset)"
  "$PYTHON" -u reranker_eval.py \
    --model-name-or-path "$MODEL_OUTPUT_DIR" \
    --split-filter test \
    --subset-filter boundary_sensitive \
    --out outputs/eval_boundary_test
fi

echo
echo "[4/5] compare before/after"
"$PYTHON" -u reranker_finetune.py compare \
  --before "$BASE_EVAL_DIR/metrics.json" \
  --after "$FINETUNED_EVAL_DIR/metrics.json" \
  --out "$COMPARE_REPORT"

echo
echo "done."
echo "  data dir:          $DATA_DIR"
echo "  loss history:      $MODEL_OUTPUT_DIR/loss_history.jsonl"
echo "  loss curve:        $MODEL_OUTPUT_DIR/loss_curve.png"
echo "  base metrics:      $BASE_EVAL_DIR/metrics.json"
echo "  finetuned metrics: $FINETUNED_EVAL_DIR/metrics.json"
echo "  compare report:    $COMPARE_REPORT"
echo
"$PYTHON" - <<PY
import json
from pathlib import Path

base = json.loads(Path("$BASE_EVAL_DIR/metrics.json").read_text(encoding="utf-8"))
fin = json.loads(Path("$FINETUNED_EVAL_DIR/metrics.json").read_text(encoding="utf-8"))

print("quick summary")
print(f"  base      mrr={base['mrr']:.4f} recall@5={base['recall@5']:.4f} hits={base['hits']}/{base['total']}")
print(f"  finetuned mrr={fin['mrr']:.4f} recall@5={fin['recall@5']:.4f} hits={fin['hits']}/{fin['total']}")
print(f"  delta     mrr={fin['mrr']-base['mrr']:+.4f} recall@5={fin['recall@5']-base['recall@5']:+.4f}")
PY
