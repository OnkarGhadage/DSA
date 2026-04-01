'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
'''

class Solution:
    def findPairsWithGivenSum(self, head, target):
        # Your code goes here
        pairs = []

        if not head:
            return pairs

        left = head

        right = head
        while right.next:
            right = right.next

        while left != right and left.prev != right:
            total = left.val + right.val

            if total == target:
                pairs.append([left.val, right.val])
                left = left.next
                right = right.prev 
            elif total < target:
                left = left.next
            else:
                right = right.prev
        
        return pairs