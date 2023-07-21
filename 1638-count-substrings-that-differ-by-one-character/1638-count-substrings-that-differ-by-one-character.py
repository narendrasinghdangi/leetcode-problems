class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        count=0
        for i in range(1,len(s)+1):
            for j in range(len(s)-i+1):
                l=s[j:i+j]
                for k in range(len(t)-i+1):
                    m=t[k:i+k]
                    c=0
                    for n in range(len(m)):
                        if l[n]==m[n]:
                            c=c+1
                    if len(m)==c+1:
                        count=count+1
        return count