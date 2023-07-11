class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        li=[[1],[1,1]]
        for i in range(rowIndex-1):
            lol=[1]
            for j in range(i+1):
                lol.append(li[-1][j]+li[-1][j+1])
            lol.append(1)
            li.append(lol)
        return li[rowIndex]
            