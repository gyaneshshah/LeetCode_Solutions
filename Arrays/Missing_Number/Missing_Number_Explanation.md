# Missing Number

This is an Easy Array Questions

## Question
We need to find out a missing number from a (0,n) range. We are given an array *nums* having *n* values which has all the elements from the range 0 to n except one. 

## Approach
We know the range, we can calculate **n** by getting the length of **nums**, Using the summation formula [n(n+1)/2] we calculate the sum of all elements from the range and subtract the sum of **nums**. 
The value remaining will be our number. Return it.
