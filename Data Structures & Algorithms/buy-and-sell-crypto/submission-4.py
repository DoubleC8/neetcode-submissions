class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        l = 0 
        r = 1

        while r < n:
            curr_profit = prices[r] - prices[l]
            max_profit = max(max_profit, curr_profit)
            if prices[l] < prices[r]:
                r += 1
            else:
                l = r
                r += 1
        
        return max_profit
            

            
