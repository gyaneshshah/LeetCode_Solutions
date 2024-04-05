# Remove Duplicates from Sorted List

This is an Easy Linked List question

## Question
Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

## Approach
We store the head of the linked list in `temp` and in `ans`
The logic is to check the value of the current node and the next node, if it is equal we delete the duplicate.
We want to keep checking until the next value is not equal to the current node's value, once that is the case we move to the next node.
We use a while loop to run until the next value of `head` is none.
We then check if the current value of `head` is equal to the next node's value, 
if it is we use the `temp` variable to temporarily store the next node and we set the current node to next to next node (skipping the duplicate)
Now the duplicate has been removed, but we do not know if the new next value is also the same, so we keep the loop running
Only if the next value is not equal to the current value we move head to the next node, we do this using else.

We return the initial node stored in `ans`
