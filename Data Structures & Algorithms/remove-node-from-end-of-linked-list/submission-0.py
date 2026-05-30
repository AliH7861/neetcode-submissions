# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

      # So basically we would just have to write a conditional
      # At that stage, we have nxt value saved
      # We update curr to Null and then equal it to the next value

      dummy = ListNode(0)
      dummy.next = head

      slow = fast = dummy

      for n in range(n):
        fast = fast.next

      while fast.next:
          slow = slow.next
          fast = fast.next
      
      slow.next = slow.next.next

      return dummy.next
      

        