import requests
from ai_dev_agent.config import settings
from ai_dev_agent.models.types import Requirement

def _adf_to_text(value) -> str:
    if isinstance(value, str):
        return value
    parts: list[str] = []
    def walk(node):
        if isinstance(node, dict):
            if node.get("type") == "text":
                parts.append(node.get("text", ""))
            for child in node.get("content", []):
                walk(child)
        elif isinstance(node, list):
            for item in node:
                walk(item)
    walk(value)
    return " ".join(parts)

def get_jira_requirement(issue_key: str, mock: bool = False) -> Requirement:
    if mock:
        return Requirement(
            source="mock-jira",
            key=issue_key,
            title="Add health endpoint",
            body="Add GET /health endpoint returning {'status': 'ok'}",
            acceptance_criteria=["GET /health returns 200", "Body contains status ok"],
        )

    if not all([settings.jira_base_url, settings.jira_email, settings.jira_api_token]):
        raise RuntimeError("Missing Jira environment variables.")

    url = f"{settings.jira_base_url}/rest/api/3/issue/{issue_key}"
    response = requests.get(url, auth=(settings.jira_email, settings.jira_api_token), timeout=30)
    response.raise_for_status()
    data = response.json()
    fields = data["fields"]

    return Requirement(
        source="jira",
        key=issue_key,
        title=fields.get("summary", issue_key),
        body=_adf_to_text(fields.get("description", "")),
        acceptance_criteria=[],
    )
