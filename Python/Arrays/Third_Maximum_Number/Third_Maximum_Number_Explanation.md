# Third Maximum Number

This is an Easy Array question

## Question
We are given an array *nums* and we have to find the third distinct maximum number.

## Approach
We shall create another array called **sortnums** and store the unique values of **nums** sorted in descending order.
We can do that by creating a set and then converting it to list and then applying the sorted() function with reverse as True.
Once we have that we create an integer variable called **ans**. We shall store the maximum distinct value in it. Basically the first element of **sortednums**.
The we shall check if the length of **sortednums** is greater than equal to three, if it is that means we do have a third distinct maximum. We store that in ans and return it.

