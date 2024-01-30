"""
What is a happy number?

A happy number is defined as an integer in which the following sequence ends with the number 1.

    Calculate the sum of the square of each individual digit.

    If the sum is equal to 1, then the number is happy.

    If the sum is not equal to 1, then repeat from steps 1.

    A number is considered unhappy once the same number occurs multiple times in a sequence because this means there is a loop and it will never reach 1.

For example, the number 7 is a "happy" number:

7² = 49 --> 4² + 9² = 97 --> 9² + 7² = 130 --> 1² + 3² + 0² = 10 --> 1² + 0² = 1

On the other hand, the number 6 is not a happy number as the sequence that is generated is the following:

6, 36, 45, 41, 17, 50, 25, 29, 85, 89, 145, 42, 20, 4, 16, 37, 58, 89

Once the same number occurs twice in the sequence, the sequence is guaranteed to go on infinitely, never hitting the number 1, since it repeat this cycle.
Your task:

Write a function perf_happy(n) that returns a list of all happy numbers from 1 to n inclusive.

perf_happy(100)   =>  [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]

The challenge:

    you are going to be challenged for 30 tests up to n = 10_000_000
    you are not allowed to hardcode the sequence: you'll have to compute it (max length of the code: 1700 characters)

Credits

This kata is based on a variation of Happy Numbers by TySlothrop.

It's a different view of Happy Numbers (performance edition) by FArekkusu.

(ok, ok, I've copied a lot from them)
"""

from functools import cache
from bisect import bisect

@cache
def is_happy(num):
    seen = set()
    while num not in seen:
        seen.add(num)
        num = sum(r * r for r in map(int, str(num)))
    return num == 1

def make_happy():
    #   567 is the sum for 9999999, the highest possible output from the sum opperation
    small = [is_happy(i) for i in range(568)]
    res, current_sum, digit = [], 1, 1
    for n in range(1, 10000001):
        if small[current_sum]:
            res.append(n)
        if digit < 9:
            current_sum += 2 * digit + 1
            digit += 1
        else:
            current_sum = sum(r * r for r in map(int, str(n + 1)))
            digit = 0
    return res
        
HAPPY = make_happy()
    
def perf_happy(n):
    return HAPPY[:bisect(HAPPY, n)]
    
