from random import randint, choice

from string import ascii_lowercase, ascii_uppercase, punctuation, digits


class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwds):
        return ''.join([choice(self.psw_chars) for _ in range(randint(self.min_length, self.max_length))])
    