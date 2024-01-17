class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        return int((length*(length+1)/2) - sum(nums))
