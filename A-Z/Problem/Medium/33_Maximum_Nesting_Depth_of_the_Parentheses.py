class Solution:
    def maxDepth(self, s: str) -> int:
        # Your code goes here
        level = 0
        max_depth = 0
        for i in s:
            max_depth = max(max_depth, level)
            if i == '(':
                level += 1
            elif i == ')':
                level -= 1
        return max_depth