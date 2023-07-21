class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        for i in range(n-1,0,-1):
            for j in range(n):
                m=min(grid[i])
                if m==grid[i][j]:
                    m=float("inf")
                    for k in range(n):
                        if j!=k:
                            m=min(m,grid[i][k])
                grid[i-1][j]=grid[i-1][j]+m
        return min(grid[0])
                    