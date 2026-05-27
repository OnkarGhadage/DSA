class Solution:
    def roseGarden(self, n, bloomDay, m, k):
        if len(bloomDay) < (m * k):
            return -1

        low, high = min(bloomDay), max(bloomDay)

        while low <= high:
            mid = (low + high) // 2

            possible_bouques = self.count(bloomDay, mid, k)

            if possible_bouques >= m:
                high = mid - 1
            else:
                low = mid + 1

        return low
        
    def count(self, bloomDay, day, k):
        bouques = 0
        streak = 0

        for i in bloomDay:
            if i <= day:
                streak += 1
                if streak == k:
                    bouques += 1
                    streak = 0
            else:
                streak = 0

        return bouques