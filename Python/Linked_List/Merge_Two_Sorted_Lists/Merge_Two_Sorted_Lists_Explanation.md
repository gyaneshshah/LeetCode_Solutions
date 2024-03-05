# Merge Two Sorted Lists

This is an Easy Linked List question

## Question
You are given the heads of two sorted linked lists *list1* and *list2*.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

## Approach
We create two sub functions that will convert Node to Array and then Array to Node.
Node to Array will take in the node and update the value in an array until the end.
Array to Node will create a Node and will take in each value of the array.
We use the Node2Arr function to convert both the nodes to array and then combine those two arrays into **combinedarr**.
We pass **combinedarr** to the Arr2Node function and return the Node.
