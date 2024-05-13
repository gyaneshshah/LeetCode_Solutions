# Word Pattern
This is an Easy Hash Table question

## Question
Given a `pattern` and a string `s`, find if `s` follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.

## Approach
We are going to use two dictionaries and give each unique letter/word a number so to compare the pattern.
We will first split the string `s` to get all the words. If the length of `pattern` is not equal to the no of words then we return false immediately.
We create two dictionaries `dict1` and `dict2`. Two values variables to keep the count and add them as values.
We will then iterate over the list of words. For every unique char/word we will store it in their respective dictionary. Then we will compare the current index's `pattern` and `s`'s value in the dictionary,
if it is not equal then we return False.
If the loop runs till the end then we return True.
