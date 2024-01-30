# Intersection of Two Arrays

This is an Easy Array question

## Question
Given two integer arrays *nums1* and *nums2*, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

## Approach
We take the set of both the arrays to eliminate duplicates.
We use list comprehension to create an array by iterating over one array and checking if the elements are in the other.
We return that array.
