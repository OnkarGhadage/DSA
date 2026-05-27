# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def deleteHead(self, head):
        #your code goes here
        head = head.next
        ele = []
        curr = head
        while curr:
            ele.append(curr.data)
            curr = curr.next
        return ele