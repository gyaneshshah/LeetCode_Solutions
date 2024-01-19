# Single Number

Single Number is an Easy Array Question.

## Question:
We have an array *nums* that has all the numbers repeated twice except one. We need to find that one unique number.  

## Approach:
The method I used was to first create a unique array. Creating a set and then converting into a list.
Then run a loop with those unique values and remove the nos one by one and check for them again in **nums**. If they are not there then we have found our value.
Break the loop. Return the value.
