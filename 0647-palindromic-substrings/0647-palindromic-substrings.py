class Solution:
    def countSubstrings(self, s: str) -> int:
        c=len(s)
        for i in range(1,len(s)):
            for j in range(len(s)-i):
                lol=s[j:j+i+1]
                if lol==lol[::-1]:
                    c=c+1
        return c