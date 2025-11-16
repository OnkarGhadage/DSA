class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = x
        reverse = 0
        while x > 0:
            reverse = reverse*10 + (x%10)
            x //= 10
        return True if reverse == y else False
s1 = Solution()
print(s1.isPalindrome(-121))