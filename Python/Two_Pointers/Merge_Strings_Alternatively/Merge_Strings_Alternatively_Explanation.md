# Merge Strings Alternatively

This is an Easy Two Pointer question

## Question
You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

## Approach
We store the length of `word1` and `word2` in `word1_len` and `word2_len` respectively.
We initialise a counter `i` and an empty string `ans_s`.
We run a while loop until `i` is smaller than `word1_len` and `word2_len`.
Now we will add the letters, first from `word1` and then from `word2`. We will increment `i`.
After the loop ends, we still need to check for the remaining letters in the bigger string.
We check using if-else, which is the bigger string and then we add the remaining letters from `i` till the string's length.
We return `ans_s`.
