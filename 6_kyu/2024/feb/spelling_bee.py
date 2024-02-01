"""
How many bees are in the beehive?

    bees can be facing UP, DOWN, LEFT, or RIGHT
    bees can share parts of other bees

Examples

Ex1

bee.bee     
.e..e..
.b..eeb

Answer: 5

Ex2

bee.bee     
e.e.e.e
eeb.eeb

Answer: 8
Notes

    The hive may be empty or null/None/nil/...
    Python: the hive is passed as a list of lists (not a list of strings)
"""

def count_bees(hive):
    return sum([''.join(x).count("bee") + ''.join(x).count("eeb") for x in hive])

def how_many_bees(hive):
    return count_bees(hive) + count_bees(zip(*hive)) if hive else 0
