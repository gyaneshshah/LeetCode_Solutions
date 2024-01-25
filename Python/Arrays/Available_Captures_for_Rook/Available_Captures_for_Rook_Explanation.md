# Available Captures for Rook

This is an Easy Array question

## Question
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.
When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.
Return the number of available captures for the white rook.

## Approach
We shall divide this problem into two stages. Finding the Rook's position and Checking for Pawns.
To find the Rooks position we iterate over the **board** array and check if Rook is present in any of the rows.
If it is we store the row and column of the rook. I have stored it in **posy** and **posx** respectively.
For the second stage we have four loops going from:
Rooks position in its row till the end of that row
Rooks position in its row till the start of that row
Rooks position in the column till the end of the column
Rooks position in the column till the start of the column

In all these loops we check if we can find the pawn, if we do we add it to the count and break the loop
We also check for bishops and break the loop if we find them.

We return **cnt**
