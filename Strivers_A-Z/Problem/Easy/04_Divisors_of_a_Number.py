class Solution:
    def divisors(self, n):
        if n == 0:
            return []
        divisors = []
        for i in range(1,n+1):
            if n%i == 0:
                divisors.append(i)
        return divisors

s1 = Solution()
print(s1.divisors(int(input())))