# Smallest Index With Equal Value

This is an Easy Array question

## Question
Given a 0-indexed integer array *nums*, return the smallest index i of nums such that i mod 10 == *nums*[i], or -1 if such index does not exist.
x mod y denotes the remainder when x is divided by y.

## Approach
We initialize a variable **ans** with the value -1.
We iterate over **nums**, using if condition we check if the condtion "index%10" is equal to **nums**[index].
If yes we set **ans** to the index and break the loop.
We return **ans**
