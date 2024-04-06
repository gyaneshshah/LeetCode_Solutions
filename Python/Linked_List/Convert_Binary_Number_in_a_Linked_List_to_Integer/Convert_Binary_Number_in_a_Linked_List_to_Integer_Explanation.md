# Convert Binary Number in a Linked List to Integer

This is an Easy Linked List question

## Question
Given `head` which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.
The most significant bit is at the head of the linked list.

## Approach
We create an empty string `string_num` to store the binary value.
We loop over all the values in the linked list and keep adding the value to `string_num`.
In the end we will have the binary number in string format, we return the integer conversion using the *int* function.
