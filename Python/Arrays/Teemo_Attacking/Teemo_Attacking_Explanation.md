# Teemo Attacking

This is an Easy Array question

## Question
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly *duration* seconds. 
More formally, an attack at second *t* will mean Ashe is poisoned during the inclusive time interval *[t, t + duration - 1]*. 
If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.
You are given a non-decreasing integer array *timeSeries*, where *timeSeries[i]* denotes that Teemo attacks Ashe at second *timeSeries[i]*, and an integer duration.

## Approach
Looking at the problem, we see that the duration is affected only when the difference between two time intervals is lesser than or equal to **duration**.
Initialise a variable, here I named it **ans**. Set it to 0, we shall increment it later and return it.
We iterate through all the values in **timeSeries**. We use if-else to create conditions wherein:
if the difference between time t+1 and t is greater than **duration** then we can increment **ans** by **duration**
else we increment by the difference
We shall run the loop for 1 element less as the last element won't have a t+1 to calculate the difference. To make up for that we shall increment by duration once after the for loop.
Return **ans**.
