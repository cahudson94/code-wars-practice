"""
The Pell sequence is the sequence of integers defined by the initial values

P(0) = 0, P(1) = 1

and the recurrence relation

P(n) = 2 * P(n-1) + P(n-2)

The first few values of P(n) are

0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, 80782, 195025, 470832, ..

Task

Your task is to return the nth Pell number
"""

cache = {}

def pell(n):
    while n > 1:
        if cache.get(n, None) is None:
            cache[n] = 2 * pell(n - 1) + pell(n - 2)
        return cache[n]
    return n
