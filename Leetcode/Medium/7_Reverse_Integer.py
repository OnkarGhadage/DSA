class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)

        # Reversing the number
        reverse_no = 0
        while n > 0:
            reverse_no = reverse_no*10 + (n%10)
            n //= 10
        
        # Set negative reverse number for negative number
        if x < 0:
            reverse_no = -reverse_no
            
        # Return reverse_number if number in the range otherwise 0
        if (x >= -2147483648 and x <= 2147483647 and abs(reverse_no) < 2147483647):
            return reverse_no
        else:
            return 0

s1 = Solution()
print(s1.reverse(0))
        
# -------------- Refernished -------------- #

class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)

        # Reversing the number
        reverse_no = 0
        while n > 0:
            reverse_no = reverse_no*10 + (n%10)
            n //= 10
            
        if -2147483648 < reverse_no < 2147483647:
            return reverse_no if x > 0 else -reverse_no
        return 0

s1 = Solution()
print(s1.reverse(0))