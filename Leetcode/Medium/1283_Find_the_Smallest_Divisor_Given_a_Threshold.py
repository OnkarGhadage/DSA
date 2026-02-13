import math
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low, high = 1, max(nums)

        while low <= high:
            mid = (low + high) // 2

            division = self.cal_div(nums, mid)

            if division <= threshold:
                high = mid - 1
            else:
                low = mid + 1

        return low
    
    def cal_div(self, nums, mid):
        division = 0
        for i in nums:
            division += math.ceil(i/mid)
        return division