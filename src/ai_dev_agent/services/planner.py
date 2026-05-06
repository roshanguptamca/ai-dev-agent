from ai_dev_agent.models.types import Requirement, Plan
from ai_dev_agent.services.openai_client import chat, parse_json

FRAMEWORK_RULES = {
    "fastapi": "Use FastAPI route style, APIRouter if present, and Pydantic models where appropriate.",
    "django": "Use Django app structure, urls.py routing, Django ORM, and existing view style.",
    "aiohttp": "Use async handlers and existing aiohttp route registration style.",
    "python": "Use plain Python module style and avoid introducing a framework unless required.",
}

def create_plan(requirement: Requirement, context: str, framework: str, mock_ai: bool = False) -> Plan:
    if mock_ai:
        return Plan(
            tasks=["Implement requirement with minimal code changes", "Add or update tests"],
            files_to_modify=["app/main.py", "tests/test_main.py"],
            tests_to_add_or_update=["tests/test_main.py"],
            risk_level="low",
        )

    prompt = f"""
Requirement source: {requirement.source}
Requirement key: {requirement.key}
Title: {requirement.title}
Body:
{requirement.body}

Acceptance criteria:
{requirement.acceptance_criteria}

Framework: {framework}
Framework rules: {FRAMEWORK_RULES.get(framework, FRAMEWORK_RULES["python"])}

Relevant repository context:
{context}

Return JSON only:
{{
  "tasks": ["..."],
  "files_to_modify": ["..."],
  "tests_to_add_or_update": ["..."],
  "risk_level": "low|medium|high"
}}
"""
    raw = chat("You are a senior software architect for Python projects.", prompt)
    data = parse_json(raw)
    return Plan(**data)
