# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        n = 1
        curr = head
        while curr.next:
            n += 1
            curr = curr.next
        k = k % n
        if k == 0:
            return head
        tail = curr

        tail.next = head

        steps = n - k - 1

        new_tail = head
        while steps > 0:
            steps -= 1
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None

        return new_head