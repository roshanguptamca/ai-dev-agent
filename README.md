# AI Dev Agent

AI-powered local development agent that converts requirements from Jira, PDFs, DOCX, and code context into validated GitHub pull requests.

## Install

```bash
pip install ai-dev-agent
```

## Usage

```bash
ai-dev-agent --help
```

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev,rag]"
pytest
ruff check .
```

## Build locally

```bash
python -m build
twine check dist/*
```

## Publish

This repository is configured for GitHub Actions + PyPI Trusted Publishing.
Create a GitHub release or push a tag like:

```bash
git tag v0.1.0
git push origin v0.1.0
```
