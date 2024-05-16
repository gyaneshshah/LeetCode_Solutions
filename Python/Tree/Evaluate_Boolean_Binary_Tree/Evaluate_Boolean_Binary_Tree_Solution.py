# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def post_order(current_node):
            if not current_node.left and not current_node.right:
                return bool(current_node.val)
            
            left_val = post_order(current_node.left) if current_node.left else False
            right_val = post_order(current_node.right) if current_node.right else False
            
            if current_node.val == 2:  
                return left_val or right_val
            elif current_node.val == 3:  
                return left_val and right_val
            else:
                return False
        
        return post_order(root)
