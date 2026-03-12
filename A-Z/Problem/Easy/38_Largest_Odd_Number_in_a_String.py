class Solution:  
    def largeOddNum(self, s: str) -> str:
        #your code goes here
        i = len(s) - 1
        while i >= 0:
            if s[i] in '13579':
                break
            i -= 1

        if i < 0:
            return ""

        j = 0
        while j <= i and s[j] == '0':
            j += 1
        

        return s[j:i + 1]