class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        for i in range(len(costs)):
            c=costs[i]+c
            if c==coins:
                return i+1
            if c>coins:
                return i
        return len(costs)
            
            