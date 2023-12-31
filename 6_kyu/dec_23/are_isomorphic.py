"""
Two strings a and b are called isomorphic if there is a one to one mapping possible for every character of a to every character of b. And all occurrences of every character in a map to same character in b.
Task

In this kata you will create a function that return True if two given strings are isomorphic to each other, and False otherwise. Remember that order is important.

Your solution must be able to handle words with more than 10 characters.
Example

True:

CBAABC DEFFED
XXX YYY
RAMBUNCTIOUSLY THERMODYNAMICS

False:

AB CC
XXY XYY
ABAB CD

optimized:
def isomorph(a, b):
    return len(a) == len(b) and len(set(a)) == len(set(b)) == len(set(zip(a, b)))
"""

def isomorph(a, b):
    if len(a) != len(b):
        return False
    a_char = {}
    b_char = {}
    for i in range(len(a)):
        a_char.setdefault(a[i], [i, 0])
        b_char.setdefault(b[i], [i, 0])
        a_char[a[i]][1] += 1
        b_char[b[i]][1] += 1
        if a_char[a[i]][0] != b_char[b[i]][0]:
            return False
    return True
    
