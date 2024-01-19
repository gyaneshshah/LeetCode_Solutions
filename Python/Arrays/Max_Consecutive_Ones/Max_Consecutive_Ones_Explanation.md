# Max Consecutive Ones

This is an Easy Array Question

## Question 
We are given an array *nums* which has 0s and 1s, we need to find the length of the maximum consecutive 1s

## Approach
We shall initialise a **cnt** integer and a **counts** array. We run a for loop for all the numbers in **nums** and if we find 1 we increase **cnt**.
If we find 0 we append the **cnt** value to **counts** and reset **cnt**. We do this until the end and also append **cnt** one last time [so that if **nums** ends in 1 the last 1s streak is also counted]
after the for loop.
We return the maximum value of **counts**.
