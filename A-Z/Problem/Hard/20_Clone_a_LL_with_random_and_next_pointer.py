# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None, random=None):
#         self.val = val
#         self.next = next
#         self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head: return head

        curr = head
        dic = {}
        while curr:
            new_node = ListNode(curr.val)
            dic[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            new_node = dic[curr]
            new_node.next = dic[curr.next] if curr.next else None
            new_node.random = dic[curr.random] if curr.random else None
            curr = curr.next
        
        return dic[head]