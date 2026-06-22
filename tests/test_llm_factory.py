"""Tests for LLM factory env parsing and model construction (mocked)."""

from unittest.mock import MagicMock, patch

import pytest

from src.llm.factory import LLMProvider, create_chat_model, get_llm_provider


class TestGetLLMProvider:
    def test_defaults_to_ollama(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.delenv("LLM_PROVIDER", raising=False)
        assert get_llm_provider() is LLMProvider.OLLAMA

    def test_parses_ollama(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLM_PROVIDER", "ollama")
        assert get_llm_provider() is LLMProvider.OLLAMA

    def test_parses_openai(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLM_PROVIDER", "openai")
        assert get_llm_provider() is LLMProvider.OPENAI

    def test_parses_gemini(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLM_PROVIDER", "gemini")
        assert get_llm_provider() is LLMProvider.GEMINI

    def test_strips_and_lowercases(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLM_PROVIDER", "  OPENAI  ")
        assert get_llm_provider() is LLMProvider.OPENAI

    def test_invalid_provider_raises(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLM_PROVIDER", "anthropic")
        with pytest.raises(ValueError, match="Invalid LLM_PROVIDER"):
            get_llm_provider()


class TestCreateChatModel:
    @patch("langchain_ollama.ChatOllama")
    def test_creates_ollama_with_defaults(
        self,
        mock_chat_ollama: MagicMock,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setenv("LLM_PROVIDER", "ollama")
        monkeypatch.delenv("OLLAMA_BASE_URL", raising=False)
        monkeypatch.delenv("OLLAMA_MODEL", raising=False)
        monkeypatch.delenv("LLM_TEMPERATURE", raising=False)
        mock_instance = MagicMock()
        mock_chat_ollama.return_value = mock_instance

        result = create_chat_model()

        mock_chat_ollama.assert_called_once_with(
            base_url="http://localhost:11434",
            model="llama3.2",
            temperature=0.2,
        )
        assert result is mock_instance

    @patch("langchain_ollama.ChatOllama")
    def test_creates_ollama_with_custom_env(
        self,
        mock_chat_ollama: MagicMock,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setenv("LLM_PROVIDER", "ollama")
        monkeypatch.setenv("OLLAMA_BASE_URL", "http://ollama:11434")
        monkeypatch.setenv("OLLAMA_MODEL", "llama3.2")
        monkeypatch.setenv("LLM_TEMPERATURE", "0.5")

        create_chat_model()

        mock_chat_ollama.assert_called_once_with(
            base_url="http://ollama:11434",
            model="llama3.2",
            temperature=0.5,
        )

    @patch("langchain_community.chat_models.openai.ChatOpenAI")
    def test_creates_openai(
        self,
        mock_chat_openai: MagicMock,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setenv("LLM_PROVIDER", "openai")
        monkeypatch.setenv("OPENAI_API_KEY", "sk-test-key")
        monkeypatch.setenv("OPENAI_MODEL", "gpt-4o-mini")

        create_chat_model(temperature=0.1)

        mock_chat_openai.assert_called_once_with(
            api_key="sk-test-key",
            model="gpt-4o-mini",
            temperature=0.1,
        )

    def test_openai_missing_api_key_raises(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLM_PROVIDER", "openai")
        monkeypatch.delenv("OPENAI_API_KEY", raising=False)

        with pytest.raises(ValueError, match="OPENAI_API_KEY"):
            create_chat_model()

    @patch("langchain_google_genai.ChatGoogleGenerativeAI")
    def test_creates_gemini(
        self,
        mock_chat_gemini: MagicMock,
        monkeypatch: pytest.MonkeyPatch,
    ) -> None:
        monkeypatch.setenv("LLM_PROVIDER", "gemini")
        monkeypatch.setenv("GOOGLE_API_KEY", "gemini-test-key")
        monkeypatch.setenv("GEMINI_MODEL", "gemini-2.0-flash")

        create_chat_model()

        mock_chat_gemini.assert_called_once_with(
            google_api_key="gemini-test-key",
            model="gemini-2.0-flash",
            temperature=0.2,
        )

    def test_gemini_missing_api_key_raises(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setenv("LLM_PROVIDER", "gemini")
        monkeypatch.delenv("GOOGLE_API_KEY", raising=False)

        with pytest.raises(ValueError, match="GOOGLE_API_KEY"):
            create_chat_model()
