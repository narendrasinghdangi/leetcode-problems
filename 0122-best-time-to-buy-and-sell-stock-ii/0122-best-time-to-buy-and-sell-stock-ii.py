class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s=0
        for a, b in pairwise(prices):
            s=s+max(b - a, 0)
        return s