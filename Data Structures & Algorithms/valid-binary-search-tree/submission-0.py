# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # This is a dfs question you would need to go top-down here


        def dfs(node, low, high):

            # Base Case
            if not node:
                return True

            # Is not valid binary search tree
            if not(low < node.val < high):
                return False
           
           
            # The children must be valid as well
            return dfs(node.left, low, node.val) and dfs (node.right, node.val, high)
        
        return dfs(root, float('-inf'), float('inf'))
        