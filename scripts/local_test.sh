#!/usr/bin/env bash
set -euo pipefail
python -m pip install -e ".[dev]"
pytest
quick-pr --requirement-file tests/fixtures/requirements/health.md --repo tests/fixtures/mock_repo --dry-run --mock-ai
