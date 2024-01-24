# Number of Steps to Reduce a Number to Zero

This is an Easy Math question

## Question
Given an integer *num*, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

## Approach
We shall use a while loop to check if **num** has reached zero. In the while loop we shall use if-else to perform operations on **num**.
We initialise a variable called **cnt** to count the number of steps.
We use the while loop to check if **num** has reached zero. Inside we check for **num** if it is even or odd.
If it is even we divide it by 2.
If odd we subtract it by 1
We return **cnt** in the end.
