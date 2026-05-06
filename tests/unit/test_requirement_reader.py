from ai_dev_agent.services.requirement_reader import read_requirement_file

def test_read_markdown_requirement():
    req = read_requirement_file("tests/fixtures/requirements/health.md")
    assert "health endpoint" in req.body.lower()
    assert req.title == "Add health endpoint"
