class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        s=0
        while k:
            a=2
            b=3
            if k==1 or k==2 or k==3 or k==5:
                s=s+1
                return s
            for i in range(k):
                if k>=(a+b):
                    a,b=b,a+b
                else:
                    k=k-b
                    s=s+1
                    break
        return s
                    