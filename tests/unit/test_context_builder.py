from ai_dev_agent.models.types import Requirement
from ai_dev_agent.services.repo_indexer import index_repo
from ai_dev_agent.services.context_builder import build_context

def test_context_contains_files():
    req = Requirement(source="test", key=None, title="health endpoint", body="add health")
    chunks = index_repo("tests/fixtures/mock_repo")
    context = build_context(req, chunks)
    assert "# FILE:" in context
