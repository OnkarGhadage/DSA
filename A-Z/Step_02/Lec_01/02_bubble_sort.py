class Solution:
    def bubble_sort(self, nums: list[int]) -> list:
        n = len(nums)
        for i in range(n-1):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums


s1 = Solution()
print(s1.bubble_sort([9,5,8,1,6,7,11]))