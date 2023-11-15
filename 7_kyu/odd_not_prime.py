"""
For "x", determine how many positive integers less than or equal to "x" are odd but not prime. Assume "x" is an integer between 1 and 10000.

Example: 5 has three odd numbers (1,3,5) and only the number 1 is not prime, so the answer is 1

Example: 10 has five odd numbers (1,3,5,7,9) and only 1 and 9 are not prime, so the answer is 2
"""

# https://stackoverflow.com/questions/46841968/fastest-way-of-testing-if-a-number-is-prime
def first_prime(n):
    if n & 1 == 0:
        return 2
    d= 3
    while d * d <= n:
        if n % d == 0:
            return d
        d= d + 2
    return n

def odd_not_prime(n):
    return len([x for x in range(1, n + 1, 2) if first_prime(x) != x or x == 1])
