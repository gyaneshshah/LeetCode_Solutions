# Convert Sorted Array to Binary Search Tree

This is an Easy Array question

## Question
Given an integer array *nums* where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

## Approach
We shall use a recursive function to tackle this problem. We have a sorted array, let us divide it into left right and middle.
When we take the middle element and make it the root, we see that the elements on the left will go on the left of the root node and vice versa.
We create a recursive function called **nodeassign** that takes in left and right values. 
In this we are going to make the middle value the root node and then assign the left and right nodes, again move the middle value and so on..
We know that in a binary tree the left child cannot be greater than the right child, we create that condition and return None if that is the case.
We calculate the middle index and assign that value as the root node.
For the left and right node, we use the recursive function and pass it with the new left and right values after middle (root) node assignment.
We return root for the **nodeassign** function and get out of that function.
We pass the first and last index of **nums** to the **nodeassign** function and return it.
