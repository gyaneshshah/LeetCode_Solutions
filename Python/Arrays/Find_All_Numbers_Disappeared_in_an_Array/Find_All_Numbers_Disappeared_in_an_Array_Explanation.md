# Find All Numbers Disappeared in an Array

This is an Easy Array question

## Question
We are given an array *nums* with *n* integers within the range 1 to *n*. We need to find the missing numbers in the array from the range 1 to *n*. We need to complete this in 0(n) runtime without using extra space.

## Approach
We create an array **complete_list** with all the numbers from 1 to **n**. 
We know when the **nums** array has numbers within the range 1 to **n** and total values are equal to **n**. So there are going to be a lot of numbers repeated.
We create a set of the **nums** array and store it in **uniquenums**
Using list comprehension we create an **ans** array and store the values from **complete_list** that are not in **uniquenums**.
We return **ans**.
