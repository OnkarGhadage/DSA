class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        insert_index = len(nums)
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
                insert_index = mid
            else:
                low = mid + 1
        return insert_index