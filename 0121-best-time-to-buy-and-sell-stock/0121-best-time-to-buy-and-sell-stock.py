class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val=prices[0]
        prices[0]=0
        for i in range(1,len(prices)):
            min_val=min(min_val,prices[i])
            prices[i]=prices[i]-min_val
        return max(prices)