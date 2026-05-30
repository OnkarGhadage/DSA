class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0
        
        sign = 1
        result = 0

        if s[0] == '-' or s[0] == '+':
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        
        result = result * sign

        if result < -2 ** 31:
            return -2**31
        elif result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        
        return result

# Using recursion
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        sign = 1
        index = 0

        if s[index] in '+-':
            if s[index] == '-':
                sign = -1
            index += 1
        
        MAX = 2**31 - 1
        MIN = -2**31

        def helper(i, num):
            if i >= len(s) or not s[i].isdigit():
                return num
            
            num = num * 10 + int(s[i])

            return helper(i+1,  num)
            
        
        result = helper(index, 0)

        if sign * result > MAX:
            return MAX
        if sign*result < MIN:
            return MIN
        
        return sign * result