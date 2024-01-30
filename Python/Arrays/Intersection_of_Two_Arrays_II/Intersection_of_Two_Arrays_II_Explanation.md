# Intersection of Two Arrays II

This is an Easy Array question

## Question
Given two integer arrays *nums1* and *nums2*, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

## Approach
We can run a for loop to iterate over all numbers in one array. 
We can then check if it is present in the other array, if yes we append the no in the **ans** array and remove the no from the other array [to check for multiple entry]
We then return **ans**
