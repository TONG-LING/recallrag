#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from recallrag.eval import load_questions
from recallrag.text_utils import mixed_token_set, normalize_text

ASCII_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build a query-held-out eval set by rewriting existing questions."
    )
    parser.add_argument(
        "--questions",
        default="case_zh_dureader/eval/questions.jsonl",
        help="Source questions.jsonl",
    )
    parser.add_argument(
        "--out",
        default="case_zh_dureader/eval/questions_heldout.jsonl",
        help="Output held-out questions.jsonl",
    )
    parser.add_argument(
        "--patch-source-out",
        default=None,
        help="Optional explicit patch-source questions copy. Recommended for audit clarity.",
    )
    parser.add_argument(
        "--log-out",
        default=None,
        help="Optional rewrite audit json path. Defaults to <out>.rewrite_audit.json",
    )
    parser.add_argument(
        "--endpoint",
        default="http://localhost:1234/v1/chat/completions",
        help="Rewrite endpoint",
    )
    parser.add_argument(
        "--model",
        default="hy-mt2-1.8b",
        help="Rewrite model name",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.4,
        help="Rewrite temperature",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=120,
        help="Max generation tokens",
    )
    parser.add_argument(
        "--retries",
        type=int,
        default=3,
        help="Retry count when rewrite is empty or unchanged",
    )
    parser.add_argument(
        "--protocol",
        choices=["openai_chat", "messages", "anthropic_messages"],
        default="openai_chat",
        help="Request protocol",
    )
    parser.add_argument(
        "--api-key",
        default=None,
        help="Optional API key",
    )
    parser.add_argument(
        "--auth-mode",
        choices=["auto", "none", "authorization", "x-api-key"],
        default="auto",
        help="Auth header mode",
    )
    parser.add_argument(
        "--api-version",
        default="2023-06-01",
        help="Anthropic/messages API version",
    )
    parser.add_argument(
        "--disable-thinking",
        action="store_true",
        help="Disable thinking for messages-style endpoints when supported",
    )
    parser.add_argument(
        "--qid-suffix",
        default="_holdout",
        help="Suffix appended to the original qid",
    )
    return parser.parse_args()


def _system_prompt() -> str:
    return (
        "你是中文检索评测集改写助手。"
        "请把用户问题改写成另一种自然问法。"
        "要求：语义不变，关键实体不要丢，尽量换表达，不要解释任务，不要加引号，只输出改写后的一个问题。"
    )


def _user_prompt(question: str, attempt: int) -> str:
    extra = ""
    if attempt > 1:
        extra = "这次请在不改变含义的前提下继续换表达，但不能改掉方向词、否定词、型号、版本号、专有名词。"
    return (
        "请把下面这个问题换一种中文问法。\n"
        "硬性要求：\n"
        "1. 语义必须完全一致；\n"
        "2. 不得改变方向、数量、时态、正反含义；\n"
        "3. 型号、版本号、英文词、专有名词必须保留；\n"
        "4. 只输出改写后的问题，不要解释。\n"
        f"原问题：{question}\n"
        f"{extra}"
    )


def _normalize_protocol(protocol: str) -> str:
    return "messages" if protocol == "anthropic_messages" else protocol


def _headers(protocol: str, api_key: str | None, auth_mode: str, api_version: str) -> dict[str, str]:
    headers = {"Content-Type": "application/json"}
    if auth_mode == "auto":
        auth_mode = "x-api-key" if protocol == "messages" else "authorization"
    if protocol == "messages":
        headers["anthropic-version"] = api_version
    if api_key:
        if auth_mode == "authorization":
            headers["Authorization"] = f"Bearer {api_key}"
        elif auth_mode == "x-api-key":
            headers["x-api-key"] = api_key
    return headers


