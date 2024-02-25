"""
Task

You are given a string s.

Let us call a substring of s with 2 or more adjacent identical letters a group (such as "aa", "bbb", "cccc"...).

Let us call a substring of s with 2 or more adjacent groups a big group (such as "aabb","bbccc"...).

Your task is to count the number of big groups in the given string.
Examples

    "ccccoodeffffiiighhhhhhhhhhttttttts" => 3

    The groups are "cccc", "oo", "ffff", "iii", "hhhhhhhhhh", "ttttttt".

    The big groups are "ccccoo", "ffffiii", "hhhhhhhhhhttttttt".

    "gztxxxxxggggggggggggsssssssbbbbbeeeeeeehhhmmmmmmmitttttttlllllhkppppp" => 2

    The big groups are :

    "xxxxxggggggggggggsssssssbbbbbeeeeeeehhhmmmmmmm" and "tttttttlllll"

    "soooooldieeeeeer" => 0

    There is no big group.

Input/Output

    [input] string s

    A string of lowercase Latin letters.

    [output] an integer

    The number of big groups.
"""

def repeat_adjacent(st):
    count = 0
    in_set = 0
    current_letter = ""
    for idx, x in enumerate(st[1:-1]):
        if x == st[idx]:
            if in_set != 2:
                in_set = 1
        elif x == st[idx + 2]:
            if in_set == 1:
                in_set = 2
                count += 1
        else:
            in_set = 0
        current_letter = x
    return count
