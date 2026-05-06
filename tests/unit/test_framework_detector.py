from ai_dev_agent.services.framework_detector import detect_framework

def test_detect_fastapi():
    assert detect_framework("tests/fixtures/mock_repo") == "fastapi"

def test_override():
    assert detect_framework("tests/fixtures/mock_repo", override="django") == "django"
