# Construct the rectangle

This is an Easy Math question

## Question
A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:

The area of the rectangular web page you designed must equal to the given target area.
The width W should not be larger than the length L, which means L >= W.
The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

## Approach
We are going to store two things, one is the answer in an array form. Other is the difference. We shall store them in **ans** and **diff** respectively.
We can iterate over elements until we reach the half of **area**. Basically we go from 2 to **area**/2. The reason we do not go from 1 is because we are going to define its difference and answer array outside.
We do this so that for 1 the loop does not have to go through all the if statements. 
We store the elements in **ans** and **diff** for the first value.
We then go inside the for loop, we check if the number is a factor and if length is greater than or equal to width.
We then check if they both are equal, if they are we save the answer and break the loop. Cause that will be of the lowest difference.
If not we check for difference and see if it is lower than the previous one [For the 1 iteration it will check the difference we stored for 1] then save that as the new **diff** and **ans**.
We return **ans**

