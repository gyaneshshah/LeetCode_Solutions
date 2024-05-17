# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def traverse(node):
            if not node:
                return None
            node.left = traverse(node.left)
            node.right = traverse(node.right)

            if node.left is None and node.right is None and node.val==target:
                return None
            return node
        
        return traverse(root)
