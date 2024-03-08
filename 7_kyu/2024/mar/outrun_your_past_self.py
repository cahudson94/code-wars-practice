"""
You are running a race on a circular race track against the ghost of your past self.

Each time you lap your ghost, you get a confidence boost because you realize how much faster you got.

Given your speed (km/h), your ghosts speed (km/h), the length of the circular race track (km) and the time you run (h),
predict how often you will lap your ghost.

Lapping your ghost means going from being behind your ghost to being in front of your ghost.
"""

from math import ceil

def number_lappings(my_speed,ghost_speed,time,round_length):
    if my_speed <= ghost_speed:
        return 0
    return ceil(((my_speed * time) - (ghost_speed * time)) / round_length) - 1
