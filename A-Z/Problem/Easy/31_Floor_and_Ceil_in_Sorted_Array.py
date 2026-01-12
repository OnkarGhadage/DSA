class Solution:
    def getFloorAndCeil(self, nums, x):
        floor, ceil = -1, -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == x:
                return nums[mid], nums[mid]
            elif nums[mid] > x:
                high = mid - 1
                ceil = nums[mid]
            else:
                low = mid + 1
                floor = nums[mid]
        return floor, ceil
