class Solution:
    def longestSubarray(self, nums, k):
        prefix_sum = 0
        hashmap = {}
        max_len = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum == k:
                max_len = max(max_len, i + 1)

            if (prefix_sum - k) in hashmap:
                length = i - hashmap[prefix_sum - k]
                max_len = max(max_len, length)

            if prefix_sum not in hashmap:
                hashmap[prefix_sum] = i

        return max_len