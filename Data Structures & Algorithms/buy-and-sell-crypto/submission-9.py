class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        i = 0 # left, buy index
        for j in range(1, len(prices)): # right, sell index
            if prices[j] < prices[i]: # if sell price less than buy price, move it up
                i = j 
            else:
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)

        
        return maxProfit

