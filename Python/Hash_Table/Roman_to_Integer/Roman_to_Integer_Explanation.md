# Roman to Integer

This is an Easy Hash Table question

## Question
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

## Approach
We create a dictionary `symbols` to store the roman numerals as the key and their integer form as values. 
We run a for loop to iterate over all the roman numerals and keep adding the value of each numeral to a variable called `summ`.
Now the catch is that if 'I', 'X', 'C' is placed before 'V' and 'X', 'L' and 'C', 'D' and 'M' respectively, then it has to be negative.
So we create an if statement to check if the current numeral is one of those and if it is placed before the above mentioned numerals. If so we subtract 2, 20, 200 respectively.
The reason we subtract double of their values is because we have already added their value before the if statement.
We return `summ`.
