class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runsum=0
        arr=[]
        for no in nums:
            runsum+=no
            arr.append(runsum)
        return arr
