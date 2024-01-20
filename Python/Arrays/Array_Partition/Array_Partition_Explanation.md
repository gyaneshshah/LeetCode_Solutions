# Array Partition

This is an Easy Array question

## Question
Given an integer array *nums* of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

## Approach
When you look at the problem. You see that at every step we need to add the 2nd maximum number. We can sort the array in descending order and then add up the odd index (index starting from 0) elements.
We initialise a variable, I called it **ans** to store the sum and return in the end.
We sort the array **nums** in descending order. We run a for loop and add up all the odd index elements to **ans**
We return **ans**.
