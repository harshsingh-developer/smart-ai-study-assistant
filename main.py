"""
AI Study Assistant — CLI Entry Point
=====================================
Run this file to start an interactive study session.

Usage:
    python main.py

Environment Variables Required:
    GEMINI_API_KEY — Your Google Gemini API key.
    (Set this in a .env file; see .env.example)
"""

import os
from dotenv import load_dotenv

from src.assistant import study_assistant, create_client
from src.config import PERSONALITIES, TEMPERATURE_PRESETS

# Load API key from .env file
load_dotenv()


def select_persona() -> str:
    """Prompt user to select a personality and return the key."""
    personas = list(PERSONALITIES.keys())
    print("\n┌─────────────────────────────────┐")
    print("│   Choose Your Study Assistant   │")
    print("└─────────────────────────────────┘")
    for i, name in enumerate(personas, start=1):
        print(f"  {i}. {name}")

    while True:
        choice = input("\nEnter number (default = 1): ").strip() or "1"
        if choice.isdigit() and 1 <= int(choice) <= len(personas):
            return personas[int(choice) - 1]
        print("  Invalid choice. Please enter a valid number.")


def select_temperature() -> float:
    """Prompt user to select temperature preset."""
    print("\n┌──────────────────────────────────────┐")
    print("│   Response Style (Temperature)       │")
    print("└──────────────────────────────────────┘")
    for i, (name, val) in enumerate(TEMPERATURE_PRESETS.items(), start=1):
        print(f"  {i}. {name.capitalize():<18} (temp = {val})")

    while True:
        choice = input("\nEnter number (default = 2 — Balanced): ").strip() or "2"
        keys = list(TEMPERATURE_PRESETS.keys())
        if choice.isdigit() and 1 <= int(choice) <= len(keys):
            return TEMPERATURE_PRESETS[keys[int(choice) - 1]]
        print("  Invalid choice. Please enter a valid number.")


def run_session() -> None:
    """Main interactive session loop."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY not found. "
            "Create a .env file with: GEMINI_API_KEY=your_key_here"
        )

    client = create_client(api_key)

    print("\n" + "=" * 45)
    print("   🎓  AI Study Assistant  🎓")
    print("=" * 45)
    print("  Type 'quit' or 'exit' to end the session.")
    print("  Type 'reset' to start a new conversation.")
    print("  Type 'switch' to change persona.\n")

    persona = select_persona()
    temperature = select_temperature()
    conversation_history: list[dict] = []

    print(f"\n✅ Assistant ready | Persona: {persona} | Temp: {temperature}")
    print("-" * 45)

    while True:
        try:
            user_input = input("\n📚 You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ("quit", "exit"):
                print("\n👋 Good luck with your studies! Goodbye.\n")
                break

            if user_input.lower() == "reset":
                conversation_history = []
                print("🔄 Conversation history cleared.")
                continue

            if user_input.lower() == "switch":
                persona = select_persona()
                conversation_history = []
                print(f"🔀 Switched to '{persona}'. History cleared.")
                continue

            print("\n🤖 Assistant: ", end="", flush=True)
            response, conversation_history = study_assistant(
                client=client,
                question=user_input,
                persona=persona,
                conversation_history=conversation_history,
                temperature=temperature,
            )
            print(response)

        except ValueError as e:
            print(f"\n⚠️  Configuration error: {e}")
        except KeyboardInterrupt:
            print("\n\n👋 Session interrupted. Goodbye!\n")
            break
        except Exception as e:
            print(f"\n❌ API Error: {e}")
            print("   If this is a rate limit error, wait a moment and try again.")


if __name__ == "__main__":
    run_session()