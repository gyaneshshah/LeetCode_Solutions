# Contains Duplicate II
This is an Easy Array question

## Question
Given an integer array `nums` and an integer `k`, return true if there are two distinct indices i and j in the array such that `nums[i]` == `nums[j]` and abs(i - j) <= `k`.

## Approach
We are going to use a hash table for this approach. We will keep a track of all the unique value in `nums` and when we come across any duplicate value, we shall check for the `k` condition.
We create an empty dictionary `dup`. We iterate over `nums`. If the no in `nums` is not a key in `dup` then we create one with the value being the index.
If the key exists we check for the absolute difference condition, if it passes we return true, if not we update the value of that key to the new index.
The reason we update it to the new index is, if there is another occurence of the same no then the difference is going to be smaller if we have the latest index.
We return False in the end if there are no duplicates with the condition.
