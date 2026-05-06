import shlex
import subprocess
from ai_dev_agent.config import settings

def run_validation(repo_path: str) -> dict:
    commands = [c.strip() for c in settings.validation_commands.split("&&") if c.strip()]
    logs = []
    ok = True

    for command in commands:
        result = subprocess.run(
            shlex.split(command),
            cwd=repo_path,
            capture_output=True,
            text=True,
        )
        logs.append(f"$ {command}\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}")
        if result.returncode != 0:
            ok = False
            break

    return {"ok": ok, "logs": "\n\n".join(logs)}
