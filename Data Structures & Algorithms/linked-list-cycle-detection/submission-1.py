# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# The slow and fast technique
# Slow goes one step fast goes two
# if both slow and fast equal each otehr than it means, its a cycle

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

      # Both slow and fast points at the first node of head
      slow = fast = head

      # Loop
      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # If slow and fast equals at one poijnt
        if(slow == fast):
          return True

      return False







   #   seen = set()
    #  curr = head

   #   while curr:
        # Check if curr.val is in set
  #      if(curr in seen):
          # If not in set, return True
   #       return True
        # Go to the next value if in set
    #    seen.add(curr)
   #     curr = curr.next

      # Index equals -1 you return false
     # return False