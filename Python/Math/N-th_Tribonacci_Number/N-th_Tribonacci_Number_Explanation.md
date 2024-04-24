# N-th Tribonacci Number

This is a Easy Math question

## Question:
The Tribonacci sequence Tn is defined as follows: 
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given `n`, return the value of Tn.

## Approach
We create a list `tri` with the first three numbers of the tribonacci sequence. If `n` is lesser than three then we return the `n`th value of `tri`.
Now we create an integer `summ` to store the updated value of the sequence. We run a loop until `n`-2 and at each iteration we calculate the sum of the previous three and store it in `summ`.
We then append the new value and remove the first value from `tri`. That way `tri` has the latest three elements of the sequence.
In the end we return `summ`.
