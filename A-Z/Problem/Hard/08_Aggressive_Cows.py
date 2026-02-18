class Solution:
    def aggressiveCows(self, nums, k):
        low, high = 1, max(nums)
        nums.sort()
        min_max_distance = 0

        while low <= high:
            mid = (low + high) // 2

            if self.cal(nums, mid, k):
                min_max_distance = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return min_max_distance
    
    def cal(self, nums, distance, k):
        cows = 1
        last_placed_cow = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - last_placed_cow >= distance:
                cows += 1
                last_placed_cow = nums[i]
        return True if cows >= k else False