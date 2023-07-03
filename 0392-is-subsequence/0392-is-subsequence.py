class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        n=""
        for i in range(len(s)):
            while j<len(t):
                if s[i]==t[j]:
                    n=n+s[i]
                    j=j+1
                    break
                j=j+1
        return n==s