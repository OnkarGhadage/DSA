class Solution:
    def selection_sort(self, nums: list[int]) -> list:
        for i in range(len(nums)-1):
            minimum = i
            for j in range(i,len(nums)):
                if nums[j] < nums[minimum]:
                    minimum = j
            nums[i], nums[minimum] = nums[minimum], nums[i]
        return nums
        
s1 = Solution()
print(s1.selection_sort([9,5,8,1,6,7,11]))