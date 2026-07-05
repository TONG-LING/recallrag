from __future__ import annotations
import re
from .schemas import Document, Chunk

def _heading_before(text: str, offset: int) -> tuple[str, str]:
    heading = ""
    path: list[str] = []
    for m in re.finditer(r'^(#{1,6})\s+(.+?)\s*$', text[:offset], flags=re.MULTILINE):
        level = len(m.group(1))
        title = m.group(2).strip()
        path = path[:level-1] + [title]
        heading = title
    return heading, " > ".join(path)

def fixed_char_chunk(
    docs: list[Document],
    chunk_size: int = 380,
    overlap: int = 0,
    keep_heading: bool = False,
    strategy_name: str | None = None,
) -> list[Chunk]:
    if overlap >= chunk_size:
        raise ValueError('overlap must be smaller than chunk_size')
    strategy_name = strategy_name or f'fixed_char_{chunk_size}_overlap_{overlap}_heading_{keep_heading}'
    chunks: list[Chunk] = []
    for doc in docs:
        text = doc.text
        start = 0
        idx = 0
        step = chunk_size - overlap
        while start < len(text):
            end = min(len(text), start + chunk_size)
            raw = text[start:end].strip()
            if raw:
                heading, section_path = _heading_before(text, start)
                chunk_text = raw
                if keep_heading and section_path:
                    chunk_text = f'[Section: {section_path}]\n' + raw
                chunks.append(Chunk(
                    chunk_id=f'{doc.doc_id}::c{idx:04d}',
                    doc_id=doc.doc_id,
                    text=chunk_text,
                    start_offset=start,
                    end_offset=end,
                    strategy=strategy_name,
                    section_title=heading,
                    section_path=section_path,
                ))
                idx += 1
            if end >= len(text):
                break
            start += step
    return chunks
