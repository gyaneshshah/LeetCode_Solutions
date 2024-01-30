class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for no in nums1:
            if no in nums2:
                ans.append(no)
                nums2.remove(no)
        return ans
