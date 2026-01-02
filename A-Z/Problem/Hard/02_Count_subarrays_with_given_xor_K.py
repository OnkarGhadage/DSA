class Solution:
    def subarraysWithXorK(self, nums, k):
        x_or = 0
        count = 0
        dic = {0: 1}
        
        for num in nums:
            x_or ^= num

            target = x_or ^ k
            count += dic.get(target, 0)

            dic[x_or] = dic.get(x_or, 0) + 1

        return count
