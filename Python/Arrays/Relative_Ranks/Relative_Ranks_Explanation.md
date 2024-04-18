# Relative Ranks

This is an Easy Array question

## Question
You are given an integer array `score` of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

## Approach
We store the sorted `score` from descending to ascending.
We create an empty list `ans` to store the string values.
Then we iterate over all the scores and if we have the highest, second highest or the third highest we append Gold, Silver and Bronze Medals respectively.
For the other scores we append the position of that value in `sorted_score` + 1 (cause 0 indexing) in string format.
We return `ans`.
