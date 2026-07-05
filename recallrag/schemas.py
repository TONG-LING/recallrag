from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class Document:
    doc_id: str
    path: str
    text: str

@dataclass
class Chunk:
    chunk_id: str
    doc_id: str
    text: str
    start_offset: int
    end_offset: int
    strategy: str
    section_title: str = ""
    section_path: str = ""
    source_index: str = "main"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
