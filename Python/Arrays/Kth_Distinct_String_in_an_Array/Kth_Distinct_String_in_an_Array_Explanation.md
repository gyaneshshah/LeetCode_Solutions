# Kth Distinct String in an Array

This is an Easy Array question

## Question
A distinct string is a string that is present only once in an array.
Given an array of strings *arr*, and an integer *k*, return the *k*th distinct string present in *arr*. If there are fewer than *k* distinct strings, return an empty string "".
Note that the strings are considered in the order in which they appear in the array.

## Approach
We shall initialize a counter and an **ans** variable.
Using a for loop, iterate over the strings in the array. If the count of the strings is 1 then increase the counter.
Add another if condition to check if the counter has reached **k**, if it has then assign the string to **ans** and break the loop.
Return **ans**
