class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp=[[0]*len(matrix[0]) for i in range(len(matrix))]
        c=0
        for i in range(len(matrix)):
            dp[i][0]=matrix[i][0]
            c=c+dp[i][0]
        for i in range(1,len(matrix[0])):
            dp[0][i]=matrix[0][i]
            c=c+dp[0][i]
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]:
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
                    c=c+dp[i][j]
        return c
                