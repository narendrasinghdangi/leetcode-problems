class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        n=0
        for i in range(len(s)):
            while j<len(t):
                if s[i]==t[j]:
                    n=n+1
                    j=j+1
                    break
                j=j+1
        return n==len(s)