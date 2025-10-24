
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objetivo

Build a command-line Hangman game where students practise string manipulation, loops and conditionals by letting a player guess letters to reveal a hidden word before running out of attempts.

## 📝 Tarefas

### 🛠️	Build the Hangman Game

#### Description
Create a playable Hangman program in Python. The game should run in the terminal, accept single-letter guesses from the player, and show the current word progress and number of remaining incorrect attempts.

#### Requirements
Completed program should:

- Randomly select words from a predefined list (at least 10 words).
- Accept letter guesses and display the current progress in the `_ _ _` format (hidden letters shown as underscores).
- Track and display the number of incorrect guesses remaining (suggested default: 6 attempts).
- End the game when the word is fully guessed or when attempts are exhausted.
- Display a clear win or lose message including the correct word when the game ends.

#### Example input / output
```
Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: e
Good guess! Word: _ e _ _ _
Incorrect guesses left: 6
Guess a letter: x
Sorry, no 'x'. Incorrect guesses left: 5
...
You win! The word was 'apple'.
```

> Notes: Keep prompts and messages student-friendly. You can include optional features (score tracking, hint system, reading words from a file) but do not remove any required behavior above.
