from pathlib import Path
from .schemas import Document

def load_markdown_docs(docs_dir: str | Path) -> list[Document]:
    docs_dir = Path(docs_dir)
    docs: list[Document] = []
    for path in sorted(docs_dir.glob('*.md')):
        docs.append(Document(doc_id=path.name, path=str(path), text=path.read_text(encoding='utf-8')))
    if not docs:
        raise FileNotFoundError(f'No .md files found in {docs_dir}')
    return docs
