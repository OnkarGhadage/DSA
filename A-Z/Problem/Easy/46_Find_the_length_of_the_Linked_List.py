class Solution:
    def getLength(self, head):
        # Your code goes here
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        return length