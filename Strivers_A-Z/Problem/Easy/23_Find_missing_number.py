class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        total = (n*(n+1))//2
        nums_total = 0
        for i in nums:
            nums_total += i
        return total - nums_total