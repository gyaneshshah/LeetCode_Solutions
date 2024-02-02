class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postord(tree, arr=[]):
            if tree is not None:
                postord(tree.left, arr)
                postord(tree.right, arr)
                arr.append(tree.val)
            return arr
        return postord(root)
