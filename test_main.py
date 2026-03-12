# Generated with gemini
import pytest
from main import update_game_state, word_to_guess, decrypt_guess_word, letters_available, play_again

# --- Logic Tests ---

def test_update_game_state_correct_guess():
    # If guess is in word: lives should stay same, guess added to list
    guessed = [" "]
    new_guessed, lives = update_game_state("APPLE", guessed, "A", 6)
    assert "A" in new_guessed
    assert lives == 6

def test_update_game_state_wrong_guess():
    # If guess is NOT in word: lives should decrease
    guessed = [" "]
    new_guessed, lives = update_game_state("APPLE", guessed, "Z", 6)
    assert "Z" in new_guessed
    assert lives == 5

# --- Output/Print Tests ---

def test_word_to_guess_output(capsys):
    word_to_guess("APPLE PIE")
    captured = capsys.readouterr()
    # "APPLE PIE" -> _ _ _ _ _   _ _ _ 
    assert "_ _ _ _ _   _ _ _" in captured.out

def test_decrypt_guess_word_partial(capsys):
    decrypt_guess_word([" ", "A", "P"], "APPLE PIE")
    captured = capsys.readouterr()
    # A P P L E   P I E -> A P P _ _   P _ _
    assert "A P P _ _   P _ _" in captured.out

def test_letters_available_removes_guessed(capsys):
    letters_available(["A", "B", "C"])
    captured = capsys.readouterr()
    # Check that A, B, and C are NOT in the "available" string
    assert "A" not in captured.out[20:] # Skipping the "You can use..." prefix
    assert "D" in captured.out

# --- Input/Interaction Tests ---

def test_play_again_yes(monkeypatch):
    # Simulate user typing 'y'
    monkeypatch.setattr('builtins.input', lambda _: "y")
    assert play_again() is True

def test_play_again_no(monkeypatch):
    # Simulate user typing 'n'
    monkeypatch.setattr('builtins.input', lambda _: "n")
    assert play_again() is False

# --- Integration/Edge Case Test ---

def test_win_condition_logic():
    # Mimicking the 'all()' check in your play_game loop
    secret = "HI"
    guess_letters = [" ", "H", "I"]
    win = all(ch == " " or ch in guess_letters for ch in secret)
    assert win is True

    guess_letters_incomplete = [" ", "H"]
    win_fail = all(ch == " " or ch in guess_letters_incomplete for ch in secret)
    assert win_fail is False