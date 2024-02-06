# Product Sales Analysis I

This is an Easy Database question

## Question
Table: *Sales*

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
 
Table: *Product*

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.
 
Write a solution to report the product_name, year, and price for each sale_id in the Sales table.
Return the resulting table in any order.

## Approach
We select the **product_name**, **year** and **price** from their respective tables.
We have to show all the values in the sales table.
Looking at the output, we will have a column from the **Product** on the left and two columns from **Sales** on the right.
We want all the values from the right table's column so we perform a RIGHT Join.
