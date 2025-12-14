class Solution:
    def sortZeroOneTwo(self, nums):
        l, m, h = 0, 0, len(nums)-1
        while m <= h:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m += 1
            elif nums[m] == 2:
                nums[h], nums[m] = nums[m], nums[h]
                h -= 1
            else:
                m += 1