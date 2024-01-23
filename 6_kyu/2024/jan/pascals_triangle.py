"""
In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula
(nk)=n!k!(n−k)!\lparen {n \atop k} \rparen = \frac {n!} {k!(n-k)!}(kn​)=k!(n−k)!n!​

where n denotes a row of the triangle, and k is a position of a term in the row.

Pascal's Triangle

You can read Wikipedia article on Pascal's Triangle for more information.
Task

Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional list/array.
Example:

n = 1: [1]
n = 2: [1,  1, 1]
n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]
"""

def pascals_triangle(n):
    out = [1]
    for x in range(2, n + 1):
        for i in range(x):
            if not i or i == x - 1:
                out.append(1)
            else:
                out.append(out[-x + 1] + out[-x])
    return out
