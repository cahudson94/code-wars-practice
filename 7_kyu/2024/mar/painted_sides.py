"""
Task

You are given a big cube, made up of several tiny cubes.
You paint the outside of the big cube and are now supposed to find out how many of the tiny cubes (each of side length 1 cm) have zero faces painted,
one face painted, two faces painted, etc.

Write a function painted_faces which acceps two parameters:

    length: The side length of the big cube (in cm.)
    n: The number of faces painted

You have to figure out how many of the little cubes have n faces painted.

Example:

painted_faces(4,3)

=> result: 8      #Only the vertices of the big cube will have three faces painted

If n>3 then return 0 as it is not possible for a painted cube to have more than 3 sides painted (Unless s = 1...in that case it will have 6 faces painted).
"""

def painted_faces(length, n):
    if length < 3:
        return 0 if not length else int(n == 6) if length == 1 else 8 if n == 3 else 0
    if n >= 3:
        return 0 if n > 3 else 8
    return (length - 2) * 12 if n == 2 else (length - 2) ** 2 * 6 if n == 1 else (length - 2) ** 3
