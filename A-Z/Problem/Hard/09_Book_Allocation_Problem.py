class Solution:
    def findPages(self, nums, m):
        if len(nums) < m:
            return -1
        low, high = max(nums), sum(nums)

        while low <= high:
            mid = (low + high) // 2

            is_possible = self.cal(nums, mid, m)

            if is_possible:
                high = mid - 1

            else:
                low = mid + 1

        return low
    
    def cal(self, nums, mid, m):
        students = 1
        sum = 0
        for i in nums:
            if sum + i > mid:
                students += 1
                sum = i
            else:
                sum += i
        return students <= m