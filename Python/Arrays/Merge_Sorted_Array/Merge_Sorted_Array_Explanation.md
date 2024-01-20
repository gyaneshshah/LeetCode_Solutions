# Merge Sorted Array

This is an Easy Array question

## Question
You are given two integer arrays *nums1* and *nums2*, sorted in non-decreasing order, and two integers *m*and *n*, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array *nums1*.
To accommodate this, *nums1* has a length of *m* + *n*, where the first *m* elements denote the elements that should be merged, and the last *n* elements are set to 0 and should be ignored. 
*nums2* has a length of *n*.

## Approach
We can use a shortcut method and then append the values in **nums1**
We create a temp array and store the elements of **nums1** until **m** and then all the elements of **nums2**.
We sort it in decreasing order.
We use a for loop to change each element to match the values of **temp**
