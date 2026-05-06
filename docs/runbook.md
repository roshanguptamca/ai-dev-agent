# Runbook

## Local dry run

```bash
quick-pr --requirement-file tests/fixtures/requirements/health.md --repo tests/fixtures/mock_repo --dry-run --mock-ai
```

## Real requirement file

```bash
quick-pr --requirement-file ./story.docx --repo . --dry-run
```

## Jira

```bash
quick-pr --issue DEV-123 --repo . --dry-run
```

## Real PR

```bash
quick-pr --issue DEV-123 --repo . --create-pr
```
