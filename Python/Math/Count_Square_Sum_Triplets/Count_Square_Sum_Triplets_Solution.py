class Solution:
    def countTriples(self, n: int) -> int:
        squares = [no*no for no in range(1,n+1)]
        cnt = 0
        for i in range(n-1, -1, -1):
            for j in range(i-1, 0, -1):
                for k in range(j-1, -1, -1):
                    if squares[i] == squares[j]+squares[k]:
                        cnt+=1
        return cnt*2
