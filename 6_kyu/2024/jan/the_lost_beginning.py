"""
You are given a string of consecutive natural numbers.
Your task is to determine the smallest number that can be the first in this string.
The string ends with an untruncated number.
Examples

"123456789101112131415" -> 1
"17181920" -> 17
"72637236" -> 72637236
"1112" -> 11
"91011" -> 9
"99100" -> 99
"431243" -> 431243, not 4312
"577495" -> 577495, not 57749

Size limits

0 < length string < 140
0 < smallest number < 1 000 000 000
"""

def find(s):
    for i in range(len(s)):
        x = int(s[:i + 1])
        t = s[len(str(x)):]
        pops = 1
        while t:
            if int(t[:len(str(x + pops))]) != x + pops:
                break
            if len(t) >= len(str(x + pops)):
                t = t[len(str(x + pops)):]
            pops += 1
        if not t:
            return x
