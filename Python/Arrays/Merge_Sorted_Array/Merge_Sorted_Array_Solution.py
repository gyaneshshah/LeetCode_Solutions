class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = nums1[0:m]
        temp=sorted(temp+nums2)
        for i in range(0, m+n):
            nums1[i]=temp[i]       
