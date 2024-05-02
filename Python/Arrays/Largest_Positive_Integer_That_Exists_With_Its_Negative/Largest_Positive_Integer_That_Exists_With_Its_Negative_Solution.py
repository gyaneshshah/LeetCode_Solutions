class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        num_dec = [no for no in nums if no<0]
        for i in range(len(nums)):
            if nums[i]>0:
                if nums[i]*-1 in num_dec:
                    return nums[i]
        return -1   
