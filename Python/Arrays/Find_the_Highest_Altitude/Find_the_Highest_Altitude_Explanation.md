# Find the Highest Altitude

This is an Easy Array question

## Question
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array `gain` of length n where `gain[i]` is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

## Approach
We at every step check for the maximum altitude. We first initialise two variables `max_alt` and `curr_alt` to 0.
We iterate over each gain, and we increment the `curr_alt`. If the `curr_alt` is greater than `max_alt` then we set `max_alt` to `curr_alt`.
We return `max_alt` in the end.
