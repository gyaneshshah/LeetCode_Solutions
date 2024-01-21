# Find Index of the First Occurence in a String

This is an Easy Two Pointers question

## Question
Given two strings *needle* and *haystack*, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

## Approach
We store the length of **haystack*8 and **needle**.
We set **ans** to -1.
We can traverse each character in **haystack** until its length - **needle**'s length.
Upon traversal we check if the first character of both match or not,
if they do, we check if the substring from that index till the length of **needle** matches to **needle**.
If they do we store it in **ans** and then break the loop.
We return **ans**
