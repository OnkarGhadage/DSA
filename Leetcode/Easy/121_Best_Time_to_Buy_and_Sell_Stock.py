class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        price = prices[0]
        profit = 0
        for i in prices:
            price = min(price, i)
            profit = max(profit, i - price)
        return profit