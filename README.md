# AI Dev Agent

AI-powered local development agent that converts requirements from Jira, PDFs, DOCX, and code context into validated GitHub pull requests.

## Features

- Jira → PR automation
- PDF/DOCX requirement ingestion
- Framework-aware generation
  - FastAPI
  - Django
  - aiohttp
  - plain Python
- Context-aware code generation
- Validation before PR creation
- Local-first architecture
- GitHub PR automation

---

## Install

```bash
pip install smartpr-ai
```

---

## Usage

```bash
quick-pr --help
```

Example:

```bash
quick-pr --issue PROJ-123 --repo /path/to/repo --dry-run
```

---

## Development

```bash
python -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e ".[dev,rag]"

pytest
ruff check .
```

---

## Build locally

```bash
python -m build
twine check dist/*
```

---

## Publish

This repository is configured for GitHub Actions + PyPI Trusted Publishing.

Create a release tag:

```bash
git tag v0.1.0
git push origin v0.1.0
```

---

## Architecture

```text
Requirements → Context Retrieval → AI Planning → Code Generation → Validation → GitHub PR
```

---

## License

Apache License 2.0