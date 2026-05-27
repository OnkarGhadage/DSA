class Solution:
    def majorityElement(self, nums):
        count = 0
        variable = None
        for num in nums:
            if count == 0:
                variable = num
            if variable == num:
                count += 1
            else:
                count -= 1
        return variable