def _payload(
    protocol: str,
    model: str,
    question: str,
    attempt: int,
    temperature: float,
    max_tokens: int,
    disable_thinking: bool,
) -> dict:
    if protocol == "openai_chat":
        return {
            "model": model,
            "messages": [
                {"role": "system", "content": _system_prompt()},
                {"role": "user", "content": _user_prompt(question, attempt)},
            ],
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
    payload = {
        "model": model,
        "system": _system_prompt(),
        "messages": [{"role": "user", "content": _user_prompt(question, attempt)}],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if disable_thinking:
        payload["thinking"] = {"type": "disabled"}
    return payload


def _extract_text(protocol: str, data: dict) -> str:
    if protocol == "openai_chat":
        choices = data.get("choices") or []
        message = choices[0].get("message", {}) if choices else {}
        content = message.get("content") or ""
        if isinstance(content, list):
            parts = []
            for item in content:
                if isinstance(item, dict) and item.get("type") == "text" and item.get("text"):
                    parts.append(str(item["text"]))
            content = "\n".join(parts)
        return normalize_text(str(content))
    content = data.get("content") or []
    if isinstance(content, str):
        return normalize_text(content)
    if not isinstance(content, list):
        return ""
    parts = []
    for item in content:
        if isinstance(item, dict) and item.get("type") == "text" and item.get("text"):
            parts.append(str(item["text"]))
    return normalize_text("\n".join(parts))


def _critical_char_mismatch(source: str, rewritten: str) -> str | None:
    for ch in ("左", "右", "上", "下", "前", "后"):
        if ch in source and ch not in rewritten:
            return ch
    neg_source_patterns = ("不能", "不可以", "不行", "无法", "不会", "不具", "无效", "禁止", "不可", "不是")
    neg_rewrite_patterns = neg_source_patterns + ("避免", "忌", "禁")
    source_has_negation = any(pattern in source for pattern in neg_source_patterns)
    rewritten_has_negation = any(pattern in rewritten for pattern in neg_rewrite_patterns)
    if source_has_negation and not rewritten_has_negation:
        return "NEGATION"
    return None


def _missing_ascii_tokens(source: str, rewritten: str) -> list[str]:
    source_tokens = {token.lower() for token in ASCII_TOKEN_RE.findall(source) if len(token) >= 2}
    rewritten_tokens = {token.lower() for token in ASCII_TOKEN_RE.findall(rewritten) if len(token) >= 2}
    return sorted(source_tokens - rewritten_tokens)


def _is_valid_rewrite(source: str, rewritten: str) -> tuple[bool, str]:
    source_norm = normalize_text(source)
    rewritten_norm = normalize_text(rewritten)
    if not rewritten_norm:
        return False, "empty"
    if rewritten_norm == source_norm:
        return False, "unchanged"
    missing_ascii = _missing_ascii_tokens(source_norm, rewritten_norm)
    if missing_ascii:
        return False, f"missing_ascii:{','.join(missing_ascii)}"
    mismatch = _critical_char_mismatch(source_norm, rewritten_norm)
    if mismatch:
        return False, f"missing_critical_char:{mismatch}"
    return True, "ok"


def _rewrite_question(
    question: str,
    *,
    endpoint: str,
    model: str,
    temperature: float,
    max_tokens: int,
    retries: int,
    protocol: str,
    api_key: str | None,
    auth_mode: str,
    api_version: str,
    disable_thinking: bool,
) -> tuple[str, int]:
    protocol = _normalize_protocol(protocol)
    last_text = ""
    for attempt in range(1, retries + 1):
        payload = _payload(protocol, model, question, attempt, temperature, max_tokens, disable_thinking)
        req = urllib.request.Request(
            endpoint,
            data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
            headers=_headers(protocol, api_key, auth_mode, api_version),
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as response:
                data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "ignore")
            raise RuntimeError(f"rewrite request failed: HTTP {exc.code}: {detail}") from exc
        except Exception as exc:
            raise RuntimeError(f"rewrite request failed: {exc}") from exc

        text = _extract_text(protocol, data).strip(" \"'“”‘’")
        last_text = text
        ok, _ = _is_valid_rewrite(question, text)
        if ok:
            return text, attempt
    if not last_text:
        raise RuntimeError(f"failed to rewrite question after {retries} attempts: {question}")
    ok, reason = _is_valid_rewrite(question, last_text)
    if not ok:
        raise RuntimeError(f"invalid rewrite after {retries} attempts: {question} -> {last_text} ({reason})")
    return last_text, retries


def _token_overlap(a: str, b: str) -> float:
    a_tokens = mixed_token_set(a, drop_stopwords=True, min_ascii_len=2)
    b_tokens = mixed_token_set(b, drop_stopwords=True, min_ascii_len=2)
    if not a_tokens or not b_tokens:
        return 0.0
    union = a_tokens | b_tokens
    if not union:
        return 0.0
    return len(a_tokens & b_tokens) / len(union)


def main() -> None:
    args = parse_args()
    questions = load_questions(args.questions)
    out_path = Path(args.out)
    patch_source_path = Path(args.patch_source_out) if args.patch_source_out else None
    log_path = Path(args.log_out) if args.log_out else out_path.with_suffix(".rewrite_audit.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if patch_source_path:
        patch_source_path.parent.mkdir(parents=True, exist_ok=True)

    heldout_rows: list[dict] = []
    audit_rows: list[dict] = []

    for row in questions:
        rewritten, attempts = _rewrite_question(
            row["question"],
            endpoint=args.endpoint,
            model=args.model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            retries=args.retries,
            protocol=args.protocol,
            api_key=args.api_key,
            auth_mode=args.auth_mode,
            api_version=args.api_version,
            disable_thinking=args.disable_thinking,
        )
        heldout_row = dict(row)
        heldout_row["qid"] = f"{row['qid']}{args.qid_suffix}"
        heldout_row["question"] = rewritten
        heldout_row["heldout_source_qid"] = row["qid"]
        heldout_row["heldout_source_question"] = row["question"]
        heldout_row["heldout_split"] = "query_rewrite"
        heldout_row["rewrite_model"] = args.model
        heldout_row["rewrite_endpoint"] = args.endpoint
        heldout_rows.append(heldout_row)
        audit_rows.append(
            {
                "source_qid": row["qid"],
                "heldout_qid": heldout_row["qid"],
                "original_question": row["question"],
                "rewritten_question": rewritten,
                "attempts": attempts,
                "normalized_equal": normalize_text(row["question"]) == normalize_text(rewritten),
                "token_jaccard": round(_token_overlap(row["question"], rewritten), 4),
            }
        )
        print(f"[rewrite] {row['qid']} -> {heldout_row['qid']}: {rewritten}")

    out_path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in heldout_rows) + "\n",
        encoding="utf-8",
    )
    if patch_source_path:
        patch_source_path.write_text(
            "\n".join(json.dumps(row, ensure_ascii=False) for row in questions) + "\n",
            encoding="utf-8",
        )
    log_path.write_text(
        json.dumps(
            {
                "source_questions": str(Path(args.questions).resolve()),
                "patch_source_questions": str(patch_source_path.resolve()) if patch_source_path else None,
                "output_questions": str(out_path.resolve()),
                "model": args.model,
                "endpoint": args.endpoint,
                "temperature": args.temperature,
                "max_tokens": args.max_tokens,
                "rows": audit_rows,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"wrote held-out questions -> {out_path}")
    if patch_source_path:
        print(f"wrote patch-source questions -> {patch_source_path}")
    print(f"wrote rewrite audit -> {log_path}")


if __name__ == "__main__":
    main()
