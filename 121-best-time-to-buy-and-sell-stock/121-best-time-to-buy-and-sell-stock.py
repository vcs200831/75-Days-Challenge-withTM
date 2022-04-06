class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1 # left=Buy and right=Sell
        maxmP = 0
        
        while right<len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxmP = max(maxmP , profit)
            else:
                left = right
            right+=1
        return maxmP
            
        