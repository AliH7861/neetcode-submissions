# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Start the count

        def dfs(node):
            
            # So if nothing return the function
            if node is None:
                return 0
            
            # If it has left children add 1 and call the child
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            # Find the maximum value between left and right tree nodes
            return 1 + max(left_depth, right_depth)

           
        return dfs(root)