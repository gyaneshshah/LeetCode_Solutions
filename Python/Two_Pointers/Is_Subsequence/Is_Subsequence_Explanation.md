# Is Subsequence

This is an Easy Two Pointer question

## Question
Given two strings `s` and `t`, return true if `s` is a subsequence of `t`, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

## Approach
We take care of the edge case first. If string `s` is empty, we return True.
We initialise an int `ind` to 0 for indexing.
We iterate over all characters in `t`, if the current character is equal to the first character of `s`, then only we increment `ind`.
This will make sure to check if the characters in `s` are present in `t` in the same sequence.
Once the characters in `s` are over meaning the index has reached the end, that means `s` is a subsequence. We add an if statement to return True in this case.
If the loop gets over and all characters of `s` are not covered then we return False.
