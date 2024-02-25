"""
Santa is coming to town and he needs your help finding out who's been naughty or nice. You will be given an entire year of JSON data following this format:

{
    January: {
        '1': 'Naughty','2': 'Naughty', ..., '31': 'Nice'
    },
    February: {
        '1': 'Nice','2': 'Naughty', ..., '28': 'Nice'
    },
    ...
    December: {
        '1': 'Nice','2': 'Nice', ..., '31': 'Naughty'
    }
}

Your function should return "Naughty!" or "Nice!" depending on the total number of occurrences in a given year (whichever one is greater).
If both are equal, return "Nice!"
"""

def naughty_or_nice(data):
    nice = 0
    for x in data:
        nice += sum([1 if y == "Nice" else -1 for y in data[x].values()])
    return "Nice!" if nice >= 0 else "Naughty!"
