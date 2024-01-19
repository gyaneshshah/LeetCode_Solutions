# Next Greater Element

This is an Easy Array Question

## Question
We are given two arrays *nums1* and *nums2*. *nums1* is a subset of *nums2*. For every element in *nums1* we need to find the value in *nums2* and find the greater element after it. 
If there is no greater element than that, then return -1 for that value.

## Approach 
Create an empty array to store the result array. I have named it **ans**. I took the lengths of both the array.
Next run a nested loop. The outer loop shall run through all the elements of **nums1**.
For each value of **nums1** we shall find the index of that value in **nums2**.
We shall temporarily append -1 to the **ans** array.
The inner loop will run from that index value to the end of **nums2**
The inner loop will check for the next greater number, if found it will replace the -1 for that value to the greater value and break the inner loop.
We shall return the **ans** array.
