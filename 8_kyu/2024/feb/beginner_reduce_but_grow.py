"""
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

option:
from math import prod as grow
"""

from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)
