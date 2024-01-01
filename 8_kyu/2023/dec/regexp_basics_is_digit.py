"""
Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.

Python solution:
def is_digit(n):
    return n.isdigit() and len(n) == 1
"""
import re

def is_digit(n):
    return bool(re.match(r"\d\Z", n))
