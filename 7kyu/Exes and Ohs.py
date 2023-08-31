'''
Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. 
The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''


def xo(s):
    total_x = 0
    total_o = 0
    for char in s:
        if char.lower() == 'x':
            total_x += 1
        if char.lower() == 'o':
            total_o += 1
    return total_x == total_o
