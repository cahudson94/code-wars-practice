"""
You are given a certain integer, n, n > 0. You have to search the partition or partitions, of n, with maximum product value.

Let'see the case for n = 8.

Partition                 Product
[8]                          8
[7, 1]                       7
[6, 2]                      12
[6, 1, 1]                    6
[5, 3]                      15
[5, 2, 1]                   10
[5, 1, 1, 1]                 5
[4, 4]                      16
[4, 3, 1]                   12
[4, 2, 2]                   16
[4, 2, 1, 1]                 8
[4, 1, 1, 1, 1]              4
[3, 3, 2]                   18   <---- partition with maximum product value
[3, 3, 1, 1]                 9
[3, 2, 2, 1]                12
[3, 2, 1, 1, 1]              6
[3, 1, 1, 1, 1, 1]           3
[2, 2, 2, 2]                16
[2, 2, 2, 1, 1]              8
[2, 2, 1, 1, 1, 1]           4
[2, 1, 1, 1, 1, 1, 1]        2
[1, 1, 1, 1, 1, 1, 1, 1]     1

So our needed function will work in that way: If there is only one partition with maximum product value, it will return a list of two elements, the unique partition and the product value.
Example (input -> output)

8 -> [[3, 3, 2], 18]

If there are more than one partition with maximum product value, the function should output the partitions in a length sorted way.
Example (input -> output)

10 --> [[4, 3, 3], [3, 3, 2, 2], 36]

Enjoy it!

optimized:
def find_part_max_prod(n):
	if n == 1: return [[1], 1]
	q, r = divmod(n, 3)
	if not r:
		return [[3] * q, 3 ** q]
	if r == 1:
		return [[4] + [3] * (q - 1), [3] * (q - 1) + [2, 2], 3 ** (q - 1) * 2 ** 2]
	return [[3] * q + [2], 3 ** q * 2]
"""

from math import prod

def make_partitions(n):
    partitions = {}
    catch = [0 for _ in range(n + 1)]
    iterrator = 1
    y = n - 1
    while iterrator != 0:
        x = catch[iterrator - 1] + 1
        iterrator -= 1
        while 2 * x <= y:
            catch[iterrator] = x
            y -= x
            iterrator += 1
        l = iterrator + 1
        while x <= y:
            catch[iterrator] = x
            catch[l] = y
            partitions.setdefault(prod(catch[:iterrator + 2]), []).append(sorted(catch[:iterrator + 2], reverse=True))
            x += 1
            y -= 1
        catch[iterrator] = x + y
        y = x + y - 1
        partitions.setdefault(prod(catch[:iterrator + 1]), []).append(sorted(catch[:iterrator + 1], reverse=True))
    return partitions
        
def find_part_max_prod(n):
    partitions = make_partitions(n)
    return sorted(partitions[max(partitions)], reverse=True) + [max(partitions)]
