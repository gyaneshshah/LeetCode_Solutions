# Number of Students Unable to Eat Lunch

This is an Easy Array question

## Question
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.
The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:
If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]` is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and `students[j]` is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). 
Return the number of students that are unable to eat.

## Approach
We will implement the stack first.
Using the while loop which will run until the `students` array is empty.
We store the first value of `students` and `sandwiches` in `student` and `sandwich` respectively.
The logic is, if the value of `student` matches the `sandwich` then we delete the current `student` and `sandwich` from the arrays.
If the type of student does not match the `sandwich`, the `student` will move back to the line (delete and append) but the `sandwich` will remain there.
We implement the above logic using if-else statement.
Now the only thing left is to check if the current `sandwich` is not accepted by any of the `students`, the while loop runs in an infinite loop in this case.
We add a counter. We initialise `count` as 0 before the loop. In the else case we increase `count` by 1 and in the if case where student matches the sandwich we shall reset `count` to 0.
After the if-else we add another if to check if the `count` is equal to the current number of `students` or `sandwiches`, if it is we break the while loop.
We return the length of `students` or `sandwiches`
