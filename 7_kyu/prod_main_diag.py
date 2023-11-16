"""
Given a list of rows of a square matrix, find the product of the main diagonal.

Examples:

  [[1, 0], [0, 1]] should return 1
  [[1, 2, 3], [4, 5, 6], [7, 8, 9]] should return 45

http://en.wikipedia.org/wiki/Main_diagonal
"""

from math import prod
def main_diagonal_product(mat):
    return prod([mat[x][x] for x in range(len(mat))])
