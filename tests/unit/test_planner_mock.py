from ai_dev_agent.models.types import Requirement
from ai_dev_agent.services.planner import create_plan

def test_mock_plan():
    req = Requirement(source="test", key="X-1", title="Add health", body="body")
    plan = create_plan(req, "context", "fastapi", mock_ai=True)
    assert plan.tasks
