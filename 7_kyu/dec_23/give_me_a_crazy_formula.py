"""
Given a non-negative number, sum all its digits using the following rules:

    If the number of digits is even, remove the last digit

    a. If the middle digit is odd, subtract it instead of adding

    b. If both the middle digit and the last digit are even, subtract the last digit instead of adding

    c. If the middle digit is even but the last digit is odd, the first digit must be squared

Repeat this process until only 1 digit is left.

Note: if at some point the number becomes negative, remove the minus sign.
Examples

5  =>  5

214  =>  2 - 1 + 4 = 5   =>  5
126  =>  1 + 2 - 6 = -3  =>  3

2234  =>  223  =>  2^2 + 2 + 3 = 9  =>  9
"""

def crazy_formula(n):
    n = str(n)
    while len(n) > 1:
        if not len(n) % 2:
            n = n[:-1]
        n = [int(x) for x in n]
        mid = n[len(n) // 2]
        last = n[-1]
        if int(mid) % 2:
            n[len(n) // 2] = -mid
        else:
            if int(last) % 2:
                n[0] = n[0] ** 2
            else:
                n[-1] = -last
        n = str(sum(n))
        if n[0] == "-":
            n = n[1:]
    return int(n)
