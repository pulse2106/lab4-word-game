# Lab 4 - Word Game

A terminal-based Python word guessing game inspired by Hangman.

The project includes:
- A manual mode where the player guesses letters.
- An auto-play mode where the game picks random letters.
- Unit tests for core logic and output behavior.

## Features

- Random secret phrase selection from a predefined list.
- Input validation for guesses (single, unused letter).
- Lives system (6 lives per round).
- Win detection using Python's `all()` function.
- Replay support.

## Project Structure

- `main.py`: Main game logic and game loops.
- `test_main.py`: Automated tests using `pytest`.
- `REPORT.md`: Reflection on development and Copilot usage.
- `MY_NOTES.md`: Design notes and early planning.

## Requirements

- Python 3.10 or newer

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Game

```bash
python main.py
```

You will be prompted to choose auto mode or manual mode.

## Run Tests

```bash
pytest -q
```

## Notes

- The game currently uses a static in-code word list.
- Input and output are terminal-based (`input()` and `print()`).
