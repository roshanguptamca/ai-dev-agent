import shutil
import subprocess
from pathlib import Path
from ai_dev_agent.runner import run_agent

def test_runner_mock_ai_dry_run(tmp_path):
    src = Path("tests/fixtures/mock_repo")
    repo = tmp_path / "repo"
    shutil.copytree(src, repo)
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-m", "init"], cwd=repo, check=True, capture_output=True)

    result = run_agent(
        requirement_file="tests/fixtures/requirements/health.md",
        repo=str(repo),
        dry_run=True,
        mock_ai=True,
    )

    assert result.framework == "fastapi"
    assert result.validation_ok is True
    assert result.dry_run is True
