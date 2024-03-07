"""
Description:

Convert the continuous exclamation marks or question marks to a digit, Use all the digits to form a number.
If this number is a prime number, return it. If not, divide this number by the smallest factor that it is greater than 1, until it becomes a prime number.

You can assume that all test results are greater than 1 and the length of a continuous substring(! or ?) is always less than 10.
Examples

convert("!!") == 2
convert("!??") == 3
(12 --> 6 --> 3)
convert("!???") == 13
convert("!!!??") == 2
(32 --> 16 --> 8 --> 4 --> 2)
convert("!!!???") == 11
(33 --> 11)
convert("!???!!") == 11
(132 --> 66 --> 33 --> 11)
convert("!????!!!?") == 53 
(1431 --> 477 --> 159 --> 53)
convert("!!!!!!!???????") == 11 
(77 --> 11)
"""

from gmpy2 import is_prime

def first_factor(n):
    for num in range(2, int(n ** .5) + 1):
        if n % num == 0:
            return num

def convert(s):
    digits = []
    last = ""
    for x in s:
        if not last or x != last:
            last = x
            digits.append(1)
        else:
            digits[-1] += 1
    num = int("".join(str(x) for x in digits))
    while not is_prime(num):
        num //= first_factor(num)
    return num
