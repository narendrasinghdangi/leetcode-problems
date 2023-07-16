class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s=""
        for i in range(n):
            if k-26<n-1:
                for j in range(n-1):
                    s=s+"a"
                s=s+chr(k-(n-1)+96)
                break
                
            else:
                s=s+"z"
                k=k-26
                n=n-1
        s=list(s)
        s.sort()
        return "".join(s)
                
                