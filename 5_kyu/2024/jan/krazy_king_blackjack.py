"""
Krazy King BlackJack is just like blackjack, with one difference: the kings!
Instead of the kings being simply worth 10 points, kings are worth either 10 points or some other number of points announced by the dealer at the start of the game.
Whichever value yields the best hand is the one that plays (much like how aces are worth either 1 or 11 points).

Write a function that inputs a list of strings (representing a blackjack hand) and an integer that represents the alternative king value.
The function should output an integer representing the value of the hand if it is less than or equal to 21, and False if it exceeds 21.
Other than the alternative king value, normal blackjack rules apply.

The cards, in order ace-through king, are represented as strings as follows:

['A', '2', '3','4', '5', '6','7', '8', '9','10', 'J', 'Q','K']

A hand has between 2 and 20 cards, inclusive.
The alternative king value is between 2 and 9, inclusive.

Blackjack rules: the value of a hand is determined by maximizing the value of the sum of its cards while not exceeding 21 if possible.
Number cards are worth their value, Jacks ('J') and Queens ('Q') are worth 10, Aces are worth either 1 or 11, and kings, again, are worth either 10 or their alternative value.

optimized:

from itertools import product

def krazy_king_blackjack(hand, king_value):
    vals = {str(x): (x,) for x in range(2, 11)}
    vals.update({"J": (10,), "Q": (10,), "K": (10, king_value), "A": (1, 11)})
    hands = [sum(hand_vals) for hand_vals in product(*[vals[card] for card in hand]) if sum(hand_vals) < 22]
    return max(hands) if hands else False
"""

from itertools import combinations_with_replacement

def krazy_king_blackjack(hand, king_value):
    vals = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10}
    hand_val = sum(vals[x] for x in hand if x in vals)
    ace_count = hand.count("A")
    king_count = hand.count("K")
    king_options = []
    hand_options = []
    if king_count:
        for x in combinations_with_replacement((1,0), king_count):
            king_options.append(sum(10 if y == 1 else king_value for y in x) + hand_val)
    if ace_count:
        for x in combinations_with_replacement((1,0), ace_count):
            if king_options:
                for hand_option in king_options:
                    hand_options.append(sum(1 if y == 1 else 11 for y in x) + hand_option)
            else:
                hand_options.append(sum(1 if y == 1 else 11 for y in x) + hand_val)
    if not hand_options:
        if not king_options:
            return hand_val if hand_val < 22 else False
        vals = sorted(x for x in king_options if x < 22)
    else:
        vals = sorted(x for x in hand_options if x < 22)
    return vals[-1] if vals else False
