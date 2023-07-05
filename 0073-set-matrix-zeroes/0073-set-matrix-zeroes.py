class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        li=[]
        lj=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    li.append(i)
                    lj.append(j)
        li=li[::-1]
        lj=lj[::-1]
        while len(li)>0:
            i=li[-1]
            j=lj[-1]
            for k in range(len(matrix[0])):
                matrix[i][k]=0
            for k in range(len(matrix)):
                matrix[k][j]=0
            li.pop()
            lj.pop()
                