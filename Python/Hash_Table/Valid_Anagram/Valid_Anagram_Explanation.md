# Valid Anagram

This is an Easy Hash Table question

## Question
Given two strings `s` and `t`, return true if `t` is an anagram of `s`, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Approach
We know that for an anagram both the words should have the same letters. We can just sort them and compare them.
We return the boolean value of the comparison of sorted `t` and `s`.
