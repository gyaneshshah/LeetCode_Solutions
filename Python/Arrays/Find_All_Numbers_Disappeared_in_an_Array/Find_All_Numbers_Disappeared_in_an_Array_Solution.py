class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        complete_list = [x for x in range(1, len(nums)+1)]
        uniquenums = set(nums)
        ans = [x for x in complete_list if x not in uniquenums]
        return ans
