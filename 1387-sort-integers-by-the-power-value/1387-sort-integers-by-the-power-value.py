class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp={1:0}
        t=True
        for i in range(2,hi+1):
            c=0
            if i%2==0:
                i=i//2
                dp[2*i]=dp[i]+1
            else:
                lol=i
                t=True
                while t:
                    if lol%2==0:
                        lol=lol//2
                        c=c+1
                    else:
                        lol=lol*3+1
                        c=c+1
                    if lol in dp:
                        dp[i]=dp[lol]+c
                        t=False
        lol={}
        for i in range(lo,hi+1):
            lol[i]=dp[i]
        lol=dict(sorted(lol.items(), key =lambda i:i[1]))
        l=0
        for i in lol:
            l=l+1
            if k==l:
                return i