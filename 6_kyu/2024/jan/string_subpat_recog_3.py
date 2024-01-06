"""
Similar to the previous kata, but this time you need to operate with shuffled strings to identify if they are composed repeating a subpattern

Since there is no deterministic way to tell which pattern was really the original one among all the possible permutations of a fitting subpattern, return a subpattern with sorted characters, otherwise return the base string with sorted characters (you might consider this case as an edge case, with the subpattern being repeated only once and thus equalling the original input string).

For example:

has_subpattern("a") == "a"; #no repeated pattern, just one character
has_subpattern("aaaa") == "a" #just one character repeated
has_subpattern("abcd") == "abcd" #base pattern equals the string itself, no repetitions
has_subpattern("babababababababa") == "ab" #remember to return the base string sorted"
has_subpattern("bbabbaaabbaaaabb") == "ab" #same as above, just shuffled

If you liked it, go for either the previous kata or the next kata of the series!

optimized:
from functools import reduce
from math import gcd

def has_subpattern(string):
    c = {x: string.count(x) for x in set(string)}
    m = reduce(gcd, c.values())
    return ''.join(sorted(k * (v // m) for k, v in c.items()))
"""

from math import gcd

def has_subpattern(string):
    chars = {x: string.count(x) for x in set(string)}
    set_string = ''.join(sorted(set(string)))
    if len(chars) == 1:
        return set_string[0]
    total_gcd = gcd(chars[set_string[0]], chars[set_string[1]])
    for i in range(2, len(set_string)):
        total_gcd = gcd(total_gcd, chars[set_string[i]])
    if total_gcd == 1:
        return ''.join(sorted(string))
    return ''.join(x * int(chars[x] / total_gcd)  for x in set_string)
