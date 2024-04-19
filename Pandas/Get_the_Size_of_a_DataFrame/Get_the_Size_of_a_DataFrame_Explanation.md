# Get the Size of a DataFrame

This is an Easy Pandas question

## Question
DataFrame `players`:
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+
Write a solution to calculate and display the number of rows and columns of players.

Return the result as an array:

`[number of rows, number of columns]`

## Approach
We use the `shape` function to give us the rows and the columns and then we return it as elements of an array.
