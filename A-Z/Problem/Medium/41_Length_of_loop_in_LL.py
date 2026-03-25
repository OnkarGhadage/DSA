# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findLengthOfLoop(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return 0
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        length = 1
        fast = fast.next
        while slow != fast:
            length += 1
            fast = fast.next
        
        return length