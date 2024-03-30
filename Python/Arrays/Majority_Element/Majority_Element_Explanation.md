# Majority Element

This is an Easy Array question

### Question
Given an array `nums` of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

### Approach
We create a **set** of all the `nums` and store it in `uniqnums`.
We calculate the floor of n/2 and store it in `check`.
We iterate over the values in the set `uniqnums` and check if for any number the count is greater than `check`.
If it is, we return that number and break the loop.
