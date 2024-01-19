class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        l1 = len(nums1)
        l2 = len(nums2)
        for n in range(0, l1):
            ans.append(-1)
            for k in range(nums2.index(nums1[n]), l2):
                if nums2[k]>nums1[n]:
                    ans[n] = nums2[k]
                    break
        return ans
