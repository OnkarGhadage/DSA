from collections import Counter

class Solution:
    def countFrequencies(self, nums):
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        return freq

    def countFrequencies1(self, nums):
        # return Counter(nums)
        return dict(Counter(nums))

s1 = Solution()
print(s1.countFrequencies([1,2,3,1,2,1]))
print(s1.countFrequencies1([1,2,3,1,2,1]))