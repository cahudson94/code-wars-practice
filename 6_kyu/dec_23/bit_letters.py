"""
I often send "bit letter" to my colleagues to talk about our boss or what do we have for dinner.

A bit letter takes 1 char, just like ASCII, but there are some "parameters" in upper 3 bits to describe it.

0           0       0       0  0  0  0  0
[punctuation]   [capital]   [letter index]

[punctuation]

0 = null;
1 = space (before letter);
2 = comma (after letter);
3 = dot (after letter)
[capital]

0 = lowercase;
1 = uppercase;
[letter index]

The letter's index in alphabet, start with 0.

==========================

For example:

  'a'  = 0B00000000 = 0   (a)
  'A'  = 0B00100000 = ‭32‬  (A)
  " a" = 0B01000000 = 64  (space + a)
  "A," = 0B10100000 = ‭160‬ (A + comma)
  "a." = 0B11000000 = ‭192‬ (a + dot)

==========================

Complete function bit_letter(n), for example, if n=[39,4,11,11,142,86,14,17,11,195], function will return 'Hello, world.'.
"""

def bit_letter(n):
    out_str = ""
    str_key = "abcdefghijklmnopqrstuvwxyz"
    for x in n:
        bin_str = bin(x)
        if len(bin_str) < 10:
            bin_str = bin_str[:2] + ((10 - len(bin_str)) * "0") + bin_str[2:]
        letter = str_key[int(f"0b{bin_str[5:]}", 2)]
        if bin_str[4] == "1":
            letter = letter.upper()
        if bin_str.startswith("0b11"):
            out_str += f"{letter}."
        elif bin_str.startswith("0b10"):
            out_str += f"{letter},"
        elif bin_str.startswith("0b01"):
            out_str += f" {letter}"
        else:
            out_str += letter
    return out_str
