class Solution:
    def singleNonDuplicate(self, nums):
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2

            mid = mid if mid % 2 == 0 else mid - 1

            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid - 1
        
        return nums[low]
