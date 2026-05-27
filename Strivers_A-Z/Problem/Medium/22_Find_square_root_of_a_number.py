class Solution:
    def floorSqrt(self, n: int) -> int:
        low, high = 0, n
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if (mid * mid) == n:
                return mid
            elif (mid * mid) > n:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
        return ans