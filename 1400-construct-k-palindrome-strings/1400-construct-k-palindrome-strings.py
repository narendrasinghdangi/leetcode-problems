class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        d=Counter(s)
        c=0
        for i in d:
            if d[i]%2!=0:
                c=c+1
        if c>k:
            return False
        return True
        