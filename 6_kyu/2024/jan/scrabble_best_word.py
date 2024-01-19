"""
You're playing to scrabble. But counting points is hard.

You decide to create a little script to calculate the best possible value.

The function takes two arguments :

    `points` : an array of integer representing for each letters from A to Z the points that it pays
    `words` : an array of strings, uppercase


You must return the index of the shortest word which realize the highest score.

If the length and the score are the same for two elements, return the index of the first one.
"""

def get_best_word(points, words):
    max_score, max_idx, word_length = 0, 0, 0
    for idx, word in enumerate(words):
        score = sum(points[ord(x) - 65] for x in word)
        if score > max_score:
            max_score = score
            max_idx = idx
            word_length = len(word)
        elif score == max_score and len(word) < word_length:
            max_idx = idx
            word_length = len(word)
    return max_idx
