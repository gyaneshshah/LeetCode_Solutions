# Reverse Linked List

This is an Easy Linked List question

## Question
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

## Approach
We create three variables, `before`, `temp` and `after`, they will be pointing towards None, head and head.next respectively.
We iterate over a while loop until `temp` is none.
We need to reverse all the next of the nodes to the elements on their left.
The logic is we will have three variables going one node after the other, one will hold the previous value (`before`), one the current value (`temp`) and one the next value (`after`).
We will make:
`after` becomes the one next to `temp`
`temp` point to the `before`
`before` becomes the `temp`
`temp` becomes the `after`

In the end `temp` and `after` will be None and `before` will be our last element, which will be the first after reversal
We return `before`.
