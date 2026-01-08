class Solution:
    def maxProduct(self, nums):
        start = end = 1
        product = float('-inf')
        for i in range(len(nums)):
            if start == 0:
                start = 1
            if end == 0:
                end = 1
            
            start *= nums[i]
            end *= nums[len(nums)-i-1]
            product = max(product, start, end)
            
        return product
