# Maximize Happiness of Selected Children

This is a Medium Array question

## Question
You are given an array happiness of length `n`, and a positive integer `k`.
There are n children standing in a queue, where the ith child has happiness value `happiness[i]`. You want to select `k` children from these `n` children in k turns.
In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.
Return the maximum sum of the happiness values of the selected children you can achieve by selecting `k` children.

## Approach
When you look at the question it might a bit complicated but it is not. To maximize the happiness we will pick the happiest `k` children. 
To do that we will sort `happiness` in descending order and then pick the first `k` children. But there are two catches, first is that in every turn all the children not picked, their happiness decreases by 1.
The other catch is that happiness cannot be negative. For this we will use an if statement.
We start by sorting `happiness` in descending order and create a variable `summ` to store the maximum happiness.
We iterate from 0, to `k` (not included. Now we will increment summ to the first variable of `happiness` and so on and also decrease it by the iteration number `i`. That is how we will overcome the first catch.
Now, when the happiness becomes zero we need not increment any further, cause all the elements after that will be zero too, as we are traversing from highest to lowest.
So we add an if statement in the beginning to check if the current happiness is 0, if it is we return the `summ`.
We return `summ` again in the end if no happiness reaches zero.
