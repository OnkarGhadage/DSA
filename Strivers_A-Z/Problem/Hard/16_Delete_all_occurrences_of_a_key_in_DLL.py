# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def deleteAllOccurrences(self, head, target):
        curr = head.next
        while curr.next:
            if curr.val == target:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            curr = curr.next
        
        if curr.val == target:
            curr.prev.next = None

        if head.val == target:
            head = head.next
            head.prev = None

        return head