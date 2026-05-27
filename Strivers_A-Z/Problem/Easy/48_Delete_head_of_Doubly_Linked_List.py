"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def deleteHead(self, head: ListNode) -> ListNode:
        # Your code goes here
        if head is None:
            return None
        if head.next is None:
            return None
        
        new_head = head.next
        new_head.prev = None
        return new_head