# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        stack = []
        while fast:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        twin_sum = 0
        while slow:
            twin_sum = max(twin_sum, stack.pop()+slow.val)
            slow = slow.next
        return twin_sum