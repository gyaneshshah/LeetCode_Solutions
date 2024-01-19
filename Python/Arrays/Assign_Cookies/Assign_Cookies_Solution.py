class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        ind = 0
        for i in range(0, len(s)):
            if cnt == len(g):
                break
            if s[i]>=g[ind]:
                cnt+=1
                ind+=1
        return cnt 
