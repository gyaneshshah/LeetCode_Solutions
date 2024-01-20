class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans = 0
        nums.sort(reverse = True)
        for i in range(1, len(nums), 2):
            ans+=nums[i]
        return ans
