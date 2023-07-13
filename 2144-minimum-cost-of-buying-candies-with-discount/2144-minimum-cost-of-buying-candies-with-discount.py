class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        c=0
        for i in range(len(cost)):
            if i%3!=2:
                c=c+cost[i]
        return c