class Solution:
    def rearrangeArray(self, nums):
        pos = [x for x in nums if x > 0]
        neg = [x for x in nums if x < 0]
        merged = []
        for i,j in zip(pos, neg):
            merged.append(i)
            merged.append(j)
        return merged