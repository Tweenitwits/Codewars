"""
Your task is simply to count the total number of lowercase letters in a string.

Examples
"abc" ===> 3

"abcABC123" ===> 3

"abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3

"" ===> 0;

"ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0

"abcdefghijklmnopqrstuvwxyz" ===> 26
"""

def lowercase_count(strng):
    counter = 0
    for letter in strng:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            counter += 1
    return counter
