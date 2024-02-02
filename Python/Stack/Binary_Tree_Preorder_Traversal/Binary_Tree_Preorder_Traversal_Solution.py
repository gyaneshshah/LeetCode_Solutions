class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preord(tree, arr=[]):
            if tree is not None:
                arr.append(tree.val)
                preord(tree.left, arr)
                preord(tree.right, arr)
            return arr
        return preord(root)
