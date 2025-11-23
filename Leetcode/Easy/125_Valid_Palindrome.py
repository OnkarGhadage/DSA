class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char.lower() for char in s if char.isalnum())
        return True if cleaned == cleaned[::-1] else False
s1 = Solution()
print(s1.isPalindrome(""))