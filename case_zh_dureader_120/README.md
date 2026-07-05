# 中文 DuReader 长文档评测集

这套数据不是原始 DuReader 评测格式，而是从公开的 `DuReader Retrieval` dev 数据派生出来的长文档版本，专门用于测试 RecallRAG 的 chunk / patch 逻辑。

构造方式：
- 来源：`https://huggingface.co/datasets/zyznull/dureader-retrieval-ranking/resolve/main/dev.jsonl.gz`
- 样本数：`120`
- 每个文档混入的负样本段数：`4`
- 正样本长度范围：`[380, 1400]`

目录：
- `docs/`：长文档 markdown
- `eval/questions.jsonl`：中文查询与 gold span
- `source_metadata.json`：来源映射，方便审计

说明：
- `gold_span` 对应原始正样本文段。
- 文档中加入了同 query 的负样本文段，目的是构造更接近 RAG 长文档检索的干扰环境。
- 这是一套面向 RecallRAG 的中文复杂文档测试集，不等同于原始 benchmark leaderboard 用法。
