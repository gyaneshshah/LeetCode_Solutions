class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        if len(nums)>2:
            ans=nums[1]
        else:
            ans=-1
        return ans
