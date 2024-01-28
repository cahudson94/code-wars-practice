"""
The problem

How many zeroes are at the end of the factorial of 10? 10! = 3628800, i.e. there are 2 zeroes. 16! (or 0x10!) in hexadecimal would be 0x130777758000, which has 3 zeroes.
Scalability

Unfortunately, machine integer numbers has not enough precision for larger values. Floating point numbers drop the tail we need. We can fall back to arbitrary-precision ones - built-ins or from a library, but calculating the full product isn't an efficient way to find just the tail of a factorial. Calculating 100'000! in compiled language takes around 10 seconds. 1'000'000! would be around 10 minutes, even using efficient Karatsuba algorithm
Your task

is to write a function, which will find the number of zeroes at the end of (number) factorial in arbitrary radix = base for larger numbers.

    base is an integer from 2 to 256
    number is an integer from 1 to 1'000'000

Note Second argument: number is always declared, passed and displayed as a regular decimal number. If you see a test described as 42! in base 20 it's 4210 not 4220 = 8210.
"""

def get_power(num, power):
    count = 0
    r = power
    while r <= num:
        count += num // r
        r *= power
    return count

def get_factors(base):
    factors = []
    i = 2
    while base > 1:
        if not base % i:
            count = 0
            while not base % i:
                base //= i
                count += 1
            factors.append((i, count))
        i += 1
    return factors

def zeroes(base, number):
    prime_factors = get_factors(base)
    idx = 0
    ans = float("inf")
    while idx < len(prime_factors):
        ans = min(ans, get_power(number, prime_factors[idx][0]) // prime_factors[idx][1])
        idx += 1
    return ans
