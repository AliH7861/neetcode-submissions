# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Now that you have the same tree function
        # You check each node that if it equals to the subtree while going through the function

        # If the big tree ends then no subtree
        if not root:
            return False
        
        # Check if the root starts the subtree
        if self.sameTree(root, subRoot):
            return True
        
        # If not the case then
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    
    def sameTree(self, s, t):

        # Base Cases
        # 1) If both are null return true
        if not s and not t:
            return True
        
        # 2) If structure inbalance occurs
        if not s or not t:
            return False
        
        # 3) if values do not equal
        if s.val != t.val:
            return False
        
        return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)