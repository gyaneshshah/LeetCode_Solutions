# Plus One

Plus one is an Easy Array Question.

## Question:
We have a long integer but in a array (named digits) format, each digit is a value of the integer ordered from most significant to least significant in left-to-right order. We need to increment the integer by 1 and return the integer array.  

## Approach:
We need to increment 1 to the right most digit and then add the carry forward to the other digits moving left.
We know for sure that the rightmost digit has to be incremented by 1. We shall increment the right most digit by 1 and change its value to the ones digit we get after the addition, the tens digit will be carry forwarded.
We then run a for loop going from the second last digit till the first digit. We perform the same carry forward method on all the digits.
If the last digit is 9 and is added by 1, we shall have a carry forward in the end, in this case we need to add an additional number to the leftmost side. 
We can use an if statement to check if we have a carry forward in the end, if yes then we can use the insert function to add the number.
Return the digits array.