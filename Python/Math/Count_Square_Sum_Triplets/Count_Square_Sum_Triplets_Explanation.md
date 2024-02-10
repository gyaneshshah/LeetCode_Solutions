# Count Square Sum Triplets

This is an Easy Math question

## Question 
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
Given an integer *n*, return the number of square triples such that 1 <= a, b, c <= n.

## Approach
We shall create an array with all the squares from 1 to **n**.
Next, we shall iterate over that array from the last element to the first element and check if there are any combinations matching the triplet case.
We have a counter which is incremented when a triplet is found.
As, the loops move in one order, we will have to multiply the counter by 2 in the end to makeup for the same values but a different order.
