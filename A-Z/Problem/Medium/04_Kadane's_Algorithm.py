class Solution:
    def maxSubArray(self, nums):
        cur_sum = 0
        max_sum = nums[0]
        for num in nums:
            cur_sum += num
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
                continue
        return max_sum