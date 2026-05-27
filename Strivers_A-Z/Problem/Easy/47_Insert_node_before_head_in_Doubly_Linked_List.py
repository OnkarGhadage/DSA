"""
# Definition for a Node.
class ListNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
"""

class Solution:
    def insertBeforeHead(self, head: ListNode, X: int) -> ListNode:
        # Your code goes here
        new_node = ListNode(X)

        if head is None:
            return new_node

        new_node.next = head
        head.prev = new_node


        return new_node