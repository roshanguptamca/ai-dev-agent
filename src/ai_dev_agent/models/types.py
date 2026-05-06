from dataclasses import dataclass, field

@dataclass
class Requirement:
    source: str
    key: str | None
    title: str
    body: str
    acceptance_criteria: list[str] = field(default_factory=list)

@dataclass
class CodeChunk:
    path: str
    content: str
    score: int = 0

@dataclass
class Plan:
    tasks: list[str]
    files_to_modify: list[str]
    tests_to_add_or_update: list[str] = field(default_factory=list)
    risk_level: str = "medium"

@dataclass
class AgentResult:
    requirement_title: str
    framework: str
    branch: str | None
    changed: bool
    validation_ok: bool
    dry_run: bool
    pr_url: str | None = None
    plan: dict | None = None
    logs: str = ""
