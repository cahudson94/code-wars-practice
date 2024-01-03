"""
You need to write a password generator that meets the following criteria:

    6 - 20 characters long
    contains at least one lowercase letter
    contains at least one uppercase letter
    contains at least one number
    contains only alphanumeric characters (no special characters)

Return the random password as a string.

Note: "randomness" is checked by counting the characters used in the generated passwords - all characters should have less than 50% occurance.
Based on extensive tests, the normal rate is around 35%.
"""

from random import randint

def password_gen():
    pass_out = ""
    chars = randint(6, 20)
    while chars:
        if not len(pass_out) % 3:
            pass_out += str(randint(0,9))
        else:
            char = "abcdefghijklmnopqrstuvwxyz"[randint(0,25)]
            if not len(pass_out) % 2:
                char = char.upper()
            pass_out += char
        chars -= 1
    return pass_out
