class Solution:
    def maxDepth(self, s: str) -> int:
        maximum = 0
        count = 0
        for char in s:
            if char == '(':
                count+=1
            if char == ')':
                count-=1
            if count>maximum:
                maximum=count
        return maximum


        
