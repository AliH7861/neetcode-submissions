# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(node):

            # Base Case
            if not node:
                return None
            
            # Case two where root is in between p and q or equal to
            if p.val < node.val and q.val < node.val:
                return dfs(node.left)

            if p.val > node.val and q.val > node.val:
                return dfs(node.right)
            
            # if not the case it will check the children
            return node

        return dfs(root)
        