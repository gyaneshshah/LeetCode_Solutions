# Maximum Nesting Depth of the Parentheses

This is an Easy String question

### Question
A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string `s`, return the nesting depth of `s`.

### Approach
We want to check what is the maximum depth of the parentheses in the given string.
We can use a simple approach to count the depth by checking the '(' and ')'.
For every instance of '(' we can add 1, for every instance of ')' we can subtract 1.
The maximum depth will be the maximum count at any instant.

We iterate over the characters in the string `s`.
If we find a '(' or ')', we count accordingly.
We store the maximum at any instant in the `maximum` variable and run the loop till the end.
We return `maximum`.
