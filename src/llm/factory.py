"""LLM factory — Ollama-first with optional OpenAI and Gemini providers."""

from __future__ import annotations

import os
from enum import StrEnum
from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel


class LLMProvider(StrEnum):
    """Supported LLM backends."""

    OLLAMA = "ollama"
    OPENAI = "openai"
    GEMINI = "gemini"


def get_llm_provider() -> LLMProvider:
    """Parse LLM_PROVIDER from environment (default: ollama)."""
    raw = os.getenv("LLM_PROVIDER", "ollama").strip().lower()
    try:
        return LLMProvider(raw)
    except ValueError as exc:
        supported = ", ".join(p.value for p in LLMProvider)
        msg = f"Invalid LLM_PROVIDER={raw!r}. Supported: {supported}"
        raise ValueError(msg) from exc


def _require_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        msg = f"{name} is required when using the selected LLM provider."
        raise ValueError(msg)
    return value


def create_chat_model(**kwargs: Any) -> BaseChatModel:
    """Return a LangChain chat model based on LLM_PROVIDER env configuration.

    Environment variables:
        LLM_PROVIDER: ollama | openai | gemini (default: ollama)
        OLLAMA_BASE_URL: Ollama API base (default: http://localhost:11434)
        OLLAMA_MODEL: Ollama model tag (default: llama3.2)
        OPENAI_API_KEY, OPENAI_MODEL: Required for openai provider
        GOOGLE_API_KEY, GEMINI_MODEL: Required for gemini provider
    """
    provider = get_llm_provider()
    temperature = kwargs.pop("temperature", float(os.getenv("LLM_TEMPERATURE", "0.2")))

    if provider is LLMProvider.OLLAMA:
        from langchain_ollama import ChatOllama

        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        model = os.getenv("OLLAMA_MODEL", "llama3.2")
        return ChatOllama(
            base_url=base_url,
            model=model,
            temperature=temperature,
            **kwargs,
        )

    if provider is LLMProvider.OPENAI:
        from langchain_community.chat_models.openai import ChatOpenAI

        api_key = _require_env("OPENAI_API_KEY")
        model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        return ChatOpenAI(
            api_key=api_key,
            model=model,
            temperature=temperature,
            **kwargs,
        )

    if provider is LLMProvider.GEMINI:
        from langchain_google_genai import ChatGoogleGenerativeAI

        api_key = _require_env("GOOGLE_API_KEY")
        model = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
        return ChatGoogleGenerativeAI(
            google_api_key=api_key,
            model=model,
            temperature=temperature,
            **kwargs,
        )

    # Exhaustive guard for new enum members
    raise AssertionError(f"Unhandled provider: {provider}")
