class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = sorted(t)
        s = sorted(s)
        for i in range(len(s)):
            if t[i] != s[i]:
                return t[i]
        return t[-1]
