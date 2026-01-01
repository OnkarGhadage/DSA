class Solution:
    def maxLen(self, arr):
        # Your code goes here
        dic = {0: -1}
        max_len = 0
        subarr_sum = 0
        for i, num in enumerate(arr):
            subarr_sum += num

            if subarr_sum in dic:
                max_len = max(max_len, i - dic[subarr_sum])
            else:
                dic[subarr_sum] = i
        return max_len