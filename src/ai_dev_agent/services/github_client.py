import requests
from ai_dev_agent.config import settings

def create_github_pr(branch: str, title: str, body: str) -> str:
    if not settings.github_token or not settings.github_repo:
        raise RuntimeError("Missing GITHUB_TOKEN or GITHUB_REPO.")

    url = f"https://api.github.com/repos/{settings.github_repo}/pulls"
    headers = {
        "Authorization": f"Bearer {settings.github_token}",
        "Accept": "application/vnd.github+json",
    }
    payload = {
        "title": title,
        "head": branch,
        "base": settings.github_base_branch,
        "body": body,
    }
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    return response.json().get("html_url", "")
