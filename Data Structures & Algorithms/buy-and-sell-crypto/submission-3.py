class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        l = 0 
        r = 1

        while r < n:
            cur_profit = prices[r] - prices[l]
            if cur_profit < 0:
                l = r
            else:
                r += 1
            max_profit = max(max_profit, cur_profit)
        
        return max_profit
