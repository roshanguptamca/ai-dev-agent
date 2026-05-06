from pathlib import Path
from ai_dev_agent.models.types import Requirement

def read_requirement_file(path: str) -> Requirement:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)

    suffix = p.suffix.lower()
    if suffix in {".txt", ".md"}:
        body = p.read_text(encoding="utf-8")
    elif suffix == ".pdf":
        body = _read_pdf(p)
    elif suffix in {".docx", ".doc"}:
        body = _read_docx(p)
    else:
        raise ValueError(f"Unsupported requirement file type: {suffix}")

    title = body.strip().splitlines()[0].strip("# ").strip() if body.strip() else p.stem
    return Requirement(source=str(p), key=None, title=title, body=body)

def _read_pdf(path: Path) -> str:
    from pypdf import PdfReader
    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def _read_docx(path: Path) -> str:
    from docx import Document
    doc = Document(str(path))
    return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
