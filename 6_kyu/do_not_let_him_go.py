"""
Task

An employee wishes to resign. Do not let him go.

Locate the entrance to his office so we can send its coordinates to the orbital obstacle placement service (OOPS).

The floor plan of the office is given as a list (python) or an array (java) of strings. Walls are marked with a # and interior with .. Strings can vary in length, and if they do, align them to the left.

Return the coordinates of the office entrance as a tuple (x, y) in python or Point in java. Top left is (0, 0), x is oriented to the right ("columns") and y downwards ("rows"):

+----> x
|
|
V
y

Examples

###.###
#.....#
#.....#  ->  (3, 0)
#....##
######

 #####
 #...#
 ....#
 #...#  ->  (1, 2)
##...#
#....#
######
"""

from typing import List, Tuple


def locate_entrance(office: List[str]) -> Tuple[int, int]:
    if "." in office[0]:
        return (office[0].index("."), 0)
    elif "." in office[-1]:
        return (office[-1].index("."), len(office) - 1)
    else:
        for idx, row in enumerate(office[1:-1]):
            if row.strip().startswith("."):
                return (row.index("."), idx + 1)
            if row.strip().endswith("."):
                return (row.rindex("."), idx + 1)
            for ix, i in enumerate(row):
                if i == ".":
                    if ix >= len(office[idx + 2]) or ix >= len(office[idx]):
                        return ix, idx + 1
                    if (office[idx + 2][ix] == " " or office[idx][ix] == " "):
                        return ix, idx + 1
