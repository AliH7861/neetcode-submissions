class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

      # so made new revdrsed linked list start
      prev = None

      # have original linked list
      curr = head

      # While the curr node is not null
      while curr:
        # Save what is acc next
        nxt = curr.next

        # Point whats next to nothing or the one before
        curr.next = prev

        # Then move the pointers so now prev = curr
        prev = curr

        # And now we focus on the next element
        curr = nxt
      
      return prev




