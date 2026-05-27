class Solution:
    def longestSubarray(self, nums, k):
        win_sum = 0
        longest = 0
        dic = {}

        for i, num in enumerate(nums):
            win_sum += num

            if win_sum == k:
                longest = max(longest, i)

            if win_sum-k in dic:
                longest = max(longest, i-dic[win_sum-k])

            if win_sum not in dic:
                dic[win_sum] = i

        return longest