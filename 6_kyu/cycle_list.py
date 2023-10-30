"""
Implement a function which when given the arguments

    Direction to which to cycle the current value
    List of values
    Current value

returns the value next to current value in the specified direction.

The function should pick the next value from the other side of the list in case there are no values in the given direction.
Examples

# Given the direction 1, returns the value next to 1 on the right
cycle(1, [1,2,3], 1)   # => 2

# Given the direction -1 and value 1, wraps around list returning the last element
cycle(-1, [1,2,3], 1)  # => 3

# 0 does not exist in the list, returns null
cycle(1, [1,2,3], 0)   # => null

# Corner case: multiple instances of given value, picks next relative to first occurrence
cycle(1, [1,2,2,3], 2) # => 2
"""

def cycle(d, v, c):
    try:
        return v[v.index(c) + d]
    except ValueError:
        return None
    except IndexError:
    	return v[0]
