"""
Create a function that returns the total of a meal including tip and tax.
You should not tip on the tax.

You will be given the subtotal, the tax as a percentage and the tip as a percentage.
Please round your result to two decimal places.
"""

def calculate_total(subtotal, tax, tip):
    return round(subtotal * (1 + tax / 100.0 + tip / 100.0), 2)
