# CodeAlpha_HangmanGame

A simple text-based Hangman game built in Python as part of the CodeAlpha Python Programming internship (Task 1).

## About

The player guesses a randomly chosen word one letter at a time. Each wrong guess brings them closer to losing, and the game ends when the word is fully guessed or the wrong-guess limit is reached.

## Features

- A small pool of 5 predefined words
- Up to 6 wrong guesses allowed per game
- Shows guessed letters in place and underscores for the rest
- Option to play again after each round
- Basic input validation (rejects empty input, multiple letters, or repeated guesses)

## Requirements

- Python 3.6+

No external dependencies — uses only the standard library (`random`).

## Usage

Run the script:

```bash
python hangman.py
```

Guess one letter at a time when prompted. The game shows your progress after every guess.

## Example

```
Welcome to Hangman!
The word has 6 letters. You have 6 wrong guesses allowed.

Word: ______
Wrong guesses: 0/6
Guess a letter: p

Word: p_____
Wrong guesses: 0/6
Guess a letter: l
```

## Concepts Used

`random`, `while` loops, `if-else`, strings, lists.

## License

Free to use, modify, and distribute.
