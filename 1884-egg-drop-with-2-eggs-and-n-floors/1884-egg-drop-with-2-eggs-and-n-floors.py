class Solution:
    def twoEggDrop(self, n: int) -> int:
        c=0
        i=1
        while n>c:
            c=c+i
            i=i+1
        return i-1