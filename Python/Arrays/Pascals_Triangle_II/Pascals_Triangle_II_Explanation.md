# Pascals Triangle II

Pascals Triangle is an Easy Array Question.

## Question:
Given an integer *rowIndex*, return the *rowIndex*th (0-indexed) row of the Pascal's triangle.

## Approach:
Let us look at the Pascal Triangle. We notice that at each row it starts and ends with 1. The first row is only a one integer array 1.
Looking at the constraint we see that the numRows can be anywhere between 1 and 30 including both. 
We take an **ans** nested array with the first row already in place.
We will use this first array inside **ans** to calculate the values of the other rows.
See the example of 5 numRows, what else do you notice? 
The length of array increases with every row. 5 numRows will have 5 arrays with length 1-5.
Let us take a nested for loop. First we shall increment by range **rowIndex**+1. The second for loop we shall have a range of the current value of the first loop.
Since, we already have the first array in ans already we shall start the for loop from the second element (index 1).
In the first loop we take the previous array in **ans** and store it in an array called **prev**.
We initialise a **temp** empty array and an incrementor integer called **inc**. **Temp** will be the row array which we shall append in the **ans** nested array. **inc** will be the index incrementor for values that need to be added.
Now let us move to the inner loop. We know that the first and last element of any row is 1 so we create that condition using if else.
For the other values we shall use the **prev** array and add the current value and the value next to it. We shall use the **inc** variable to get these indexes and move by one after adding.
Once the inner loop is done appending all the elements in **temp**, we shall append it in **ans**.
We shall return the lasrt value of **ans** in the end.
