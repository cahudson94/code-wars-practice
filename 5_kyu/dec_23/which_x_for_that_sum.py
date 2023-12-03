"""
Consider the sequence U(n, x) = x + 2x**2 + 3x**3 + .. + nx**n where x is a real number and n a positive integer.

When n goes to infinity and x has a correct value (ie x is in its domain of convergence D), U(n, x) goes to a finite limit m depending on x.

Usually given x we try to find m. Here we will try to find x (x real, 0 < x < 1) when m is given (m real, m > 0).

Let us call solve the function solve(m) which returns x such as U(n, x) goes to m when n goes to infinity.
Examples:

solve(2.0) returns 0.5 since U(n, 0.5) goes to 2 when n goes to infinity.

solve(8.0) returns 0.7034648345913732 since U(n, 0.7034648345913732) goes to 8 when n goes to infinity.
Note:

You pass the tests if abs(actual - expected) <= 1e-12

High efficiency math solution: return (2 * m + 1 - (4 * m + 1) ** 0.5) / (2 * m)
"""

def solve(m):
    epsilon = 0.000000000001
    low, high = 0.0, 1.0

    while high - low > epsilon:
    	mid = (high + low) / 2
    	mid_sum = mid / (1 - mid) ** 2

    	if mid_sum < m:
    		low = mid
    	else:
    		high = mid

    return low
