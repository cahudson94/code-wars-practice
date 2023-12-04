"""
We are given two arrays of integers A and B and we have to output a sorted array with the integers that fulfill the following constraints:

    they are present in both ones

    they occur more than once in A and more than once in B

    their values are within a given range

    thay are odd or even according as it is requested

arrA = [1, -2, 7, 2, 1, 3, 7, 1, 0, 2, 3]
arrB = [2, -1, 1, 1, 1, 1, 2, 3, 3, 7, 7, 0]
rng = [-4, 4] # is the range of the integers from -4 to 4 (inclusive)
wanted = 'odd'

Process to obtain the result:

0, 1, 2, 3, 7, are the numbers present in arrA and arrB
1, 2, 3, 7,  occur twice or more in arrA and arrB
1, 2, 3,  are in the range [-4, 4]
1, 3, are odd
output: [1, 3] 

For the case:

arrA = [1, -2, 7, 2, 1, 3, 4, 7, 1, 0, 2, 3, 0, 4]
arrB = [0, 4, 2, -1, 1, 1, 1, 1, 2, 3, 3, 7, 7, 0, 4]
rng = [-4, 4]
wanted = 'even'
output[0, 2, 4] 

If there are no elements to fulfill the constraints given above the result will be the empty array.

The name of the function with the corresponding order of its arguments and the data structure for the output is as it follows below:

find_arr(arrA, arrB, rng, wanted) ----> []

(For Javascript the function will be findArr()) Features of the tests:

Number of Random Tests = 300
Length of the arrays A and B between 1000 and 10000

You may assume that you will always receive valid entries for all the tests. Enjoy it!! Very Important: For javascript run the tests only in Node v6.6.0 and Node v6.6.0/Babel.
"""

def find_arr(arrA, arrB, rng, wanted):
    a_counts = {}
    b_counts = {}
    a_repeats = set()
    answer = set()
    for x in arrA:
        a_counts[x] = a_counts.get(x, 0) + 1
        if a_counts[x] > 1:
            a_repeats.add(x)
    for x in arrB:
        b_counts[x] = b_counts.get(x, 0) + 1
        if b_counts[x] > 1 and x in a_repeats:
            answer.add(x)
    return sorted([x for x in answer if x in range(rng[0], rng[1] + 1) and x % 2 == (wanted == "odd")])
