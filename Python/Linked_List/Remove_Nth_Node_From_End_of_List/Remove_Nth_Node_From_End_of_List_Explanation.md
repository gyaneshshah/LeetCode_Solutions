# Remove Nth Node From End of List

This is a Medium Linked List question

## Question
Given the head of a linked list, remove the *n*th node from the end of the list and return its head.

## Approach
We can solve this question by breaking it into two parts. First is retrieving the length of the node and calculate the index from the beginning and then update the node by removing that said index.
We create a function LengthOfNode that traverses over the node values increasing a counter. The function returns the counter value after complete traversal.
Next, we calculate the index by subtracting **n** from the length of the node.
We check if the index is 0, if yes we return the next value of the node. Else, we run a while loop to run until the said index and then skip the value at index.
We return the node.
