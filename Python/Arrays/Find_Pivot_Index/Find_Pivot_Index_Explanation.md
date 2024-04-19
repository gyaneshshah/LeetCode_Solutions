# Assign Cookies

This is an Easy Array question

## Question
Given an array of integers `nums`, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

## Approach
For the 0 condition we check if the sum of all elements from index 1 till the end is 0, if it is we return 0.
Next we run a for loop from 1 till the length of `nums`. We check if the sum of `nums` from starting till an element before the current index is equal to the sum of `nums` starting from the next index till the end. 
If it is true then we return the current index i.
If not in the end we return -1.
