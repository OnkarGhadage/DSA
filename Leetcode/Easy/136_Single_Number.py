class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        single = 0
        for i in nums:
            single ^= i
        return single