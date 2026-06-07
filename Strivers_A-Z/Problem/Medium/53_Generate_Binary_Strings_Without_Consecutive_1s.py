class Solution:
    def recursion(self, n, s, result):
        if len(s) == n:
            result.append(s)
            return 

        self.recursion(n, s+'0', result)

        if not s or s[-1] == '0':
            self.recursion(n, s+'1', result)

    def generateBinaryStrings(self, n):
        result = []
        self.recursion(n, '', result)
        return result
