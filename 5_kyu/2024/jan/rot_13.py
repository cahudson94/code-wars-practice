"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.

cheating?:
def rot13(message):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return message.translate(str.maketrans(alpha + alpha.upper(), alpha[13:] + alpha[:13] + alpha.upper()[13:] + alpha.upper()[:13]))
"""

def rot13(message):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    for x in alpha:
    	if x in alpha:
    		out += alpha[(alpha.index(x) + 13) % 26]
    	elif x.lower() in alpha:
    		out += alpha[(alpha.index(x.lower()) + 13) % 26]
    	else:
    		out += x
    return out
