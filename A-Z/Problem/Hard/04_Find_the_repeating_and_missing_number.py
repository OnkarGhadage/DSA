class Solution:
    def findMissingRepeatingNumbers(self, nums):
        n = len(nums)
        S = n * (n + 1) // 2
        S2 = n * (n + 1) * (2 * n + 1) // 6
        actual_S = 0
        actual_S2 = 0
        for i in nums:
            actual_S += i
            actual_S2 += i * i
        
        x1 = actual_S - S
        x2 = actual_S2 - S2

        x2 = x2 // x1

        R = (x1 + x2) // 2
        M = S - (actual_S-R)

        return [R, M]


s1 = Solution()
print(s1.findMissingRepeatingNumbers([1, 2, 3, 6, 7, 5, 7]))