from ai_dev_agent.models.types import Requirement, Plan
from ai_dev_agent.services.generator import generate_diff

def test_mock_diff():
    req = Requirement(source="test", key="X-1", title="Add health", body="body")
    plan = Plan(tasks=["x"], files_to_modify=["app/main.py"])
    diff = generate_diff(req, plan, "context", "fastapi", mock_ai=True)
    assert "diff --git" in diff
    assert "/health" in diff
