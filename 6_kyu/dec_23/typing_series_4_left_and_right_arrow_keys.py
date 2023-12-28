"""
You are given a string of lowercase letters and spaces that you need to type out. However, there are some arrow keys inside. What do you do then?

Here are a few examples:

abcdefgh<<xyz -> abcdefxyzgh

Walkthrough:
                   v
type this: abcdefgh

go back two characters such that the pointer is right in front of 'f' then continue typing
      v
abcdefxyzgh

Try it yourself by typing on your keyboard! Ok, lets see more examples.

'extra large<<<<<< extra>>>>>> pizza' -> 'extra extra large pizza'

Walkthrough:

type this: extra large

go back six characters. the pointer is now right in front of 'a'
     v
extra large
           v
extra extra large

go forward six characters. the pointer is now at the front again
                 v
extra extra large
                       v
extra extra large pizza

Now lets add a new function: multiplication.

It's quite straightforward. Example: >*6 = >>>>>>

Examples:

'completing on <*3kata >*3codewars' -> 'completing kata on codewars'

' thstorm<*100>>>*1under' -> ' thunderstorm'

Okay, that second example might not have been the most obvious, however you can always try typing it out yourself on a text editor to check some cases.

Notes:

    In the function >*n, n is always a positive integer (1, 2, 3, ...)
    >>>*5 = >>(>*5) = >*7
    Although mentioned before, if the command tells you to go left but the pointer is at the start, it doesn't move. Same for the right command.

Good luck!
"""

def type_out(s):
    s = s.split("*")
    for idx, x in enumerate(s):
        if (x.endswith(">") or x.endswith("<")) and idx != len(s) - 1:
            next_val = s[idx + 1]
            num = ""
            for y in next_val:
                if not y.isdigit():
                    break
                num += y
            s[idx] = x[:-1] + (x[-1] * int(num))
            s[idx + 1] = s[idx + 1][len(num):]
    s = "".join(s).lstrip("<>").rstrip("<>")
    idx_offset = 0
    out_str = ""
    for x in s:
        if x == "<":
            idx_offset = max(idx_offset - 1, 0)
            continue
        if x == ">":
            idx_offset = min(idx_offset + 1, len(out_str))
            continue
        out_str = out_str[:idx_offset] + x + out_str[idx_offset:]
        idx_offset += 1
    return out_str
