"""
Cubic Tap Code

This works similarly to Tap Code except instead of being mapped onto a 5x5 square, letters are mapped onto a 3x3x3 cube, left to right, top to bottom, front to back with space being the 27th "letter".
Letters are represented by a series of taps (represented as dots .) and pauses (represented by spaces  ), for example A is represented as . . . (first column, first row, first layer) and  is represented as ... ... ... (third column, third row, third layer).

For reference the three layers of the cube are as follows (underscore represents space):

1  1  2  3 
1  A  B  C
2  D  E  F
3  G  H  I

2  1  2  3 
1  J  K  L
2  M  N  O
3  P  Q  R

3  1  2  3 
1  S  T  U
2  V  W  X
3  Y  Z  _

Your task (should you choose to accept it)

Create two functions encode() and decode(), to encode and decode strings to and from cubic tap code.
Input

encode() takes a string of uppercase letters and spaces and outputs a string of dots and spaces.
decode() takes a string of dots and spaces and outputs a string of uppercase letters and spaces.
All inputs will be valid.
Examples

encode("N") => ".. .. .."
encode("TEST") => ".. . ... .. .. . . . ... .. . ..."
encode("HELLO WORLD") => ".. ... . .. .. . ... . .. ... . .. ... .. .. ... ... ... .. .. ... ... .. .. ... ... .. ... . .. . .. ."

decode(".. .. ..") => "N"
decode(".. . ... .. .. . . . ... .. . ...") => "TEST"
decode(".. ... . .. .. . ... . .. ... . .. ... .. .. ... ... ... .. .. ... ... .. .. ... ... .. ... . .. . .. .") => "HELLO WORLD"
"""

from math import ceil

chars = {" ": ("... ... ...")}
for idx, x in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    col = (idx + 1) % 3 if (idx + 1) % 3 else 3
    row = ceil((idx + 1) % 9 / 3) if (idx + 1) % 9 else 3
    layer = 1 if (idx + 1) < 10 else 2 if (idx + 1) < 19 else 3
    chars[x] = f'{col * "."} {row * "."} {layer * "."}'
taps = {val: key for key, val in chars.items()}
    
def encode(string):
    return " ".join(map(chars.get, string))

def decode(string):
    string = string.split()
    return "".join(taps[' '.join(x)] for x in [string[i:i + 3] for i in range(0, len(string), 3)])
