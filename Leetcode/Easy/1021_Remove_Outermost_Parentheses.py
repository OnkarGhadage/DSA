class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        level = 0
        for char in s:
            if char == '(':
                level += 1
                if level > 1:
                    result += char
            else:
                level -= 1
                if level > 0:
                    result += char
        return result