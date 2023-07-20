class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        
        # find 
        for i in range(m):
            for j in range(1,n):
                dp[j] += dp[j - 1] 
        
        # return 
        return dp[-1]
            