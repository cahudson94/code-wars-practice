"""
Mount the Bowling Pins!
Task:

Did you ever play Bowling? Short: You have to throw a bowl into 10 Pins arranged like this:

I I I I  # each Pin has a Number:    7 8 9 10
 I I I                                4 5 6
  I I                                  2 3
   I                                    1

You will get an array of integers between 1 and 10, e.g. [3, 5, 9], and have to remove them from the field like this:

I I   I
 I   I
  I   
   I   

Return a string with the current field.
Note that:

    The pins rows are separated by a newline (\n)
    Each Line must be 7 chars long
    Fill the missing pins with a space character ( )

Have fun!
"""

def bowling_pins(arr : list[int]) -> str:
    pins = ["I" if x not in arr else " " for x in range(1, 11)]
    rows = []
    for i in range(4):
        rows.append(pins[:i + 1])
        pins = pins[i + 1:]
    return "\n".join(" ".join(x for x in row).center(7) for row in rows[::-1])
