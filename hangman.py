# Hangman Game
import random

words = ["python", "laptop", "guitar", "planet", "bottle"]

def play_hangman():
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You have {max_wrong} wrong guesses allowed.")

    while wrong_guesses < max_wrong:
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter
            else:
                display += "_"

        print("\nWord: " + display)
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong}")

        if display == word:
            print("\nCongratulations! You guessed the word!")
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            wrong_guesses += 1
            print("Wrong guess!")

    print(f"\nGame Over! The word was: {word}")

def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
