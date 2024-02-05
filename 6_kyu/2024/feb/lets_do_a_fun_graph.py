"""
You have done some data collection today and you want the data to be well presented by a graph so you have decided to make a quick diagram.
Suppose that for this kata your data is presented by an array by their value eg [10,5,3,1,4], then you must present your data as follows:


for data = [10,5,3,1,4] :
 ____ ........................ ^ 10
|    |........................ | 9
|    |........................ | 8
|    |........................ | 7
|    |........................ | 6
|    | ____ .................. | 5
|    ||    |............ ____  | 4
|    ||    | ____ ......|    | | 3
|    ||    ||    |......|    | | 2
|    ||    ||    | ____ |    | | 1
|    ||    ||    ||    ||    | | 0

GOOD TO KNOW :

    Each bar is always of width 6.

    The vertical axis must be surrounded with one space character on each side.

    No trailing spaces on any line.

    For this kata we use :
        the following characters : '_',' ','|','.','^'.
        some numbers.

    Return type :
        Your code must return a character string joined by \n.
        [] and [0] has different returns "" and " ____  ^ 0"

CRITERIA :

    The length of the array is always less than 50.
    The value of a data is also less than 50 and always positive.

GOOD LUCK :)

optimized:
def graph(arr):
    if not arr: 
        return ''
    top, res = max(arr), []
    for i in range(top, -1, -1):
        row = ''.join(' ____ ' if x == i else '......' if x < i else '|    |' for x in arr) 
        flag = ' {} {}'.format('|' if i < top else '^', i)
        res.append(row + flag)
    return '\n'.join(res)
"""

def graph(arr):
    if not arr:
        return ""
    ordered = sorted(arr, reverse=True)
    max_bar = ordered[0]
    out, seen = [], []
    bar = " ____ "
    end = f" ^ {ordered[0]}"
    for y in range(max_bar + 1):
        line = []
        for i in range(len(arr)):
            if arr[i] == max_bar:
                line.append(bar)
                seen.append(i)
            elif i not in seen:
                line.append("......")
            else:
                line.append("|    |")
        out.append("".join(line) + end)
        max_bar -= 1
        end = f" | {max_bar}"
        if ordered:
            ordered.pop(0)
    return "\n".join(out)

