class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        if x==2:
            return 1
        for i in range(x):
            if i*i>x:
                return i-1
            