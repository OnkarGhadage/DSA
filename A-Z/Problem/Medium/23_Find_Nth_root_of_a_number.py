class Solution:
    def NthRoot(self, n, m):
        low, high = 1, m
        while low <= high:
            mid = (low + high) // 2
            val = 1

            for _ in range(n):
                val *= mid
                if val > m:
                    break

            if val == m:
                return mid
            elif val < m:
                low = mid + 1
            else:
                high = mid - 1
        return -1