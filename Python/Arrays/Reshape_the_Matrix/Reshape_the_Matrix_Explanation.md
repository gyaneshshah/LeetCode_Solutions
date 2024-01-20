# Reshape the Matrix

This is an Easy Array question

## Question
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix *mat* and two integers *r* and *c* representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

## Approach
We create a list that contains all the elements in mat, even the sublist element.
I used list comprehension and stored them in **l**. 
We first check the condition if the reshape operation is legal. For this we can use if-else to check if the no of elements in **l** is equal to the product of *r* and *c*.
If it is legal we run a nested for loop with range as **r** and **c**. We create temporary arrays of size **c** and append them in the **ans** array.
If it is not legal we return **mat**
We return the **ans** array.
