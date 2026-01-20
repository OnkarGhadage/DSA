class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2

            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else: # nums[mid] > nums[mid + 1]
                high = mid
        return low