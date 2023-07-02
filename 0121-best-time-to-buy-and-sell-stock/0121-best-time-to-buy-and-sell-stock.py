class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        min_val=prices[0]
        
        for i in range(1,len(prices)):
            min_val=min(min_val,prices[i])
            if prices[i]-min_val>ans:
                ans=prices[i]-min_val
        return ans
            