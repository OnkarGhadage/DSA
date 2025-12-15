class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        variable = None
        for n in nums:
            if count == 0:
                variable = n
            count += 1 if n == variable else - 1
        return variable