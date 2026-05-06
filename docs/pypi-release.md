# PyPI Release Guide

## 1. Create package on PyPI

Create a PyPI account, then configure Trusted Publishing for:

- Owner: roshanguptamca
- Repository: ai-dev-agent
- Workflow file: publish.yml
- Environment name: leave blank unless you add one

## 2. Local validation

```bash
pip install -e ".[dev]"
pytest
ruff check .
python -m build
twine check dist/*
```

## 3. Release

```bash
git tag v0.1.0
git push origin v0.1.0
```

GitHub Actions will build and publish to PyPI.
