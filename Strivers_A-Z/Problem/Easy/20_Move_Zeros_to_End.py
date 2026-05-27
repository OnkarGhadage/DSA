class Solution:
    def moveZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1

s1 = Solution()
arr = [0, 0, 0, 1, 3, -2]
s1.moveZeroes(arr)
print(arr)