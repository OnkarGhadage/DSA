class Solution:
    def shipWithinDays(self, weights, days):
        low, high = max(weights), sum(weights)

        while low <= high:
            mid = (low + high) // 2

            days_req = self.cal_days(weights, mid)

            if days >= days_req:
                high = mid - 1
            else:
                low = mid + 1
        
        return low
    
    def cal_days(self, weights, mid):
        days = 1
        current = 0
        for w in weights:
            if current + w > mid:
                days += 1
                current = w
            else:
                current += w
        return days