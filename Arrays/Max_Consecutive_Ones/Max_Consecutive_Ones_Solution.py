class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        counts = []
        for no in nums:
            if no==1:
                cnt+=1
            else:
                counts.append(cnt)
                cnt=0
        counts.append(cnt)
