# Keyboard Row

This is an Easy Array question

## Question
Given an array of strings *words*, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

## Approach
We create arrays of the three rows, with elements in upper case and lower case.
i have stored them in arrays **firstarray**, **secondarray**, and **thirdarray** respectively.
We create an empty array called **ans** to store in the words to return.
We run a loop to iterate through words and check where the first letter of the each is in. Using that we store the row they belong to in. I have stored it in a variable called **check**.
Set a variable **cnt** to 1. This will check if the letters of the word are coming from a single row or not.
Inside the loop run another loop to iterate through the letters, if the letters are outside of the row in check then break the loop.
If the **cnt** is 1 then append the word to **ans**.
Return **ans**
