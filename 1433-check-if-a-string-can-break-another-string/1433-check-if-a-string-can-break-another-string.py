class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1=list(s1)
        s2=list(s2)
        s1.sort()
        s2.sort()
        a=0
        b=0
        for i in range(len(s1)):
            if s1[i]>=s2[i]:
                a=a+1
            if s2[i]>=s1[i]:
                b=b+1
        return a==len(s1) or b==len(s1)
                