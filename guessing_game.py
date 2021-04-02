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

# set high_score to 0


def start_game():
    """This function runs the entire game: the user is asked to guess a
    random number between 1 and 10 repeatedly until they guess
    correctly, with feedback being shown after each incorrect guess to
    narrow their future guesses. Once they guess correctly, the number
    of total guesses is displayed and the game ends.
    """
    print("Welcome to the Number guessing game!")

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

        # if guess is outside range of 1-10
        #   print "Sorry, that number is outside the valid range. Your guess must be a number between 1 and 10."
        #   continue to next iteration
        # proceed as below...
        if guess == random_number:
            print("You got it! The number was {}!".format(random_number))
            print("It took you {} guess(es) to get it.".format(guess_counter))
            break
        elif guess > random_number:
            print("{} is too high. Guess lower!".format(guess))
        else:
            print("{} is too low. Guess higher!".format(guess))

        guess_counter += 1

    # return number of guesses
    print("\nThank you for playing!")


# while true
#   set high_score to call start_game function
#   get should_replay from user
#   if should_replay is equal to "yes"
#       print "The current highscore is {high_score}"
#       continue to next iteration
#   else the game should stop
#       print "Thank you for playing!"
#       exit loop
#   endif
# endwhile
start_game()
