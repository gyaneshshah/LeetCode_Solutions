# K-th Smallest Prime Fraction
This is a Medium Array question

## Question
You are given a sorted integer array `arr` containing 1 and prime numbers, where all the integers of `arr` are unique. You are also given an integer `k`.
For every i and j where 0 <= i < j < `arr`.length, we consider the fraction `arr[i]` / `arr[j]`.
Return the `k`th smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == `arr[i]` and answer[1] == `arr[j]`.

## Approach
The approach I have used is not the most optimal but it works. I am going to store all the fractions in a dictionary with its list form and then I am going to sort and pick the `k`th smallest one and return its list form.
We will first create an empty dictionary called `prime_dict`. We will use two loops nested. The outer loop will run till the second last element and the inner loop will run from the index of the outer loop till the end.
This way we will be able to cover all the fractions. As all the values are going to be unique, we do not have to check whether or not a value is present as a key in the dictionary. At every iteration we will create the fraction in float to be the key and the list format to be the value.
Once the loops are done we will create a variable `numbers` which will have the sorted list of keys of `prime_dict`. We will then return the value of the `k`th smallest value.
