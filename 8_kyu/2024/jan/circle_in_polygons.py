"""
You are the owner of a box making company.

Your company can produce any equal sided polygon box, but plenty of your customers want to transport circular objects in these boxes. Circles are a very common shape in the consumer industry. Tin cans, glasses, tyres and CD's are a few examples of these.

As a result you decide to add this information on your boxes: The largest (diameter) circular object that can fit into a given box.
"""

from math import tan, radians

def circle_diameter(sides, side_length):
    return side_length / tan(radians(180 / sides))
