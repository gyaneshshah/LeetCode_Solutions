# Range Sum Query-Immutable

This is an Easy Array question

## Question
Given an integer array `nums`, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the `NumArray` class:
`NumArray`(int[] nums) Initializes the object with the integer array nums.
int `sumRange`(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

## Approach
We instantiate an object `arr` which is equal to `nums`.
In the `sumRange` function we return the sum of values between left and right (inclusive).
