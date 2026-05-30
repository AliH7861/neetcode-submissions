# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Divide the list into half
        slow = fast = head

        # Now tranverse the list
        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next

        # Set new pointers
        prev = None
        curr = slow.next
        slow.next = None # Ends first point

        while curr:
          nxt = curr.next   # 1) Save next node (don’t lose the rest)
          curr.next = prev   # 2) Reverse the link  (pointer points to prev value)
          prev = curr   # 3) Move prev to new head  (prev gets updated value)
          curr = nxt   # 4) Move curr forward  9CURR MOVES AHEAD

        first = head
        second = prev

        dummy = ListNode(0)
        outcurr = dummy

        while second:
          tmp1 = first.next
          tmp2 = second.next
          
          first.next = second
          second.next = tmp1

          first = tmp1
          second = tmp2

         


        
        # So when fast ends the slow hits mid points
        # It is time to reverse the question

        prev = None
        curr = slow.next
        
