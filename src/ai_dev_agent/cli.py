import argparse

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="ai-dev-agent",
        description="AI-powered local development agent for generating validated GitHub PRs."
    )
    parser.add_argument("--version", action="store_true", help="Show package version")
    parser.add_argument("--issue", help="Requirement source key, such as Jira issue key")
    parser.add_argument("--repo", help="Local repository path")
    parser.add_argument("--dry-run", action="store_true", help="Run without pushing changes")
    args = parser.parse_args()

    if args.version:
        from ai_dev_agent import __version__
        print(__version__)
        return

    if not args.issue:
        parser.print_help()
        return

    print(f"AI Dev Agent would process requirement: {args.issue}")
    if args.repo:
        print(f"Repository: {args.repo}")
    if args.dry_run:
        print("Dry run enabled")
