class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp={}
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j):
            lol=0
            if (i,j) in dp:
                return dp[(i,j)]
            if i==0 and j==0:
                return grid[i][j]
            if i<0 or j<0:
                return float("inf")
            lol=grid[i][j]+min(dfs(i-1,j),dfs(i,j-1))
            dp[(i,j)]=lol
            grid[i][j]=lol
            return grid[i][j]
                
            
        return dfs(n-1,m-1)