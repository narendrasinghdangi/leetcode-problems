class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=0
        for i in range(len(prices)-1):
            s=s+max(prices[i+1] - prices[i], 0)
        return s