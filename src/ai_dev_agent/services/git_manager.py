from pathlib import Path
import shutil
from git import Repo

def prepare_repo(repo: str | None, repo_url: str | None, target_dir: str = "repos/work") -> str:
    if repo:
        path = Path(repo)
        if not path.exists():
            raise FileNotFoundError(repo)
        return str(path)

    if not repo_url:
        raise ValueError("Provide repo path or repo-url.")

    target = Path(target_dir)
    if target.exists():
        shutil.rmtree(target)
    Repo.clone_from(repo_url, target)
    return str(target)

def ensure_git_repo(repo_path: str) -> None:
    try:
        Repo(repo_path)
    except Exception as exc:
        raise RuntimeError(f"Not a git repository: {repo_path}") from exc

def create_branch(repo_path: str, branch: str) -> None:
    repo = Repo(repo_path)
    repo.git.checkout("-B", branch)

def has_changes(repo_path: str) -> bool:
    repo = Repo(repo_path)
    return repo.is_dirty(untracked_files=True)

def commit_all(repo_path: str, message: str) -> bool:
    repo = Repo(repo_path)
    if not has_changes(repo_path):
        return False
    repo.git.add(A=True)
    repo.index.commit(message)
    return True

def push(repo_path: str, branch: str) -> None:
    repo = Repo(repo_path)
    repo.git.push("--set-upstream", "origin", branch)
