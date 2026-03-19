# Contributing to AI Study Assistant

Thank you for considering a contribution! 🎉

## How to Contribute

1. **Fork** this repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/smart-ai-study-assistant.git`
3. **Create a branch**: `git checkout -b feature/your-feature-name`
4. **Make your changes** following the code style below
5. **Run tests**: `pytest tests/ -v`
6. **Commit**: `git commit -m "feat: describe your change"`
7. **Push**: `git push origin feature/your-feature-name`
8. **Open a Pull Request** with a clear description

## Code Style

- Follow PEP 8
- Add docstrings to all functions
- Keep functions small and single-purpose
- Write a test for any new feature

## Adding a New Personality

Add a new key-value pair to `PERSONALITIES` in `src/config.py`:
```python
"YourPersona": (
    "Your system prompt here. Be specific about tone, style, and behavior."
)
```

## Reporting Issues

Use GitHub Issues. Include:
- What you expected to happen
- What actually happened
- Steps to reproduce

## Code of Conduct

Be respectful. Constructive feedback only.