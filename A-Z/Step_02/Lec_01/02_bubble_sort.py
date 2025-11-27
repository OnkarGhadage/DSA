class Solution:
    def bubble_sort(self, nums: list[int]) -> list:
        n = len(nums)
        for i in range(n-1):
            swaped = False
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swaped = True
            if not swaped:
                break
        return nums


s1 = Solution()
print(s1.bubble_sort([9,5,8,1,6,7,11]))