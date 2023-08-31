'''
When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"
'''


import string


def position(alphabet):
    alphabet_list = list(string.ascii_lowercase)
    return f'Position of alphabet: {alphabet_list.index(alphabet) + 1}'
