class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j=0
        c=0
        for i in range(len(t)):
            while len(s)>j:
                if s[j]==t[i]:
                    j=j+1
                    c=c+1
                    break
                j=j+1
        return len(t)-c
            