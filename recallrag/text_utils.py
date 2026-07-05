from __future__ import annotations

import re

LATIN_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")
CJK_SPAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]+")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?。！？；;])\s+|\n+")
EN_STOPWORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "was",
    "were",
    "be",
    "being",
    "been",
    "to",
    "of",
    "in",
    "on",
    "for",
    "and",
    "or",
    "but",
    "why",
    "how",
    "what",
    "when",
    "where",
    "can",
    "could",
    "should",
    "would",
    "does",
    "do",
    "did",
    "it",
    "this",
    "that",
    "with",
    "without",
    "into",
    "from",
    "by",
    "as",
    "at",
    "if",
    "then",
    "than",
}


def normalize_text(text: str) -> str:
    return " ".join((text or "").replace("\u3000", " ").replace("\xa0", " ").split())


def mixed_tokens(
    text: str,
    *,
    drop_stopwords: bool = False,
    min_ascii_len: int = 1,
    cjk_ngram: int = 2,
) -> list[str]:
    norm = normalize_text(text).lower()
    tokens: list[str] = []

    for token in LATIN_TOKEN_RE.findall(norm):
        if len(token) < min_ascii_len:
            continue
        if drop_stopwords and token in EN_STOPWORDS:
            continue
        tokens.append(token)

    for span in CJK_SPAN_RE.findall(norm):
        chars = [ch for ch in span if ch.strip()]
        if not chars:
            continue
        if len(chars) < cjk_ngram:
            tokens.extend(chars)
            continue
        tokens.extend(
            "".join(chars[i : i + cjk_ngram])
            for i in range(len(chars) - cjk_ngram + 1)
        )
    return tokens


def mixed_token_set(
    text: str,
    *,
    drop_stopwords: bool = False,
    min_ascii_len: int = 1,
    cjk_ngram: int = 2,
) -> set[str]:
    return set(
        mixed_tokens(
            text,
            drop_stopwords=drop_stopwords,
            min_ascii_len=min_ascii_len,
            cjk_ngram=cjk_ngram,
        )
    )


def split_sentences(text: str, min_chars: int = 18) -> list[str]:
    sentences: list[str] = []
    for part in SENTENCE_SPLIT_RE.split((text or "").replace("\r", "\n")):
        cleaned = normalize_text(part).strip("。！？；;.!? ").strip()
        if len(cleaned) >= min_chars:
            sentences.append(cleaned)
    return sentences
