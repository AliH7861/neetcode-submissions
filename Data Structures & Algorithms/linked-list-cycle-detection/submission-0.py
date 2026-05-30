# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

      seen = set()
      curr = head

      while curr:
        # Check if curr.val is in set
        if(curr in seen):
          # If not in set, return True
          return True
        # Go to the next value if in set
        seen.add(curr)
        curr = curr.next

      # Index equals -1 you return false
      return False