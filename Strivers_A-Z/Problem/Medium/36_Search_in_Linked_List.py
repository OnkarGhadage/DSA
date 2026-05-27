class Solution:
    def searchKey(self, head, key):
        # Your code goes here
        curr = head
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False