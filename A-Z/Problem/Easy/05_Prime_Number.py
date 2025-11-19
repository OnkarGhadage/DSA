class Solution:
    def isPrime(self, n):
        #your code goes here
        if n == 1 or n == 0:
            return False
        for i in range(2,n//2+1):
            if n%i == 0:
                return False
        else:
            return True

s1 = Solution()
print(s1.isPrime(int(input())))