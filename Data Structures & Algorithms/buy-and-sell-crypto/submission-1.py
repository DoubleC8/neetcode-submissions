class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        l = 0
        r = 1

        while r < n:
            curr_profit = prices[r] - prices[l]
            if curr_profit < 0:
                l = r
                r += 1
            elif curr_profit >= 0:
                max_profit = max(max_profit, curr_profit)
                r += 1
        
        return max_profit