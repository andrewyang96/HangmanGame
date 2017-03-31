"""Function to fetch words."""

import random

WORDLIST = 'wordlist.txt'


def get_random_word():
    """Get a random word from the wordlist."""
    words = []
    with open(WORDLIST, 'r') as f:
        for word in f:
            words.append(word)
    return random.choice(words)


def get_random_word_scalable():
    """Get a random word from the wordlist using no extra memory."""
    num_words_processed = 0
    curr_word = None
    with open(WORDLIST, 'r') as f:
        for word in f:
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    return curr_word
