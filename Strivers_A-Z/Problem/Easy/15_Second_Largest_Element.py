class Solution:
    def secondLargestElement(self, nums):
        maximum = max(nums)
        second_max = float('-inf')
        for i in nums:
            if i < maximum and i > second_max:
                second_max = i
        return second_max if second_max!=float('-inf') else -1

s1 = Solution()
print(s1.secondLargestElement([10, 5, 10]))