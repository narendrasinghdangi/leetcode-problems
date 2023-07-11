class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        li=[[1],[1,1]]
        for i in range(2,numRows):
            lol=[1]
            for j in range(i-1):
                lol.append(li[-1][j]+li[-1][j+1])
            lol.append(1)
            li.append(lol)
        return li
                
            
        