'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
'''


def find_short(s):
    result = []
    for word in s.split():
        result.append(len(word))
    return min(result)
