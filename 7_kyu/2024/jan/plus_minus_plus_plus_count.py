"""
Count how often sign changes in array.
result

number from 0 to ... . Empty array returns 0
example

const arr = [1, -3, -4, 0, 5];

/*
| elem | count |
|------|-------|
|  1   |  0    |
| -3   |  1    |
| -4   |  1    |
|  0   |  2    |
|  5   |  2    |
*/

catchSignChange(arr) == 2;
"""

def catch_sign_change(lst):
    if not lst:
        return 0
    pos = lst[0] >= 0
    count = 0
    for x in lst[1:]:
        if (x >= 0 and not pos) or (x < 0 and pos):
            pos = not pos
            count += 1
    return count
