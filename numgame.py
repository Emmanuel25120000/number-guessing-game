import random


def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("=" * 40)

    while True:
        guess_input = input("Enter your guess: ").strip()

        if not guess_input.isdigit():
            print("Please enter a valid whole number.\n")
            continue

        guess = int(guess_input)

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.\n")
            continue

        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.\n")
        elif guess > number_to_guess:
            print("Too high! Try again.\n")
        else:
            print(f"\nCongratulations! You guessed it right!")
            print(f"The number was {number_to_guess}.")
            print(f"It took you {attempts} attempt(s) to guess correctly.")
            break


def main():
    play_game()

    while True:
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again == "y":
            print()
            play_game()
        elif again == "n":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
