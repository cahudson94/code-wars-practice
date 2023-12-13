"""
We are given a sequence of coplanar points and see all the possible triangles that may be generated which all combinations of three points.

We have the following list of points with the cartesian coordinates of each one:

Points [x, y]
   A   [1, 2]
   B   [3, 3]
   C   [4, 1]
   D   [1, 1]
   E   [4, -1]

With these points we may have the following triangles:
	ABC, ABD, ABE, ACD, ACE, ADE, BCD, BCE, BDE, CDE.
There are three special ones: 
	ABC, ACD and CDE, that have an angle of 90°.

All is shown in the picture below:

[source: imgur.com]

We need to count all the rectangle triangles that may be formed by a given list of points.
Note that possible duplicate points should be counted only once to form a triangle.

The case decribed above will be:

count_rect_triang([[1, 2],[3, 3],[4, 1],[1, 1],[4, -1]]) == 3

Observe this case:

count_rect_triang([[1, 2],[4, -1],[3, 3],[4, -1],[4, 1],[1, 1],[4, -1], [4, -1], [3, 3], [1, 2]]) == 3

If no rectangle triangles may be generated the function will output 0.

Enjoy it!

"""

def isright(a,b,c):
    a_b, b_c, c_a = sorted(
    	sum(
    		(x - y) ** 2 for x, y in zip(point_1, point_2)
    	) for point_1, point_2 in [(a, b), (b, c), (c, a)]
    )
    return a_b + b_c == c_a

def count_rect_triang(points):
    points = set([tuple(x) for x in points])
    count = 0
    for i, x in enumerate(list(points)[:-2]):
        for j, y in enumerate(list(points)[i + 1:-1]):
            for z in list(points)[i+j+2:]:
                if isright(x,y,z):
                    count += 1
    return count
