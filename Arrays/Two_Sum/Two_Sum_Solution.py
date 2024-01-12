class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating an array to return
        ans=[]    
        # Creating a flag to break the loop
        no="Not Found"
        # Iterating over the values in nums
        for i in range(0, len(nums)):
            if no=='Found':
                break
            for j in range(0, len(nums)):
                # Check for two numbers that add up to target
                if nums[i]+nums[j]==target:
                    no=='Found'
                    ans = [i, j]
                    break
        return ans