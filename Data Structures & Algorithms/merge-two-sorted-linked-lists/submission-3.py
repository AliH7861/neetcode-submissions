class Solution:
    def mergeTwoLists(self, list1, list2):
       curr1 = list1
       curr2 = list2

       dummy = ListNode(0)
       curr = dummy

       # So while both of the Lists are not 0
       while curr1 and curr2:
        if curr1.val <= curr2.val:
          curr.next = curr1
          curr1 = curr1.next
        else:
          curr.next = curr2
          curr2 = curr2.next
        
        curr = curr.next
       curr.next = curr1 or curr2
       return dummy.next

       
        

        
