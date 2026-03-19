"""
AI Study Assistant - Core Logic
================================
A conversational AI-powered study assistant with multiple
personalities, configurable generation settings, and
multi-turn conversation memory.
"""

from google import genai
from google.genai import types
from src.config import PERSONALITIES, DEFAULT_TEMPERATURE, DEFAULT_MAX_TOKENS


def create_client(api_key: str) -> genai.Client:
    """
    Initialize and return a Gemini API client.

    Args:
        api_key: Your Gemini API key.

    Returns:
        An authenticated genai.Client instance.
    """
    return genai.Client(api_key=api_key)


def study_assistant(
    client: genai.Client,
    question: str,
    persona: str,
    conversation_history: list[dict] | None = None,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
) -> tuple[str, list[dict]]:
    """
    Generate a response from the AI Study Assistant.

    Supports multi-turn conversation by accepting and returning
    conversation history, enabling follow-up questions.

    Args:
        client:               Authenticated Gemini API client.
        question:             The user's question or input.
        persona:              Personality key from PERSONALITIES dict.
        conversation_history: List of prior turns [{"role":..., "text":...}].
        temperature:          Creativity level (0.0 = deterministic, 2.0 = creative).
        max_tokens:           Maximum tokens in the model's response.

    Returns:
        A tuple of (response_text, updated_conversation_history).

    Raises:
        ValueError: If an unsupported persona is provided.
        Exception:  Propagates API errors for the caller to handle.
    """
    if persona not in PERSONALITIES:
        raise ValueError(
            f"Unknown persona '{persona}'. "
            f"Available personas: {list(PERSONALITIES.keys())}"
        )

    # Initialize history if this is a fresh conversation
    if conversation_history is None:
        conversation_history = []

    # Append the new user message to history
    conversation_history.append({"role": "user", "text": question})

    # Build the full conversation as a structured prompt string.
    # Each prior turn is included so the model understands context.
    conversation_prompt = "\n".join(
        f"{turn['role'].capitalize()}: {turn['text']}"
        for turn in conversation_history
    )

    system_prompt = PERSONALITIES[persona]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=temperature,
            max_output_tokens=max_tokens,
        ),
        contents=conversation_prompt,
    )

    response_text = response.text

    # Append the assistant's reply to maintain conversation context
    conversation_history.append({"role": "assistant", "text": response_text})

    return response_text, conversation_history