class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        uniqnums = set(nums)
        check = len(nums)//2
        for no in uniqnums:
            if nums.count(no)>check:
                return no
                break
