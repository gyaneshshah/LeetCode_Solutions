class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dup = {}

        for i, no in enumerate(nums):
            if no not in dup.keys():
                dup[no] = i
            else:
                if abs(dup[no] - i) <= k:
                    return True
                dup[no] = i
        
        return False
