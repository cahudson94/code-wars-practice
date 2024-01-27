"""
Your task is to write a function that receives as its single argument a string that contains numbers delimited by single spaces. Each number has a single alphabet letter somewhere within it.

Example : "24z6 1x23 y369 89a 900b"

As shown above, this alphabet letter can appear anywhere within the number. You have to extract the letters and sort the numbers according to their corresponding letters.

Example : "24z6 1x23 y369 89a 900b" will become 89 900 123 369 246 (ordered according to the alphabet letter)

Here comes the difficult part, now you have to do a series of computations on the numbers you have extracted.

    The sequence of computations are + - * /. Basic math rules do NOT apply, you have to do each computation in exactly this order.
    This has to work for any size of numbers sent in (after division, go back to addition, etc).
    In the case of duplicate alphabet letters, you have to arrange them according to the number that appeared first in the input string.
    Remember to also round the final answer to the nearest integer.

Examples :
"24z6 1x23 y369 89a 900b" = 89 + 900 - 123 * 369 / 246 = 1299
"24z6 1z23 y369 89z 900b" = 900 + 369 - 246 * 123 / 89 = 1414
"10a 90x 14b 78u 45a 7b 34y" = 10 + 45 - 14 * 7 / 78 + 90 - 34 = 60

optimized:
from operator import add, sub, mul, truediv

def do_math(st):
	st = sorted(st.split(), key=lambda x: next(c for c in x if c.isalpha()))
	st = [int(''.join(filter(str.isdigit, x))) for x in st]
	ops = [add, sub, mul, truediv]
	total = st[0]
	for idx, x in enumerate(st[1:]):
		total = ops[idx % 4](total, x)
	return round(total)
"""

def do_math(st) :
    out = {}
    for x in st.split():
        num = ""
        char = ""
        for y in x:
            if y.isdigit():
                num += y
            else:
                char = y
        out.setdefault(char, []).append(int(num))
    ordered_vals = []
    for x in sorted(out.keys()):
        ordered_vals.extend(out[x])
    total = ordered_vals[0]
    for idx in range(len(ordered_vals[1:])):
        if not idx % 4:
            total += ordered_vals[idx + 1]
        elif idx % 4 == 1:
            total -= ordered_vals[idx + 1]
        elif idx % 4 == 2:
            total *= ordered_vals[idx + 1]
        else:
            total /= ordered_vals[idx + 1]
    return round(total)
