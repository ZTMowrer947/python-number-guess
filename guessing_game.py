"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
-----------------------------------------------------------------------
This project implements a simple version of the number guessing game.

The user is prompted to guess a random number between 1 and 10, and
does so until they guess correctly. At the end, they see how many
guesses they took to guess the random number.
"""

import random


def play_game():
    """This function runs the entire game: the user is asked to guess a
    random number between 1 and 10 repeatedly until they guess
    correctly, with feedback being shown after each incorrect guess to
    narrow their future guesses. Once they guess correctly, the number
    of total guesses is displayed and the game ends.
    """

    random_number = random.randint(1, 10)

    guess_counter = 1

    while True:
        guess = input("\nPick a number between 1 and 10: ")
        try:
            guess = int(guess)
        except ValueError:
            print(
                "Sorry, that isn't a valid guess. Your guess must be a number between 1 and 10.")
            continue

        if guess not in range(1, 11):
            print("Sorry, {} is outside the valid range. Your guess must be a number between 1 and 10.".format(guess))
            continue
        elif guess == random_number:
            print("You got it! The number was {}!".format(random_number))
            print("It took you {} guess(es) to get it.".format(guess_counter))
            break
        elif guess > random_number:
            print("{} is too high. Guess lower!".format(guess))
        else:
            print("{} is too low. Guess higher!".format(guess))

        guess_counter += 1

    # return number of guesses
    return guess_counter


# set high_score to 0
high_score = 0

print("Welcome to the Number guessing game!")

# while true
while True:
    # set game_score to call play_game function
    game_score = play_game()

    # get should_replay from user
    should_replay = input("\nWould you like to play again? (yes/no) ")
    # if should_replay is equal to "yes"
    if should_replay.lower() == "yes":
        # if game_score is less than high_score or high_score is not initialized
        if game_score < high_score or high_score == 0:
            # set high_score to game_score
            high_score = game_score
        # endif

        print("\nThe current high score is {}".format(high_score))
        # continue to next iteration
        continue
    # else the game should stop
    else:
        # print "Thank you for playing!"
        print("\nThank you for playing!")
        # exit loop
        break
    # endif
# endwhile
