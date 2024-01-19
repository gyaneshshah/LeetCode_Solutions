class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        cnt = 0
        while zero in nums:
            nums.remove(zero)
            cnt+=1
        while cnt != 0:
            nums.append(zero)
            cnt-=1
