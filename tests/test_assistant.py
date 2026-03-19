"""
Unit Tests — AI Study Assistant
================================
Tests core logic without making real API calls.
Uses unittest.mock to isolate the Gemini client.

Run with:
    pytest tests/ -v
"""

import pytest
from unittest.mock import MagicMock
from src.assistant import study_assistant
from src.config import PERSONALITIES


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def mock_client():
    """Return a mock Gemini client whose generate_content returns dummy text."""
    client = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "This is a mocked response."
    client.models.generate_content.return_value = mock_response
    return client


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestPersonaValidation:
    def test_valid_persona_friendly(self, mock_client):
        response, _ = study_assistant(mock_client, "What is AI?", "Friendly")
        assert isinstance(response, str)

    def test_valid_persona_academic(self, mock_client):
        response, _ = study_assistant(mock_client, "Explain neural nets", "Academic")
        assert isinstance(response, str)

    def test_invalid_persona_raises_value_error(self, mock_client):
        with pytest.raises(ValueError, match="Unknown persona"):
            study_assistant(mock_client, "Hello", "InvalidPersona")


class TestConversationHistory:
    def test_initial_history_is_none(self, mock_client):
        _, history = study_assistant(mock_client, "First question", "Friendly")
        assert len(history) == 2  # user turn + assistant turn

    def test_multi_turn_history_accumulates(self, mock_client):
        _, history = study_assistant(mock_client, "Q1", "Friendly")
        _, history = study_assistant(mock_client, "Q2", "Friendly", history)
        assert len(history) == 4  # 2 turns × 2 roles

    def test_history_roles_are_correct(self, mock_client):
        _, history = study_assistant(mock_client, "What is ML?", "Friendly")
        assert history[0]["role"] == "user"
        assert history[1]["role"] == "assistant"

    def test_history_contains_correct_question(self, mock_client):
        question = "What is gradient descent?"
        _, history = study_assistant(mock_client, question, "Friendly")
        assert history[0]["text"] == question


class TestAPICallParameters:
    def test_temperature_is_passed_to_api(self, mock_client):
        study_assistant(mock_client, "Test", "Friendly", temperature=0.9)
        call_kwargs = mock_client.models.generate_content.call_args
        config = call_kwargs.kwargs["config"]
        assert config.temperature == 0.9

    def test_max_tokens_is_passed_to_api(self, mock_client):
        study_assistant(mock_client, "Test", "Friendly", max_tokens=500)
        call_kwargs = mock_client.models.generate_content.call_args
        config = call_kwargs.kwargs["config"]
        assert config.max_output_tokens == 500

    def test_correct_system_prompt_is_used(self, mock_client):
        study_assistant(mock_client, "Test", "Academic")
        call_kwargs = mock_client.models.generate_content.call_args
        config = call_kwargs.kwargs["config"]
        assert config.system_instruction == PERSONALITIES["Academic"]


class TestReturnValues:
    def test_returns_string_response(self, mock_client):
        response, _ = study_assistant(mock_client, "Test", "Friendly")
        assert response == "This is a mocked response."

    def test_returns_list_history(self, mock_client):
        _, history = study_assistant(mock_client, "Test", "Friendly")
        assert isinstance(history, list)