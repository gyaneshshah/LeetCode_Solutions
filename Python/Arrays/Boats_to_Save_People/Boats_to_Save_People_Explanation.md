# Boats to Save People

This is a Medium Array question

## Question
You are given an array people where `people[i]` is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of `limit`. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most `limit`.
Return the minimum number of boats to carry every given person.

## Approach
We know that the boat will carry a maximum of two people only, and we want the pair to be the best so that we can fit maximum number of pairs. We are going to sort `people` in the descending order of weights.
The best pair will be the heaviest and the lightest person. So we will check if that pair is equal or below the `limit`, if yes then we will move them to the boat and take the next heaviest and lightest. If the pair does not work out, we will send the heaviest person on the boat.

So we will create a variable `no_of_boats` to count the number of boats. We will sort `people` in descending order.
We shall run a while loop until `people` is None. We will first check if there are more than 1 people remaining (to be able to check for the heaviest and the lightest). If yes we will check if the first and last value of `people` is lesser than equal to the `limit`.
If it is we will remove the lightest first. Then outside of the if we will remove the heaviest (We do this so the code is cleaner. We know that in both the cases we are going to remove the heaviest). Then we increment the `no_of_boats`.
We return `no_of_boats` in the end.
