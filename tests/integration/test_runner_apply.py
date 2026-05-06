import shutil
import subprocess
from pathlib import Path
from ai_dev_agent.runner import run_agent

def test_runner_mock_ai_apply(tmp_path):
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
        dry_run=False,
        create_pr=False,
        mock_ai=True,
    )

    assert result.changed is True
    assert result.validation_ok is True
    assert "/health" in (repo / "app/main.py").read_text()
