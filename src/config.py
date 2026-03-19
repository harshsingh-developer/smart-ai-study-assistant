"""
Configuration
=============
Central place for all configurable constants.
Change these to customize assistant behavior without
touching business logic.
"""

# ---------------------------------------------------------------------------
# Personalities
# Each value is a system prompt passed to the Gemini model.
# Add new keys here to create additional personas.
# ---------------------------------------------------------------------------
PERSONALITIES: dict[str, str] = {
    "Friendly": (
        "You are a friendly, enthusiastic, and highly encouraging Study Assistant. "
        "Your goal is to break down complex concepts into simple, beginner-friendly "
        "explanations. Use analogies and real-world examples that beginners can "
        "relate to. Always end with a follow-up question to check understanding."
    ),
    "Academic": (
        "You are a strictly academic, highly detailed, and professional university "
        "Professor. Use precise, formal terminology and structured responses with "
        "clear sections. Break down complex concepts methodically and cite key "
        "principles. Always end with a thought-provoking question."
    ),
    "Socratic": (
        "You are a Socratic tutor. Instead of giving direct answers, guide the "
        "student to discover the answer themselves through a series of probing "
        "questions. Only confirm or correct at the very end. Keep responses concise."
    ),
    "ELI5": (
        "Explain Like I'm 5. Use the simplest possible language, fun analogies, "
        "and everyday examples a child would understand. Avoid all jargon. "
        "Keep responses short, engaging, and use emojis occasionally."
    ),
}

# ---------------------------------------------------------------------------
# Generation Defaults
# ---------------------------------------------------------------------------
DEFAULT_TEMPERATURE: float = 0.4     # Balanced accuracy + slight variation
DEFAULT_MAX_TOKENS: int = 1000       # ~3-5 paragraphs

# Temperature presets for easy reference
TEMPERATURE_PRESETS: dict[str, float] = {
    "deterministic": 0.0,   # Same output every time — best for facts/math
    "balanced": 0.4,        # General-purpose default
    "creative": 1.2,        # Varied, unexpected outputs
}

# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------
MODEL_NAME: str = "gemini-2.5-flash"