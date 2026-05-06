from ai_dev_agent.services.repo_indexer import index_repo

def test_index_repo():
    chunks = index_repo("tests/fixtures/mock_repo")
    assert chunks
    assert any(c.path == "app/main.py" for c in chunks)
