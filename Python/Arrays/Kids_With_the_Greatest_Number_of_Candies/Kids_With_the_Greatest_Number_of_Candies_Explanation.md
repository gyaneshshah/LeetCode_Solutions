# Kids With the Greatest Number of Candies

This is an Easy Array question

### Question
There are n kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the ith kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.
Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.

### Approach
The logic used in this solution is to find the maximum number of candies first and then find for each candy if the current candy+`extraCandies` is greater or equal to the maximum.
We use the max function and store the maximum candy in `max_candy`.
Using list comprehension we store the boolean value of (candy+`extraCandies`) >= `max_candy`.
We return the array with the boolean values.
