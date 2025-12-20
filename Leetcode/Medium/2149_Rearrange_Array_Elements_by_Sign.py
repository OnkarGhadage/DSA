class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        positive = [x for x in nums if x > 0]
        negative = [x for x in nums if x < 0]
        merged = []
        for i, j in zip(positive, negative):
            merged.append(i)
            merged.append(j)
        return merged