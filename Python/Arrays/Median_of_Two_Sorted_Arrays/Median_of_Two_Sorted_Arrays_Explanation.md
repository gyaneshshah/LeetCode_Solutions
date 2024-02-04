# Median of Two Sorted Arrays

This is a Hard Array question

## Question
Given two sorted arrays *nums1* and *nums2* of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

## Approach
Median means the middle value of a sorted list of numbers. In case there is an even list of numbers then we take the average of the middle two values.
We first combine both the arrays and sort them. I have saved them in **arr**.
We take the length of **arr** and check if it is even or odd. If even we return the middle two values divided by 2, if odd we return the middle value.
The index starts with 0 in Python, so make sure to subtract by 1.
