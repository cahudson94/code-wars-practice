"""
Simpler and similar kata here.

A generalization of perfect numbers are (m,k)-perfect number. It is a series of numbers that satisfy the following condition:
σm(n)=kn\Huge \sigma^{m}(n) = knσm(n)=kn

where σm is the divisor function (or sum of all divisors) [Wikipedia link] applied m times, k a constant.

For example "normal" perfect numbers are (1,2)-perfect number.

Goal:
Write a function first_mk_perfectnumber(m,k) that, give in input the m and k of the previous equation ( σm(n) = kn ),
it returns the first number (n) that satisfy the relation.

Pay attention to the performance of your algorithm!! This function must run within the maximum time very big number (>200000).
My solution's time of execution in any language is around 4 seconds.

Wikipedia Page : Superperfect Number [Generalization at bottom]

Example:
first_mk_perfectnumber(2,2) return 2 because
σ(σ(1)) = 1 so 1 != 2*1 while σ(σ(2)) = 4 so 4 == 2*2

Hint 1: You can execute divisor function speedly with prime factors. You can find formula here: Wiki Page Wolfram Page
"""

from functools import cache
from gmpy2 import is_prime, next_prime

@cache
def σ(m, n):
    s, p = 1, 2
    while n > 1:
        while n % p:
            p = n if is_prime(n) else next_prime(p)
        i = 1
        while n % p == 0:
            n //= p
            i += 1
        s *= (p ** i - 1) // (p - 1)
    return s if m == 1 else σ(m - 1, s)

def first_mk_perfectnumber(m, k):
    i = 1
    while σ(m, i) != k * i:
        i += 1
    return i
