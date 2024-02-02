# Binary Tree Inorder Traversal

This is an Easy Stack question

## Question
Given the *root* of a binary tree, return the inorder traversal of its nodes' values.

## Approach
We are given a **root**. We can create a recursive function with an array which takes in value as soon as we reach the node.
I created a recursive function called **inord** It takes in the tree and an array.
After checking if the tree is not null, we first pass the left value to the recursive function, then append the current node value and then pass the left value to the recursive function.
We return the array in the end of the recursive function.
We pass in the **root** to the **inord** function and return it.
