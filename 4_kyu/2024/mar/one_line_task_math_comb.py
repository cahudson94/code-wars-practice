"""
Big thanks to @dfhwze for the approval.

This kata is inspired by @Voile's One Line Task: Hard Fibonacci Numbers.

Task

Write a function that takes two non-negative integers n and k, and computes the mathematical combination (nk)\binom{n}{k}(kn​).
Examples

    (10)=1, (11)=1, (12)=0

    (63)=20, (64)=15, (69)=0

Note

    ∀n∈N∪{0} ⟹ (n0)=(nn)=1

    ∀n,k∈N∪{0}∧k>n ⟹ (nk)=0

    Lines of your code must not exceed 1.

    Length of your code must not exceed 44. (Record: @monadius's 41 characters)

    Disabled modules are numpy, scipy, sklearn, gmpy2, math and sys.

    Disabled built-in functions are open, exec, eval, globals, locals and exit.

    Credits to @Blind4Basics's module forbidder.

Tests

    For all tests, n,k∈N∪{0}∧k<max⁡(n+2,2n)n.

    108 fixed tests, including 6 example tests, 93 mini tests and 9 big tests.

    300 small random tests, n∈[100,200)n.

    20 big random tests, n∈[1100,1200)n.

    One Last Test, n∈[4990,5000)∧k∈[⌊49n100⌋,⌊51n100⌋)n.

I hope you enjoy the tests. I had fun writing them. ;)
"""

comb=lambda n,k:(x:=2<<n|1)**n>>n*k+k&x-2
