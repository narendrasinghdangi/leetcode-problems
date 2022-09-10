class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        l = len(grid)
        r = []
        c = []
        li = [[0]*l for i in range(l)]
        for i in range(l):
            r.append(max(grid[i][:]))
            m = grid[0][i]
            for j in range(1, l):
                ma = grid[j][i]
                if ma > m:
                    m = ma
            c.append(m)
        print(r)
        print(c)
        s = 0
        for i in range(l):
            for j in range(l):
                s = s+abs(min(r[i], c[j])-grid[i][j])
        print(s)


s = Solution()
s.maxIncreaseKeepingSkyline(
    [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
