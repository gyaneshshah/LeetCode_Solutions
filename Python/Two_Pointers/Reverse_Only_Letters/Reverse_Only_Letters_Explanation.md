# Reverse Only Pointers

This is an easy Two Pointers question

## Question
Given a string `s`, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return `s` after reversing it.

## Approach
We only have to reverse the alphabets.
Using list comprehension we first create a list of only the alphabets in the string, storing it in `letters reversed`.
We then iterate over all the characters in the string and when we find a character that is an alphabet we replace that with the letter from `letters reversed` starting from the last letter.
We then return `s`. 
