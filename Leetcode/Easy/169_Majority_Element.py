from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        variable = None
        for n in nums:
            if count == 0:
                variable = n
            count += 1 if n == variable else - 1
        return variable