class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0 or n==1:
            return n
        li=[0,1]
        for  i in range(1,n//2+1):
            li.append(li[i])
            if len(li)>n:
                break
            li.append(li[i]+li[i+1])
        return max(li)