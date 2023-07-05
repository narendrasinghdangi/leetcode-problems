class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r, t, b = 0, len(matrix)-1, 0, len(matrix)-1
        res = []
        while l<=r and t<=b:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
            for i in range(t, b+1):
                res.append(matrix[i][r])
            r -= 1
            if l>r or t>b:
                break     
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b -= 1
            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l += 1
        res=res[::-1]
        l, r, t, b = 0, len(matrix)-1, 0, len(matrix)-1
        while l<=r and t<=b:
            for i in range(t, b+1):
                matrix[i][r]=res.pop()
            r -= 1
            if l>r or t>b:
                break     
            for i in range(r, l-1, -1):
                matrix[b][i]=res.pop()
            b -= 1
            for i in range(b, t-1, -1):
                matrix[i][l]=res.pop()
            l += 1
            for i in range(l, r+1):
                matrix[t][i]=res.pop()
            t += 1
        
            