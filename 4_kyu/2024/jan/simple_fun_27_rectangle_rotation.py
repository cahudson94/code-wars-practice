"""
Task

A rectangle with sides equal to even integers a and b is drawn on the Cartesian plane.
Its center (the intersection point of its diagonals) coincides with the point (0, 0),
but the sides of the rectangle are not parallel to the axes; instead,
they are forming 45 degree angles with the axes.

How many points with integer coordinates are located inside the given rectangle (including on its sides)?
Example

For a = 6 and b = 4, the output should be 23

Input/Output

    [input] integer a

    A positive even integer.

    Constraints: 2 ≤ a ≤ 10000.

    [input] integer b

    A positive even integer.

    Constraints: 2 ≤ b ≤ 10000.

    [output] an integer

    The number of inner points with integer coordinates.
"""

def rectangle_rotation(a, b):
    a //= 2**0.5
    b //= 2**0.5
    r = (a + 1) * (b + 1) + a * b
    return r + r % 2 - 1
