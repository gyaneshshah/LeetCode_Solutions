# Delete Leaves With a Given Value
This is a Medium Tree question

## Question
Given a binary tree root and an integer `target`, delete all the leaf nodes with value `target`.
Note that once you delete a leaf node with value `target`, if its parent node becomes a leaf node and has the value `target`, it should also be deleted (you need to continue doing that until you cannot).

## Approach
We will use the post order traversal method to traverse the tree as we want to reach the leaves first.
We will modify the post-order traversal recursive function. We will go left first and then right and then the current node, we will check if it is a leaf node and has the target value, if that is the case we will return None.
This function will run recursively until all the nodes are traversed and only return the node following the leaf target condition.
We return the root.
