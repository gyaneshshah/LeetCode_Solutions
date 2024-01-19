class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Creating a set type of nums
        unique_nums = set(nums)
        ans = False
        # Checking the difference in the length of the set and the list
        if len(unique_nums)-len(nums)!=0:
            ans = True
        return ans