"""
Background

A spider web is defined by

    "rings" numbered out from the centre as 0, 1, 2, 3, 4

    "radials" labelled clock-wise from the top as A, B, C, D, E, F, G, H

Here is a picture to help explain:
[source: imgur.com]
Web Coordinates

As you can see, each point where the rings and the radials intersect can be described by a "web coordinate".

So in this example the spider is at H3 and the fly is at E2
Kata Task

Our friendly jumping spider is resting and minding his own spidery business at web-coordinate spider.

An inattentive fly bumbles into the web at web-coordinate fly and gets itself stuck.

Your task is to calculate and return the distance the spider must jump to get to the fly.
Example

The solution to the scenario described by the picture is 4.63522
Notes

    The centre of the web will always be referred to as A0
    The rings intersect the radials at evenly spaced distances of 1 unit

Good Luck!
DM

optimized:
from math import cos, radians

def spider_to_fly(spider, fly):
    a, b = int(spider[1]), int(fly[1])
    return (a ** 2 + b ** 2 - 2 * a * b * cos(radians((ord(spider[0]) - ord(fly[0])) * 45))) ** 0.5
"""

from math import cos, radians

def spider_to_fly(spider, fly):
    if spider == fly:
        return 0
    if spider == "A0" or fly == "A0":
        return max(int(fly[1]), int(spider[1]))
    if fly[0] == spider[0]:
        return abs(int(fly[1]) - int(spider[1]))
    radials = "ABCDEFGH"
    distances = {x: {y: 0 for y in radials[:idx] + radials[idx+1:]} for idx, x in enumerate(radials)}
    for idx, x in enumerate(radials):
        for i in range(3):
            if idx + i + 1 < len(radials):
                distances[x][radials[idx + i + 1]] = 1 + i
            else:
                distances[x][radials[(idx + i + 1) % 8]] = 1 + i
            if idx - i - 1 < len(radials):  
                distances[x][radials[idx - i - 1]] = 1 + i
        distances[x][radials[idx - 4]] = 4
    if distances[spider[0]][fly[0]] == 4:
        return int(spider[1]) + int(fly[1])
    if distances[spider[0]][fly[0]] == 3:
        return (int(spider[1]) ** 2 + int(fly[1]) ** 2 - (2 * int(fly[1]) * int(spider[1]) * cos(radians(135)))) ** .5
    if distances[spider[0]][fly[0]] == 2:
        return (int(spider[1]) ** 2 + int(fly[1]) ** 2) ** .5
    return (int(spider[1]) ** 2 + int(fly[1]) ** 2 - (2 * int(fly[1]) * int(spider[1]) * cos(radians(45)))) ** .5

