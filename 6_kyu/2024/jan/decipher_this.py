"""
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

    the second and the last letter is switched (e.g. Hello becomes Holle)
    the first letter is replaced by its character code (e.g. H becomes 72)

    there are no special characters used, only letters and spaces
    words are separated by a single space
    there are no leading or trailing spaces

Examples

'72olle 103doo 100ya' --> 'Hello good day'
'82yade 115te 103o'   --> 'Ready set go'
"""

def get_char(word):
    ord_val = ""
    last_idx = None
    for idx, x in enumerate(word):
        if x.isdigit():
            ord_val += x
        else:
            last_idx = idx
            break
    return chr(int(ord_val)) + word[last_idx:] if last_idx else chr(int(ord_val))

def decipher_this(s):
    s = [get_char(x) for x in s.split()]
    return ' '.join(x[0] + x[-1] + x[2:-1] + x[1] if len(x) > 2 else x for x in s)
