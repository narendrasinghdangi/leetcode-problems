class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        n = len(rowSum)
        m = len(colSum)

        ans = [[0]*m for i in range(n)]

        for i in range(n):
            for j in range(m):
                if rowSum[i] < colSum[j]:
                    ans[i][j] = rowSum[i]
                    colSum[j] -= rowSum[i]
                    rowSum[i] = 0
                else:
                    ans[i][j] = colSum[j]
                    rowSum[i] -= colSum[j]
                    colSum[j] = 0
        print(ans)


s = Solution()
s.restoreMatrix([5, 7, 10],  [8, 6, 8])
