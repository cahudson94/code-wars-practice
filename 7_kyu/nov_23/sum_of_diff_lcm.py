"""
In this kata you need to create a function that takes a 2D array/list of non-negative integer pairs and returns the sum of all the "saving" that you can have getting the LCM of each couple of number compared to their simple product.

For example, if you are given:

[[15,18], [4,5], [12,60]]

Their product would be:

[270, 20, 720]

While their respective LCM would be:

[90, 20, 60]

Thus the result should be:

(270-90)+(20-20)+(720-60)==840

This is a kata that I made, among other things, to let some of my trainees familiarize with the euclidean algorithm, a really neat tool to have on your belt ;)
"""

def get_lcm(x, y):
    high = max(x, y)
    low = min(x, y)
    if not high or not low:
        return 0
    while high % low:
    	high, low = low, high % low
    return (x * y) / low
    
def sum_differences_between_products_and_LCMs(pairs):
    return sum([(x[0] * x[1]) - get_lcm(x[0], x[1]) for x in pairs])
