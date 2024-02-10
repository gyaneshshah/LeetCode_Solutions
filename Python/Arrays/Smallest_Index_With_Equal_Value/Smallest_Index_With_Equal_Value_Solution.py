class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        ans = -1
        for i in range(0, len(nums)):
            if i%10 == nums[i]:
                ans = i
                break
        return ans
