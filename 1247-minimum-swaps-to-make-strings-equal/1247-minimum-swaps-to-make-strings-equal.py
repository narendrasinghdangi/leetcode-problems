class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy,yx=0,0
        
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if s1[i]=="x":
                    xy=xy+1
                else:
                    yx=yx+1
        
        if xy%2!=yx%2:
            return -1
        return xy//2 + yx//2 + xy%2 + yx%2
            
        