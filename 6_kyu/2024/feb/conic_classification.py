"""
The conic curves may be obtained doing different sections of a cone and we may obtain the three principal groups: ellipse, hyperbola and parabola.

The circle is a special case of ellipses.

In mathematics all the conics may be represented by the following equation:

A, B, C, D, E and F are coefficients that may have different values in the real numeric field.

Hesse in the nineteenth century, introduced the use of the invariants, useful tool in order to classify the different conic curves.

The invariants M, N, and S are:

It may be proved that if the system of coordinates changes, for example moving the center of the system of coordinates or rotating the coordinates axes,
or doing both things, the invariants will have the same value, even though the coefficients A, B, C, D, E, and F change.

The following chart shows how the values of M, N and S classify the gender of the conics and the special cases when the conics are degenerated
(points or lines) or they are imaginary:

The function classify_conic() will do this work.
This function will receive the different coefficients of the conic equation and will output the result of the classification as a string

classify_conic(A, B, C, D, E, F) == result

Let's see some cases:

Case1
A = 1 , B = 1, C = 1, D = 2, E = 2, F = -4
classify_conic(A, B, C, D, E, F) == "A real ellipse"

Case2
A = 1 , B = 1, C = -1, D = 2, E = 2, F = 4
classify_conic(A, B, C, D, E, F) == "A real hyperbola"

Case3
A =1, B = 0, C = 0, D = 4; E = 4, F = 4
classify_conic(A, B, C, D, E, F) == "A real parabola"

Case1
A = 1 , B = 1, C = 1, D = 2, E = 2, F = -4
classifyConic(A, B, C, D, E, F) == "A real ellipse"

Case2
A = 1 , B = 1, C = -1, D = 2, E = 2, F = 4
classifyConic(A, B, C, D, E, F) == "A real hyperbola"

Case3
A =1, B = 0, C = 0, D = 4; E = 4, F = 4
classifyConic(A, B, C, D, E, F) == "A real parabola"

The graph showing the above three cases is the following:

[source: imgur.com]

The messages for the special cases, having degenerated or imaginary conics will be:

# For elliptic gender:
"An imaginary ellipse"
"A degenerated ellipse: One point"

# For hyperbolic gender:
"A degenerated hyperbola: two intersecting lines"

# For parabolic gender:
"A degenerated parabola: two parallel lines"
"A degenerated parabola: two coinciding lines"
"A degenerated parabola: two imaginary lines"

Enjoy it!! #Note:

    The given coefficients A, B, C, D, E and F, (a, b, c, d, eandf` in Ruby) will be always integers.

    In order to avoid precision problems, the determinant values of M and N should be obtained by the rule of Sarrus.
    (See: https://en.wikipedia.org/wiki/Rule_of_Sarrus)
"""

def det(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    return sum((-1) ** i * matrix[0][i] * det([row[:i] + row[i + 1:] for row in matrix[1:]]) for i in range(len(matrix)))

def classify_conic(A, B, C, D, E, F):
    M = det([[2 * A, B, D], [B, 2 * C, E], [D, E, 2 * F]])
    N = det([[B, 2 * A], [2 * C, B]])
    S = A + C
    if N < 0:
        if M != 0:
            if M * S < 0:
                return "A real ellipse"
            return "An imaginary ellipse"
        return "A degenerated ellipse: One point"
    if N > 0:
        if M != 0:
            return "A real hyperbola"
        return "A degenerated hyperbola: two intersecting lines"
    else:
        if M == 0:
            val = D * D - 4 * A * F
            if val > 0:
                return "A degenerated parabola: two parallel lines"
            if val < 0:
                return "A degenerated parabola: two imaginary lines"
            return "A degenerated parabola: two coinciding lines"
        return "A real parabola"
