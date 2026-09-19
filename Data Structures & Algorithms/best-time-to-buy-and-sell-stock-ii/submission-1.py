class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        prev_hold = -1
        for i, p in enumerate(prices):
            if prev_hold != -1:
                profit += p - prev_hold
                prev_hold = -1
            if i + 1 < len(prices) and prices[i+1] > p:
                prev_hold = p
        return profit
            