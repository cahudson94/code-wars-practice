"""
You order a shirt for your friend that has a word written in sign language on it,
you would like to fool your friend into thinking it says something other than what it actually says.

Your friend is smart, but he can't know what he doesn't already know, he only knows a certain amount of letters in sign language.
Given the word on the shirt, the word you are attempting to make your friend believe is on the shirt,
and the letters in sign language your friends knows, figure out if he can tell that you are fooling him.
Return true if your friend can figure out you are fooling him, otherwise return false.

It is guaranteed that both words will be the same length and will be in lowercase letters (a-z)

Example 1:
Word on shirt: snack
Word you said: snake
Letters your friend knows: [c]

return true
Your friend knows the 4th letter is a c rather than a k.

If the word on the shirt and the word you told your friend is the same then you aren't fooling your friend, so you should return false

Example 2:
Word on shirt: snack
Word you said: snack
Letters your friend knows: [s, n, a, c, k]

return false 
Since you are not fooling your friend

Example 3:
Word on shirt: snake
Word you said: snack
Letters your friend knows: [c]

return true 
Your friend knows that the 4th letter is not a c

optimized:
return any(x != y and (x in friends_letters or y in friends_letters) for x, y in zip(shirt_word, your_word))
"""

def gaslighting(shirt_word:str, your_word:str, friends_letters:str) -> bool:
    if shirt_word == your_word:
        return False
    for x, y in zip(shirt_word, your_word):
        if x != your_word[idx] and (x in friends_letters or your_word[idx] in friends_letters):
            return True
    return False
