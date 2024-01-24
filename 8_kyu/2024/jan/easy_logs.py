"""
Add two logs with base X, with the value of A and B. Example log A + log B where the base is X.

alternative:
def logs(x, a, b):
    return log(a * b, x)
"""

from math import log

def logs(x, a, b):
    return sum([log(a, x), log(b, x)])
