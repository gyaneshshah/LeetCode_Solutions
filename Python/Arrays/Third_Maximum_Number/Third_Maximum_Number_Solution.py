class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sortnums = sorted(list(set(nums)), reverse=True)
        ans = sortnums[0]
        if len(sortnums)>=3:
            ans = sortnums[2]
        return ans
