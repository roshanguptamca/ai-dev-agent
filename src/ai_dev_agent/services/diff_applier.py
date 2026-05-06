import subprocess
from pathlib import Path


def apply_patch(repo_path: str, diff: str, check_only: bool = False) -> bool:
    """
    Apply unified git diff safely.
    """

    if not diff.strip():
        return False

    patch_path = Path(repo_path) / ".smartpr.patch"
    patch_path.write_text(diff, encoding="utf-8")

    cmd = ["git", "apply"]

    if check_only:
        cmd.append("--check")

    cmd.append(str(patch_path))

    result = subprocess.run(
        cmd,
        cwd=repo_path,
        capture_output=True,
        text=True,
    )

    patch_path.unlink(missing_ok=True)

    if result.returncode != 0:
        raise RuntimeError(
            f"git apply failed:\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )

    return not check_only