# Search in a Binary Search Tree

This is an Easy Tree question

## Question
You are given the `root` of a binary search tree (BST) and an integer `val`.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

## Approach
We first take care of the edge cases. If the `root` is None (It is an empty tree), then we return None.
We store the root value in another variable `temp`.
We run a while loop as we do not know the length of the tree, we run it until True.
If `val` is greater than the `temp`'s value then we know we have to move right, we check if there is anything on the right, if nothing then we return None.Else we move to the node on the right.
Else if `val` is equal to the current `temp` then we return the current `temp`.
Else `val` is lesser than the `temp`'s value then we know we have to move left, we check if there is anything on the left, if nothing then we return None.Else we move to the node on the left.
This loop will iterate until it reaches the end or if it finds the value.
