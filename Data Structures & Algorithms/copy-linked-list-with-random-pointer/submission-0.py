"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
      # Sp if head is not there it returns NOTHING
       if not head:
        return None

       # Map the node within a HashMap
       # So essentiall
       copy = {}
      
      # coppies only the values of each node
       curr = head
       while curr:
          copy[curr] = Node(curr.val)
          curr = curr.next

        # copies the pointers of each node
       curr = head
       while curr:
          # The pointers to next and random
          # We need to use get to get access to the node property
          copy[curr].next = copy.get(curr.next)
          copy[curr].random = copy.get(curr.random)
          curr = curr.next

       return copy[head]


