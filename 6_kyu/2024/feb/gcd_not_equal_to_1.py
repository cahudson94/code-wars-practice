"""
You are given 3 positive integers a, b, k.
Using one operation you can change a or b (but not both) by k (add or subtract are all ok).
Count the minimun number of opearations needed to make a, b > 0 and gcd(a, b) > 1.

You have to write a function gcd_neq_one() which receives 3 positive integers a, b, k and return a positive integer: the solution of the problem.

You can read the original, Vietnamese statement at my page (TLEoj): https://tleoj.edu.vn/problem/21c

optimized:
import math

def gcd_neq_one(a, b, k):
    t = 0
    while True:
        for i in range(t + 1):
            if math.gcd(a + i * k, b + (t - i) * k) > 1:
                return t
            x, y = a - i * k, b - (t - i) * k
            if x > 0 and y > 0 and math.gcd(x, y) > 1:
                return t
            x, y = x, y + 2 * (t - i) * k
            if x > 0 and math.gcd(x,y)>1:
                return t
            x,y=x+2*i*k,y-2*(t-i)*k
            if y>0 and math.gcd(x,y)>1:
                return t
        t += 1
"""

from math import gcd

def gcd_neq_one(a, b, k):
    seen = {}
    to_check = [(a, b, 0)]
    while to_check:
        current = to_check[0]
        if gcd(current[0], current[1]) != 1:
            return current[2]
        x, y, x_k, y_k, x_neg_k, y_neg_k = current[0], current[1], current[0] + k, current[1] + k, current[0] - k, current[1] - k
        if x_neg_k > k:
            next_a_neg = (current[0] - k, current[1])
            if not seen.get(next_a_neg, None):
                to_check.append((current[0] - k, current[1], current[2] + 1))
                seen[next_a_neg] = current[2] + 1
        if y_neg_k > k:
            next_b_neg = (current[0], current[1] - k)
            if not seen.get(next_b_neg, None):
                to_check.append((current[0], current[1] - k, current[2] + 1))
                seen[next_b_neg] = current[2] + 1
        next_a = (current[0] + k, current[1])
        if not seen.get(next_a, None):
            to_check.append((current[0] + k, current[1], current[2] + 1))
            seen[next_a] = current[2] + 1
        next_b = (current[0], current[1] + k)
        if not seen.get(next_b, None):
            to_check.append((current[0], current[1] + k, current[2] + 1))
            seen[next_b] = current[2] + 1
        to_check.pop(0)
