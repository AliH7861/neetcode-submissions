# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # We want to change the values of the left and right
        
        # If not node it breaks
        if not root:
            return None

        # Swtich rigth and left values
        root.left, root.right = root.right, root.left
        
        # Apply this on the child
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        