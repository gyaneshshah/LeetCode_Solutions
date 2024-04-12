class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        temp = root
        while True:
            if val>temp.val:
                if temp.right is None:
                    return None
                temp = temp.right
            elif val == temp.val:
                return temp
            else:
                if temp.left is None:
                    return None
                temp = temp.left
