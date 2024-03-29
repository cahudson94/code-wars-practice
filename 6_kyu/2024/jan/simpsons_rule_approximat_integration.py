"""
An integral:
∫abf(x)dx\int_{a}^{b}f(x)dx∫ab​f(x)dx

can be approximated by the so-called Simpson’s rule:
b−a3n(f(a)+f(b)+4∑i=1n/2f(a+(2i−1)h)+2∑i=1n/2−1f(a+2ih))\dfrac{b-a}{3n}(f(a)+f(b)+4\sum_{i=1}^{n/2}f(a+(2i-1)h)+2\sum_{i=1}^{n/2-1}f(a+2ih))3nb−a​(f(a)+f(b)+4∑i=1n/2​f(a+(2i−1)h)+2∑i=1n/2−1​f(a+2ih))

Here h = (b - a) / n, n being an even integer and a <= b.

We want to try Simpson's rule with the function f:
f(x)=32sin⁡(x)3f(x) = \frac{3}{2}\sin(x)^3f(x)=23​sin(x)3

The task is to write a function called simpson with parameter n which returns the value of the integral of f on the interval [0, pi] (pi being 3.14159265359...).
Notes:

    Don't round or truncate your results. See in "RUN EXAMPLES" the function assertFuzzyEquals or testing.
    n will always be even.
    We know that the exact value of the integral of f on the given interval is 2.
    Please ask before translating.

Complement: you can see: https://www.codewars.com/kata/5562ab5d6dca8009f7000050/ about rectangle method and trapezoidal rule.
"""

from math import pi, sin

def get_sin(idx, x, n):
    return 1.5 * sin(x) ** 3 if idx in [0, n] else 6 * sin(x) ** 3 if idx % 2 else 3 * sin(x) ** 3

def simpson(n):
    end_points = [((pi - 0) / n) * i for i in range(n + 1)]
    function_vals = [get_sin(idx, x, n) for idx, x in enumerate(end_points)]
    return (((pi - 0) / n) / 3) * sum(function_vals)
