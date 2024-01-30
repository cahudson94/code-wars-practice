"""
Task

Create a function that takes a list of integers and a group length as parameters. Your task is to determine if it's possible to split all the numbers from the list into groups of the specified length, while ensuring that consecutive numbers are present within each group.
Input

lst / arr: A list / array of integers representing the numbers to be divided into groups.

group_len / groupLen: An integer indicating the desired length of each group.
Output

The function should return True if it's possible to create groups according to the criteria, and False otherwise.
Examples

consecutive_nums([1, 3, 5], 1) ➞ True
# It is always possible to create groups of length 1.

consecutive_nums([5, 6, 3, 4], 2) ➞ True
# Two groups of length 2: [3, 4], [5, 6]

consecutive_nums([1, 3, 4, 5], 2) ➞ False
# It is possible to make one group of length 2, but not a second one.

consecutive_nums([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) ➞ True
# [1, 2, 3], [2, 3, 4], [6, 7, 8]

consecutive_nums([1, 2, 3, 4, 5], 4) ➞ False
# The list length is not divisible by the group’s length.

Input Constraints

    3 <= len(lst) <= 10^4
    1 <= group_len <= 10
"""

def consecutive_nums(lst, group_len):
    if len(lst) % group_len:
        return False
    if group_len == 1:
        return True

    lst = sorted(lst)
    counts = {}
    for x in lst:
        counts.setdefault(x, 0)
        counts[x] += 1
    for val in lst[:-group_len + 1]:
        if not counts[val]:
            continue
        n = counts[val]
        for x in range(val, val + group_len):
            if counts.get(x, 0) < n:
                return False
            counts[x] -= n
    return not sum(counts.values())
