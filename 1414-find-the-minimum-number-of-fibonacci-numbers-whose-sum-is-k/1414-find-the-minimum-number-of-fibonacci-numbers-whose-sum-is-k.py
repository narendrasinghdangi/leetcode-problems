class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        s=0
        while k:
            a=1
            b=1
           
            for i in range(k):
                if k>=(a+b):
                    a,b=b,a+b
                else:
                    k=k-b
                    s=s+1
                    break
        return s
                    