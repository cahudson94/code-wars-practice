"""
Task:

Based on the received dimensions, a and b, of an ellipse, calculare its area and perimeter.
Example:

Input: ellipse(5,2)

Output: "Area: 31.4, perimeter: 23.1"

Note: The perimeter approximation formula you should use: π * (3/2(a+b) - sqrt(ab))
"""

from math import pi

def ellipse(a, b):
    return f"Area: {pi * a * b:.1f}, perimeter: {pi * (3 / 2 * (a + b) - (a * b) ** .5):.1f}"
