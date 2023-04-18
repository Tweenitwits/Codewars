"""
Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
"""


def replace_exclamation(s):
    result = ''
    for char in s:
        if char in 'aeiouAEIOU':
            result += '!'
        else:
            result += char
    return result
