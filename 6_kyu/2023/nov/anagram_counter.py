"""
An anagram is a word, a phrase, or a sentence formed from another by rearranging its letters. An example of this is "angel", which is an anagram of "glean".

Write a function that receives an array of words, and returns the total number of distinct pairs of anagramic words inside it.

Some examples:

    There are 2 anagrams in the array ["dell", "ledl", "abc", "cba"]
    There are 7 anagrams in the array ["dell", "ledl", "abc", "cba", "bca", "bac"]
"""

def anagram_counter(words):
    word_counts = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        word_counts[sorted_word] = word_counts.get(sorted_word, 0) + 1
    return sum((count - 1) * (count / 2) for count in word_counts.values())
