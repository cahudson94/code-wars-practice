"""
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters.
E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.

This is the second kata in series:

    Find the unique number
    Find the unique string (this kata)
    Find The Unique
"""

def find_uniq(arr):
    base = set(arr[0].lower())
    for idx, x in enumerate(arr[1:]):
        if set(x.lower()) != base:
            if idx != 0:
                return x
            elif set(arr[2].lower()) == base:
                return x
            else:
                return arr[0]
