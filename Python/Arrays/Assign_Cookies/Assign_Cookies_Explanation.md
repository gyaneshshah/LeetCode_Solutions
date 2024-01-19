# Assign Cookies

This is an Easy Array question

## Question
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor *g[i]*, which is the minimum size of a cookie that the child will be content with; and each cookie *j* has a size *s[j]*. 
If *s[j] >= g[i]*, we can assign the cookie *j* to the child *i*, and the child *i* will be content. 
Your goal is to maximize the number of your content children and output the maximum number.

## Approach
We first sort the arrays **g** and **s**. Then we initialise two integers **cnt** and **ind**, they will count the number of children content and the index value of the children.
We run a for loop the size of elements in **s**. We check if the cookie size is greater than or equal to the greed factor, if it is we increment **cnt** and **ind** by 1.
We add another if statement in the loop to check if the count of content children has reached the length of the number of children. This if statement is added in case all the children are content but there are cookies remaining.
The loop won't run unnecessarily.
Return **cnt**.
