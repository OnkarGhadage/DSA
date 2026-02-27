class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low, high = max(nums), sum(nums)

        while low <= high:
            mid = (low + high) // 2

            if self.is_possible(nums, mid, k):
                high = mid - 1
            else:
                low = mid + 1
        return low
    
    def is_possible(self, nums, mid, k):
        subarray_count = 1
        current_sum = 0
        for i in nums:
            if current_sum + i > mid:
                subarray_count += 1
                current_sum = i
            else:
                current_sum += i
        return subarray_count <= k