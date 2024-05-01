# Reverse Prefix of Word

This is an Easy Two Pointers question

## Question
Given a 0-indexed string `word` and a character `ch`, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.
For example, if `word` = "abcdefd" and `ch` = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.

## Approach
The approach is very simple, we iterate over all the characters in `word`. If we find `ch` we slice the string at that index.
We then reverse the first half of the slice and join the second half and return it.
We iterate using a for loop and using an if statement check if the current character is equal to `ch`.
If it is we return the sliced string joined together with the first slice reversed.
After the end of the loop we return `word`, this is in case `ch` was  not found in the word.
