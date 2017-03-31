"""Main hangman game.

Use Python 3.
"""

from string import ascii_lowercase
from words import get_random_word


def _get_num_attempts():
    while True:
        num_attempts = input('How many attempts do you want? [1-25] ')
        try:
            num_attempts = int(num_attempts)
            if num_attempts <= 0 or num_attempts >= 26:
                print('{0} is not between 1 and 25'.format(num_attempts))
            else:
                return num_attempts
        except ValueError:
            print(
                '{0} is not an integer between 1 and 25'.format(num_attempts))


def _get_display_word(word, idxs):
    if len(word) != len(idxs):
        raise ValueError('Word length and indices length are not the same')
    displayed_word = ''.join(
        [letter if idxs[i] else '×' for i, letter in enumerate(word)])
    return displayed_word.strip()


def _get_next_letter(remaining_letters):
    if len(remaining_letters) == 0:
        raise ValueError('There are no remaining letters')
    while True:
        next_letter = input('Choose the next letter: ').lower()
        if len(next_letter) != 1:
            print('{0} is not a single character'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('{0} is not a letter'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('{0} has been guessed before'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter


def play_hangman():
    """Play a game of hangman.

    At the end of the game, returns if the player wants to retry.
    """
    print('Starting a game of Hangman...')
    attempts_remaining = _get_num_attempts()
    print('Selecting a word...')
    word = get_random_word()
    print()

    idxs = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set(ascii_lowercase)
    absent_letters = []
    word_solved = False

    while attempts_remaining > 0 and not word_solved:
        print('Word: {0}'.format(_get_display_word(word, idxs)))
        print('Attempts Remaining: {0}'.format(attempts_remaining))
        print('Previous Guesses: {0}'.format(' '.join(absent_letters)))
        next_letter = _get_next_letter(remaining_letters)

        if next_letter in word:
            print('{0} is in the word!'.format(next_letter))
            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            print('{0} is NOT in the word!'.format(next_letter))
            attempts_remaining -= 1
            absent_letters.append(next_letter)

        if False not in idxs:
            word_solved = True
        print()

    print('The word is {0}'.format(word))
    if word_solved:
        print('Congratulations! You won!')
    else:
        print('Try again next time!')

    try_again = input('Would you like to try again? [y/Y] ')
    print()
    return try_again.lower() == 'y'


if __name__ == '__main__':
    while play_hangman():
        pass
