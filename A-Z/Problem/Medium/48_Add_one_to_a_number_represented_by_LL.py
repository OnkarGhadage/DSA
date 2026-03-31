# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addOne(self, head):
        head = self.reverse(head)

        curr = head
        carry = 1

        while curr:
            total = curr.val + carry
            curr.val = total % 10
            carry = total // 10

            if carry == 0:
                break

            if curr.next is None and carry:
                curr.next = ListNode(carry)
                carry = 0
                break
            
            curr = curr.next
        
        return self.reverse(head)

    def reverse(self, head):
        curr = head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev