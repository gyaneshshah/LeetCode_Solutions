# Length of Last Word

This is an Easy String question

## Question
Given a string `s` consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
 
## Approach
We create two variables, one `flag` set it to False and one `count` set it to 0.
We run a for loop going in reverse. We use if cases to check if the current letter is not a space. If it is not then we turn `flag` into True, now we can start counting knowing we do not have a space.
If it is a space and the `flag` is True means that we have come to an end of our word. We will break the loop in this case.
This way we will be counting only the last word by checking the space before and after it.
We return `count`.
