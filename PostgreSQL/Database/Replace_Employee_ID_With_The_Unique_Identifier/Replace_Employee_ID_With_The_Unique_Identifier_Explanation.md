# Replace Employee ID With The Unique Identifier

This is an Easy Database question

## Question
Table: *Employees*

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.
 
Table: *EmployeeUNI*

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.
 
Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.
Return the result table in any order.
The result format is in the following example.

## Approach
We select the unique_id and the name from their respective tables.
We have to show null values in place of any user that does not have any unique id.
Looking at the output, we will have a column from the **EmployeeUNI** on the left and a column from **Employees** on the right.
We want all the values from the right table's column so we perform a RIGHT Join.
I have ordered the resultant table to make it look clean. It was not a part of the question.
