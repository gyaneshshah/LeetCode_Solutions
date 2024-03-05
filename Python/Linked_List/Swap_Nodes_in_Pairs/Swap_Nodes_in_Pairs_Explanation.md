# Swap Nodes in Pairs

This is a Medium Linked List question

## Question
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

## Approach
We shall create variables **prev_node**, **first_node** and **second_node** and iterate through the linked list.
Before we iterate we should check if the list is empty or if it has only one node. If so we return the list as is.
Create a **new_node** empty list. Point its next element to the head.
Set **prev_node** as **new_node**.
Run a while loop checking if the current and the next node are present.
Set the **first_node** as the **head**, **second_node** as the next of **head**.
Now to update, we shall set next of the **prev_node** as the **second_node** (Taking the second node and putting it first).
Set the next of the **first_node** to the next of the **second_node**.
Set the next of the **second_node** to the **first_node** (Taking the first node and putting it second).
Next we move one step ahead, we set **prev_node** to the **first_node** and the head to the next of the **first_node**.

We return the next of **new_node** outside the while loop.
