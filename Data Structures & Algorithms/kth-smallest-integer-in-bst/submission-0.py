# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Array
        result = []

        def dfs(node):

            # Base Case
            if not node:
                return
            
            # Call the left side
            left = dfs(node.left)

            # Parent Append
            result.append(node.val)

            # Call Right
            right = dfs(node.right)
           

            return node.val
            
        
        dfs(root)
        return result[k - 1]
            


        