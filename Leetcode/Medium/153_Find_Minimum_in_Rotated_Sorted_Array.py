class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        minimum = nums[0]

        while low <= high:
            mid = (low + high) // 2

            if nums[low] <= nums[high]:
                minimum = min(minimum, nums[low])
                break
            
            if nums[low] <= nums[mid]:
                minimum = min(minimum, nums[low])
                low = mid + 1
            else:
                minimum = min(minimum, nums[mid])
                high = mid - 1
        
        return minimum