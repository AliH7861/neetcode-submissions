# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0

        def dfs(node, maxValue):
            
            # Base Case
            # If node has no children return None
            if not node:
                return 
            
            # If node is a bad node
            if node.val >= maxValue:
                self.count +=1
                maxValue = node.val
            
            # Call the children
            dfs(node.left, maxValue)
            dfs(node.right, maxValue)

        dfs(root, root.val)
        return self.count
                
            
          
            

        