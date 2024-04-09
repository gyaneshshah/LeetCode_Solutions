# Time Needed to Buy Tickets

This is an Easy Arrays question

## Question
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person is at the back of the line.
You are given a 0-indexed integer array `tickets` of length n where the number of tickets that the ith person would like to buy is tickets[i].
Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not have any tickets left to buy, the person will leave the line.
Return the time taken for the person at position `k` (0-indexed) to finish buying tickets.
## Approach
This is almost a stack. The logic used here is to decrement all the elements of an array by 1 and add +1 to time only when the element is non zero.
We initialise `ind` (for indexing), `time` (to count the time taken), and `people` (to store the length of tickets).
We run a while loop which breaks only when `tickets[k]` is 0.
Inside we move from one element to the other, decrementing each by 1 and incrementing `time` by 1 if they are non zero.
If the index reaches the length of `tickets`, we reset it to 0.
We return `time`.
