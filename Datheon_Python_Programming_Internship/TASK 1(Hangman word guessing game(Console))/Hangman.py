
import os
import random

MAX_WRONG = 6
WORD_FILE = "words.txt"
MIN_WORD_LENGTH = 2
FALLBACK_WORDS = ["python", "gallows", "keyboard", "planet", "guitar",
                  "window", "bridge", "coffee", "rocket", "garden"]

GALLOWS = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========""",
]


def load_words(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, filename)
    try:
        with open(path, "r", encoding="utf-8") as file:
            words = []
            for line in file:
                word = line.strip().lower()
                if word.isalpha() and word.isascii() and len(word) >= MIN_WORD_LENGTH:
                    words.append(word)
            return words
    except OSError:
        return []


def get_word_list():
    words = load_words(WORD_FILE)
    if not words:
        print(f"Note: could not use '{WORD_FILE}' (missing or empty). "
              "Using the built-in word list instead.")
        words = FALLBACK_WORDS
    return words


def get_masked_word(secret_word, guessed_letters):
    shown = []
    for letter in secret_word:
        shown.append(letter.upper() if letter in guessed_letters else "_")
    return " ".join(shown)


def get_valid_guess():
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1:
            print("Please enter exactly ONE letter.")
        elif not (guess.isalpha() and guess.isascii()):
            print("Only letters A-Z are allowed.")
        else:
            return guess


def show_status(secret_word, guessed_letters, wrong_count):
    print(GALLOWS[wrong_count])
    print("\nWord:", get_masked_word(secret_word, guessed_letters))
    if guessed_letters:
        print("Guessed letters:", " ".join(sorted(guessed_letters)).upper())
    print(f"Wrong guesses: {wrong_count}/{MAX_WRONG}  "
          f"(attempts left: {MAX_WRONG - wrong_count})\n")


def play_round(secret_word):
    guessed_letters = set()
    wrong_count = 0
    print("\nI have picked a word with", len(secret_word), "letters. Good luck!")

    while wrong_count < MAX_WRONG:
        show_status(secret_word, guessed_letters, wrong_count)

        if all(letter in guessed_letters for letter in secret_word):
            break

        guess = get_valid_guess()

        if guess in guessed_letters:
            print(f"You already guessed '{guess.upper()}'. No penalty - try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Good job! '{guess.upper()}' is in the word.")
        else:
            wrong_count += 1
            print(f"Sorry, '{guess.upper()}' is not in the word.")

    won = all(letter in guessed_letters for letter in secret_word)
    if won:
        show_victory(secret_word)
    else:
        show_defeat(secret_word, wrong_count)
    return won


def show_victory(secret_word):
    print("=" * 40)
    print("    VICTORY! YOU SAVED HIM! ")
    print(f"   The word was: {secret_word.upper()}")
    print("=" * 40)


def show_defeat(secret_word, wrong_count):
    print(GALLOWS[wrong_count])
    print("=" * 40)
    print("   GAME OVER - YOU LOST ")
    print(f"   The word was: {secret_word.upper()}")
    print("=" * 40)


def ask_play_again():
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type 'y' or 'n'.")


def main():
    print("=" * 40)
    print("        HANGMAN - GUESS THE WORD")
    print("=" * 40)
    words = get_word_list()

    while True:
        secret_word = random.choice(words)
        play_round(secret_word)
        if not ask_play_again():
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame closed. Goodbye!")