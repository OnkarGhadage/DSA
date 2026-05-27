class Solution:
    def subarraySum(self, nums, k):
        sum_ = 0
        count = 0
        dic = {0:1}
        
        for i, num in enumerate(nums):
            sum_ += num

            if sum_-k in dic:
                count += dic[sum_-k]

            dic[sum_] = dic.get(sum_, 0) + 1
        return count