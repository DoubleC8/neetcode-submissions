class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        l = 0
        r = 1

        while r < n:
            curr_profit = prices[r] - prices[l]
            max_profit = max(max_profit, curr_profit)

            if curr_profit < 0:
                l = r
                r += 1
            else:
                r += 1

        return max_profit
                 