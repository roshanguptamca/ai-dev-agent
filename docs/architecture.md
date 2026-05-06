# Architecture

```text
CLI
 ↓
Requirement Reader
 ├─ Jira
 ├─ PDF
 ├─ DOCX
 └─ TXT/Markdown
 ↓
Repo Indexer
 ↓
Context Builder
 ↓
Planner
 ↓
Diff Generator
 ↓
Patch Applier
 ↓
Validator
 ↓
GitHub PR Creator
```

The LLM only returns plans and diffs. It does not execute shell commands or call external services directly.
