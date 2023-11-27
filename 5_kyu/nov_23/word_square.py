"""
A Word Square is a set of words written out in a square grid, such that the same words can be read both horizontally and vertically.
The number of words, equal to the number of letters in each word, is known as the order of the square.

For example, this is an order 5 square found in the ruins of Herculaneum:

Given a string of various uppercase letters, check whether a Word Square can be formed from it.

Note that you should use each letter from letters the exact number of times it occurs in the string.
If a Word Square can be formed, return true, otherwise return false.

Example

    For letters = "SATORAREPOTENETOPERAROTAS", the output should be WordSquare(letters) = true.
    It is possible to form a word square in the example above.

    For letters = "AAAAEEEENOOOOPPRRRRSSTTTT", (which is sorted form of "SATORAREPOTENETOPERAROTAS"), the output should also be WordSquare(letters) = true.

    For letters = "NOTSQUARE", the output should be WordSquare(letters) = false.

Input/Output

    [input] string letters

    A string of uppercase English letters.

    Constraints: 3 ≤ letters.length ≤ 100.

    [output] boolean

    true, if a Word Square can be formed;

    false, if a Word Square cannot be formed.
"""

def word_square(letters):
    count = len(letters)
    root = int(count ** 0.5)
    letter_counts = {l: letters.count(l) for l in set(letters)}
    return root ** 2 == count and sum([x % 2 for x in letter_counts.values()]) <= root
