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


s1 = Solution()
List = [1,2,3,4,5]
s1.bubble_sort(List)
print(List)