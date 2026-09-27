class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_ = prices[0]
        for i in range(1, len(prices)):
            min_ = min(prices[i],min_)
            profit = max(profit, prices[i] - min_)
        return profit