"""
Your job is to find the gravitational force between two spherical objects (obj1 , obj2).
input

Two arrays are given :

    arr_val (value array), consists of 3 elements
        1st element : mass of obj 1
        2nd element : mass of obj 2
        3rd element : distance between their centers
    arr_unit (unit array), consists of 3 elements
        1st element : unit for mass of obj 1
        2nd element : unit for mass of obj 2
        3rd element : unit for distance between their centers

mass units are :

    kilogram (kg)
    gram (g)
    milligram (mg)
    microgram (μg)
    pound (lb)

distance units are :

    meter (m)
    centimeter (cm)
    millimeter (mm)
    micrometer (μm)
    feet (ft)

Note

value of G = 6.67 × 10−11 N⋅kg−2⋅m2

1 ft = 0.3048 m

1 lb = 0.453592 kg

return value must be Newton for force (obviously)

μ copy this from here to use it in your solution
"""

def solution(arr_val, arr_unit) :
    distance_conversions = {
        "m": 1,
        "cm": .01,
        "mm": .001,
        "μm": .000001,
        "ft": .3048
    }
    mass_conversions = {
        "kg": 1,
        "g": .001,
        "mg": .000001,
        "μg": .000000001,
        "lb": .453592
    }
    mass = arr_val[0] * mass_conversions[arr_unit[0]] * arr_val[1] * mass_conversions[arr_unit[1]]
    dist = arr_val[2] * distance_conversions[arr_unit[2]]
    return 6.67 * (10 ** -11) * mass / dist ** 2
