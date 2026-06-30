class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        l = 0
        r = 1

        while r < n:
            cur_profit = prices[r] - prices[l]

            # implies there is a lower buying price
            # since prices[r] < prices[l]
            # always better to buy at lower price
            if cur_profit < 0:
                l = r
                r += 1
            else:
                max_profit = max(max_profit, cur_profit)
                r += 1
        
        return max_profit