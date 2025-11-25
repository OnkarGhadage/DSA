from collections import Counter
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0
        window_sum = 0
        max_freq = 0
        for r in range(len(nums)):
            window_sum += nums[r]
            cost = nums[r] * (r-l+1) - window_sum
            while cost > k:
                window_sum -= nums[l]
                l += 1
                cost = nums[r] * (r-l+1) - window_sum
            max_freq = max(max_freq, r-l+1)
        return max_freq

s1 = Solution()
print(s1.maxFrequency([1,4,8,13],5))