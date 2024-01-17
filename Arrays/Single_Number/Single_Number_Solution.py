class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniqnums = list(set(nums))
        for no in uniqnums:
            nums.remove(no)
            if no not in nums:
                ans = no
                break
        return ans
