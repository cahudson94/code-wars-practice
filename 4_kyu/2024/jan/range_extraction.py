"""
A format for expressing an ordered list of integers is to use a comma separated list of either

    individual integers
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

Courtesy of rosettacode.org

optimized:
def solution(args):
    args = sorted(args)
    range_start = range_end = args[0]
    out = []
    for x in args[1:] + [None]:
    	if x != range_end + 1:
			if range_start == range_end:
				out.append(str(range_start))
			elif range_end - range_start < 2:
				out.extend([str(range_start), str(range_end)])
			else:
				out.append(f"{range_start}-{range_end}")
			range_start = x
    	range_end = x
	return ','.join(out)
"""

def solution(args):
    args = sorted(args)
    range_start = None
    range_end = None
    out = []
    for idx, x in enumerate(args):
        if range_start is None:
            range_start = x
        elif range_end is None:
            if x == range_start + 1:
                range_end = x
            else:
                out.append(str(range_start))
                range_start = x
        else:
            if x == range_end + 1:
                range_end = x
            else:
                if range_end - range_start < 2:
                    out.append(str(range_start))
                    out.append(str(range_end))
                else:
                    out.append(f"{range_start}-{range_end}")
                range_start = x
                range_end = None
    if range_end is not None:
        if range_end - range_start < 2:
            out.append(str(range_start))
            out.append(str(range_end))
        else:
            out.append(f"{range_start}-{range_end}")
    else:
        out.append(str(range_start))
    return ','.join(out)
