import json
from openai import OpenAI
from ai_dev_agent.config import settings

def chat(system: str, user: str, temperature: float = 0.1) -> str:
    if not settings.openai_api_key:
        raise RuntimeError("OPENAI_API_KEY is missing. Use --mock-ai for local testing.")
    client = OpenAI(api_key=settings.openai_api_key)
    response = client.chat.completions.create(
        model=settings.openai_model,
        messages=[{"role": "system", "content": system}, {"role": "user", "content": user}],
        temperature=temperature,
    )
    return response.choices[0].message.content or ""

def parse_json(text: str) -> dict:
    s = text.strip()
    if s.startswith("```"):
        s = s.strip("`")
        s = s.replace("json\n", "", 1)
    return json.loads(s)
