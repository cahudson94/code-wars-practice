"""
Balanced?

Usually when we talk about converting between bases, we assume that the value assigned to the characters within the base are always the same; '3' in base 7 is the same as '3' in base 16.
However, we could just as easily pick a different selection of values.

So, in balanced base nine, the characters will be as follows:

    0-4 will map onto 0-4 as you would expect
    £, $, %, ^ will map onto -1, -2, -3, and -4 respectively

This leads to some interesting conversions. For example, 6 = 1% because it is equal to 9 - 3.
Notice that all negative numbers can be represented without a negative sign as well.
The Goal

You must program a function that takes in a number and converts it to a string representing its balanced base nine form.
For example, the number 26 as an input should return 3^, and -14 should return $4.
Of course, your algorithm will have to cope with much bigger numbers.
"""

def balanced_base_nine(num: int) -> str:
    base_nine = ""
    while num:
        d = num % 9
        base_nine += '01234^%$£'[d]
        num = num // 9 + (d > 4)
    return base_nine[::-1] or '0'
