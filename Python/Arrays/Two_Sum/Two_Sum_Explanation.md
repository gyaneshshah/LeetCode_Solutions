# Two Sum
Two Sum is an Easy Array Question

### Question:
We need to find two values in nums (an array given) that add up to target (a value given to us)

### Approach:
We shall run two for loops (as we need to find two values) to iterate over nums.
As we cannot repeat the numbers, the second loop will start from a value after the starting value of the first loop.
Therefore the first loop will end one value before the last value of nums to avoid index error.
In the nested loop we shall check for the sum of two numbers, if they match the target then we shall save the values and break the inner loop.
A flag will be used to break the outer loop. 
Return the saved values in an array.
