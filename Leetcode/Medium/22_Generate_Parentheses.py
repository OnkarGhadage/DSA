class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(l, r, s):
            if l == r == n:
                result.append(s)
                return 
            if l > n or r > n or l < r:
                return
            helper(l+1, r, s+'(')
            helper(l, r+1, s+')')

        result = []
        helper(0, 0, '')
        return result