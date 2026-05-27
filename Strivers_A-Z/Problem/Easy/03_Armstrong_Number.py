import math
class Solution:
    def isArmstrong(self, n):
        total = int(math.log10(n)) + 1
        x = n
        sum = 0
        for i in range(total):
            sum += (x%10)**total
            x //= 10
        if sum == n:
            return True
        return False

N = int(input())
n1 = Solution()
print(n1.isArmstrong(N))