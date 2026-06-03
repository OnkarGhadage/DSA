class Solution:
    def insert(self, stack, top_ele):
        if not stack:
            stack.append(top_ele)
            return
        temp = stack.pop()
        self.insert(stack, top_ele)
        stack.append(temp)

    def reverseStack(self, stack):
        # Your code goes here
        if not stack:
            return
        top_ele = stack.pop()
        self.reverseStack(stack)
        self.insert(stack, top_ele)