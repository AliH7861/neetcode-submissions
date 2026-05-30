# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

      # two pointers to the linkedlist
      list1 = l1
      list2 = l2
      carry = 0

      # So we will make a dummy linked output list
      dummy = ListNode(0)
      curr = dummy

      # While List 1 and List 2 are not empty
      while list1 or list2 or carry:

        # Add the sum of list1 and list 2 together
        v1 = list1.val if list1 else 0
        v2 = list2.val if list2 else 0

        total = v1 + v2 + carry
        carry = total // 10
        

        # You need to add that to dummy linked list so you put that value within ListNode()
        # Move it to the next pointer
        curr.next = ListNode(total % 10)
        curr = curr.next

        # You need to move the pointers of both lists
        if list1:
          list1 = list1.next
        if list2:
          list2 = list2.next

        
      # You need to return the dummy Linkedlist
      return dummy.next


      



        