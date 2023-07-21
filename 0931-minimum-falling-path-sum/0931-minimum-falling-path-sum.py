class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        matrix = [[inf]+x+[inf] for x in matrix]
        for i in range(m-2,-1,-1):
            for j in range(1,m+1):
                matrix[i][j]+= min(matrix[i+1][j-1],matrix[i+1][j],matrix[i+1][j+1])
        return min(matrix[0])