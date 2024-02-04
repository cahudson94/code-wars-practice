"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

optimized:
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate 90
    return out
"""

def snail(snail_map):
    if not snail_map[0]:
        return []
    snail_map_90 = list(zip(*snail_map))
    turns = 5 + ((len(snail_map) - 3) * 2)
    end = len(snail_map) - 1
    direction = 0
    start = [0, 0]
    out = []
    while turns:
        if direction == 0:
            out.extend(snail_map[start[0]][start[1]:end])
            start[0] = end
            direction += 1
        elif direction == 1:
            out.extend(snail_map_90[start[0]][start[1]:end])
            direction += 1
        elif direction == 2:
            out.extend(snail_map[start[0]][end:start[1]:-1])
            direction += 1
            start[0] = start[1]
        else:
            out.extend(snail_map_90[start[0]][end:start[1]:-1])
            direction = 0
            end -= 1
            start[1] += 1
            start[0] = start[1]
        turns -= 1
    if len(snail_map) % 2:
        return out + [snail_map[len(snail_map) // 2][len(snail_map) // 2]]
    return out + [snail_map[len(snail_map) // 2][len(snail_map) // 2 - 1]]
