class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        cnt=0
        posy = -1
        # Finding the Rook's position
        for row in board:
            posy+=1
            if 'R' in row:
                posx=row.index('R')
                break
        # Checking for pawns
        for i in range(posx, 8):
            if board[posy][i] == 'p':
                cnt+=1
                break
            elif board[posy][i] == 'B':
                break
        for i in range(posx, -1, -1):
            if board[posy][i] == 'p':
                cnt+=1
                break
            elif board[posy][i] == 'B':
                break
        for i in range(posy, 8):
            if board[i][posx] == 'p':
                cnt+=1
                break
            elif board[i][posx] == 'B':
                break
        for i in range(posy, -1, -1):
            if board[i][posx] == 'p':
                cnt+=1
                break
            elif board[i][posx] == 'B':
                break
        return cnt
