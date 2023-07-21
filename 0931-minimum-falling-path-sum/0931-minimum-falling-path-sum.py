class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        matrix = [[inf]+x+[inf] for x in matrix]
        for i in range(m-1,0,-1):
            for j in range(1,m+1):
                matrix[i-1][j]+= min(matrix[i][j-1],matrix[i][j],matrix[i][j+1])
        return min(matrix[0])