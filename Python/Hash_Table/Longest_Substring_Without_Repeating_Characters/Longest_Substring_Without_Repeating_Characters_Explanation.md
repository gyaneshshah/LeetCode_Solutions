# Longest Substring Without Repeating Characters

This is a Medium Hash Table question

## Question
Given a string *s*, find the length of the longest substring without repeating characters.

## Approach
We take a for loop that iterates over every element. Now we need to check the presence of continous unique characters from each element. We have to return the length of the longest one.
We can take a while loop that breaks if the characters are not unique, another condition we have to add is that the length does not go out of bounds.
We store the values in every for loop iteration in a **temp** array. This is to check if the current value is unique or not. We clear the array in the beginning of every iteration.
In the end, we check if the length of unique substring is the longest, we compare it to the **ans** variable and if it is longer than the previous one, we store it in **ans**.
We return **ans**
