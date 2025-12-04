class Solution:
    def check(self, nums: list[int]) -> bool:
        break_points = 0
        for i, val in enumerate(nums):
            if nums[i-1] > val:
                break_points += 1
        print(break_points)
        return break_points <= 1

s1 = Solution()
print(s1.check([6,10,6,6]))