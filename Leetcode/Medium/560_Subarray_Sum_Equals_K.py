class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        wind_sum = 0
        count = 0
        dic = {0:1}

        for i, num in enumerate(nums):
            wind_sum += num

            if wind_sum-k in dic:
                count += dic[wind_sum-k]

            dic[wind_sum] = dic.get(wind_sum, 0) + 1
        
        return count