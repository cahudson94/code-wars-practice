"""
Task

Write a function that takes the string and finds a repeating character in this string (there may or may not be several of them), returns the minimum difference between the indices of these characters and the character itself.

    For example, in the string “aabcba” the minimum position difference of repeated characters will be equal to 1, since for the character “a” the position difference will be equal to 1.

The output should be a tuple.

    If there are no duplicate characters in the line, it should output None.

    The string can only lowercase ones, and nothing else!!!(there cannot be an empty line)

    If the difference between repeated characters is the same, print the first character encountered.

Examples of outputs:

"aa" => (1, 'a')

"aabbca" => (1, 'a')

"abka" => (3, 'a')

"abcded" => (2, 'd')

"abbbbbc" => (1, 'b')

"abc" => None
"""

def min_repeating_character_difference(txt):
    diff = None
    char = ""
    
    for x in range(len(txt) - 1):
        if txt[x] in txt[x + 1:]:
            current_diff = txt[x + 1:].index(txt[x]) + 1
            
            if diff is None or current_diff < diff:
                diff, char = current_diff, txt[x]
    
    return (diff, char) if diff else None
