class Solution:
    def minimumMoves(self, s: str) -> int:
        s=list(s)
        c=0
        i=0
        while len(s)-3>=i:
            if s[i]=="X":
                s[i]="O"
                if s[i+1]=="X":
                    s[i+1]="O"
                if s[i+2]=="X":
                    s[i+2]="O"
                c=c+1
            i=i+1
        if s[-1]=="X" or s[-2]=="X":
            c=c+1
            
        return c