# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
            :type linkedList1: Optional[ListNode]
            :type linkedList2: Optional[ListNode]
            :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.data if l1 else 0
            v2 = l2.data if l2 else 0

            total = v1 + v2 + carry

            curr.next = ListNode(total % 10)
            carry = total // 10

            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next