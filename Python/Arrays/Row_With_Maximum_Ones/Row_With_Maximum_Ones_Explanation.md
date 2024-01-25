# Row With Maximum Ones

This is an Easy Array question

## Question
Given a m x n binary matrix *mat*, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.
In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.
Return an array containing the index of the row, and the number of ones in it.

## Approach
We shall go through each row and count the sum of the row (The constraints are that the values will be either 0 or 1)
We take a for loop to iterate over all the arrays in **mat**
We save the sum in variable **cnt** and then append it in **count**
After we have all the counts, we store the maximum value of it in **maxcnt**.
We return an array with index of **maxcnt** and **maxcnt**.
