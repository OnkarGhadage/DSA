class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        start = end = 0
        max_prod = float('-inf')
        for i in range(len(nums)):
            if start == 0:
                start = 1
            if end == 0:
                end = 1
            
            start *= nums[i]
            end *= nums[len(nums) - i - 1]

            max_prod = max(max_prod, start, end)
        
        return max_prod
