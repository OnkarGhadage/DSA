class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        i, j = 0, 0
        count=0
        while i < len(nums) and j < len(nums):
            while i < len(nums) and nums[i] != 1:
                i+=1
            j = i
            while j < len(nums) and nums[j] == 1:
                j+=1
            if count < j-i:
                count = j-i
            i = j
        return count