class Solution:
    def function(self, n, s, result):
        if len(s) == n:
            result.append(s)
            return

        self.function(n, s+'1', result)

        if not s or s[-1] != '0':
            self.function(n, s+'0', result)

    def validStrings(self, n: int) -> List[str]:
        result = []
        self.function(n, '', result)
        return result