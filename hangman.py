"""Main hangman game.

Use Python 3.
"""

from string import ascii_lowercase
from words import get_random_word


def get_num_attempts():
    """Get user-inputted number of attempts for the game."""
    pass  # TODO: get user-inputted number of attempts and return it


def get_display_word(word, idxs):
    """Get the word suitable for display."""
    pass  # TODO: return word suitable for display


def get_next_letter(remaining_letters):
    """Get the user-inputted next letter."""
    pass  # TODO: return next letter


def play_hangman():
    """Play a game of hangman.

    At the end of the game, returns if the player wants to retry.
    """
    # TODO: implement the hangman game

    # Ask player if he/she wants to try again
    try_again = input('Would you like to try again? [y/Y] ')
    return try_again.lower() == 'y'


if __name__ == '__main__':
    while play_hangman():
        print()
