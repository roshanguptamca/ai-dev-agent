from pathlib import Path
from ai_dev_agent.config import settings

SUPPORTED = {"fastapi", "django", "aiohttp", "python", "auto"}

def detect_framework(repo_path: str, override: str | None = None) -> str:
    selected = override or settings.framework
    if selected and selected != "auto":
        if selected not in SUPPORTED:
            raise ValueError(f"Unsupported framework: {selected}")
        return selected

    root = Path(repo_path)
    if (root / "manage.py").exists():
        return "django"

    sample = []
    for path in root.rglob("*.py"):
        if _ignored(path):
            continue
        try:
            sample.append(path.read_text(encoding="utf-8", errors="ignore")[:5000])
        except OSError:
            pass

    text = "\n".join(sample).lower()
    if "from fastapi import" in text or "fastapi(" in text:
        return "fastapi"
    if "from aiohttp import web" in text or "aiohttp.web" in text:
        return "aiohttp"
    return "python"

def _ignored(path: Path) -> bool:
    ignored = {".git", ".venv", "venv", "__pycache__", ".pytest_cache", "node_modules"}
    return any(part in ignored for part in path.parts)
