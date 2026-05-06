from pathlib import Path
from ai_dev_agent.models.types import CodeChunk

IGNORE_DIRS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", ".mypy_cache", "node_modules"}
INCLUDE_SUFFIXES = {".py", ".toml", ".yaml", ".yml", ".json", ".md"}

def index_repo(repo_path: str, max_lines: int = 80) -> list[CodeChunk]:
    root = Path(repo_path)
    chunks: list[CodeChunk] = []
    for file_path in root.rglob("*"):
        if not file_path.is_file():
            continue
        if any(part in IGNORE_DIRS for part in file_path.parts):
            continue
        if file_path.suffix.lower() not in INCLUDE_SUFFIXES:
            continue
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = str(file_path.relative_to(root))
        lines = text.splitlines()
        for i in range(0, max(len(lines), 1), max_lines):
            chunk = "\n".join(lines[i:i + max_lines])
            if chunk.strip():
                chunks.append(CodeChunk(path=rel, content=chunk))
    return chunks
