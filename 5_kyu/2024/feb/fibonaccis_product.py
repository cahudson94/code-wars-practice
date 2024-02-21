"""
You are given a positive integer n greater than one.

How many ways are there to represent it as a product of some Fibonacci numbers greater than one?

(Fibonacci sequence: 1, 1, 2, 3, 5, 8...).

For example, there are two ways for n = 40:

    2 * 2 * 2 * 5
    5 * 8

But you can't represent n = 7 in an aforementioned way.

Note that n may be really big (up to 10^36). Good luck!
"""

from functools import cache

@cache
def fib_prod(n, a = 1, b = 2):
    if n == 1:
        return 1
    if b > n:
        return 0
    
    total = 0
    while True:
        total += fib_prod(n, b, a + b)
        if n % b == 0:
            n //= b
        else:
            return total
