class Solution:
    def longestSubarray(self, nums, k):
        j = 0
        win_sum = 0
        longest = 0

        for i, num in enumerate(nums):
            win_sum += num

            while win_sum > k:
                win_sum -= nums[j]
                j -= 1
            
            if win_sum == k:
                longest = max(longest, i-j+1)
                
        return longest