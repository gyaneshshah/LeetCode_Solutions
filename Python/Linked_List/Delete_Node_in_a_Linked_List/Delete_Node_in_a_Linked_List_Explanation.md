# Delete Node in a Linked List

This is a Medium Linked List question

## Question
There is a singly-linked list `head` and we want to delete a node `node` in it.
You are given the node to be deleted `node`. You will not be given access to the first node of `head`.
All the values of the linked list are unique, and it is guaranteed that the given node `node` is not the last node in the linked list.
Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before `node` should be in the same order.
All the values after `node` should be in the same order.

**Custom testing**:
For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.

## Approach
At first this problem seems impossible but when you look at it, we do not have to return anything, just modify the linked list by deleting the given node.
We can change the current node's value to that of the next node and so on until in the end we will have two nodes with the same value, we shall remove the last node.

We will run a while loop until next of the current node is None. We will then copy the value of the next node to the current node and move to the next node.
To delete the last node, we will need access to the node before it, so we will store the previous node in `prev` which will run one node slower than `node`.
After the while loop ends, we shall just set the next of `prev` to None so to remove the last node.
