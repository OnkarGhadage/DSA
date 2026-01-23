import math
class Solution:
    def minimumRateToEatBananas(self, nums, h):
        low, high = 1, max(nums)
        
        while low <= high:
            mid = (low + high) // 2

            count = self.count_hours(nums, mid)

            if count <= h:
                high = mid - 1
            else:
                low = mid + 1 
        
        return low

    def count_hours(self, nums, k):
        count = 0
        for i in nums:
            count += math.ceil(i/k)
        return count
