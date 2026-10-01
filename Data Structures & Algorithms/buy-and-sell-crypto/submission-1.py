class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1
        minVal = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minVal:
                minVal = prices[i]
            
            profit = max(profit, prices[i]-minVal)
        return profit
            

            
            
            