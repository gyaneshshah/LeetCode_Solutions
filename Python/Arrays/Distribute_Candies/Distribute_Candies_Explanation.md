# Distribute Candies

This is an Easy Array question

## Question
Alice has n candies, where the ith candy is of type *candyType[i]*. Alice noticed that she started to gain weight, so she visited a doctor.
The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.
Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

## Approach
We know that if the unique candy types are less or equal to what Alice is allowed to have then she can have all the different types of candies.
We first create a list of unique candy types. I have the variable named **unique_candyTypes**.
We take the length of both the **candyType** and the **unique_candyTypes**
Using if statement we check if the length of **unique_candyTypes** is lesser than or equal to the length of **candyTypes**/2 (She is allowed to have n/2 of the candies she has. 
If it is, we return the length of the unique candy types.
Else, we return the length of **candyTypes**/2.
I have stored it in **ans**. Return it.
