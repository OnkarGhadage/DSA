class Solution:
    def insertion_sort(self, nums: list[int]):
        n = len(nums)
        for i in range(1,n):
            while nums[i] < nums[i-1] and i > 0:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                i -= 1

s1 = Solution()
List = [8,6,9,7,2,4,1]
s1.insertion_sort(List)
print(List)