class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        arr.append(0)
        dp=[0]*(len(arr)+1)
        dp[0]=0
        for i in range(1,k+1):
            dp[i]=max(arr[:i])*i
        for i in range(k,len(arr)):
            m=0
            for j in range(k):
                lol=dp[i-j]+max(arr[i-j:i+1])*(j+1)
                if lol>m:
                    m=lol
            dp[i+1]=m
        return dp[-2]
            
            
                    
                    