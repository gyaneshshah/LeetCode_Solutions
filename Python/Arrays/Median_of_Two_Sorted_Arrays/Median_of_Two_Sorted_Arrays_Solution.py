class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1+nums2)
        l = len(arr)
        if l%2==0:
            return (arr[int(l/2)-1]+arr[int(l/2)])/2 
        else:
            return arr[int((l+1)/2-1)]
