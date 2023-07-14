class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        r=[]
        c=[]
        for i in range(len(grid)):
            r.append(max(grid[i][:]))
            ma=0
            for j in range(len(grid)):
                if grid[j][i]>ma:
                    ma=grid[j][i]
            c.append(ma)
            s=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                s=s+abs(min(r[i],c[j])-grid[i][j])
        return s