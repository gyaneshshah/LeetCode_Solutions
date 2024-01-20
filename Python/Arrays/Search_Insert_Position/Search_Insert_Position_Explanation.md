# Search Insert Position

This is an Easy Array question

## Question
Given a sorted array of distinct integers and a *target* value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

## Approach
We know the array is already sorted. We need to check first if the **target** value is present in the array or not.
If we find it we need to return the index, if not we need to insert it in order and give the index.
What we can do is append the **target** to the array **nums** and then sort it.
We then return the first occurence of the **target**. 
