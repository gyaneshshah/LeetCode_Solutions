# Find the Pivot Integer

This is an Easy Math question

## Question
Given a positive integer n, find the pivot integer x such that:
The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

## Approach
We run a for loop from **n**/2 i.e half of **n** to **n**.
For each value of **n** we check if the sum of numbers up till there are equal to the sum of number from there till **n**. 
If it is present we break the loop and return the current value. If not we return -1.
