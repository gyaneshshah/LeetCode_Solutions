# Reverse Vowels of a String

This is an Easy Two Pointer question

### Question
Given a string `s`, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

### Approach
The logic used in this solution is to first create an array of only the vowels in the string and then reverse it.
Then we iterate over the given string and whenever we come across a vowel we append the element from the reversed vowel array.
We create an array `vowels` to store uppercase and lowercase vowels. Using that and list comprehension we create an array `only_vow` to store only the vowels from `s`.
We then reverse the array `only_vow`.
We create an empty string called `reversed_s` and an index counter `ind` set to 0.
We iterate over all the characters in `s`
if we encounter any vowel we add the `ind` element of `only_vow` to `reversed_s`. We then increment `ind` by 1.
else we add the current character to `reversed_s`.
We return `reversed_s`. 
