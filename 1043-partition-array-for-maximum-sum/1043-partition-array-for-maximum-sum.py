class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        arr.append(0)
        dp=[0]*(len(arr)+1)
        dp[0]=0
        for i in range(1,k+1):
            dp[i]=max(arr[:i])*i
        for i in range(k,len(arr)):
            lol=[]
            for j in range(k):
                lol.append(dp[i-j]+max(arr[i-j:i+1])*(j+1))
            dp[i+1]=max(lol)
        return dp[-2]
            
            
                    
                    