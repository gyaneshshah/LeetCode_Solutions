# Island Perimeter

This is an Easy Array question

## Question
You are given row x col `grid` representing a map where `grid`[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

## Approach
We need to calculate the sides which are land and either on the edge or are next to water. We can iterate over all the elements in the matrix and count the perimeter using if-else.
We create a variable `perimeter` to increment the sides.
We create two variables to store the length of the rows and the columns.
We iterate over all the elements using nested loops.
First we check if the current square is land (if it is equal to 1).
If it is we check the squares next to it.
To check if the current square is on the edge, we check if the index before or after is less than 0 or equal to the length.
To check if it is next to water we check if the value before or after is 0.
We do that for all four sides of the square for all the squares and increment `perimeter` by 1 in each case.
We return `perimeter`.
