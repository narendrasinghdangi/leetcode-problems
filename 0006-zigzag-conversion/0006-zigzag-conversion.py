class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        li=["" for i in range(numRows)]
        add=0
        inc=1
        for i in s:
            li[add]=li[add]+i
            
            if add==0:
                inc=1
            elif add == numRows - 1:
                inc = -1
            add=add+inc
            
        return "".join(li)