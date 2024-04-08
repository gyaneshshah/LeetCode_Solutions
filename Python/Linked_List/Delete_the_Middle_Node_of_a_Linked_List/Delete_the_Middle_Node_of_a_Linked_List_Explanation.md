# Delete the Middle Node of a Linked List

This is a Medium Linked List question

## Question
You are given the `head` of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
## Approach
The logic I used was to store all the nodes in an array and then delete the middle one.
Firstly we take care of the edge cases. If the list is empty or has only one value we return None.
We create two variables to store head, `temp` and `ans`. We create an empty array `arr`.
We run a while loop until `temp` is None, we append the current node `temp` in the array and then we move `temp` to the next node.
After the loop ends we will have all the nodes in `arr`.
We get the node before the middle node by n/2th-1 (n = nuomber of nodes). We store it in `prev`.
Now the middle node is just after `prev`, so `prev.next`.
We want to delete the middle node so we point the next of `prev` to the next of `middle`.
To remove the middle node completely, we point the next of `middle` to None.
We return `ans`
