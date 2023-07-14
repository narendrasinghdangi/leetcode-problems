class Solution:
    def minFlips(self, target: str) -> int:
        j="0"
        c=0
        for i in target:
            if j!=i:
                c=c+1
                j=i
        return c
                