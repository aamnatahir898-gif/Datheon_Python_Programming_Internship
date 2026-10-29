# Hangman Word Guessing Game 🎮

A simple, interactive, terminal-based Hangman game built with Python 3. Guess the hidden English word one letter at a time. You have 6 incorrect guesses to figure out the word before the game ends.

## ✨ Features

-  Random word selection using `random.choice()`
-  ASCII Hangman drawing with 7 stages
-  Hidden word displayed using underscores
-  Correct guesses reveal matching letters
-  Maximum of 6 incorrect guesses per round
-  Repeated guesses do not count as incorrect attempts
-  Input validation for empty input, numbers, symbols, and multiple characters
-  Separate victory and defeat screens
-  Option to play again after each round
-  Loads words from `words.txt`
-  Uses a built-in fallback word list if `words.txt` is missing or empty

## 📁 Project Structure

```text
Hangman-Game/
│
├── hangman.py    # Main game logic
├── words.txt     # English word list
└── README.md     # Project documentation
```

##  Requirements

- Python 3.x
- No external libraries required

The game uses Python's built-in `random` and `os` modules.

##  Installation and Setup

### 1. Install Python

Download and install Python 3 from the official website:

https://www.python.org/downloads/

### 2. Download the Project

Clone the repository using Git:

```bash
git clone YOUR_REPOSITORY_URL
```

Alternatively, download the project as a ZIP file from GitHub and extract it.

### 3. Open the Project Folder

Open a terminal or Command Prompt in the folder containing `hangman.py`.

### 4. Run the Game

Execute the following command:

```bash
python hangman.py
```

On Windows, you can also use:

```bash
py hangman.py
```

##  How to Play

1. Start the game using the command provided above.
2. The game selects a random word and displays it with hidden letters.

   **Example:**

   ```text
   _ A _ _ E
   ```

3. Enter one letter and press Enter. Uppercase and lowercase letters are both accepted.
4. If the letter is correct, it is revealed in every matching position.
5. If the letter is incorrect, one part is added to the Hangman drawing.
6. Guess the complete word before making 6 incorrect guesses to win.
7. If all 6 incorrect guesses are used, the game ends and reveals the hidden word.
8. After each round, enter `y` to play again or `n` to exit.

**Note:** Invalid input and previously guessed letters do not reduce the remaining attempts.

## 🧩 Code Structure

| Function | Description |
|---|---|
| `load_words()` | Reads and cleans words from `words.txt`. |
| `get_word_list()` | Returns words from the file or uses a fallback list. |
| `get_masked_word()` | Creates the hidden-word display. |
| `get_valid_guess()` | Accepts and validates a single-letter guess. |
| `show_status()` | Displays the Hangman drawing, word, guessed letters, and remaining attempts. |
| `play_round()` | Runs one complete round of the game. |
| `show_victory()` | Displays the winning message. |
| `show_defeat()` | Displays the losing message. |
| `ask_play_again()` | Asks the player whether to start another round. |
| `main()` | Starts the game and manages replay. |

##  Technologies Used

- **Programming Language:** Python 3
- **Modules:** `random`, `os`
- **Core Concepts:**
  - Functions and modular programming
  - Loops and conditional statements
  - Sets and string manipulation
  - User input validation
  - File handling
  - Random selection

##  Learning Objectives

This project demonstrates the practical use of Python fundamentals, including:

- Organizing code into reusable functions
- Managing user input and game state
- Working with sets to track guessed letters
- Reading data from text files
- Handling missing or empty input files
- Implementing game logic with loops and conditions

---

**Enjoy the game, and good luck guessing the word! **
