# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            # Base Case
            if not node:
                return 0
            
            # Checks the left and right node
            left = dfs(node.left)
            right = dfs(node.right)

            # Returns whatever value is currently + 1
            return max(left, right) + 1
        
        # Call the root of the tree
        return dfs(root)
            
            
        
        


        
    