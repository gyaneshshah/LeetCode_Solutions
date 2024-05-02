# Largest Positive Integer That Exists With Its Negative

This is an Easy Array question

## Question
Given an integer array `nums` that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
Return the positive integer k. If there is no such integer, return -1.

## Approach
We are going to create another array with only the negative values called `num_dec` and we are going to sort `nums` in descending order.
We will then iterate over the sorted nums and if we find negative of that number in `num_dec` then we return that number. If the loop is completed and nothing is returned then we return -1.
