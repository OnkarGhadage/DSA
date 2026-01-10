class Solution:
    def upperBound(self, nums, x):
        low, high = 0, len(nums) - 1
        i = len(nums)
        while low <= high:
            mid = (low + high) // 2
            if x < nums[mid]:
                i = mid
                high = mid - 1
            else:
                low = mid + 1
        return i