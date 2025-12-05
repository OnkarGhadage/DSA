class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1

s1 = Solution()
print(s1.removeDuplicates([0, 0, 3, 3, 5, 6]))