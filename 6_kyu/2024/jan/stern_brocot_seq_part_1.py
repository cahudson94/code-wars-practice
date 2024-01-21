"""
The Stern-Brocot sequence is much like the Fibonacci sequence and has some cool implications. Let's learn about it:

It starts with [1, 1] and adds two new terms every iteration: nextTerm which is the sum of a previous pair; and termAfterThat which is the second term of this previous pair. Here is how to find those terms:

[1, 1] + [nextTerm: 1 + 1 = 2; termAfterThat: 1] ==> [1, 1, 2, 1]
 ^  ^

Then you shift the pairs with one index in the sequence:

[1, 1, 2, 1] + [1 + 2, 2] ==> [1, 1, 2, 1, 3, 2]
    ^  ^

And so on... doing this for 2 more iterations will yield:

[1, 1, 2, 1, 3, 2, 3, 1, 4, 3]

Complete the code that takes a positive integer n, and returns the index of the first occurrence of n in the sequence. Note: indexing start at zero.
Examples

[1, 1, 2, 1, 3, 2, 3, 1, 4, 3, ...]
       ^     ^           ^
n = 2 ==> 2 
n = 3 ==> 4
n = 4 ==> 8

alternate, better lookup time:
def stern_brocot(n):
    seq, idx, key = {0: 1, 1: 1}, 0, 2
    while n != seq[key - 2] and n != seq[key - 1]:
        seq[key] = seq[idx] + seq[idx + 1]
        seq[key + 1] = seq[idx + 1]
        idx += 1
        key += 2
    return key - 2
"""

def stern_brocot(n):
    seq, idx = [1, 1], 0
    while seq[-1] != n and seq[-2] != n:
        seq.extend([seq[idx] + seq[idx + 1], seq[idx + 1]])
        idx += 1
    return seq.index(n)
