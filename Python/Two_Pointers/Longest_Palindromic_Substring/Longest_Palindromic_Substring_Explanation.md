# Longest Palindromic Substring

This is a medium Two Pointers question

## Question
Given a string `s`, return the longest palindromic substring in `s`.

## Approach
The approach is simple, we shall iterate over all the substrings (from longest to shortest) and check if they are a palindrome or not.
We initialise two variables `palindrome_length` and `longest_palindrome`.
We use two for loops (nested), the outer one will iterate until the length of the string. The inner one will run from the outer loop's variable until the end (in reverse).
We first check if the length of the current substring is greater than `palindrome_length`. If it is we check if the current substring is a palindrome or not, if it is we store the current palindrome in `longest_palindrome` and the length in `palindrome_length`.
In the end we return `longest_palindrome`.
