class Solution:
    def numSplits(self, s: str) -> int:
        c=0
        ll=[]
        ld={}
        c=0
        for i in range(len(s)-1):
            if s[i] not in ll:
                c=c+1
                ll.append(s[i])
                ld[i]=c
                
            else:
                ld[i]=c
        rl=[]
        rd={}
        c=0
        for i in range(len(s)-1,0,-1):
            if s[i] not in rl:
                c=c+1
                rl.append(s[i])
                rd[i]=c
                
            else:
                rd[i]=c
        ans=0
        for i in range(len(s)-1):
            if ld[i]==rd[i+1]:
                ans=ans+1
        return ans