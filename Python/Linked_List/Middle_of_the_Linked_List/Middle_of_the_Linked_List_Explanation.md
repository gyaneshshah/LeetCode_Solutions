# Middle of the Linked List

This is an Easy Linked List question

## Question
Given the `head` of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

## Approach
We create an empty array `arr`.
We use a while loop to run through all the elements in the linked list and store them in the array
We then check for the length of `arr`.
If it is an even length we return the second middle node (can be directly acquired by dividing the length by 2, indexing starts from 0)
If it is an odd length we return the middle node (can be acquired by subtracting one from the length and then dividing by 2)
