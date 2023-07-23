class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m=[[0]*n for _ in range(n)]
        c=1
        l,r,t,b=0,n-1,0,n-1
        while r>=l and b>=t:
            for i in range(l,r+1):
                m[t][i]=c
                c=c+1
            t=t+1
            for i in range(t,b+1):
                m[i][r]=c
                c=c+1
            r=r-1
            for i in range(r,l-1,-1):
                m[b][i]=c
                c=c+1
            b=b-1
            for i in range(b,t-1,-1):
                m[i][l]=c
                c=c+1
            l=l+1
        return m
            