import re
from ai_dev_agent.models.types import CodeChunk, Requirement

STOPWORDS = {
    "the", "and", "for", "with", "this", "that", "from", "into", "return", "should",
    "when", "then", "have", "will", "add", "update", "create"
}

def tokenize(text: str) -> set[str]:
    return {
        t.lower()
        for t in re.findall(r"[A-Za-z_][A-Za-z0-9_]{2,}", text)
        if t.lower() not in STOPWORDS
    }

def build_context(requirement: Requirement, chunks: list[CodeChunk], limit: int = 12) -> str:
    terms = tokenize(requirement.title + "\n" + requirement.body + "\n".join(requirement.acceptance_criteria))
    ranked = []
    for chunk in chunks:
        haystack = (chunk.path + "\n" + chunk.content).lower()
        score = sum(1 for term in terms if term in haystack)
        if any(name in chunk.path.lower() for name in ["test", "router", "view", "main", "urls", "models"]):
            score += 1
        ranked.append(CodeChunk(path=chunk.path, content=chunk.content, score=score))

    ranked.sort(key=lambda c: c.score, reverse=True)
    selected = ranked[:limit]
    return "\n\n".join(f"# FILE: {c.path}\n{c.content}" for c in selected)
