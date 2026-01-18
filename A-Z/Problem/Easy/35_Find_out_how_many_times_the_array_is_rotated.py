class Solution:
    def findKRotation(self, nums):
        low, high = 0, len(nums) - 1
        index = 0

        while low <= high:
            mid = (low + high) // 2
            
            if nums[low] <= nums[mid]:
                if nums[low] < nums[index]:
                    index = low
                low = mid + 1
            else:
                if nums[mid] < nums[index]:
                    index = mid
                high = mid - 1

            # if nums[mid] <= nums[high]:
            #     if nums[mid] < nums[index]:
            #         index = mid
            #     high = mid - 1
            # else:
            #     if nums[low] < nums[mid]:
            #         index = low
            #     low = mid + 1

        return index
