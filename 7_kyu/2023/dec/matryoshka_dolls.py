"""


Matryoshka dolls are traditionally wooden dolls that can be nested by fitting smaller dolls into larger ones. Similarly, we can nest lists by placing smaller lists into larger ones, following specific rules.

Rules for Nesting:

    List A can be nested inside List B if:
        The minimum value in List A is greater than the minimum value in List B.
        The maximum value in List A is smaller than the maximum value in List B.

Example 1:

    List A: [2, 3, 9, 5]
    List B: [10, 2, 1]
    Explanation:
        min(A) = 2 > 1 = min(B)
        max(A) = 9 < 10 = max(B)
    Result: A can be nested inside B.

Example 2:

    List A: [4, 5]
    List B: [6, 3]
    Explanation:
        min(A) = 4 > 3 = min(B)
        max(A) = 5 < 6 = max(B)
    Result: A can be nested inside B.

Example 3:

    List A: [7, 1]
    List B: [7, 6, 5, 4, 3, 2]
    Explanation:
        Both lists share the same maximum value (7).
    Result: A cannot be nested properly inside B.

Example 4:

    List A: [1, 5]
    List B: [2, 6]
    Explanation:
        Elements in the lists overlap, making nesting impossible.
    Result: A cannot be nested inside B.

Example 5:

    List A: [1,2,3,4]
    List B: [0,3,5]
    List C: [2,2,3]]
    Explanation:
        List C and List A meet the criteria because 2 > 1 and 3 < 4.
        List A and List B also meet the criteria because 1 > 0 and 4 < 5.
    Result: List B can be nested inside List A, and List A can be nested inside List C.

Additional Notes:

    Sublists can be nested in either ascending (smallest to largest) or descending (largest to smallest) order.
    Strict nesting is required; no two lists can share the same maximum or minimum values.
"""

def matryoshka(lst):
	# sort the inner lists and then the outer
    lst = sorted(sorted(x) for x in lst)
    # get the min and max value from each list
    min_set = [x[0] for x in lst]
    max_set = [x[-1] for x in lst[::-1]]
    # check that there are no overlaps and collisions of the stacking biggest -> smallest or vice versa
    return sorted(set(min_set)) == min_set and sorted(set(max_set)) == max_set
