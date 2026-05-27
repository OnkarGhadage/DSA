class Solution:
    def leaders(self, nums):
        result = []
        max_leader = nums[-1] - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > max_leader:
                result.append(nums[i])
                max_leader = nums[i]
        return result[::-1]