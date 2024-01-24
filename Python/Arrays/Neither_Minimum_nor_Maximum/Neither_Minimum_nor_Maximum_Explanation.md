#  Neither Minimum nor Maximum

This is an Easy Array question

## Question
Given an integer array *nums* containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

## Approach
We can convert the array into a set and then sort it.
This will remove duplicates and we shall have the unique values in ascending order.
If the length is more than 2 then we can return the 2nd number (index=1).
If not, we return -1.

