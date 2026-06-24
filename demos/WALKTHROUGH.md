# Demo Walkthrough — Cyber AI Project Template

**Pattern:** Shared Scaffold  
**Captured:** 2026-06-24 with `USE_MOCK_LLM=true` (no Docker/Ollama required)

---

## Prerequisites

```bash
cp .env.example .env   # optional for mock demo
pip install -r requirements.txt
```

---

## Step 1 — One-command demo

```bash
export USE_MOCK_LLM=true
python scripts/run_demo.py
```

This runs the same FastAPI `TestClient` path as CI — real code, real JSON output.

### Step 2 — Health & metrics

```bash
curl http://localhost:8080/health
curl http://localhost:8080/metrics
```

**Captured `/health` response:**

```json
{
  "status": "ok"
}
```

**Metrics excerpt:**

```
# HELP cyber_ai_up Application is running
# TYPE cyber_ai_up gauge
cyber_ai_up 1
# HELP cyber_ai_http_requests_total Total HTTP requests (stub)
# TYPE cyber_ai_http_requests_total counter
cyber_ai_http_requests_total{endpoint="health"} 0
```

### Step 3 — LLM factory smoke test

The template ships `create_chat_model()` with Ollama/OpenAI/Gemini providers. CI uses mocked Ollama:

```json
{
  "llm_provider": "ollama",
  "llm_sample": "Portfolio template: shared LLM factory and Docker scaffold for security AI repos."
}
```

---

## Architecture callout (2-min video)

> Shared scaffold: LLM factory (Ollama/OpenAI/Gemini/Mock), Docker Compose stack, Prometheus metrics — foundation for 10 derived security repos.

Highlight in your recording:

1. **Problem → pattern** — why this agent architecture fits the security domain
2. **Tool/trace output** — show structured JSON, not just the final answer
3. **`docs/architecture.md`** — Mermaid diagram for the close

---

## Artifacts

| File | Description |
|------|-------------|
| [`demos/captured/request.json`](captured/request.json) | API request payload |
| [`demos/captured/response.json`](captured/response.json) | Live captured response |
| [`demos/captured/trace.json`](captured/trace.json) | Agent trace array |
| [`demos/captured/terminal-session.txt`](captured/terminal-session.txt) | Terminal replay for Loom |

---

## Record your video

```bash
python scripts/run_demo.py
```

Use [`demos/RECORDING_SCRIPT.md`](RECORDING_SCRIPT.md) for shot list and narration cues.
