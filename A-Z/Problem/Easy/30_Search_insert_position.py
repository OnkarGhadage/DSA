class Solution:
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1
        ans = len(nums)
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans