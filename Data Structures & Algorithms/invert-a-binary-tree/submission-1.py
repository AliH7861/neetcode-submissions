# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Return Nothing if there is no value
        if root is None:
            return None
        
        # Implement Queue
        queue = deque([root])

        # While queue is not empty
        while queue:
            # First check its size
            level_size = len(queue)
       
            for i in range(level_size):

                # You pop the element to manipulate
                node = queue.popleft()

                # You switch the right nodes and the left nodes
                node.left, node.right = node.right, node.left

                # If it has a left child, the append node left
                if node.left:
                    queue.append(node.left)

                # If it has a right child append node right
                if node.right:
                    queue.append(node.right)
            
        return root

        


           
            
            
            
        