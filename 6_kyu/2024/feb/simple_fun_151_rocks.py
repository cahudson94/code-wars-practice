"""
Task

Vanya gets bored one day and decides to enumerate a large pile of rocks.
He first counts the rocks and finds out that he has n rocks in the pile, then he goes to the store to buy labels for enumeration.

Each of the labels is a digit from 0 to 9 and each of the n rocks should be assigned a unique number from 1 to n.

If each label costs $1, how much money will Vanya spend on this project?
Input/Output

    [input] integer n

The number of rocks in the pile.

1 ≤ n ≤ 10^9

    [output] an integer

the cost of the enumeration.
Example

For n = 13, the result should be 17.

the numbers from 1 to n are:
1 2 3 4 5 6 7 8 9 10 11 12 13
we need 17 single digit labels:
1 2 3 4 5 6 7 8 9 1 0 1 1 1 2 1 3
each label cost $1, so the output should be 17.

optimized:
def rocks(n):
    l = len(str(n))
    return int(n + 1 - 10 ** (l - 1)) * l + sum(9 * i * 10**(i - 1) for i in range(l))
"""

def rocks(n):
    count = 0
	# calc max for number of digits
    for i in range(len(str(n))):
        count += 9 * int(str(i + 1) + "0" * i)
    return count - ((int("9" * len(str(n))) - n) * int(len(str(n))))
