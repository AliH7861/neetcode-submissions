# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.isbalanced = None
        output = True
        result = 0

        def dfs(node):
            if not node:
                # Return 0 because the return type must be the same type
                return 0

            # Now we calculate the left and right side
            left = dfs(node.left)
            right = dfs(node.right)

            # Now here there is a condition
            if abs(left - right) > 1:
                self.isbalanced = -1

            return max(left, right) + 1
        
        # Call the dfs
        dfs(root)

        # If Statement
        if(self.isbalanced == -1):
            return False
        
        return output
        
        
        