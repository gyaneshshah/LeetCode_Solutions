# Reverse Integer

This is a Medium Math question

## Question
Given a signed 32-bit integer *x*, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

## Approach
We easily solve this using string methods and if-else statement. First we check for negative numbers
If the number is negative, we convert the number into a string, remove the first element and reverse the string. We then convert it back to integer and multiply it by -1.
If the number is positive we convert it into a string and reverse it.
We store the value in **ans**. In both the cases we check if the number is exceeding 32 bit. If yes we set **ans** to 0.
We return **ans**.
