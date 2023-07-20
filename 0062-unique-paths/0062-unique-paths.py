class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a=m+n-2
        b=m-1
        d=n-1
        c=1
        e=1
        for i in range(1,a+1):
            c=c*i
        for i in range(1,b+1):
            e=e*i
        c=c/e
        e=1
        for i in range(1,d+1):
            e=e*i
        
        return round(c/e)
            