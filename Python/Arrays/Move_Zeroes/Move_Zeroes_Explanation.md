# Move Zeroes

This is an Easy Array question

## Question
We have an array *nums* and we need to move all the zero elements to the end of the array, without copying the array and in place without changing the relative order of the non-zero elements.

## Approach
We take two while loops. One to remove zeros until there are none and also count them, the other to append zeros until the count is done.
We need not return nums as the program asks us to only change the value of it and not return anything.
