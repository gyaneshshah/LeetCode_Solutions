class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        pos_big = nums[-1]*nums[-2]*nums[-3]
        neg_big = nums[-1]*nums[0]*nums[1]
        if pos_big>=neg_big:
            return pos_big
        else:
            return neg_big
