"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
---------------------------------
"""

import random


def start_game():
    """This function runs the entire game as described in the module help."""
    print("Welcome to the Number guessing game!")

    random_number = random.randint(1, 10)

    guess_counter = 1

    while True:
        guess = input("\nPick a number between 1 and 10: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Sorry, that isn't a valid guess. Your guess must be a number.")
            continue

        if guess == random_number:
            print("You got it! The number was {}!".format(random_number))
            print("It took you {} guess(es) to get it.".format(guess_counter))
            break
        elif guess > random_number:
            print("{} is too high. Guess lower!".format(guess))
        else:
            print("{} is too low. Guess higher!".format(guess))

        guess_counter += 1

    print("\nThank you for playing!")


start_game()
