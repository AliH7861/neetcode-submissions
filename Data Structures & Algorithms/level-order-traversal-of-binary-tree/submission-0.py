# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

            if not root:
                return []
            
            result = []

            # Starts the processs of going thru the tree
            queue = deque([root])

            # When queue is not empty
            while queue:
                level_size = len(queue) # number of nodes per level
                # So we want to add all the values of the current level into result array
                current_level = []

                for i in range(level_size):
                    node = queue.popleft()
                    current_level.append(node.val)
                
                    # Add generation to it
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                
                
                
                result.append(current_level)
            
            return result
        
