class Solution:
    def climbStairs(self, n: int) -> int:
        o,t=1,1
        for i in range(n-1):
            o,t=o+t,o
        return o