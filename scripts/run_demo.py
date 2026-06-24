#!/usr/bin/env python3
"""One-command demo runner for screen recording (mock LLM, no Docker/Ollama)."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# Ensure project root is on PYTHONPATH when run as `python scripts/run_demo.py`
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

# ANSI colors for terminal recording
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def banner(text: str) -> None:
    print(f"\n{BOLD}{CYAN}{text}{RESET}")
    print(f"{DIM}{'=' * min(len(text), 60)}{RESET}")


def section(title: str) -> None:
    print(f"\n{BOLD}{YELLOW}▸ {title}{RESET}")


def main() -> int:
    os.environ.setdefault("USE_MOCK_LLM", "true")
    os.environ.setdefault("LLM_PROVIDER", "mock")

    banner("Cyber AI Project Template")
    print(f"{DIM}Pattern: Shared Scaffold · USE_MOCK_LLM=true (no Ollama/Docker required){RESET}\n")
    section("Health check")
    from fastapi.testclient import TestClient
    from src.api.main import app

    client = TestClient(app)
    health = client.get("/health")
    print(f"  GET /health → {{GREEN}}{health.status_code}{{RESET}}")
    print(json.dumps(health.json(), indent=2))

    section("Prometheus metrics (excerpt)")
    metrics = client.get("/metrics").text.strip().split("\n")[:6]
    for line in metrics:
        print(f"  {{DIM}}{{line}}{{RESET}}")

    section("LLM factory (mocked Ollama in CI)")
    from unittest.mock import MagicMock, patch
    from src.llm.factory import create_chat_model, get_llm_provider

    mock_llm = MagicMock()
    mock_llm.invoke.return_value = MagicMock(
        content="Portfolio template: shared LLM factory and Docker scaffold for security AI repos."
    )
    with patch("langchain_ollama.ChatOllama", return_value=mock_llm):
        llm = create_chat_model()
        out = llm.invoke("Summarize portfolio template purpose in one sentence.")
    print(f"  Provider: {{get_llm_provider().value}}")
    print(f"  {{GREEN}}{{out.content}}{{RESET}}")

    section("Captured output saved to demos/captured/")
    captured = Path(__file__).resolve().parent.parent / "demos" / "captured"
    print(f"  {{DIM}}{{captured}}{{RESET}}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
