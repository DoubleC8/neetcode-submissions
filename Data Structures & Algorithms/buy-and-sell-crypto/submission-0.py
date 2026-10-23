class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_prof = 0 
        l = 0
        r = l + 1 

        while r < n:
            curr_prof = prices[r] - prices[l]
            max_prof = max(max_prof, curr_prof)

            if curr_prof < 0:
                l = r
            else:
                r += 1
        
        return max_prof