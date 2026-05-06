from ai_dev_agent.models.types import Requirement, Plan
from ai_dev_agent.services.openai_client import chat


def generate_diff(
    requirement: Requirement,
    plan: Plan,
    context: str,
    framework: str,
    mock_ai: bool = False,
) -> str:
    """
    Generate unified git diff for repository changes.
    """

    if mock_ai:
        return """diff --git a/app/main.py b/app/main.py
--- a/app/main.py
+++ b/app/main.py
@@ -1,16 +1,21 @@
 try:
     from fastapi import FastAPI
 except ModuleNotFoundError:
     class FastAPI:
         def get(self, *_args, **_kwargs):
             def decorator(func):
                 return func
             return decorator
 
 
 app = FastAPI()
 
 
 @app.get("/")
 def root():
     return {"message": "hello"}
+
+
+@app.get("/health")
+def health():
+    return {"status": "ok"}
diff --git a/tests/test_main.py b/tests/test_main.py
--- a/tests/test_main.py
+++ b/tests/test_main.py
@@ -1,2 +1,8 @@
 def test_placeholder():
     assert True
+
+
+def test_health_shape():
+    from app.main import health
+
+    assert health() == {"status": "ok"}
"""

    prompt = f"""
Requirement:
{requirement}

Implementation plan:
{plan}

Framework:
{framework}

Repository context:
{context}

Generate ONLY a valid unified git diff.

Rules:
- Output ONLY unified diff text
- No markdown fences
- No explanations
- Include tests if required
- Keep changes minimal
- Follow existing project conventions
- Do not rewrite unrelated code
- Preserve formatting style
"""

    response = chat(
        system=(
            "You are a senior Python engineer. "
            "Return ONLY valid unified git diff output."
        ),
        user=prompt,
        temperature=0.05,
    )

    cleaned = response.strip()

    if cleaned.startswith("```"):
        cleaned = cleaned.replace("```diff", "")
        cleaned = cleaned.replace("```", "")
        cleaned = cleaned.strip()

    return cleaned