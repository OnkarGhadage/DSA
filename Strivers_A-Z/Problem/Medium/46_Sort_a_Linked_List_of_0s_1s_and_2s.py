# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def sortList(self, head):
        """
            :type head: Optional[ListNode]
            :rtype: Optional[ListNode]
        """
        zero = ListNode(-1)
        one = ListNode(-1)
        two = ListNode(-1)

        zeros = zero
        ones = one
        twos = two

        curr = head

        while curr:
            if curr.data == 0:
                zeros.next = curr
                zeros = zeros.next
            elif curr.data == 1:
                ones.next = curr
                ones = ones.next
            else:
                twos.next = curr
                twos = twos.next
            curr = curr.next
        
        zeros.next = one.next if one.next else two.next
        ones.next = two.next
        twos.next = None

        return zero.next