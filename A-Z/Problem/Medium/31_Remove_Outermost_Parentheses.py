class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Your code goes here
        result = ""
        level = 0
        for i, char in enumerate(s):
            if char == '(':
                level += 1
                if level > 1:
                    result += char
            else:
                level -= 1
                if level > 0:
                    result += char
        return result