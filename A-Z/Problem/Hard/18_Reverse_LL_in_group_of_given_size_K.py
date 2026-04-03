# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        grpPrev = dummy

        while True:
            Kth = self.getKth(grpPrev, k)
            if not Kth:
                break
            
            grpNext = Kth.next

            prev = grpNext
            curr = grpPrev.next
            while curr != grpNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            temp = grpPrev.next
            grpPrev.next = Kth
            grpPrev = temp
        return dummy.next
        
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr