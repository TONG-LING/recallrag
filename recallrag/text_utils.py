from __future__ import annotations


#分词
#eval.coverage() 和 diagnose 里的对比方法都依赖 mixed_tokens
#英文按词切，中文按字符 bigram 切


import re

# 英文，数字，下划线片段
LATIN_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")
# CJK识别
CJK_SPAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff]+")
# 在句末标点后切句，也按换行切
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?。！？；;])\s+|\n+")
# 诊断阶段可选去掉英文停用词，减少"the/is/of"这类噪声
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
    #空白处理：全角空格、不间断空格都变成普通空格，多空格合成一个
    return " ".join((text or "").replace("\u3000", " ").replace("\xa0", " ").split())


def mixed_tokens(
    text: str,
    *,
    drop_stopwords: bool = False,
    min_ascii_len: int = 1,
    cjk_ngram: int = 2,
) -> list[str]:
    """把一段文本拆成coverage用的token列表

    英文：按LATIN_TOKEN_RE切词，转小写
    中文：先抽出连续汉字段，再sliding window切成bigram（2-gram）
         汉字太少（< cjk_ngram）时取单字

    eval.coverage()用gold_span的token去chunk里做集合命中
    diagnose里算query-chunk重叠
    """
    norm = normalize_text(text).lower()
    tokens: list[str] = []

    #拉丁字母，数字段
    for token in LATIN_TOKEN_RE.findall(norm):
        if len(token) < min_ascii_len:
            continue
        if drop_stopwords and token in EN_STOPWORDS:
            continue
        tokens.append(token)

    #中文段：bigram
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
    #mixed_tokens的去重版，诊断里算query和chunk重叠时用
    return set(
        mixed_tokens(
            text,
            drop_stopwords=drop_stopwords,
            min_ascii_len=min_ascii_len,
            cjk_ngram=cjk_ngram,
        )
    )


def split_sentences(text: str, min_chars: int = 18) -> list[str]:
    """按中英文句末标点切句，过滤太短的碎片。
    patch_index生成contextual/proposition类patch时，
    会先把chunk切成句，再挑和query更相关的几句。
    """
    sentences: list[str] = []
    for part in SENTENCE_SPLIT_RE.split((text or "").replace("\r", "\n")):
        cleaned = normalize_text(part).strip("。！？；;.!? ").strip()
        if len(cleaned) >= min_chars:
            sentences.append(cleaned)
    return sentences