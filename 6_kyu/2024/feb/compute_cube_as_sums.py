"""
Can you compute a cube as a sum?

In this Kata, you will be given a number n (where n >= 1) and your task is to find n consecutive odd numbers whose sum is exactly the cube of n.

Mathematically:
n3=a1+a2+a3+…+an
a2=a1+2,a3=a2+2,…,an=an−1+2
a1,a2,…,an are all odds

For example:

n = 3, result = [7, 9, 11], because 7 + 9 + 11 = 27, the cube of 3. Note that there are only n = 3 elements in the array.

Write a function that when given n, will return an array of n consecutive odd numbers with the sum equal to the cube of n (n*n*n).
"""

def find_summands(n):
    return [i for i in range(n ** 2 - (n - 1), n ** 2 + n, 2)]  
