import random
import string


def update_game_state(
    secret_word: str, guessed_letters: list[str], guess: str, lives: int
) -> tuple[list[str], int]:
    # Store the player's guess and update lives only if the guess is wrong.
    if guess in secret_word:
        guessed_letters.append(guess)
        print(f"Correct {guess} is in the word")
        return guessed_letters, lives
    else:
        guessed_letters.append(guess)
        lives = lives - 1
        print(f"Letter {guess} is not in the word, You have {lives} lives remaining")
        return guessed_letters, lives


def word_to_guess(secret_word: str):
    # Print the hidden word as underscores, but keep spaces visible.
    for char in secret_word:
        if char == " ":
            print(" ", end=" ")
        else:
            print("_", end=" ")
    print()


def decrypt_guess_word(guess_letters: list, secret_word: str):
    # Reveal only the letters that have already been guessed.
    for char in secret_word:
        if char in guess_letters:
            print(char, end=" ")
        elif char == " ":
            print(" ", end=" ")
        else:
            print("_", end=" ")
    print()


def letters_available(guess_letters: list):
    # Show the alphabet letters that the player has not used yet.
    letters = string.ascii_uppercase
    available = [letter for letter in letters if letter not in guess_letters]
    print("You can use letters: " + ", ".join(available))


def play_again():
    # Return True when the player wants another round.
    response = input("Do you want to play again(y/n): ").upper()
    return response == "Y"


def play_game():
    game_state = input("start_playing?(y/n): ").upper()
    secret_word_list = [
        "Fruits Ninja",
        "Apple Pie",
        "Banana Split",
        "Cherry Blossom",
        "Dragon Fruit",
        "Golden Mango",
        "Purple Grape",
        "Juicy Orange",
        "Lemon Tart",
        "Coconut Water",
        "Pineapple Juice",
        "Watermelon Slice",
        "Strawberry Jam",
        "Blueberry Muffin",
        "Raspberry Cake",
        "Peach Smoothie",
        "Kiwi Delight",
        "Papaya Salad",
        "Avocado Toast",
        "Guava Nectar",
        "Lychee Dream",
        "Passion Fruit",
        "Melon Sorbet",
        "Apricot Jam",
        "Plum Pudding",
        "Blackberry Pie",
        "Cranberry Sauce",
        "Fig Newton",
        "Date Palm",
        "Pomegranate Seeds",
        "Vanilla Icecream",
        "Chocolate Cookie",
        "Caramel Candy",
        "Peanut Butter",
        "Hazelnut Spread",
        "Almond Milk",
        "Cashew Cream",
        "Walnut Brownie",
        "Pistachio Cake",
        "Cinnamon Roll",
        "Sugar Cookie",
        "Honey Biscuit",
        "Maple Syrup",
        "Ginger Bread",
        "Mint Chocolate",
        "Coffee Beans",
        "Iced Latte",
        "Green Tea",
        "Milk Shake",
        "Cheese Burger",
        "French Fries",
        "Chicken Nuggets",
        "Tomato Soup",
        "Mushroom Pasta",
        "Garlic Bread",
        "Fried Rice",
        "Spicy Noodles",
        "Veggie Pizza",
        "Beef Tacos",
        "Fish Curry",
        "Potato Chips",
        "Onion Rings",
        "Grilled Cheese",
        "Caesar Salad",
        "Pumpkin Soup",
        "Corn Bread",
        "Sushi Roll",
        "Dumpling House",
        "Pancake Stack",
        "Waffle Cone",
        "Biscuit Gravy",
        "Turkey Sandwich",
        "Ham Omelette",
        "Egg Fried Rice",
        "Chili Pepper",
        "Rainbow Candy",
        "Cotton Candy",
        "Jelly Beans",
        "Popcorn Bucket",
        "Movie Night",
        "Sunny Beach",
        "Mountain Trail",
        "Forest Cabin",
        "River Stone",
        "Desert Wind",
        "Winter Snow",
        "Autumn Leaves",
        "Spring Garden",
        "Summer Picnic",
        "City Lights",
        "Neon Street",
        "Moon Light",
        "Star Dust",
        "Cloud Nine",
        "Thunder Storm",
        "Silent Night",
        "Happy Birthday",
        "Treasure Hunt",
        "Hidden Temple",
        "Pirate Island",
        "Space Rocket",
        "Galaxy Quest",
        "Robot Dance",
        "Magic Spell",
        "Ancient Castle",
        "Brave Knight",
        "Dark Forest",
        "Golden Crown",
        "Crystal Cave",
        "Secret Tunnel",
        "Time Machine",
        "Future World",
        "Mystery Box",
        "Lucky Charm",
        "Final Level",
    ]
    # A space is included so multi-word phrases display correctly from the start.
    guess_letters = [" "]
    lives = 6
    secret_word = random.choice(secret_word_list).upper()
    word_to_guess(secret_word)
    while game_state == "Y":
        guess = input("Guess a letter: ").upper()
        # A valid guess must be one unused letter from A-Z.
        if (
            (guess not in string.ascii_uppercase)
            or (guess in guess_letters)
            or (len(guess) > 1)
        ):
            print("This is an invalid guess")
            decrypt_guess_word(guess_letters, secret_word)
            letters_available(guess_letters)
        else:
            guess_letters, lives = update_game_state(
                secret_word, guess_letters, guess, lives
            )
            decrypt_guess_word(guess_letters, secret_word)
            letters_available(guess_letters)
            # The player wins when every non-space character is already in guessed_letters.
            if all(ch == " " or ch in guess_letters for ch in secret_word):
                print("You have won")
                if play_again():
                    play_game()
                else:
                    game_state = "N"
                    break
            if lives > 0:
                continue
            else:
                print(f"You have {lives} lives left, GAME OVER")
                print(f"The word was {secret_word}")
                if play_again():
                    play_game()
                else:
                    game_state = "N"
                    break


def main():
    play = True
    # Keep starting new rounds until the player refuses to continue.
    while play:
        play_game()
        if not play_again():
            play = False
            break


main()
