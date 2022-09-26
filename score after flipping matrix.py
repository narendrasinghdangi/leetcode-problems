class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = (grid[i][j]+1) % 2

        for i in range(m):
            arr = []
            for j in range(n):
                arr.append(grid[j][i])
            z = arr.count(0)
            o = arr.count(1)
            if z > o:
                for j in range(n):
                    grid[j][i] = (grid[j][i]+1) % 2
        su = 0
        for i in range(n):
            s = ""
            for j in range(m):
                s = s+str(grid[i][j])
            su = su+int(s, 2)
        return su
