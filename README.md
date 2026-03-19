<div align="center">


🎓 AI Study Assistant

A conversational AI-powered study tool with multiple teaching personalities, 
multi-turn memory, and configurable generation settings — built with Google Gemini.

Python 
Gemini 
License: MIT 
Tests

</div>

⸻
🎯 Problem Statement

Students often get stuck on difficult concepts late at night when tutors aren't available. 
Generic search results are either too shallow or too technical. This project provides an 
AI study companion that adapts its teaching style to your learning preference — from 
casual and friendly to rigorous and academic — and remembers the context of your conversation 
so you can ask follow-up questions naturally.
⸻
✨ Features
Feature	Description
🧠 4 Teaching Personalities	Friendly, Academic, Socratic, ELI5
💬 Multi-turn Conversation	Remembers context across follow-up questions
🎛️ Configurable Generation	Control temperature and response length
🔀 Live Persona Switching	Switch teaching styles mid-session
🔒 Secure API Handling	API keys via .env, never hardcoded
🧪 Unit Tested	Mocked tests that run without an API key
⸻
🛠️ Tech Stack
Layer	Technology
Language	Python 3.10+
AI Model	Google Gemini 2.5 Flash
AI SDK	google-genai
Config Management	python-dotenv
Testing	pytest + unittest.mock
⸻
📁 Project Structure

ai-study-assistant/
├── src/
│   ├── __init__.py
│   ├── assistant.py       # Core AI logic & multi-turn conversation
│   └── config.py          # Personalities, defaults, model settings
├── tests/
│   ├── __init__.py
│   └── test_assistant.py  # Unit tests (no API key needed)
├── main.py                # CLI entry point
├── .env.example           # Environment variable template
├── .gitignore
├── requirements.txt
├── CONTRIBUTING.md
├── LICENSE
└── README.md

⸻
🚀 Getting Started

Prerequisites
- Python 3.10 or higher
- A free Google Gemini API key → Get one here

Installation

# 1. Clone the repository
git clone https://github.com/harshsingh-developer/ai-study-assistant.git
cd ai-study-assistant

# 2. Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your API key
cp .env.example .env
# Open .env and replace 'your_gemini_api_key_here' with your actual key


Running the Assistant

python main.py


You'll be prompted to choose a personality and response style, then you can start asking questions.
⸻
💻 Usage Example


   🎓  AI Study Assistant  🎓


  Choose Your Study Assistant
  1. Friendly
  2. Academic
  3. Socratic
  4. ELI5

Enter number (default = 1): 1
Response Style: 2 (Balanced)

✅ Assistant ready | Persona: Friendly | Temp: 0.4

📚 You: What are Large Language Models?

🤖 Assistant: Great question! Think of a Large Language Model (LLM)
like a super-reader who has read billions of books, articles, and websites...
[continues]

📚 You: How are they trained?
🤖 Assistant: Building on what we just covered — training is how the model
"learns" all that reading...

⸻
🧪 Running Tests

Tests use mocking — no API key required.

pytest tests/ -v


Expected output:
tests/test_assistant.py::TestPersonaValidation::test_valid_persona_friendly    PASSED
tests/test_assistant.py::TestPersonaValidation::test_invalid_persona_raises    PASSED
tests/test_assistant.py::TestConversationHistory::test_multi_turn_accumulates  PASSED
...

⸻
🗺️ Future Improvements

- [ ] Web interface using Streamlit or Flask
- [ ] Save and export conversation history to PDF
- [ ] Add a "Quiz Me" mode that generates practice questions
- [ ] Support for uploading study notes (PDF/text) as context
- [ ] Voice input/output integration
- [ ] Dockerize for one-command deployment
⸻
📐 Architecture

User Input
    │
    ▼
main.py (CLI Layer)
    │  ── selects persona, temperature
    ▼
src/assistant.py (Core Logic)
    │  ── builds conversation history
    │  ── constructs prompt with context
    ▼
Google Gemini API
    │  ── system_instruction (persona)
    │  ── temperature, max_output_tokens
    ▼
Response → returned + history updated

⸻
🤝 Contributing

Contributions are welcome! See CONTRIBUTING.md for guidelines. 
Adding a new personality is as simple as adding one entry to src/config.py.
⸻
📄 License

Distributed under the MIT License. See LICENSE for details.
⸻
<div align="center">
  Built with ❤️ by <a href="https://github.com/harshsingh-developer">Your Harsh Singh</a>
  <br/>
  <sub>⭐ Star this repo if it helped you!</sub>
</div>
