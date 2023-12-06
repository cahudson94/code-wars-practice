"""
Task:

Given a list of integers l, return the list with each value multiplied by integer n.
Restrictions:

The code must not:

    contain *.
    use eval() or exec()
    contain for
    modify l

Happy coding :)
"""

def multiply(n, l):
    ans = []
    x = 0
    while x < len(l):
        if l[x]:
            ans.append(round((n / 1) / (1 / l[x])))
        else:
            ans.append(0)
        x += 1
    return ans
