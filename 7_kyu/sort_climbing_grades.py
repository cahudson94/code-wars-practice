"""
My 5th kata, and 1st in a planned series of rock climbing themed katas.

In rock climbing (bouldering specifically), the V/Vermin (USA) climbing grades start at 'VB' (the easiest grade), and then go 'V0', 'V0+', 'V1', 'V2', 'V3', 'V4', 'V5' etc. up to 'V17' (the hardest grade). You will be given a list (lst) of climbing grades and you have to write a function (sort_grades) to return a list of the grades sorted easiest to hardest.

If the input is an empty list, return an empty list; otherwise the input will always be a valid list of one or more grades.

Please do vote, rank, and provide any feedback on the kata.
"""

def sort_grades(lst):
    grades = [
        "VB", "V0", "V0+", "V1",
        "V2", "V3", "V4", "V5",
        "V6", "V7", "V8", "V9",
        "V10", "V11", "V12", "V13",
        "V14", "V15", "V16", "V17"
    ]
    return sorted(lst, key=grades.index)

# alt solution
# def sort_grade(lst):
#     return sorted(lst, key=lambda x: int(x[1:]) if x not in ["VB", "V0", "V0+"] else 0 if x == "V0+" else -1 if x == "V0" else -2)
