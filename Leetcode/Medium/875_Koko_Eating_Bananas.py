import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low, high = 1, max(piles)

        while low <= high:
            mid = (low + high) // 2

            count = self.count_hours(piles, mid)

            if count <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
    
    def count_hours(self, nums, k):
        count = 0
        for i in nums:
            count += math.ceil(i / k)
        return count