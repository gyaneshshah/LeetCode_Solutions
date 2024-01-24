# Airplane Seat Assignment Probability

This is an Easy Math question

## Question
*n* passengers board an airplane with exactly *n* seats. The first passenger has lost the ticket and picks a seat randomly. But after that, the rest of the passengers will:

Take their own seat if it is still available, and
Pick other seats randomly when they find their seat occupied
Return the probability that the nth person gets his own seat.

## Approach
If you see the question, you will realise that the probability is going to be 0.5 regardless of **n** being any number but one.
We return 1.0 if n is equal to 1, else we return 0.5
