# My Original Thinking
- *Write down thoughts on the game, your original thoughts*
    ## States of the game
        - the start (an empty word with dashes signifying the number of letters)
        - guessing state
        - completed with the previous guesses listed and final word guessed + secret word(if user failed)
    ## Variables
        - the secret word(stored in a string or tuple)
        - number of lives allowed (fixed string)
        - previous guesses (stored in a list etc.)
    ## Rules and Invariants
        - failures should not be greater than the number of lives, limiter
        - number of lives should not change
        - should support double letter words
    ## Bugs and Edge Cases 
        - repeating letters
        - 

# CoPilot Suggestions
- Copilot Thoughts
    ## States of the game
    - A clean Hangman-style game usually needs these core states:
        ### Setup
            - Choose/load secret word
            - Initialize lives, guessed letters, and masked word
        ### Playing (Guess Loop)
            - Player enters a guess
            - Validate input (single letter, not already guessed, alphabetic)
            - Update game data:
            - correct guess: reveal letters
            - wrong guess: reduce lives
            - Stay in this state until a terminal condition is reached
        ### Won
            - All letters revealed
            - Show final word and summary of guesses
        ### Lost
            - Lives reached zero
            - Reveal secret word and summary of guesses
            - End/Replay Decision
            - Ask to play again or quit
            - Transition to Setup (replay) or Exit
        ### Useful optional states:
            - Invalid Input Feedback
            - Brief state to show why input was rejected, then return to Playing
            - Paused (if needed)
            - For menu/help/settings mid-game
    ## Variables
    - secret_word
    - guessed_letters
    - mistakes
    - max_lives
    - game_state