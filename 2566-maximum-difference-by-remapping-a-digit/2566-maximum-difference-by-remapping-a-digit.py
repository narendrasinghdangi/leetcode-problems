class Solution:
    def minMaxDifference(self, num: int) -> int:
        n1=str(num)
        for i in n1:
            if i!="9":
                n1=n1.replace(i,"9")
                break
        n2=str(num)
        for i in n2:
            if i!="0":
                n2=n2.replace(i,"0")
                break
        return int(n1)-int(n2)