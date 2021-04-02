"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
"""

import random


def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # print intro message
    # generate random number between 1 and 10
    # set random_number to result
    # set guess_counter to 1
    # get guess from user
    # while guess is not equal to random_number
    #   increment guess_counter by 1
    #   if guess is greater than random_number
    #     print "{guess} is too high. Guess lower!"
    #   else guess must be less than random_number
    #     print "{guess} is too low. Guess higher!"
    #   endif
    #   get guess from user
    # endwhile
    # print "You got it! The number was {random_number}!"
    # print "It took you {guess_counter} guesses to get it."
    # print closing message


start_game()
