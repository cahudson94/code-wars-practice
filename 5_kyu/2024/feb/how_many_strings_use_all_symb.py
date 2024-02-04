"""
Overview

Given an alphabet consisting of a distinct symbols, how many strings of exact length = n are there which use all of the a distinct symbols at least once?

Equivalent reformulation, if you prefer: how many strings are not missing any of the a distinct symbols?

For example, given the alphabet {F,G} consisting of a=2 distinct symbols,
the string of length n=5 given by FGGFG is a permitted string because it uses all of the a symbols at least once. On the other hand,
the string FFFFF is a forbidden string because it does not use all of the symbols from the alphabet {F,G} at least once (it doesn't use the symbol G).

Inputs

You will be given two integers, n and a, representing the length of the string, and the size of the alphabet i.e. the number of symbols.

Performance requirement: In the tests, n and a will be tested together up to n=250 and a=150.
Therefore, an approach in which you attempt to generate all possible strings and count which ones satisfy the requirement will probably time out.
Instead, use the walk-through examples below to develop some insight.

Outputs

Return an integer, representing the number of strings of length n that use all of the symbols from an alphabet of size a at least once.
Walk-through examples

-Example 1: n = 5 and a = 2

Suppose we use the alphabet of 2 symbols: {F,G} (the specific symbols F and G don't matter, of course, just that there are a = 2 of them).

There are 2**5 possible strings of length n = 5 using these 2 possible symbols.

Among all 2**5 such possible strings, one of them is the forbidden string FFFFF which DOES NOT contain the symbol G at least once,
and one of them is the forbidden string GGGGG which DOES NOT contain the symbol F at least once.

In all of the other possible strings, all the symbols in the alphabet {F,G} appear at least once.

Hence there are 2**5 - 1 - 1 = 2**5 - 2 = 30 strings of exact length = n = 5 in which all of the a = 2 distinct symbols appear at least once.

-Example 2: n = 5 and a = 3

Again, suppose we use the alphabet of 3 symbols: {F,G,H}.

There are 3**5 possible strings of length n = 5 using these 3 possible symbols.

Let's count the forbidden strings according to the exact number of symbols that they do not use.

Firstly, there are some forbidden strings missing exactly 2 of the 3 symbols:
among all 3**5 possible strings, one of them is the string FFFFF which DOES NOT contain either the symbols G or H at least once,
one of them is the string GGGGG which DOES NOT contain either the symbols F or H at least once,
and one of them is the string HHHHH which DOES NOT contain either the symbols F or G at least once.
Thus there are in total 1 + 1 + 1 = 3 * 1 = 3 forbidden strings which are missing exactly 2 of the a = 3 symbols in the alphabet.

Now that we have considered the forbidden strings that are missing exactly 2 of the 3 symbols,
we realise that there are also forbidden strings which are missing exactly 1 of the a = 3 symbols in the alphabet.
For example, how many forbidden strings are there that are missing exactly the symbol H ? i.e. strings which are not missing the symbols F or G ?

The answer is quite simply the number of strings with n = 5 and a = 3-1 = 2 in which all of the a = 3-1 = 2 remaining symbols must appear at least once.
But this is exactly what we calculated in Example 1.

So, for each of the 3 choices of F, G, or H there are exactly 2**5 - 2 = 30 forbidden strings in which exactly one of those symbols is missing,
but not two of them.

So, among all 3**5 strings, there are 3 * 1 = 3 forbidden strings missing exactly 2 of the symbols,
and there are 3 * ( 2**5 - 2) forbidden strings missing exactly 1 symbol.

Thus there are 3**5 - 3 - 3*(2**5 - 2) = 150 strings which are missing exactly 0 symbols,
i.e. 150 strings in which all of the a = 3 symbols appear at least once.

Hint

If you'd like to check the above results, for these small values of n and a you can easily generate all 2**5 and all 3**5 strings and loop over them,
counting which ones have all of the symbols appearing at least once.

This approach will not work for the larger values of n and a used in the full tests though,
since you won't be able to generate all 150**250 strings when e.g. n = 250 and a = 150,
but hopefully the walk-through examples above have revealed a pattern that you can use.
"""

def use_all_symbols(n,a):
    if a > n:
        return 0
    if a == 1:
        return a
    total = a ** n
    step = 1
    print(total, step, a)
    for i in range(a - 1):
        step = step * (a - i) // (i + 1)
        if i % 2:
            total += step * (a - (i + 1)) ** n
        else:
            total -= step * (a - (i + 1)) ** n
    return total
