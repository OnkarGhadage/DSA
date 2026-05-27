# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def insertAtHead(self, head, X):
      """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
      """
      new_node = ListNode(X)
      new_node.next = head
      return new_node