import argparse
import json
from ai_dev_agent import __version__
from ai_dev_agent.runner import run_agent

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="quick-pr",
        description="Generate validated pull requests from Jira or requirement documents.",
    )
    parser.add_argument("--version", action="store_true", help="Show version")
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--issue", help="Jira issue key, e.g. DEV-123")
    source.add_argument("--requirement-file", help="Path to PDF/DOCX/TXT/MD requirement file")
    parser.add_argument("--repo", default=".", help="Local repository path")
    parser.add_argument("--repo-url", help="Optional repository URL to clone")
    parser.add_argument("--dry-run", action="store_true", help="Do not commit, push, or create PR")
    parser.add_argument("--create-pr", action="store_true", help="Commit, push, and create GitHub PR")
    parser.add_argument("--mock-ai", action="store_true", help="Use deterministic mock AI output")
    parser.add_argument("--mock-jira", action="store_true", help="Use mock Jira content for --issue")
    parser.add_argument("--framework", help="Override framework: fastapi, django, aiohttp, python")
    args = parser.parse_args()

    if args.version:
        print(__version__)
        return

    if not args.issue and not args.requirement_file:
        parser.error("Provide --issue or --requirement-file")

    result = run_agent(
        issue=args.issue,
        requirement_file=args.requirement_file,
        repo=args.repo,
        repo_url=args.repo_url,
        dry_run=args.dry_run or not args.create_pr,
        create_pr=args.create_pr,
        mock_ai=args.mock_ai,
        mock_jira=args.mock_jira,
        framework_override=args.framework,
    )
    print(json.dumps(result.__dict__, indent=2))
