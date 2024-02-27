"""
Overview

Jack's chemistry teacher gave him piles of homework to complete in just ONE day and he just can't seem to get it done!
All the questions are of the same type, making the homework both tedious and time-consuming.

He has been given the chemical formula of an element and is required to find out how many moles will be there in a given mass of that element.

Will you help him write out a function to help him finish his homework?
Task

Write a function count_the_moles which returns the number of moles present in a given mass of a substance.

You will be given:

    The mass of substance taken (in grams)
    The chemical formula of that substance

Important Notes

    The chemical formulas will not be written with subscript:

i.e, Carbon dioxide = CO2

    The substances will be very simple. The no. of atoms of each element will not exceed 9

i.e, substances like sugar (C12H22O11) will not be given, but substances like carbon dioxide (CO2) will be given

    The only elements in the substance will be:
    	Carbon (atomic mass = 12u),
    	Hydrogen (atomic mass = 1u),
    	Nitrogen (atomic mass = 14u),
    	Oxygen (atomic mass = 16u),
    	Potassium (atomic mass = 39u),
    	Phosphorus (atomic mass = 31u),
    	Sulphur (atomic mass = 32u),
    	Fluorine (atomic mass = 19u)

All these elements are preloaded in the dictionary named atomic_masses
"""

from preloaded import atomic_masses
def count_the_moles(mass_of_substance,chemical_formula):
    elements = {}
    for idx, x in enumerate(chemical_formula):
        if not x.isdigit():
            elements.setdefault(x, 0)
            elements[x] += 1 * atomic_masses[x]
        else:
            chem = chemical_formula[idx - 1]
            elements[chem] += (int(x) - 1) * atomic_masses[chem]
    return mass_of_substance / sum(elements.values())
