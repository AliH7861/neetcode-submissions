# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Base Case

        # When both nodes are empty its true
        if not p and not q:
            return True

        # If one node exists and another does not
        if not p or not q:
            return False

        # If the value of p and q do not equal
        if p.val != q.val:
            return False
        
        # Call function for the left and right side (Recurrsion)
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


            
        