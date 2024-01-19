# Contains Duplicate

This is an Easy Array question

### Question
We need to find if the array nums has any duplicate values, if yes we return True or else False

### Approach
We create a **set** of the array nums. *Set* is a datatype in python that takes in unique values only.
Once we have the set, we can compare the length of both and find the difference.
If there is a difference that means there are duplicate values and vice versa.
Return the boolean value accordingly.
