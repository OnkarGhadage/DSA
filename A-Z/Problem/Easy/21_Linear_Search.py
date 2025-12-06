class Solution:
    def linearSearch(self, nums, target):
        for i,v in enumerate(nums):
            if v == target:
                return i
        return -1