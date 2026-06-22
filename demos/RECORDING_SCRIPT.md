# Video Demo Recording Script — Cyber AI Project Template

**Target length:** 2–3 minutes  
**Audience:** Interviewers, hiring managers, security engineers  
**Host:** YouTube (unlisted) or Loom

Copy this file into each derived project and customize shot names, queries, and expected outputs.

---

## Pre-Recording Checklist

- [ ] Docker Desktop running, 16 GB RAM free if possible
- [ ] `.env` copied from `.env.example`
- [ ] Terminal font size 14–16pt, dark theme
- [ ] Browser zoom 110% for Streamlit/API demos
- [ ] Close notifications; hide unrelated browser tabs

---

## Shot List

### Shot 1 — Hook (0:00–0:20)

**Visual:** README hero section + architecture diagram from `docs/architecture.md`

**Narration:**

> "This is [Project Name] — a [pattern] agent for [security domain]. It runs fully local with Ollama, ships synthetic demo data, and shows production-style observability."

---

### Shot 2 — One-Command Start (0:20–0:50)

**Visual:** Terminal

```bash
docker compose -f docker/docker-compose.yml up --build
```

**Narration:**

> "One command brings up the API, Ollama, and Chroma. Healthchecks pull llama3.2 automatically."

**Show:** `docker compose ps` — all services healthy.

---

### Shot 3 — Health & Metrics (0:50–1:05)

**Visual:** Browser or curl

```bash
curl http://localhost:8080/health
curl http://localhost:8080/metrics
```

**Narration:**

> "FastAPI exposes health and Prometheus metrics — same pattern across the portfolio."

---

### Shot 4 — Domain Demo Query (1:05–2:00)

**Visual:** Streamlit UI or API curl with formatted JSON output

**Action:** Run one realistic security query on bundled demo data.

**Narration:** Explain input, what the agent did (tools/retrieval), and why the output matters to a SOC/GRC/pentest team.

**Show (if applicable):**

- Tool call trace in logs or UI
- Retrieved chunks (RAG projects)
- Structured JSON findings

---

### Shot 5 — Architecture Close (2:00–2:30)

**Visual:** `docs/architecture.md` Mermaid diagram or exported slide

**Narration:**

> "Pattern: [ReAct / Supervisor / Agentic RAG / etc.]. Docs cover tradeoffs, demo data licensing, and runbook — link in the README."

---

## Post-Production

1. Upload to YouTube (unlisted) or Loom
2. Embed thumbnail + link in project `README.md`
3. Add CI badge and quickstart curl example matching the video

---

## Template-Specific Note

For the **template repo itself**, record a shorter 90-second walkthrough showing folder structure, `create_chat_model()`, and compose stack — no domain agent yet.
