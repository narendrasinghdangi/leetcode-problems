class Solution:
    def trailingZeroes(self, n: int) -> int:
        s=1
        for i in range(1,n+1):
            s=s*i
        t=0
        while s>=0:
            i=s%10
            if i==0:
                t=t+1
            else:
                break
            s=s//10
        return t