class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s.rstrip()
        count = 0
        flag = False
        for i in range(len(s)-1, -1, -1):
            if s[i]!= ' ':
                flag = True
            if s[i] == ' ' and flag == True:
                break
            if flag == True:
                count+=1
        return count
