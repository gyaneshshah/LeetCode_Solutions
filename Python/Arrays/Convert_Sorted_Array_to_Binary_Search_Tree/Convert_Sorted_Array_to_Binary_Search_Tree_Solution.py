class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def nodeassign(l, r):
            if l>r:
                return None
            middle = (l+r)//2
            root = TreeNode(nums[middle])
            root.left = nodeassign(l, middle-1)
            root.right = nodeassign(middle+1, r)
            return root
        return nodeassign(0, len(nums)-1)
