"""
A palindrome is a series of characters that read the same forwards as backwards such as "hannah", "racecar" and "lol".

For this Kata you need to write a function that takes a string of characters and returns the length, as an integer value,
of longest alphanumeric palindrome that could be made by combining the characters in any order but using each character only once.
The function should not be case sensitive.

For example if passed "Hannah" it should return 6 and if passed "aabbcc_yYx_" it should return 9 because one possible palindrome would be "abcyxycba".
"""

def longest_palindrome(s):
    letters = {}
    for x in s:
        if not x.isalnum():
            continue
        letters.setdefault(x.lower(), 0)
        letters[x.lower()] += 1
    return sum([x // 2 * 2 for x in letters.values()]) + any([x % 2 for x in letters.values()])
