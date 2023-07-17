class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        c1,c2=0,0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if s1[i]=="x":
                    c1=c1+1
                else:
                    c2=c2+1
        if c1%2!=c2%2:
            return -1
        return c1//2 + c2//2 + c1%2 + c2%2
            
        