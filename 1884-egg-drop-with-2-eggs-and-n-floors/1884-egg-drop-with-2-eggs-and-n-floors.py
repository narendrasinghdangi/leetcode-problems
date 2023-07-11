class Solution:
    def twoEggDrop(self, n: int) -> int:
        c=0
        while n>0:
            c=c+1
            n=n-c
        return c