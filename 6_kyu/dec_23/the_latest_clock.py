"""
Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

The time should be in HH:MM format.

Examples:

digits: 1, 9, 8, 3 => result: "19:38"
digits: 9, 1, 2, 5 => result: "21:59"

Notes

    Result should be a valid 24-hour time, between 00:00 and 23:59.
    Every input has a valid answer.
"""

def get_max_digit(pos, counts, out_str, less_than_5):
    max_dig = 9
    if pos == 0:
        if less_than_5 == 2:
            max_dig = 1
        else:
            max_dig = 2
    elif pos == 1:
        if out_str and out_str[0] == "2":
            max_dig = 3
    elif pos == 2:
        max_dig = 5
    for i in range(max_dig, -1, -1):
        if counts[i]:
            counts[i] -= 1
            out_str += str(i)
            return counts, out_str
    

def latest_clock(a, b, c, d):
    out_str = ""
    counts = {i: [a, b, c, d].count(i) for i in range(10)}
    less_than_5 = sum([counts[i] for i in range(6)])
    for x in range(4):
        print(x, out_str)
        counts, out_str = get_max_digit(x, counts, out_str, less_than_5)
        if x == 1:
            out_str += ":"
    return out_str
