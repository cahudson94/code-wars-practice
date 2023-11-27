"""
You will be given a string (map) featuring a cat "C" and a mouse "m". The rest of the string will be made up of dots (".") The cat can move the given number of moves up, down, left or right, but not diagonally.

You need to find out if the cat can catch the mouse from it's current position and return "Caught!" or "Escaped!" respectively.

Finally, if one of two animals are not present, return "boring without two animals".
Examples

moves = 5

map =
..C......
.........
....m....

returns "Caught!" because the cat can catch the mouse in 4 moves

moves = 5

map =
.C.......
.........
......m..

returns "Escaped!" because the cat cannot catch the mouse in  5 moves
"""

def cat_mouse(map_, moves):
    if not ("C" in map_ and "m" in map_):
        return "boring without two animals"
    for idx, row in enumerate(map_.split("\n")):
        if "C" in row:
            cat_x, cat_y = row.index("C"), idx
        if "m" in row:
            mouse_x, mouse_y = row.index("m"), idx
    return "Caught!" if abs(cat_y - mouse_y) + abs(cat_x - mouse_x) <= moves else "Escaped!"
