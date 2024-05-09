# Find the Maximum Achievable Number

This is an Easy Math question

## Question
You are given two integers, num and t.

An integer x is called achievable if it can become equal to `num` after applying the following operation no more than `t` times:
Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
Return the maximum possible achievable number. It can be proven that there exists at least one achievable number.

## Approach
When we look at the examples we notice a pattern, the maximum possible achievable number is equal to the sum of `num` and 2 times `t`.
We return the sum of `num` and 2 times `t`.
