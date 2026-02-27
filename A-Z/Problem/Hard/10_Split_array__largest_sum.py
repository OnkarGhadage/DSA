class Solution:
    def largestSubarraySumMinimized(self, a, k):
        low, high = max(a), sum(a)
        while low <= high:
            mid = (low + high) // 2
            if self.is_possible(a, mid, k):
                high = mid - 1
            else:
                low = mid + 1
        return low
    
    def is_possible(self, nums, mid, k):
        count = 1
        current_sum = 0
        for i in nums:
            if current_sum + i > mid:
                count += 1
                current_sum = i
            else:
                current_sum += i
        return count <= k