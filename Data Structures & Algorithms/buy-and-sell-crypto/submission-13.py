class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        buyIndex = 0
        for sellIndex in range(1, len(prices)): # hypothetical sell index
            maxProfit = max(maxProfit, prices[sellIndex] - prices[buyIndex])
            if prices[sellIndex] < prices[buyIndex]:
                buyIndex = sellIndex
        
        return maxProfit

