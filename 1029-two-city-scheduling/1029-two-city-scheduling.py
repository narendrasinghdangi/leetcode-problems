class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s=0
        dp={}
        for i in range(len(costs)):
            dp[i]=costs[i][1]-costs[i][0]
        dp=dict(sorted(dp.items() ,key= lambda x:x[1]))
        c=0
        for i in dp:
            if c<len(costs)//2:
                s=s+costs[i][1]
            else:
                s=s+costs[i][0]
            c=c+1
        return s
        
        