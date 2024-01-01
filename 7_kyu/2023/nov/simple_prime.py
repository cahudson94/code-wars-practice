"""
Your task here is to generate a list of prime numbers, starting from 2.

One way of doing this is using python's generators.

In case you choose to use generators, notice that the generator object should contain all the generated prime numbers, from 2 to an upper limit (included) provided as the argument to the function. If the input limit is less than 2 (including negatives), it should return an empty list.

Each iteration of the generator will yield one prime number. See this link for reference.

The generator object will be converted to a list outside the code, within the test cases.

There will be no check if you are using generators or lists, so use the one you feel more confortable with.
Examples

Some expected results:

list(generate_primes(10)) = [2, 3, 5, 7]
list(generate_primes(23)) = [2, 3, 5, 7, 11, 13, 17, 19, 23]
list(generate_primes(28)) = [2, 3, 5, 7, 11, 13, 17, 19, 23]
list(generate_primes(-1)) = []

Good luck!
"""

def generate_primes(x):
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
