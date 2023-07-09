class Solution:
    def hammingWeight(self, n: int) -> int:
        
        n=bin(n)
        
        c=0
        for i in n:
            if i=="1":
                c=c+1
        return c