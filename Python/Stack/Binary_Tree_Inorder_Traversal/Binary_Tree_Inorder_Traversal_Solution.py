class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inord(tree, arr=[]):
            if tree is not None:
                inord(tree.left, arr)
                arr.append(tree.val)
                inord(tree.right, arr)
            return arr
        return inord(root)
