class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_2, prev_1 = cost[0], cost[1]
        for i in range(2, len(cost)):
            curr = cost[i] + min(prev_2, prev_1)
            prev_2, prev_1 = prev_1, curr
        return min(prev_2, prev_1)

