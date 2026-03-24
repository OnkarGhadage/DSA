# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findStartingPoint(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow