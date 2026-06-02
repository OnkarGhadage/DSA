class Solution:
    def sortStack(self, stack):
        # Your code goes here
        if stack:
            temp = stack.pop()
            self.sortStack(stack)
            self.insert(stack, temp)
    
    def insert(self, stack, temp):
        if not stack or stack[-1] <= temp:
            stack.append(temp)
            return
        
        val = stack.pop()
        self.insert(stack, temp)

        stack.append(val)