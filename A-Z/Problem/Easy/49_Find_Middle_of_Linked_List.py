# Definition for Singly Linked List
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleOfLinkedList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        length = length // 2
        curr = head
        while curr:
            length -= 1
            curr = curr.next
            if length == 0:
                return curr
