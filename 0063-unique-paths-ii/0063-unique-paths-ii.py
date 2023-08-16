class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        dp=[[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0]==1:
                break

            dp[i][0]=1
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[0][j]==1:
                break

            dp[0][j]=1
                
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j]!=1:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]