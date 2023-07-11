class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp=[1,1,1,1,1]
        lol=[]
        for i in range(n):
            lol.append(sum(dp))
            for j in range(5):
                dp[j]=sum(dp[j:])
        return lol[n-1]