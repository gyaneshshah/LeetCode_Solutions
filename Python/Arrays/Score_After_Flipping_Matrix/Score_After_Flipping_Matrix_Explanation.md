# Score After Flipping Matrix
This is an Medium Array question

## Question
You are given an m x n binary matrix `grid`.
A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).
Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible score after making any number of moves (including zero moves).

## Approach
The logic is as follows: We know that if the most significant bit (MSB) (The left most bit) is 1 then the number will be higher. MSB having a value of 1 is greater than all the other bits having 1 combined. So it is always best to have the MSB as 1.
So first thing we will do is to flip all the rows which do not have 1 in their 1st column. Now we have all 1's in the first column.
Now our aim is to only flip columns and not touch the rows. We will move column by column to check how many 1s they have, if the 1s in each column is less than the no of 0s in the column, then we will flip it.

For this approach we will have helper functions.
first is the `row_flip` function.
This will take the grid and the row_no as input and iterate over all the values in the row switching the 0 to 1 and vice versa.

second is the `col_sum` function.
This will take the `grid` and the `col_no` as input and return the sum of that column. This will basically tell us how many 1s we have in the column.

As mentioned earlier, we will first check for the first column and see if there are 0s, if yes we will flip the row.
We will be calculating the score on the go. We know the power of the MSB is equal to the no of columns-1. So we will add for all the rows the value of the MSB in decimal.

Now we will iterate over the columns. For every column we will calculate its sum, if the no of 1s is greater than half of the no of rows then we do not make any changes. We will find out the bit value by the position of that column, calculate the decimal value and then multiply it by the no of 1s. If the  no of 1s is lesser than or equal to half of the no of rows, we do the same process but we multiply by the new no of 1s (subtracting the no of rows - no of 1s). 
Here we will not flip anything as it is not required. We are making changes in the column only. We do this for all the columns.
We return the score.
