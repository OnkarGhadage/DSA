# Definition of doubly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class Solution:
    def removeDuplicates(self, head):
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                next_node = curr.next
                curr.next = next_node.next

                if next_node.next:
                    next_node.next.prev = curr
            else:
                curr = curr.next
        
        return head