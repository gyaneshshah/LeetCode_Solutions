class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s)):
            temp = []
            length = 0
            while (i+length)<len(s) and s[i+length] not in temp:
                temp.append(s[i+length])
                length+=1
            if length>ans:
                ans=length
        return ans 
