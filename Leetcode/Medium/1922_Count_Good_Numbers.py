class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = helper(x, n//2)
            return (res * res * x)%MOD if n%2 else (res*res)%MOD

        even = ceil(n / 2)
        odd = n // 2

        return (helper(5, even) * helper(4, odd)) % MOD