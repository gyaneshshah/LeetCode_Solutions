# Palindrome Linked List

This is an Easy Linked List question

## Question
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

## Approach
If the linked list is empty or has only one node then we immediately return True.
We create an empty string called `string`.
We iterate over all the nodes, storing the values in string format in `string`.
We return whether `string` is equal to reversed `string`.
