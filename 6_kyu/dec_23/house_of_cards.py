"""
You want to build a standard house of cards, but you don't know how many cards you will need. Write a program which will count the minimal number of cards according to the number of floors you want to have. For example, if you want a one floor house, you will need 7 of them (two pairs of two cards on the base floor, one horizontal card and one pair to get the first floor). Here you can see which kind of house of cards I mean:

One floor:

 /\
 —
/\/\

Four floors:

    /\
    —
   /\/\
   — —
  /\/\/\
  — — —
 /\/\/\/\
 — — — —
/\/\/\/\/\

(See also http://www.wikihow.com/Build-a-Tower-of-Cards to see what it looks like in real life).
Note about floors:

This kata uses the British numbering system for building floors. If you want your house of cards to have a first floor, it needs a ground floor and then a first floor above that.
Details (Ruby & JavaScript & Python & R)

The input must be an integer greater than 0, for other input raise an error.
Details (Haskell)

The input must be an integer greater than 0, for other input return Nothing.
Details (COBOL)

The input will be an integer. If it is inferior or equal to 0, return -1.
"""

def house_of_cards(floors):
    assert floors > 0
    return sum(2 + 3 * x for x in range(floors + 1))
