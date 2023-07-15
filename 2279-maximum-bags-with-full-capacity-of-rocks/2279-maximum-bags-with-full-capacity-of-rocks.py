class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        c=0
        dp=[0]*len(rocks)
        for i in range(len(rocks)):
            dp[i]=capacity[i]-rocks[i]
        dp.sort()
        for i in range(len(dp)):
            if dp[i]==0:
                c=c+1
            elif additionalRocks>=dp[i]:
                additionalRocks=additionalRocks-dp[i]
                c=c+1
        return c
            