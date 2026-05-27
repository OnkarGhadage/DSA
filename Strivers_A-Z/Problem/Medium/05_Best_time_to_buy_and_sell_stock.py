class Solution:
    def stockBuySell(self, arr, n):
        price = arr[0]
        profit = 0
        for i in arr:
            price = min(price, i)
            profit = max(profit, i - price)
        return profit