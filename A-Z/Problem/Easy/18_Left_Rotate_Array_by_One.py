class Solution:
    def rotateArrayByOne(self, nums):
        for i in range(len(arr)-1, 0, -1):
            nums[i], nums[i-1] = nums[i-1], nums[i]

s1 =Solution()
arr = [1, 2, 3, 4, 5]
print(arr)
s1.rotateArrayByOne(arr)
print(arr)