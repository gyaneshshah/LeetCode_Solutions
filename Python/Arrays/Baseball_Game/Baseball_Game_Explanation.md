# Baseball Game

This is an Easy Array question

### Question
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
You are given a list of strings operations, where `operations[i]` is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

### Approach
We will have two variables, `records` and `sum_records`.
`records` will take care of all the operations as in the question.
`sum_records` will be adding the values according to the operations.
We iterate over all elements in `operation`.
If the current element is "+", we store the previous and the value before that in two variables, we add them and append them to `records` and increase `sum_records` by that value.
If the current element is "D", we append the previous value of `records` multiplied by 2 and add the same to `sum_records`.
If the current element is "C", we delete the previous value of `records` and subtract it from `sum_records`.
Else the current element is an integer but in string format. We append the value after converting it into int and also add it to `sum_records`.
We return `sum_records`.
