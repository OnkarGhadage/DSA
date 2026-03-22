# class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None

class Solution:
    def reverseDLL(self, head):
        # Your code goes here
        curr = head
        while curr:
            curr.next, curr.prev = curr.prev, curr.next
            new_head = curr
            curr = curr.prev
        return new_head