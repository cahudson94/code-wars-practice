"""
Write a function that takes a list of at least four elements as an argument and returns a list of the middle two or three elements in reverse order.
"""

def reverse_middle(lst):
	x = len(lst) // 2 - 1
    return lst[x:-x][::-1]