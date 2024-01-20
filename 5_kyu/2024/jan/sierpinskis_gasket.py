"""
Write a function that takes an integer n and returns the nth iteration of the fractal known as Sierpinski's Gasket.

Here are the first few iterations. The fractal is composed entirely of L and white-space characters; each character has one space between it and the next (or a newline).
0

L

1

L
L L

2

L
L L
L   L
L L L L

3

L
L L
L   L
L L L L
L       L
L L     L L
L   L   L   L
L L L L L L L L

optimized:
def sierpinski(n):
	out = ['L']
    for i in range(n):
        out_len = len(out)
        for j in range(out_len):
            out.append(out[j].ljust(out_len * 2) + out[j])
    return '\n'.join(out)
"""

def sierpinski(n):
    """Returns a string containing the nth iteration of the Sierpinski Gasket fractal"""
    if not n:
        return "L"
    out = [["L"], ["L", "L"]]
    for i in range(n - 1):
        base = 2 ** (i + 2)
        lines = [[" " for _ in range(base)] for _ in range(2 ** (i + 1))]
        for j in range(len(lines)):
            for k in range(base):
                if k < len(out[j]):
                    lines[j][k] = out[j][k]
                elif k >= base / 2:
                    l = k - base // 2
                    if l < len(out[j]):
                        lines[j][k] = out[j][l]                    
        out.extend(lines)
    return "\n".join([" ".join(y for y in x).rstrip() for x in out])
