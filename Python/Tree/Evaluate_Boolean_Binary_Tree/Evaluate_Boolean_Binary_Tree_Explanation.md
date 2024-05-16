# Evaluate Boolean Binary Tree
This is an Easy Tree question

## Question
You are given the `root` of a full binary tree with the following properties:
**Leaf nodes** have either the value 0 or 1, where 0 represents False and 1 represents True.
**Non-leaf nodes** have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
The evaluation of a node is as follows:
If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
Return the boolean result of evaluating the root node.

A **full binary tree** is a binary tree where each node has either 0 or 2 children.
A **leaf node** is a node that has zero children.

## Approach
To perform the boolean operation we need to have the leaf node or the two children. We know that we will have to move left and right and then to the parent node.
So for this we will use post order traversal. We will in the recursive function check if the node has no children, if it is true that means we have the left and right values and have calculated the boolean value. We will return it.
If not we will store the left value and the right value if they are present. Then we will have an if statement for the **AND** & **OR** operation.
So the function will first find the bottom most children, perform the boolean operation and then move upwards.

The function will return the boolean value in the end.
