# Maximum Product of Three Numbers

This is an Easy Array question

## Question
Given an integer array `nums`, find three numbers whose product is maximum and return the maximum product.

## Approach
We first sort `nums`. Now, we might think that the biggest three numbers would make te maximum product, but what if we have two large negative numbers?
In that case the product of those two large negative numbers multiplied by the biggest positive number would make the maximum product.
We store these two values and return the largest of the two.
