# Binary Tree Preorder Traversal

This is an Easy Stack question

## Question
Given the *root* of a binary tree, return the preorder traversal of its nodes' values.

## Approach
We are given a **root**. We can create a recursive function with an array which takes in value as soon as we reach the node.
I created a recursive function called **preord** It takes in the tree and an array.
After checking if the tree is not null, we append the current node value and using the function we pass in the right and left values of the current node.
We return the array in the end of the recursive function.
We pass in the **root** to the **preord** function and return it.
