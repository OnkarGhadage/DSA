"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head

        curr = head
        dic = {}
        while curr:
            new_node = Node(curr.val)
            dic[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            new_node = dic[curr]
            new_node.next = dic[curr.next] if curr.next else None
            new_node.random = dic[curr.random] if curr.random else None
            curr = curr.next
        
        return dic[head]