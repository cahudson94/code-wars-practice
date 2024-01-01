"""
Summation Of Primes

The sum of the primes below or equal to 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below or equal to the number passed in.

From Project Euler's Problem #10.
"""

def get_primes(x):
    seen = {}
    y = 2
    while y <= x:
        if y not in seen:
            yield y
            seen[y * y] = [y]
        else:
            for z in seen[y]:
                seen.setdefault(y + z, []).append(z)
            del seen[y]
        y += 1

def summation_of_primes(primes):
    return sum(get_primes(primes))
