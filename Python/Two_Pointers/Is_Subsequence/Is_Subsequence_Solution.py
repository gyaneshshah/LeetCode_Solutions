class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        if len_s==0:
            return True
        ind=0
        for i, char in enumerate(t):
            if char == s[ind]:
                ind+=1
            if ind==len_s:
                return True
        return False
